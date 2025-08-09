#subtitleFormat.py 

import subtitles_assets
import textwrap
import shutil

class SubtitleCreate:
    def __init__(self,script):
        self.script = script
        
    def addSubtitles(self):
        sub_script = textwrap.dedent(f"{self.script}")
        #print(sub_script)
        # ===== Write Subtitle in File ===== #
        with open("rawScript.txt", "w") as file:
            file.write(sub_script)
            #print("Write",file.write(sub_script))
        # ===== Store Lines and Read It ===== #
        raw_sub_text = []
        with open("rawScript.txt", "r") as f:
            raw_sub_text = [line.strip() for line in f.readlines()]       
        # ===== Convert In Time Format ===== #
        def format_ass_time(seconds):
            h = int(seconds // 3600)
            m = int((seconds % 3600) // 60)
            s = round(seconds % 60, 2)
            return f"{h}:{m:02}:{s:05.2f}"
            
        totalTextTime = []
        start_sec = 0
        ss_end_data = []
        
        for raw_text in raw_sub_text:
            #print("Raw",sub_script)
            len_text = len(raw_text)
            totalTextTime.append(len_text)
            time_taken = len(raw_text) / 12
            wrapped_text = r'\N'.join(textwrap.wrap(raw_text, width=28))
            start_time = format_ass_time(start_sec)
            end_time = format_ass_time(start_sec + time_taken)
            ass_line = f"Dialogue: 0,{start_time},{end_time},Default,,0,0,0,,{{\\fad(300,300)\\blur1\\be1}}{wrapped_text}"
            ss_end_data.append(ass_line)
            start_sec += time_taken
            print(raw_text)
        print("raw",raw_sub_text)
        totalTime_raw =  sum(totalTextTime) / 11
        totalTime = round(totalTime_raw)
        print("Video Lendth ", totalTime)
        #print(ss_end_data)
        # ===== Adding the timeline into Header .ass file ===== #
        df = "/sdcard/subtitle_format.ass"
        with open("subtitle_format.ass", "w") as put:
            put.write(subtitles_assets.header + "\n")
            for line in ss_end_data:
                put.write(line + "\n")
        shutil.move("subtitle_format.ass", df)
        print("Subtitle Create")

            
