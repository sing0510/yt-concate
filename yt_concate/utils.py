# utils is a file to save the code which all the def will use
# sample file path

import os
from os import walk

from yt_concate.setting import CAPTIONS_DIR
from yt_concate.setting import DOWNLOADS_DIR
from yt_concate.setting import VIDEOS_DIR


class Utils:
    def __init__(self):
        pass

    def create_dir(self):  # create a file
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)  # os.makedirs is a def to create file , exitst_ok=True (check file)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)

    def get_video_list_filepath(self,channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_list_file_exists(self,channel_id):
        path = self.get_captions_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]  ## to get the video id

    def get_captions_filepath(self, url):  ## save location
        return os.path.join(CAPTIONS_DIR, self.get_video_id_from_url(url) + 'txt')

    def caption_file_exists(self, url):  ## check file exist
        path = self.get_captions_filepath(url)
        return os.path.exists(path) and os.path.getsize(path) > 0  # if file exist , must be something in the txt

    #def rename(self):
        #for (dirpath, dirnames, filenames) in walk(CAPTIONS_DIR):
            #for i in filenames:
                #print(i)
                #video_id = i.split('txt.en.vtt')[0]
                #print(video_id)
                #os.rename(i, video_id + '.txt')

