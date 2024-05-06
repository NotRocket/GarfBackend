from flask import Flask, request, jsonify, render_template, send_file
from datetime import datetime
from garf_services import GarfService, Schema
from garf_consumer import garf_consume
import json


app = Flask(__name__)
@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route("/")
def hello():
    image_path = '/static/gato.jpg'
    return render_template('index.html', image=image_path)

@app.route("/garfields", methods=["GET"])
def list_times():
    garf_consume()
    return jsonify(GarfService().list())

@app.route("/garfields/<item_id>", methods=["GET"])
def display_garfield(item_id):
    # Get the path to the temporary image file
    image_path = GarfService().get_image(item_id)
    if image_path:
        # Serve the image file
        return send_file(image_path, mimetype='image/jpeg')
    else:
        return "Image not found", 404

    #jsonify(GarfService().get_by_id(item_id))

@app.route("/garfields/<item_id>", methods=["DELETE"])
def delete_garf(item_id):
    return jsonify(GarfService().delete(item_id))

if __name__ == "__main__":
    print("hello")
    Schema()
    app.run(host='0.0.0.0')