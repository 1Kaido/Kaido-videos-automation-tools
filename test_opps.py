# main.py
import os
from merge_clips import MergeClips

# ======== Merge Clips ======== #
# Provide your values
input_path = "not_neede67d.mp4"  # not used anymore
output_path = "/sdcard/output/merged_video6555.mp4"
no_clips = 3
clips_folder = os.listdir(f"/sdcard/all_Clips/night_city")

# Create instance
merger = MergeClips(input_path, output_path, no_clips, clips_folder)

# Call merge method
merger.merge_clips()

# ======== Subtitles ======= #
from subtitlesFormat import SubtitleCreate
from subtitle import SubtitleAndVoiceMerge

with open("script_dump.txt", "r", encoding="utf-8") as f:
    script = f.read()

subtitles = SubtitleCreate(script)
subtitles.addSubtitles()

subtilesMerger = SubtitleAndVoiceMerge(input_path,output_path)
subtilesMerger.mergeSubtitlesAndVoice()

# ========= Voice Over ======== #

#from createVoiceover import CreateVoiceOver
#from voiceover import VoiceOverMerge
# Create VoiceOver
#voiceoverCreater = CreateVoiceOver(script)
#voiceoverCreater.runCreateVoiceOver()
#Api reach llimit

#Merge VoiceOver 
#mergeVoiceOver = VoiceOverMerge(input_path,output_path)
#mergeVoiceOver.runVoiceMerger()
