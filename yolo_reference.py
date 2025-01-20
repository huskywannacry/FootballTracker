from ultralytics import YOLO

model = YOLO("models/best.pt", device='cuda')

# Inference
results = model.predict("videos/football.mp4", save=True, format="mp4")

print(results[0])
print("-" * 100)

for box in results[0].boxes:
    print(box)
