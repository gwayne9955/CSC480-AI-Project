from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()
inputs = os.path.join(execution_path, "image_inputs/")

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "CSC480-AI-Project/Strawberries/models/detection_model-ex-019--loss-0001.208.h5"))
detector.loadModel()
if not os.path.exists("image_outputs"):
    os.makedirs("image_outputs")
for file in os.listdir(inputs):
    filename = os.fsdecode(file)
    if filename.endswith(".jpg"):
        detections = detector.detectObjectsFromImage(input_image=os.path.join(inputs , filename), 
            output_image_path=os.path.join(execution_path , "image_outputs/{0}".format(os.path.splitext(filename)[0] + "_new" + os.path.splitext(filename)[1])))
        print("Printing Detections for" + filename)
        for eachObject in detections:
            print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
        print()
