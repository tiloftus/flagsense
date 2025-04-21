# from yolo10_package.yolo_inference import YOLOv10Detector
# import cv2

# detector = YOLOv10Detector("yv8_all_best.pt")
# results = detector.detect("../image_folders/double_image/images_jpeg_jpg.rf.40ef096d56206c0c7feb107169c99fe2.jpg")
# print(results)

# annotated_img = results[0].plot()
# cv2.imwrite("output.jpg", annotated_img)
# print("Image saved as output.jpg")

import yolo10_package
print(yolo10_package.__file__)

import yolo10_package.yolo_inference  # Import the module directly
print(yolo10_package.yolo_inference.__file__)  # Print the path

from yolo10_package.yolo_inference import YOLOv10Detector

# Initialize detector
detector = YOLOv10Detector()

# Run detection and save the annotated image automatically
image_path = "testimgs/images_jpeg_jpg.rf.40ef096d56206c0c7feb107169c99fe2.jpg"
detector.detect(image_path)

print("Detection completed. Annotated image saved.")
