---
Title: DEEP OC Image Classification (Tensorflow)
Date: 2018-11-15
Category: models, library/tensorflow, library/keras, docker
GitHub: https://github.com/deephdc/DEEP-OC-image-classification-tf
DockerHub: deephdc/deep-oc-image-classification-tf
License: Apache License 2.0
Summary: A tool to train an image classifier on your data
---

[![Build Status](https://jenkins.indigo-datacloud.eu:8080/buildStatus/icon?job=Pipeline-as-code/DEEP-OC-org/image-classification-tf/master)](https://jenkins.indigo-datacloud.eu:8080/job/Pipeline-as-code/job/DEEP-OC-org/job/image-classification-tf/job/master/)

The deep learning revolution has brought significant advances in a number of
fields [1], primarily linked to image and speech recognition. The
standardization of image classification tasks like the [ImageNet Large Scale
Visual Recognition Challenge](http://www.image-net.org/challenges/LSVRC/) [2]
has resulted in a reliable way to compare top performing architectures.

This Docker container contains the tools to train an image classifier on your custom
dataset. It is a highly customizable tool  that let's you choose between tens of different [top performing
arquitectures](https://github.com/keras-team/keras-applications) and training parameters.


### References

[1]: Yann LeCun, Yoshua Bengio, and Geofrey Hinton. [Deep learning](https://www.cs.toronto.edu/~hinton/absps/NatureDeepReview.pdf). Nature, 521(7553):436–444, may 2015.

[2]: Olga Russakovsky et al. [ImageNet Large Scale Visual Recognition Challenge](https://arxiv.org/abs/1409.0575). International Journal of Computer Vision (IJCV), 115(3):211–252, 2015.
