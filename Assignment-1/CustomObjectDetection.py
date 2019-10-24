from imageai.Detection.Custom import CustomObjectDetection

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("Strawberries/models/detection_model-ex-004--loss-0003.971.h5") 
detector.setJsonPath("Strawberries/json/detection_config.json")
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image="image_inputs/DSC_0034.JPG", output_image_path="image_outputs/DSC_0034_new.JPG")
for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
