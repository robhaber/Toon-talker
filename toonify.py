# -*- coding: utf-8 -*-
"""
Created on Wed May 12 11:08:07 2021

@author: Null
"""

import pretrained_networks
from align_images import align
from project_images import project
import numpy as np
from PIL import Image
import dnnlib.tflib as tflib
from pathlib import Path

def run():
      
    align('raw', 'aligned')
    project('aligned', 'generated')

    blended_path = "https://drive.google.com/uc?id=1H73TfV5gQ9ot7slSed_l-lim9X7pMRiU" 
    ffhq_path = "http://d36zk2xti64re0.cloudfront.net/stylegan2/networks/stylegan2-ffhq-config-f.pkl"
    
    _, _, Gs_blended = pretrained_networks.load_networks(blended_path)
    _, _, Gs = pretrained_networks.load_networks(ffhq_path)
    
    
    latent_dir = Path("generated")
    latents = latent_dir.glob("*.npy")
    for latent_file in latents:
      latent = np.load(latent_file)
      latent = np.expand_dims(latent,axis=0)
      synthesis_kwargs = dict(output_transform=dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=False), minibatch_size=8)
      images = Gs_blended.components.synthesis.run(latent, randomize_noise=False, **synthesis_kwargs)
      Image.fromarray(images.transpose((0,2,3,1))[0], 'RGB').save(latent_file.parent / (f"{latent_file.stem}-toon.jpg"))



