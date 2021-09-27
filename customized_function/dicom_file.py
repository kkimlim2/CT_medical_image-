import pandas as pd
import numpy as np

import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut

import matplotlib.pyplot as plt
%matplotlib inline

def dicom_2_array(path):
    window_center = -600
    window_width = 1600

    slice = pydicom.read_file(path)
    s = int(slice.RescaleSlope)
    b = int(slice.RescaleIntercept)
    image = s * slice.pixel_array + b

    # apply_voi_lut( )
    slice.WindowCenter = window_center
    slice.WindowWidth = window_width
    image2 = apply_voi_lut(image, slice)

    return image2

df = pd.read_csv('overview.csv')

df_contrast = df.loc[df.Contrast == True,:][:8]
df_none = df.loc[df.Contrast == False,:][:8]

df_subset =pd.concat([df_contrast, df_none]).reset_index(drop=True)

f, ax = plt.subplots(4,4, figsize=(16,20))

for i, data in enumerate(df_subset.values):
    
    path = 'dicom_dir/' + data[-1]
    image = dicom_2_array(path)
    ax[i//4, i%4].imshow(image, cmap='gray')
    ax[i//4, i%4].set_title(f'Age: {data[1]}\nContrast: {data[2]}')

pixel_array = []

for path in df.dicom_name:
    dicom_path = 'dicom_dir/' + path
    array = dicom_2_array(dicom_path)
    
    pixel_array.append(array)
    
df['pixel_array'] = pixel_array

df.to_csv("final_df.csv",index=False)
