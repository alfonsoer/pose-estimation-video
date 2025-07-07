# pose-estimation-video
# 🎯 Human Pose Estimation with YOLOv8-Pose

This project demonstrates **human pose estimation** on video using the **YOLOv8-Pose** model from [Ultralytics](https://github.com/ultralytics/ultralytics). The script processes a video file, detects human keypoints, and **annotates specific body parts** such as **nose, eyes, and shoulders** with larger readable labels. The output video is also **saved in reduced resolution** to reduce file size while maintaining visual clarity.

---
## Output

![image](https://github.com/user-attachments/assets/8c5e734d-8a69-4c71-8364-a9b27ed62382)

[<img src="https://github.com/user-attachments/assets/8c5e734d-8a69-4c71-8364-a9b27ed62382" width="50%">](https://github.com/alfonsoer/pose-estimation-video/blob/main/output/annotated_cottonbro_studio.mp4)


[![Watch the video]([https://i.sstatic.net/Vp2cE.png](https://github.com/alfonsoer/pose-estimation-video/blob/main/output/annotated_cottonbro_studio.mp4))]([https://youtu.be/vt5fpE0bzSY](https://github.com/alfonsoer/pose-estimation-video/blob/main/output/annotated_cottonbro_studio.mp4))

<video src="https://github.com/alfonsoer/pose-estimation-video/blob/main/output/annotated_cottonbro_studio.mp4" width="352" height="720"></video>
## 📌 Key Features

- ✅ Uses **YOLOv8-Pose** for fast and accurate 2D pose estimation
- ✅ Automatically annotates **nose**, **eyes**, and **shoulders** on each person detected
- ✅ Draws **large and clear labels** over selected keypoints
- ✅ Saves the output video in a **lower resolution** (configurable) to save disk space
- ✅ Accepts any `.mp4` video input

---

## 📦 Requirements

```bash
pip install ultralytics opencv-python
```


## 📁 Directory structure
##
```
project/
│
├── input/
│   └── sample_video.mp4         # Input video file
├── output/
│   └── annotated_rescaled.mp4   # Output with pose annotations
├── pose_estimation.py           # Main script
└── README.md                    # This file
```

## 🧠 Keypoints used
```
We annotate the following keypoints using COCO format indices:
Index	Name
0	Nose
1	Left Eye
2	Right Eye
5	Left Shoulder
6	Right Shoulder
```
## ▶️ Run the script
```
python pose_estimation.py
```
The script will:

    Load the YOLOv8 pose model (yolov8n-pose.pt)

    Detect persons and their keypoints

    Annotate selected keypoints with labels

    Resize the output video

    Save it as output/annotated_rescaled.mp4

## ⚙️ Configuration options
```
Inside pose_estimation.py, you can modify:
Variable	Description	Example
scale	Resize factor for output video	0.5
fontScale	Size of keypoint labels (text)	1.0
thickness	Thickness of the label text outline	2
KEYPOINT_NAMES	Dictionary of keypoints to annotate	Customizable
```
# 📝 Example output (Frame)
[<img src="https://i.ytimg.com/vi/Hc79sDi3f0U/maxresdefault.jpg" width="50%">](https://github.com/alfonsoer/pose-estimation-video/blob/main/output/annotated_cottonbro_studio.mp4)



Note: this is a placeholder image – replace with your own frame if desired.
## 📚 References
```
    Ultralytics YOLOv8 Documentation

    COCO Keypoints Format
```
## 🧠 Future wWork ideas
```
    Export keypoints to .csv for statistical analysis

    Add tracking across frames (e.g., per-person ID)

    Apply on webcam stream in real time
```
## 📸 Sample video source

You can download royalty-free, high-quality videos featuring people from:
```
    Pexels

    Pixabay

    Mixkit
```
Look for licenses that allow free reuse for personal or academic purposes.
© License

This project is open source and free to use for research and educational purposes.
