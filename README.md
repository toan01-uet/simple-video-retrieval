# Simple Video Retrieval System
## Demo
![demo](https://media.giphy.com/media/FiYxdyFWVp0gJ4UNqn/giphy.gif)
## System overview
![sys_overview](https://github.com/toan01-uet/simple-video-retrieval/blob/master/models/templates/sys_overview.png)
## Description
In this project, I aim to develop a system to automatically search and retrieve similar videos in large scale dataset. However, the time project is limit (2 week), then the small dataset was selected from UCF11 which are about humans action:  biking/cycling, diving, golf swinging, horse back riding,...

The dataset contains 121 videos :
- Biking: 25 videos
- Juggle: 27 videos
- Ridding: 24 videos
- Shooting: 22 videos
- Spiking: 23 videos

Our system consists of two parts :
- Video representation:
    - Step 1: extract keyframe/keyframes from Videos using [Katna](https://katna.readthedocs.io/en/latest/).
    - Step 2: motivated by the great success of deep learning approaches, we use pretrained model (MobileNet) from [Vectorhub](https://github.com/vector-ai/vectorhub) for representing image (key frame -> vector).
    - Strp 3: Concat vectors for representing video.
- Retrieval: a video retrieval system based on distance (FAISS)

## Reference
- [milvus-application-image-search-system](https://blog.milvus.io/milvus-application-1-building-a-reverse-image-search-system-based-on-milvus-and-vgg-aed4788dd1ea)
- [video-search-system](https://www.google.com/url?q=https://blog.milvus.io/4-steps-to-building-a-video-search-system-5a3ced633308&sa=D&source=editors&ust=1626194846639000&usg=AOvVaw08DmkOBM7p1A4ZlluwxDG1)
