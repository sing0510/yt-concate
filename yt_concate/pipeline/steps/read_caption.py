import os
import pprint  ## print function for better looking of dictionary

from .step import Step
from yt_concate.setting import CAPTIONS_DIR


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}
        for caption_file in os.listdir(CAPTIONS_DIR):  # os.listdir list all file in dictionary
            captions = {}
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r') as f:#because of the caption is not next to main.py
                time_line = False
                for line in f:
                    time = line.strip()
                    if '<c>' in line:
                        continue
                    if '-->' in line:  # --> is time_line
                        time_line = True
                        time = line
                        continue
                    if time_line and '-->' not in line:
                        caption = line
                        captions[caption] = time  ## dictionary {caption:time}
                        time_line = False
            data[caption_file] = captions  ## dictionary {file_name:captions}

        pprint(data)
        return data





