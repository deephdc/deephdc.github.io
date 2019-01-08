Title: DEEP OC Conus Classification (Theano)
Date: 2018-07-03 10:20
Modified: 2018-12-21
Category: models/toy, library/theano, library/lasagne, docker
GitHub: https://github.com/indigo-dc/DEEP-OC-conus-classification
License: Apache License 2.0
Summary: A trained ResNet50 on Theano to classify conus marine snails.

[![Build Status](https://jenkins.indigo-datacloud.eu:8080/buildStatus/icon?job=Pipeline-as-code/DEEP-OC-org/DEEP-OC-plant-classification-theano/master)](https://jenkins.indigo-datacloud.eu:8080/job/Pipeline-as-code/job/DEEP-OC-org/job/DEEP-OC-conus-classification/job/master)


Citizen science has become a powerful force for scientific inquiry, providing researchers with access to a vast array of data points while connecting non scientists to the real process of science. This citizen-researcher relationship creates a very interesting synergy, allowing for the creation, execution, and analysis of research projects. With this in mind, a Convolutional Neural Network using ResNet50 has been trained to identify conus marine snails at species level [1] in collaboration with the Museo de Ciencias Naturales in Madrid [2]. 
The taxonomy of these snails has changed significantly several times during recent years and the introduction of Deep Learning techniques allowing to classify them is a very valuable tool for the experts.This Docker container contains a trained Convolutional Neural network optimized for conus snails identification using images. The architecture used is a Resnet50 [3] using Lasagne on top of Theano. The training dataset has been provided by the Museo de Ciencias Naturales de Madrid and it consists on a dataset containing images of 68 species of conus covering three different regions: Panamic region South African region Western atlantic and mediterranean region.


## References:
[1]: Puillandre, N.; Duda, T.F.; Meyer, C.; Olivera, B.M.; Bouchet, P. (2014). "One, four or 100 genera? A new classification of the cone snails". Journal of Molluscan Studies. 81 (1): 1–23.  doi:10.1093/mollus/eyu055. PMC 4541476. PMID 26300576.
[2]: http://www.mncn.csic.es/
[3]: He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 770-778)
