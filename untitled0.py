# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rtbDthQfqiySIcenHewgGZZz9Xh8wxj-
"""

!git clone https://github.com/ultralytics/yolov5 # clone

!pip install -r /content/yolov5/requirements.txt # install

!python /content/yolov5/train.py --img 640 --batch 16 --epochs 50 --data /content/drive/MyDrive/mydatasets/helmet_labelled/data.yaml --weights yolov5x.pt

!cp "/content/yolov5/runs/train/exp3/weights/best.pt" /content/drive/MyDrive/myModels/yolo/helmet_detect_v1.pt

import torch

model = torch.hub.load( "ultralytics/yolov5",  "custom","/content/yolov5/runs/train/exp3/weights/best.pt",force_reload=True)

result = model("/content/drive/MyDrive/mydatasets/helmet_labelled/test/images/BikesHelmets187_png.rf.3be290fd2b090624721a7de228c5b3c1.jpg")
result.show()

result = model("/content/drive/MyDrive/mydatasets/helmet_labelled/test/images/BikesHelmets61_png.rf.e8eee84625faf91ed259cd39b1476225.jpg")
result.show()

result = model("/content/drive/MyDrive/mydatasets/helmet_labelled/test/images/BikesHelmets286_png.rf.b3fe8af35fe8fb6b567fac18cd087e6f.jpg")
result.show()

result = model("/content/92115371.webp")
result.show()

result = model("/content/76743034.webp")
result.show()