#voiceover.py

import createVoiceover
import subprocess

audio_path = createVoiceover.voiceover_file

class VoiceOverMerge:
    def __init__(self,input_path,output_path):
        self.input_path = input_path
        self.output_path = output_path
    def runVoiceMerger(self):
        try:
            # FFmpeg command to merge video + audio
            command = [
                "ffmpeg",
                "-i", self.output_path, #video input
                "-i", "/sdcard/voice_1754286474.mp3",    # Audio input
                "-c:v", "copy",      # Keep video as-is
                "-c:a", "aac",       # Encode audio to AAC (good compatibility)
                "-shortest",         # End output when the shortest input ends
                "sdcard/outpuut55588v.mp4"
            ]
        
            result = subprocess.run(command, capture_output=True, text=True)
        
            if result.returncode == 0:
                print("✅ Audio added successfully!")
            else:
                print("❌ FFmpeg failed!")
                print(result.stderr)
        
        except Exception as e:
            print(f"⚠️ An error occurred: {e}")
