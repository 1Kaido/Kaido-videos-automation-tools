

import subprocess 

class SubtitleAndVoiceMerge:
    def __init__(self,input_path,output_path):
        self.input_path = input_path
        self.output_path = output_path
    def mergeSubtitlesAndVoice(self):
        path = "/sdcard/subtitle_format.ass"
        subprocess.run([
            "ffmpeg",
            "-i", self.input_path,
            "-i", "/sdcard/voice_1754286474.mp3",           
            "-vf", f"ass={path}",
            "-map", "0:v:0",
            "-map", "1:a:0",
            "-c:v", "libx264",
            "-preset", "ultrafast",
            "-crf", "23",
            "-shortest",
            "-y",
            self.output_path
        ])
        print("Subtitle Merged With Video")
