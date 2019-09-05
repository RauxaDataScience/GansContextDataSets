# Gans Context DataSets
GANs Context Datasets is Sponsored by Rauxa

# Current state of GANs
GANs do not have any context when generating images: hence images look like this 

(click on image to view in a bigger size)

<img src="https://github.com/NVIDIA/pix2pixHD/blob/master/imgs/cityscapes_2.jpg" width="350" title="https://github.com/NVIDIA/pix2pixHD/blob/master/imgs/cityscapes_2.jpg"></img>

# Purpose & Code Description
Starting this repository to give GANs context from 3D models to generate realistic images like this 

<img src="https://c8.alamy.com/comp/AJ55D5/cars-driving-down-residential-suburban-road-south-manchester-uk-AJ55D5.jpg" width="350" title="https://c8.alamy.com/comp/AJ55D5/cars-driving-down-residential-suburban-road-south-manchester-uk-AJ55D5.jpg"></img>

3DModel-to-2DImage-Generator.py in this repo reads a 3D models with .STL extensions and uses elevation, azimuth & distance to generate images of the 3D model from every possible position

The code in this repo rotates a 3D model around it's (x, y, z) axis to generate an image of the model from every angle

<img src="https://cdn-images-1.medium.com/freeze/max/1000/1*FOra0GuA7DqhNGOPBwVNzg.png" width="350" title="https://cdn-images-1.medium.com/freeze/max/1000/1*FOra0GuA7DqhNGOPBwVNzg.png">

The purpose of this dataset is to train a GAN model to generate realistic images of a chair from any perspective and to move the research into having GANs generate complex realistic scenes

Realistic scenes will be generatd by GANs with multiple models that have full context of an object i.e. car, trees, road, sky, building, people, etc...

# Chair Gans Context Dataset
For our starting point we chose a 3D model of a chair because it is free, small sized and is quick for generating 2D images

Link to ChairGansContext dataset goes here <>

ChairGansContext dataset is created with the following: 
* Elevation range 0 to 180 degrees, with an increment of 1 degree
* Azimuth range 0 to 360 degrees, with an increment of 1 degree
* Distance range 5 to 25, with an increment of 1

ChairGansContext dataset only has one class "chair"

The naming convention for images: elev(E)-azim(A)-dist(D).png
* Where E has a range from 0 to 180
* Where A has a range from 0 to 360
* Where D has a range from 5 to 25

# Link to 3D Model
Link to the 3D model of the chair [View/Render 3D Model with Browser](https://pinshape.com/items/17795-3d-printed-chair)
