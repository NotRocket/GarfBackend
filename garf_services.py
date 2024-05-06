import sqlite3
from garf_sql import GarfModel


class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('garf.db')
        self.create_garf_table()

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def create_garf_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "GARF" (
          id INTEGER PRIMARY KEY,
          ObjectName TEXT,
          Image BLOB,
          DetectedOn TIMESTAMP DEFAULT (DATETIME('now'))
        );
        """
        self.conn.execute(query)


class GarfService:
    def __init__(self):
        Schema()
        self.model = GarfModel()

    def create(self, params, image):
        return self.model.create(params,image)

    def delete(self, item_id):
        return self.model.delete(item_id)

    def list(self):
        response = self.model.list_items()
        return response

    def get_by_id(self, item_id):
        response = self.model.get_by_id(item_id)
        return response
    
    def get_image(self,item_id):
        response = self.model.get_image_blob(item_id)