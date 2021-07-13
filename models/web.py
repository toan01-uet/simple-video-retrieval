from flask import Flask, render_template,request
from test import video_name,return_video_file,index as index_faiss,videos_vec
import webbrowser

app = Flask(__name__, static_folder='static')

short_name = [str(video)[81:-9]+".mp4" for video in video_name]


# dict_video_name = dict( zip(short_name,video_name_path))
@app.route('/')
def index():
    return render_template("index.html", data = short_name)
@app.route('/', methods=['POST'])
def test():
    select = request.form.get('comp_select')
    try :
        idx_of_seach_video = short_name.index(select)
        name_of_search_video = video_name[idx_of_seach_video]

        list_smilar_videos, list_scores = return_video_file(index_faiss,videos_vec,video_name,name_of_search_video )
        ## format video name -> name in static folder
        list_smilar_videos = [video[72::] for video in list_smilar_videos]

        video_score = zip(list_smilar_videos,list_scores)
    except ValueError:
        print("List does not contain value")
    return render_template('index.html', message=select, video_similar = video_score) 
 

if __name__ == '__main__':
    
    # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    # webbrowser.get(chrome_path)
    app.run(debug = True)
