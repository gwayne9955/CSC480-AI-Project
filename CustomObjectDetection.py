from imageai.Detection.Custom import CustomObjectDetection

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("CSC480-AI-Project/Strawberries/models/detection_model-ex-019--loss-0001.208.h5") 
detector.setJsonPath("CSC480-AI-Project/Strawberries/json/detection_config.json")
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image="CSC480-AI-Project/image_inputs/image2.jpg", output_image_path="CSC480-AI-Project/image_outputs/image3_new.jpg")
for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
