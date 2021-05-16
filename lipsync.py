import os 
import speech

from img2mp4 import img2mp4
import json


def run():

    req_data = json.load(open('static/uploads/input.json'))
    img2mp4('static/uploads/input_01-toon.jpg', 'vid_out.mp4')

    if req_data['gender'] == 'male':
        speech.txt_to_male(req_data['text'], 'speech_out.wav')
    else:
        speech.txt_to_female(req_data['text'], 'speech_out.wav')

    

    os.system("cd Wav2Lip && python3 inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face '../vid_out.mp4' --audio '../speech_out.wav' --pads 0 40 0 0")
 #   os.system("cd Wav2Lip && python3 inference.py --checkpoint_path  https://iiitaphyd-my.sharepoint.com/:u:/g/personal/radrabha_m_research_iiit_ac_in/EdjI7bZlgApMqsVoEUUXpLsBxqXbn5z8VTmoxp55YNDcIA?e=n9ljGW --face '../vid_out.mp4' --audio '../speech_out.wav' --pads 0 40 0 0")

    os.system("mv Wav2Lip/results/result_voice.mp4 static/output/video.mp4")

run()