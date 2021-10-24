import os
import numpy as np
import torch
from PIL import Image
from pathlib import Path

class PennFudanDataset(torch.utils.data.Dataset):
    def __init__(self, img,mask, transforms=None):
        self.transforms = transforms
        # load all image files, sorting them to
        # ensure that they are aligned
        self.imgs = sorted(list(Path(img).glob('*.png')))
        self.masks= sorted(list(Path(mask).glob('*.png')))

    def __getitem__(self, idx):
        # load images and masks

        img = Image.open(self.imgs[idx]).convert("RGB")
        mask= Image.open(self.masks[idx])

        mask = np.array(mask)
   

        mask[mask!=0]=1
        mask=Image.fromarray(mask)

        # mask = torch.as_tensor(mask, dtype=torch.uint8)

        # instances are encoded as different colors

        if self.transforms is not None:
            img = self.transforms(img)
            mask = self.transforms(mask)
        return img,mask

    def __len__(self):
        return len(self.imgs)
