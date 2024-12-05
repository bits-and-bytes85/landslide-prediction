# Breakthrough Tech MIT Project 2024 - Create Feature Matrix

import numpy as np
from scipy.io import savemat
import tifffile as tf
import os
import glob
import pandas as pd

def get_files_with_extension(folder_path, extension):
    """Gets all files with the specified extension from the given folder."""

    files = []
    for file in glob.glob(os.path.join(folder_path, f"*.{extension}")):
        files.append(file)
    return files

folder_path = "../RasterResults"
extension = "tif"
files = get_files_with_extension(folder_path, extension)

# load tiff files 
tiffs = []

for file in files:
    with tf.TiffFile(file) as tif:
        # Get the first page of the TIFF file
        page = tif.pages[0]

        # Get the pixel values as a numpy array
        image_data = page.asarray()

        tiffs.append(image_data)

# init table (2d array)
xs = tiffs[0].shape[0]
ys = tiffs[0].shape[1]

datatable = np.zeros((xs * ys, len(tiffs))) 
coords_x = np.zeros((xs * ys, 1))
coords_y = np.zeros((xs * ys, 1))

# iterate through each pixel (2 for loops- one for x, one for y)
    # make a row on the table 
    # take the value at each pixel coord and put it in the feature row and column
    # continue until full array is filled

for idx, feature in enumerate(tiffs):
    row = 0
    for x in range(xs):
        for y in range(ys):
            if (idx == 0):
                coords_x[row][0] = x
                coords_y[row][0] = y

            if (feature[x][y] != 0):
                # print(row)
                # print(feature[x][y])
                datatable[row][idx] = feature[x][y]
            row += 1 


# creating a pandas table to be exported to mat file.
features = []
feature_names = []
for file in files:
    file_name = file.replace(folder_path + "\\", "")
    file_name = file_name.replace(".tif", "")
    feature_names.append(file_name)
    features.append(file_name)

pandastable = pd.DataFrame(datatable, columns=features)
pandastable.insert(0, 'Coord y', coords_y)
pandastable.insert(0, 'Coord x', coords_x)

pandastable_nozeroes = pandastable.copy()
to_remove = []


# removes rows with zeroes in all features, to clean out irrelevant pixels.
bool = True
for index, row in pandastable.iterrows():
    for name in feature_names:
        bool = bool or (pandastable.loc[index, name] == 0)
    if (bool):
        to_remove.append(index)

pandastable_nozeroes = pandastable_nozeroes.drop(to_remove)



# # Save the dictionary to a .mat file
savemat('data_nozeroes_new.mat', {'df': pandastable_nozeroes})
# if you would not like to delete rows with zeroes in them and get the whole data set... 
# replace pandastable_nozeroes with pandastable.

print("FINISHED")