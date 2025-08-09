#createVoiceOver.py
import requests, time, subprocess

voiceover_file = ""
class CreateVoiceOver:
    def __init__(self,script):
        self.script = script
    
    def runCreateVoiceOver(self):
        API_KEY = "pdAVVLvv114Hzbi9MJw1x0HbqSyw4suWKy50thlrUkT3z4OdZZS8F4"
        payload = {
            "Text": self.script,
            "VoiceId": "bm_lewis",
            "Pitch": 0.88,
            "Speed": 0.1,
            "Bitrate": "192k",
            "OutputFormat": "uri"
        }
    
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
    
        try:
            r = requests.post("https://api.v8.unrealspeech.com/speech", json=payload, headers=headers)
            audio_url = r.json()["OutputUri"]
            filename = f"/sdcard/voice_{int(time.time())}.mp3"
            audio_data = requests.get(audio_url).content
            with open(filename, "wb") as f:
                f.write(audio_data)
                # subprocess.run(["termux-media-player", "play", filename])
            global voiceover_file 
            voiceover_file = filename            
            print("VoiceOver Created",voice_file)
        except:
            print("❌ Something went wrong. Check internet or API key.")
