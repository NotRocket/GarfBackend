GarfDetector Backend Docker Image

To run this project, you can either run it locally or on a cloud service K8's provider.
You need a confluent cloud client.properties file, so go get one from confluent cloud. 


	For local installation:

Download the project directory and navigate to it
Create a venv and run the command "pip install -r requirements.txt"
source to the venv
then run the garf_app.py script



	On a cloud server

Build the docker container from the dockerfile
Upload tagged container to a Digital Ocean Registery
Link a k8's cluster and deploy the service.yaml and deployment.yaml 
Connect to the pod's external serive IP


The web app has the following APIs

5000/ The home page, should display an image of my cat. 

5000/garfields : displays the detections

5000/garfields/<item_id> displays a specific detection iamge // not functional 

DELETE 5000/garfields/<item_id> deletes a detection from the database.
