---
Title: DEEP OC Plant Classification
Date: 2019-01-01
Category: services, library/tensorflow, library/lasagne, docker
GitHub: https://github.com/deephdc/DEEP-OC-image-classification-tf
DockerHub: deephdc/deep-oc-plant-classification-tf
Training_files: https://cephrgw01.ifca.es:8080/swift/v1/plants-tf/
License: Apache License 2.0
Summary: A trained Xception net on Tensorflow/Keras to classify plants.
---

[![Build Status](https://jenkins.indigo-datacloud.eu:8080/buildStatus/icon?job=Pipeline-as-code/DEEP-OC-org/DEEP-OC-plant-classification-tf/master)](https://jenkins.indigo-datacloud.eu:8080/job/Pipeline-as-code/job/DEEP-OC-org/job/DEEP-OC-plant-classification-tf/job/master)

The deep learning revolution has brought significant advances in a number of
fields [1], primarily linked to image and speech recognition. The
standardization of image classification tasks like the [ImageNet Large Scale
Visual Recognition Challenge](http://www.image-net.org/challenges/LSVRC/) [2]
has resulted in a reliable way to compare top performing architectures.

The use of deep learning for plant classification is not novel [3, 4] but has
mainly focused in leaves and has been restricted to a limited amount of
species, therefore making it of limited use for large-scale biodiversity
monitoring purposes.

This Docker container contains a trained Convolutional Neural network optimized
for plant identification using images.
The architecture used is an Xception [5] network using Keras on top of Tensorflow.

As training dataset it has been used the great collection of images which are
available in PlantNet under a Creative-Common AttributionShareAlike 2.0
license. It consists of around 250K images belonging to more than 6K plant
species of Western Europe. These species are distributed in 1500 genera and 200
families.

A detailed article about this network and the results obtained with it can be found in [6].

This service is based in the [Image Classification with Tensorflow](./deep-oc-image-classification-tensorflow.html) model.


**References**

[1]: Yann LeCun, Yoshua Bengio, and Geofrey Hinton. [Deep learning](https://www.cs.toronto.edu/~hinton/absps/NatureDeepReview.pdf). Nature, 521(7553):436–444, may 2015.

[2]: Olga Russakovsky et al. [ImageNet Large Scale Visual Recognition Challenge](https://arxiv.org/abs/1409.0575). International Journal of Computer Vision (IJCV), 115(3):211–252, 2015.

[3]: Sue Han Lee, Chee Seng Chan, Paul Wilkin, and Paolo Remagnino. [Deep-plant: Plant identification with convolutional neural networks](https://arxiv.org/abs/1506.08425), 2015.

[4]: Mads Dyrmann, Henrik Karstoft, and Henrik Skov Midtiby. [Plant species classification using deep convolutional neural network.](https://www.sciencedirect.com/science/article/pii/S1537511016301465) Biosystems Engineering, 151:72–80, 2016.

[5]: Chollet, François. [Xception: Deep learning with depthwise separable convolutions](https://arxiv.org/abs/1610.02357) arXiv preprint (2017): 1610-02357.

[6]: Heredia, Ignacio. [Large-scale plant classification with deep neural networks.](https://arxiv.org/abs/1706.03736) Proceedings of the Computing Frontiers Conference. ACM, 2017.
