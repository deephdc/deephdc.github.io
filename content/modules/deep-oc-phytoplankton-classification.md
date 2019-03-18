---
Title: DEEP OC Phytoplankton
Date: 2019-01-01
Category: services, library/tensorflow, library/keras, docker
GitHub: https://github.com/deephdc/DEEP-OC-phytoplankton-classification-tf
DockerHub: deephdc/deep-oc-phytoplankton-classification-tf
Training_files: https://cephrgw01.ifca.es:8080/swift/v1/phytoplankton-tf/
License: Apache License 2.0
Summary: A trained Xception net on Tensorflow/Keras to classify phytoplankton.
---

[![Build Status](https://jenkins.indigo-datacloud.eu:8080/buildStatus/icon?job=Pipeline-as-code/DEEP-OC-org/DEEP-OC-phytoplankton-classification-tf/master)](https://jenkins.indigo-datacloud.eu:8080/job/Pipeline-as-code/job/DEEP-OC-org/job/DEEP-OC-phytoplankton-classification-tf/job/master)

Citizen science has become a powerful force for scientific inquiry, providing researchers with access to a vast array of
data points while connecting non scientists to the real process of science. 
This citizen-researcher relationship creates a very interesting synergy, allowing for the creation, execution, and analysis
of research projects. With this in mind, a Convolutional Neural Network has been trained to identify phytoplankton in
collaboration with the [Vlaams Instituut voor de Zee](http://www.vliz.be/).

This Docker container contains a trained Convolutional Neural network optimized
for phytoplankton identification using images.
The architecture used is an Xception [1] network using Keras on top of Tensorflow.

As training dataset we have used a collection of images from the [Vlaams Instituut voor de Zee](http://www.vliz.be/)
which consists of around 650K images from 60 classes of phytoplankton.

<img class="fit" src="../images/phytoplankton.png"/>

This service is based in the [Image Classification with Tensorflow](./deep-oc-image-classification-tensorflow.html) model.


**References**

[1]: Chollet, François. [Xception: Deep learning with depthwise separable convolutions](https://arxiv.org/abs/1610.02357)
arXiv preprint (2017): 1610-02357.
