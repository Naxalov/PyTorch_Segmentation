"""
Plotting utils
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# sample_image_path
MAKS_DIR = Path('data/PennFudanPed/PedMasks')
MASK_LIST = list(MAKS_DIR.glob('*.png'))

def show_segmentation_masks(path,save=False,fname='mask'):
    """Plot maskDraws segmentation masks on given RGB image. 
    The values of the input image should be uint8 between 0 and 255.

    Args:
        path ([type]): [description]
    """
    img = Image.open(path).convert("RGB")
    mask = np.array(img)
    obj_ids = np.unique(img)
    print(obj_ids)
    # convert the PIL Image into a numpy array
    fig, axes = plt.subplots()
    axes.grid(False)
    # axes.axis('off')
    axes.set_axis_off()
    axes.imshow(mask[:,:,0])
    # Bounding box in inches
    # 
    if save:
        plt.savefig(f"{fname}.png",bbox_inches='tight')
    else:
        plt.show()

mask_path = 'data/PennFudanPed/PedMasks/PennPed00013_mask.png'

# show_segmentation_masks(mask_path)

for path in MASK_LIST:
    img = Image.open(path).convert("RGB")
    mask = np.array(img)
    # marge mask to one 
    mask[mask!=0]=1
    obj_ids = np.unique(img)
    print(obj_ids)
    # convert the PIL Image into a numpy array
    fig, axes = plt.subplots()
    axes.grid(False)
    # axes.axis('off')
    axes.set_axis_off()
    axes.imshow(mask[:,:,0])
    # Bounding box in inches
    # 
    print(1)
plt.show()