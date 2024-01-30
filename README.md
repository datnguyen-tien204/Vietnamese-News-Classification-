[English](README.md) | [简体中文](github/cn_Zh_ReadmeMD.md) | [Tiếng việt](github/vi_vn_ReadmeMD.md)

## Contents
1. [Vietnamese Category Classification](#introduction)
2. [Results](#results)
3. [Evaluation](#evaluation)
4. [Installation](#installation)
5. [Quick Start Overview](#quick-start-overview)
6. [Structures](#structures)
7. [Send Us Feedback!](#send-us-feedback)
8. [Thanks](#thanks)
9. [License](#license)


# Introduction

This project provides category classification for Vietnamese Newspaper. I used 3 model to train model such as BiGRU( Bidirectional GRU), BiLSTM(Bidirectional LSTM) and LSTM.

# Results
### Summary Category Vietnamese Newspaper Classification
<p align="center">
    <img src="github/video_demo.gif" width="1000">
    <br>
    <sup>Testing with Tuoi Tre newspaper <a href="https://github.com/CMU-Perceptual-Computing-Lab/openpose" target="_blank"><i> on Streamlit </i></a>
</p>

### For Vietnamese Classification
For this part, we use [YOLOv3](https://github.com/ultralytics/yolov3) to detection human in rooms. To evaluation this model we use trainval35k set, which is split from the original [MS-COCO 2017](https://cocodataset.org/#home) dataset. Result shown in Table 1. 

**Table 1. Comparison result of human detection in images with 3 other models**
|    Models   | Avg. | Precision |  IoU |
|:-----------:|:----:|:---------:|:----:|
| [Faster-RCNN](https://arxiv.org/abs/1506.01497) | 21.9 |    42.7   |   -  |
|    SSD300   | 25.2 |    43.1   | 26.1 |
|    YOLOv2   | 21.6 |     44    | 19.2 |
|   **Ours**    |**25.3**| **44.5**   | **25.9** |

        
# Installation

### With Python Base
Requirements python >= 3.7 
1. Install dependences library
 ```bash
 pip install -r requirements.txt
```
2. Install dependences files
- Change directory to ``` OpenPose/graph_models/VGG_origin```, you can change directory with this command ```cd OpenPose/graph_models/VGG_origin ```
- After you must run ``` file_requirements.py ``` or
 ``` bash
python file_requirements.py
```
3. Install dependences files with other steps ( Optional )
- If you step 2 not successfully you can download weights from [Google Drive](https://drive.google.com/drive/folders/1Y4coXLsVzCXYuCKpyDfQBqpHH8Aj-Yg5?usp=sharing)
- Move folder ```graph_models``` downloaded to ```OpenPose\graph_models``` 

### With Anaconda 
1. Install dependences library
   - You can load dependences library with ``` openpose.yaml``` file.
   - You can find ```openpose.yaml``` file in folder ```Environment```
2. Install dependences files
- Change directory to ``` OpenPose/graph_models/VGG_origin```, you can change directory with this command ```cd OpenPose/graph_models/VGG_origin ```
- After you must run ``` file_requirements.py ``` or
 ``` bash
python file_requirements.py
```
3. Install dependences files with other steps ( Optional )
- If you step 2 not successfully you can download weights from [Google Drive](https://drive.google.com/drive/folders/1Y4coXLsVzCXYuCKpyDfQBqpHH8Aj-Yg5?usp=sharing)
- Move folder ```graph_models``` downloaded to ```OpenPose\graph_models``


# Quick Start Overview
### With Python Base Environments and Anaconda Environment
1. Quick Run
 - You can run this file ```main.py``` to start this project. 
2. [Optinal]To trainning model you using ```create_data.py``` to export data points and move to folder ```Action\trainning``` and using .ipnb file ```train.ipnb``` to train.
3. [Optinal] Using VGG_origin can be slow, if you don't have GPU you can change model to ```mobilenet``` to predict faster.
   - To change model to ```mobilenet```, navigation to file ```main.py``` in main folder.
   - In line 14, change ``` estimator = load_pretrain_model('VGG_origin')``` to ```estimator = 
 load_pretrain_model('mobilenet_thin')```
   
4.[Optinal] To use your weight, you can change it in ```main.py```, in line 15 change ```action_classifier = load_action_premodel('open_pose2\Action\framewise_recognition_under_scene.h5')``` to ```action_classifier = load_action_premodel('path_to_your_weights')```
  
# Structures
**Structures for all models**
<p align="center">
    <img src="github/image/structure.png" width="500">
    <br>
</p>

# Send Us FeedBack
Our project is open source for research purposes, and we want to improve it! So let us know (create a new GitHub issue or pull request, email us, etc.) if you...
1. Find/fix any bug (in functionality or speed) or know how to speed up or improve any part of OpenPoseRNN.
2. Want to add/show some cool functionality/demo/project made on top of Students Tracking. We can add your project link to your [Issue](https://github.com/datnguyen-tien204/Tracking_Students/issues)

# Thanks
Thank you for the guidance of Dr.Minh Chuan-Pham in the process of creating this project, as well as the evaluation board consisting of Dr.Quoc Viet-Hoang, who helped us improve the results and provided feedback for this project.

# License
This project is freely available for free non-commercial use. If it useful you can give 1 star. Thanks for using.
