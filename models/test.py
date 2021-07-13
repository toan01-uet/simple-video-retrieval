# print(242//2)

import faiss
import numpy as np
from img2vec import list_file_img, class_of_img, img_path

file,x = list_file_img(img_path)
video_name, videos_vec = class_of_img(file,x)
## doi kieu tu list sang nparray

videos_vec = np.vstack(videos_vec)
videos_vec = videos_vec.astype('float32')

# print("So chieu cua vector:",len(videos_vec[0]))

# print("So vector video",len(b))
# print("So vector cua anhr:",len(x))

index = faiss.read_index("flower_faiss_128.bin")

k = 6                         # we want to see 5 nearest neighbors


def return_video_file(video_index, video_vec, video_name, search_video_name):
    '''
        tham so: 
            video_index: dung de tim kiem cua faiss
            video_vec: vector bieu dien cua cac video
            video_name: ten cua cac video, ung voi cac video_vec
            search_video_name: ten video can tim video tuong tu
        tra ve:
            ten list file cua cac video gan giong
            list score cua cac video gan giong
    '''
    
    for idx,name in enumerate(video_name):
        if name == search_video_name:
            index_of_search_video_name = idx
            break
    D, I = video_index.search(video_vec[index_of_search_video_name: (index_of_search_video_name + 1)], k) # sanity check
    list_name_of_similer_video = [video_name[i] for i in I[0][1:]]
    list_score = [ score for score in D[0][1:] ]

    # list_name_of_similer_video = [video[0][::-7] for video in list_name_of_similer_video]
    list_name_of_similer_video = [str(video[0])[0:-7]+".mp4" for video in list_name_of_similer_video]

    return list_name_of_similer_video,list_score

# x, _ = return_video_file(index,videos_vec,video_name,video_name[10] )
# print(x[0])
# print(x[0][58::-8]+".mp4")



