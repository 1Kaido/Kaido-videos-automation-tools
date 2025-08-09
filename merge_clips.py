# Merge_clips.py
import random
import subprocess

class MergeClips:
    def __init__(self,input_path,output_path,no_clips,clips_folder):
        self.input_path = input_path
        self.output_path = output_path
        self.no_clips = no_clips
        self.clips_folder = clips_folder


    def merge_clips(self):
        new_clips = []
        for _ in range(self.no_clips):
            random_clip = random.choice(self.clips_folder)
            new_clips.append(random_clip)
            print(random_clip)   
        with open("random_clips.txt", "w") as f:
            for clip in new_clips:                                              
                f.write(f"file '/sdcard/all_clips/night_city/{clip}'\n")
        command = [                                                               
            "ffmpeg", "-f", "concat", "-safe", "0",
            "-i", "random_clips.txt",                
            "-vf", "crop=ih*9/16:ih:(iw-ih*9/16)/2:0, scale=720:1280",  "-c:v", "libx264", 
            "-preset", "ultrafast",
            "-crf", "23", "-an",self.input_path
            ]
        try:   
            subprocess.run(command, check=True)
            print(f"✅ Merged into")
        except subprocess.CalledProcessError as e:
            print("❌ FFmpeg failed:", e)
        print("Clips Merged")
                     
