# from vectorhub.encoders.image.tfhub import MobileNetV12Vec
import os
from os import listdir
from os.path import isfile, join

from vectorhub.encoders.image.tfhub import MobileNetV12Vec
model = MobileNetV12Vec()

img_path = r'C:\Users\Toan\OneDrive\Desktop\YouTube_DataSet_Annotated\selectedframes'


from os import walk
import numpy as np

from pathlib import Path
### list file
def list_file_img(path):
    '''
        tham so: path
        tra ve: cac lop ten file anh va vector cua moi file anh
    '''
    f = []
    videos_vec = []
    for (dirpath, dirnames, filenames) in walk(img_path):
        # f.extend(filenames)
        for file in filenames:
            if '.jpeg' in file:
                f.append(os.path.join(dirpath, file))
                sample = model.read(os.path.join(dirpath, file))         
                vector = model.encode(sample)
                vector_nparr = np.array(vector)
                videos_vec.append(vector_nparr)
    return f,videos_vec

# file,x = list_file_img(img_path)
# print(type(x[0]))
# print(len(file))

def class_of_img(list_file, list_vec):
    '''
        tham so: cac lop ten file anh va vector cua moi file anh
        dau ra: list vecto dai dien cua moi video, list ten file anh
    '''
    class_file = []
    video_vec = []

    for i in range(0,len(list_file)):
        if i % 2 == 0:
            new_key_name = str(list_file[i])
            class_file.append([list_file[i]])
            video_vec.append(np.concatenate((list_vec[i],list_vec[i+1])))

    return class_file, video_vec
import faiss
def creat_faiss_index(video_file, videos_vec):
    videos_vec = np.vstack(videos_vec)
    videos_vec = videos_vec.astype('float32')
    index = faiss.IndexFlatL2(2048)
    # print(index.is_trained)
    index.train(videos_vec)
    index.add(videos_vec)                  # add vectors to the index
    # print(index.ntotal)

    ## write to file
    faiss.write_index(index, "flower_faiss_128.bin")

   

file,x = list_file_img(img_path)
a, b = class_of_img(file,x)
# # print("So chieu cua vector:",len(b[0]))
# # print("So vector video",len(b))
# # print("So vector cua anhr:",len(x))

creat_faiss_index(a, b)

# print(len(a))