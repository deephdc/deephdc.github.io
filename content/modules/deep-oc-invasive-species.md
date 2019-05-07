---
Title: DEEP OC Invasive Species
Date: 2019-05-03
Category: services, library/tensorflow, library/keras, docker
GitHub: https://github.com/deephdc/DEEP-OC-invasive-species-tf
DockerHub: deephdc/deep-oc-invasive-species-tf
Training_files: https://cephrgw01.ifca.es:8080/swift/v1/invasoras/
License: Apache License 2.0
Summary: A trained Xception net on Tensorflow/Keras to classify plant invasive especies
---

[![Build Status](https://jenkins.indigo-datacloud.eu:8080/buildStatus/icon?job=Pipeline-as-code/DEEP-OC-org/DEEP-OC-invasive-species-tf/master)](https://jenkins.indigo-datacloud.eu:8080/job/Pipeline-as-code/job/DEEP-OC-org/job/DEEP-OC-invasive-species-tf/job/master)

The natural parks are the most precious protected spaces and some of the most visited place by the citizens, containing the most representative and singular geo-biodiversity elements in the country. Thus, the preservation of its elements implies to keep them safe from their main thread nowadays: the invasive species. For this, the development of early alerts are the most efficient solution since they allow the experts to react and launch the corresponding measures to avoid the complete erradication once the species have been established. One possible approach would be to provide the natural parks visitors with mobile applications trained to identify the invasive species. The citizens themselves would be the ones taking pictures, identifying the species and sending them (together with the GPS location) to a centralized system controlled by experts who would confirm the find, update the image database to improve the neural network performance and start the corresponding protocole to eliminate the invasive species.

This Docker container contains a trained Convolutional Neural network optimized for invasive plants identification using images. The architecture used is an Xception [1] network using Keras on top of Tensorflow.

As training dataset it has been used a preliminary collection of images taken in the spanish Ordesa National Park and Monte Perdido.





**References**

[1]: Chollet, François. [Xception: Deep learning with depthwise separable convolutions](https://arxiv.org/abs/1610.02357) arXiv preprint (2017): 1610-02357.

