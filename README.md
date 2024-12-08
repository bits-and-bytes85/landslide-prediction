## 🌍 Landslide Susceptibility Mapping:
Official reports show that the worldwide death toll due to landslides is in the thousands, with most fatalities being due to rock falls, debris flows, or volcanic debris flows. In this project, we create a program that can generate a Landslide Susceptibility Map of areas with high landslide risk, based off of key geological features of a specific region including: distance from roads, distance from geological faults, distance from water streams, land use type, geology type, slope/aspect transformation, site exposure index (HLI), heat load index, compound topographic index (CTI), 2nd derivative slope, Surface relief ratio, Surface area ratio, Roughness, Slope position, Landform, Dissection, Flow direction, Hill shade, Aspect, Plan curvature, Profile curvature, General curvature, Slope, Elevation, Normalized difference vegetation index (NVDI), Rainfall, Standardized precipitation index (SPI), Topographic wetness index (TWI)

## 🛠️ Tools and Resources:
ArcGIS: used to compute geological data for a specific region into a raster image file that can be processed for feature data. <br>
Google Colab: used to explore and process the raster geographical data into a feature array in Python, using libraries like numpy, tifffile, and rasterio <br>
MATLAB: Imported feature data and took advantage of their extensive Mapping and Deep Learning toolboxes

## 📊 Dataset:
We extracted our data from Mus, Turkey using ArcGIS and its Gradient Metrics tool. After getting the feature data for the given location, we used bucket sampling to reduce the size of the dataset to train our model.

## 🌐 Model:
A cascade-forward neural network (CFNN) is a type of feed-forward neural network that has direct connections from the input layer and every previous layer to the following layers. We decided to use cascade-forward neural networks and feed forward networks because of their ability to identify non-linear relationships between features, which is especially important for our goal.

## 📝 Learn about our Process: 
https://docs.google.com/presentation/d/1Kmae23Ln0e6tHmd_ZEhIppsdDnLLcLShhqx0sN2E5i4/edit?usp=sharing

## This project was a part of the Mathworks Challenge Projects Program. 
