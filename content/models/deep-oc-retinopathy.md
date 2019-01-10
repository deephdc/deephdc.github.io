---
Title: DEEP OC Retinopathy
Date: 2019-01-01
Category: models, docker
GitHub: https://github.com/itokeiic/retinopathy_test
DockerHub: itokeiic/deep-oc-retinopathy_test
Dataset: https://www.kaggle.com/c/diabetic-retinopathy-detection/data
License: Apache License 2.0
Summary:
---

This use case is concerned with the classification of biomedical images (of the retina) into five disease categories or stages (from healthy to severe) using a deep learning approach.  This is a TensorFlow example implementation. The network is a standard residual network model with 50 layers (ResNet50). The model used in this use case was made available by Niklas Köhler: https://gitlab.com/niklaskoehler/retinopathy_model

Retinopathy is a fast-growing cause of blindness worldwide, over 400 million people at risk from diabetic retinopathy alone [Yau2012]. The disease can be successfully treated if it is detected early. Colour fundus retinal photography uses a fundus camera (a specialized low power microscope with an attached camera) to record color images of the condition of the interior surface of the eye, in order to document the presence of disorders and monitor their change over time. Specialized medical experts interpret such images and are able to detect the presence and stage of retinal eye disease such as diabetic retinopathy. However, due to a lack of suitably qualified medical specialists in many parts of the world a comprehensive detection and treatment of the disease is difficult. This use case focuses on a deep learning approach to automated classification of retinopathy based on color fundus retinal photography images [Eul2017].

A trained model can be accessed via the DEEPaaS API web interface.  The user provides the retina image and the trained model will return the probability of the five categories from healthy 'dr0' to the most severely pathological 'dr4'.

In the DEEPaaS API,
click on the "POST" frame,
click on the "Browse" button to select the image to classify.
Type "retinopathy_test" without quotes in the "model_name" field.
Click "Execute".

Look into the "response body" window.  For example,

[
  "{'/tmp/tmpTuMwqe': {u'probabilities': array([[0.02030031, 0.00091151, 0.04386754, 0.04448699, 0.89043367]],\n      dtype=float32), u'classes': array([4])}}"
]

means that the classification for the tested image is category 'dr4' with a probability of about 0.89.

References
[Yau2012] https://doi.org/10.2337/dc11-1909
[Eul2017] https://doi.org/10.1038/s41467-017-00623-3
