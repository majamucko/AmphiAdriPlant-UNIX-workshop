import sys
import numpy as np
from PIL import Image

def merge_images(images_list, out_file="concat_imgs.png"):
    
    imgs = [ Image.open(i) for i in images_list ]
    imgs_comb = np.vstack([np.asarray(i) for i in imgs])
    imgs_comb = Image.fromarray(imgs_comb)
    imgs_comb.save(out_file)

if __name__ == "__main__":
    images_list = sys.argv[1].split(",")
    merge_images(images_list)
