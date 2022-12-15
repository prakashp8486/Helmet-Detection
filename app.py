
import torch
	
model = torch.hub.load( "ultralytics/yolov5",  "custom","helmet_detect_v1.pt",force_reload=True)

result = model("12.mp4")

result.show()
