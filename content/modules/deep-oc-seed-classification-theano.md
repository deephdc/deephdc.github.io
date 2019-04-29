---
Title: DEEP OC Seeds Classification (Theano)
Date: 2018-09-16
Category: deprecated/services, library/theano, library/lasagne, docker
GitHub: https://github.com/deephdc/DEEP-OC-seeds-classification
DockerHub: deephdc/deep-oc-seeds-classification
Training_files: https://cephrgw01.ifca.es:8080/swift/v1/seeds/
License: Apache License 2.0
Summary: A trained ResNet50 on Theano to seeds.
---

[![Build Status](https://jenkins.indigo-datacloud.eu:8080/buildStatus/icon?job=Pipeline-as-code/DEEP-OC-org/DEEP-OC-seeds-classification/master)](https://jenkins.indigo-datacloud.eu:8080/job/Pipeline-as-code/job/DEEP-OC-org/job/DEEP-OC-seeds-classification/job/master)

---

**This service is deprecated. Please refer to the [newer Tensorflow version](./deep-oc-seed-classification.html)**

---

The deep learning revolution has brought significant advances in a number of
fields [1], primarily linked to image and speech recognition. The
standardization of image classification tasks like the [ImageNet Large Scale
Visual Recognition Challenge](http://www.image-net.org/challenges/LSVRC/) [2]
has resulted in a reliable way to compare top performing architectures.

This Docker container contains a trained Convolutional Neural network optimized
for seed identification using images. The architecture used is a Resnet50 [3]
using Lasagne on top of Theano.

As training dataset it has been used a collection of images from the
[Royal Botanical Garden](http://www.rjb.csic.es) of Spain. It consists of around
28K images from 743 species and 493 genera.


**References**

[1]: Yann LeCun, Yoshua Bengio, and Geofrey Hinton. [Deep learning](https://www.cs.toronto.edu/~hinton/absps/NatureDeepReview.pdf). Nature, 521(7553):436–444, may 2015.

[2]: Olga Russakovsky et al. [ImageNet Large Scale Visual Recognition Challenge](https://arxiv.org/abs/1409.0575). International Journal of Computer Vision (IJCV), 115(3):211–252, 2015.

[3]: He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 770-778)
