# GansDataSets
GANs Context Datasets Sponsored by Rauxa

GANs do not have any context when generating images.

Starting this repository to begin giving GANs context from 3D models to generate realistic images.

This repo is a starting point to start generating realistic images with GANs.

Code in this repo reads a 3D models with .STL extensions and uses elevation, azimuth & distance to generate images of the 3D model from every possible position.

Link to ChairGansContext dataset goes here <>

ChairGansContext dataset is created with the following:
   1. Elevation range 0 to 180, with an increment of 1
      1.1 Azimuth range -360 to 360, with an increment of 1
         1.2 Distance range 5 to 25, with an increment of 1
