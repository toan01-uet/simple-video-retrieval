from test import video_name
# print("chieu dai cua list video nam:",len(video_name))
# print("chieu dai ten cua 1 video",len(str(video_name[0])))
# print("ki tu dau tien cua ten video",str(video_name[0])[65:68])
video_name = video_name[0:3]
# short_name = [str(video[0])[81:-9]+".mp4" for video in video_name]
# print(short_name)
for video in video_name:
    print(str(video)[81:-9]+".mp4")
