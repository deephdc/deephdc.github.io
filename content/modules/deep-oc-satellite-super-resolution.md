---
Title: DEEP OC Satellite super resolution
Date: 2019-01-01
Category: models, services, library/tensorflow, library/keras, docker
GitHub: https://github.com/deephdc/DEEP-OC-satsr
DockerHub: deephdc/deep-oc-satsr
Cite: https://doi.org/10.1016/j.isprsjprs.2018.09.018
License: Apache License 2.0
Summary: A trained network to super resolve low resolution bands to high resolution in multispectral satellite imagery.
---

[![Build Status](https://jenkins.indigo-datacloud.eu:8080/buildStatus/icon?job=Pipeline-as-code/DEEP-OC-org/DEEP-OC-satsr/master)](https://jenkins.indigo-datacloud.eu:8080/job/Pipeline-as-code/job/DEEP-OC-org/job/DEEP-OC-satsr/job/master)

With the latest missions launched by the European Space Agency (ESA) and National Aeronautics and Space Administration (NASA)
equipped with the latest technologies in multi-spectral sensors, we face an unprecedented amount of data with spatial and
temporal resolutions never reached before.
Exploring the potential of this data with state-of-the-art AI techniques like Deep Learning, could potentially change the
way we think about and protect our planet's resources.

This Docker container contains a plug-and-play tool to perform super-resolution on satellite imagery.
It uses Deep Learning to provide a better performing alternative to classical pansharpening (more details in [1]).

Right now we are supporting super-resolution for the following satellites:

* [Sentinel 2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2) 
* [Landsat 8](https://landsat.gsfc.nasa.gov/landsat-8/)

Some demo images of the super-resolutions performed in non-training data can be found [here](https://github.com/deephdc/satsr/reports/figures). 
If you want to perform super-resolution on another satellite, go to the [training section](https://github.com/deephdc/satsr/blob/master/README.md#train-other-satellites)
to see how you can easily add support for additional satellites. We are happy to accept PRs!

<img class="fit" src="../images/sen2sr.png"/>

**References**

[1]: Lanaras, C., Bioucas-Dias, J., Galliani, S., Baltsavias, E., & Schindler, K. (2018).
[Super-resolution of Sentinel-2 images: Learning a globally applicable deep neural network](https://arxiv.org/abs/1803.04271).
ISPRS Journal of Photogrammetry and Remote Sensing, 146, 305-319.
