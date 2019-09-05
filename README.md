# Gans Context DataSets
GANs Context Datasets Sponsored by Rauxa

GANs do not have any context when generating images: hence images look like this [pix2pixHD](https://github.com/NVIDIA/pix2pixHD/blob/master/imgs/cityscapes_2.jpg)

Starting this repository to start giving GANs context from 3D models to generate realistic images

Code in this repo reads a 3D models with .STL extensions and uses elevation, azimuth & distance to generate images of the 3D model from every possible position

The code in this repo rotates a 3D model around it's (x, y, z) axis to generate an image of the model from every angle

<img src="https://cdn-images-1.medium.com/freeze/max/1000/1*FOra0GuA7DqhNGOPBwVNzg.png" width="350" title="https://cdn-images-1.medium.com/freeze/max/1000/1*FOra0GuA7DqhNGOPBwVNzg.png">

The purpose of this dataset is to train a GAN model to generate realistic images of a chair from any perspective and to move the research into having GANs generate complex realistic scenes

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


Link to the 3D model of the chair [View/Render 3D Model with Browser](https://pinshape.com/items/17795-3d-printed-chair)
