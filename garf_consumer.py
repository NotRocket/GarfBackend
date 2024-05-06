import numpy as np
from confluent_kafka import Consumer
from garf_services import GarfService
import json
import cv2

def read_config():
  config = {}
  with open("client.properties") as fh:
    for line in fh:
      line = line.strip()
      if len(line) != 0 and line[0] != "#":
        parameter, value = line.strip().split('=', 1)
        config[parameter] = value.strip()
  return config

def garf_consume():
  config = read_config()
  topic = "GarfDetections"
  config["group.id"] = "python-group-1"
  config["auto.offset.reset"] = "earliest"
  consumer = Consumer(config)
  consumer.subscribe([topic])

  try:
    count = 0;
    #get 5 per check
    while count <= 25:
      garf = GarfService()
      msg = consumer.poll(1.0)
      if msg is not None and msg.error() is None:
        key = msg.key().decode("utf-8")
        value = msg.value()

        print(f"Consumed message from topic {topic}: key = {key}")
        image = cv2.imdecode(np.fromstring(value, np.uint8), cv2.IMREAD_COLOR)
        newData = {
          "ObjectName" : key
          #"image" : image.tolist()
        }
        #cv2.imwrite("newImage.jpg",image) # we have a working image from confluent...
        newJson = json.dumps(newData)
        garf.create(newJson,image)

      count = count + 1
            
  except KeyboardInterrupt:
    pass
  finally:
    consumer.close()
    

#if __name__ == "__main__":
    #garf_consume()