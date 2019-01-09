---
Title: DEEP OC dogs breed determination
Date: 2018-07-03 10:20
Modified: 2018-11-26
Category: models/toy, library/tensorflow, docker
GitHub: https://github.com/indigo-dc/DEEP-OC-dogs_breed_det
DockerHub: deephdc/deep-oc-dogs_breed_det
License: Apache License 2.0
Summary: A toy example to identify Dog's breed.
---

[![Build Status](https://jenkins.indigo-datacloud.eu:8080/buildStatus/icon?job=Pipeline-as-code/DEEP-OC-org/dogs_breed_det/master)](https://jenkins.indigo-datacloud.eu:8080/job/Pipeline-as-code/job/DEEP-OC-org/job/dogs_breed_det/job/master/)

A toy example to identify Dog's breed, "Dogs breed detector", as example for [DEEPaaS API](https://github.com/indigo-dc/DEEPaaS).

Dogs breed detector is originally forked from [udacity/dogs-project](https://github.com/udacity/dog-project), dataset comes from [dog dataset](https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/dogImages.zip).

The project applies Transfer learning for dog's breed identification, implemented with Tensorflow and Keras:

From a pre-trained model (VGG16 | VGG19 | Resnet50 | InceptionV3 | Xception) the last layer is removed, then a new FC classification layer is added, which is trained. All images first pass through the pre-trained network and converted into the tensor with the shape of the 'before-last' layer of the pre-trained network, into so-called 'bottleneck_features'. These bottleneck_features are used then as input for the FC classification network.
