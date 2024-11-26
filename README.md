## 🌍 Landslide Susceptibility Mapping:
Official reports show that the worldwide death toll due to landslides is in the thousands, with most fatalities being due to rock falls, debris flows, or volcanic debris flows. In this project, we create a program that can generate a Landslide Susceptibility Map of areas with high landslide risk, based off of key geological features of a specific region.

## 🌐 Tools and Resources:
ArcGIS: used to compute geological data for a specific region into a raster image file that can be processed for feature data.
Google Colab: used to explore and process the raster geographical data into a feature array in Python, using libraries like numpy, tifffile, and rasterio
MATLAB: Imported feature data and took advantage of their extensive Mapping and Deep Learning toolboxes

## 🌐 Dataset:
We extracted our data from Mus, Turkey using ArcGIS and its Gradient Metrics tool. After getting the feature data for the given location, we used bucket sampling to reduce the size of the dataset to train our model.
