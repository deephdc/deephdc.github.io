---
Title: DEEP OC Seeds Classification
Date: 2019-01-01
Category: services, library/tensorflow, library/lasagne, docker
GitHub: https://github.com/deephdc/DEEP-OC-seeds-classification-tf
DockerHub: deephdc/deep-oc-seeds-classification-tf
Training_files: https://cephrgw01.ifca.es:8080/swift/v1/seeds-tf/
License: Apache License 2.0
Summary: A trained Xception net on Tensorflow/Keras to classify seeds.
---

[![Build Status](https://jenkins.indigo-datacloud.eu:8080/buildStatus/icon?job=Pipeline-as-code/DEEP-OC-org/DEEP-OC-seeds-classification-tf/master)](https://jenkins.indigo-datacloud.eu:8080/job/Pipeline-as-code/job/DEEP-OC-org/job/DEEP-OC-seeds-classification-tf/job/master)

The deep learning revolution has brought significant advances in a number of
fields [1], primarily linked to image and speech recognition. The
standardization of image classification tasks like the [ImageNet Large Scale
Visual Recognition Challenge](http://www.image-net.org/challenges/LSVRC/) [2]
has resulted in a reliable way to compare top performing architectures.

This Docker container contains a trained Convolutional Neural network optimized
for seed identification using images.
The architecture used is an Xception [3] network using Keras on top of Tensorflow.

As training dataset it has been used a collection of images from the
[Royal Botanical Garden](http://www.rjb.csic.es) of Spain. It consists of around
28K images from 743 species and 493 genera.

This service is based in the [Image Classification with Tensorflow](./deep-oc-image-classification-tensorflow.html) model.


**References**

[1]: Yann LeCun, Yoshua Bengio, and Geofrey Hinton. [Deep learning](https://www.cs.toronto.edu/~hinton/absps/NatureDeepReview.pdf). Nature, 521(7553):436–444, may 2015.

[2]: Olga Russakovsky et al. [ImageNet Large Scale Visual Recognition Challenge](https://arxiv.org/abs/1409.0575). International Journal of Computer Vision (IJCV), 115(3):211–252, 2015.

[3]: Chollet, François. [Xception: Deep learning with depthwise separable convolutions](https://arxiv.org/abs/1610.02357) arXiv preprint (2017): 1610-02357.
