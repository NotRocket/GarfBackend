import sqlite3
import json
import base64
import numpy as np

class GarfModel:
    TABLENAME = "GARF"

    def __init__(self):
        self.conn = sqlite3.connect('garf.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def get_by_id(self, _id):
        where_clause = f"AND id={_id}"
        return self.list_items(where_clause)

    def create(self, params,image):
        params = json.loads(params)
        query = f'INSERT INTO {self.TABLENAME} (ObjectName, Image) VALUES (?,?)'
        result = self.conn.execute(query,(params["ObjectName"],image))
        return self.get_by_id(result.lastrowid)

    def delete(self, item_id):
        query = f"DELETE FROM {self.TABLENAME} " \
                f"WHERE id = {item_id}"
        self.conn.execute(query)
        return self.list_items()


    def list_items(self, where_clause=""):
        query = f"SELECT id, ObjectName, DetectedOn " \
                f"from {self.TABLENAME}"
        result_set = self.conn.execute(query).fetchall()
        result = [{column: row[i]
                   for i, column in enumerate(result_set[0].keys())}
                  for row in result_set]
        return result

    def get_image_blob(self,item_id):
        query = f'SELECT image FROM {self.TABLENAME} WHERE id={item_id}'
        result = self.conn.execute(query).fetchone()[0]
        temp_file_path = f"{item_id}.jpg"
        print(result)
        cv2.imshow('GarfDetector', result)

        #jpg_original = base64.b64decode(result[0])
        #nparr = np.frombuffer(jpg_original, np.uint8)
        #img = cv2.imdecode(nparr, flags=1)
        #img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        #cv2.imwrite(temp_file_path, img)
        #with open(temp_file_path, 'wb') as temp_file:
            #temp_file.write(jpg_original)
        return temp_file_path



