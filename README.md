# Cartoonify

The preferred way to run the code is in the Colab notebook provided on the website.

If you choose to run it locally, you will need a GPU, and the following:

```pip install gdown
gdown https://drive.google.com/uc?id=1_UwcQZg3d_3ZzI7TlEuXolpJTjqOe8Ii
mv wav2lip_gan.pth Toon-talker/Wav2Lip/checkpoints/wav2lip_gan.pth
pip install -r requirements.txt
```

Proceed with:
```export FLASK_APP=server.py
flask run
```

Go to localhost:5000 in your browser to find the UI