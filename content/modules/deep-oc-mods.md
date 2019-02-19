---
Title: DEEP OC Massive Online Data Streams
Date: 2019-01-01
Category: services, docker
GitHub: https://github.com/deephdc/DEEP-OC-mods
DockerHub: deephdc/deep-oc-mods
License: Apache License 2.0
Summary: Massive Online Data Streams analysis.
Tosca:
   - title: Mesos (CPU)
     url: https://raw.githubusercontent.com/indigo-dc/tosca-templates/master/deep-oc/deep-oc-mods-mesos-cpu.yml
     inputs:
       - rclone_conf
       - rclone_url
       - rclone_vendor
       - rclone_user
       - rclone_pass
---

[![Build Status](https://jenkins.indigo-datacloud.eu:8080/buildStatus/icon?job=Pipeline-as-code/DEEP-OC-org/DEEP-OC-mods/master)](https://jenkins.indigo-datacloud.eu:8080/job/Pipeline-as-code/job/DEEP-OC-org/job/DEEP-OC-mods/job/master)

This use case analyzes online data streams in order to generate alerts with time-bounded constrains and in real-time.
The main study is focused on building additional intelligent module using NN and DL techniques
in co-function with underlying Intrusion Detection Systems (IDS) supervising traffic networks of compute centers.
Preserving old data for historical purposes, security analysts will be able to supervise generated alerts
and to enhance cyber security [1, 2] for such centers when large IT infrastructures and devices
products a huge amount of data streaming continuously and dynamically.

The principle of the solution is proactive time-series prediction [5] adopting NNs as well as DL to build
prediction models capable to predict next step(s) in near future based on given current and past steps.
The discrepancy between the prediction and the reality gives an indication of anomaly (i.e. anomaly detection).

The challenge of the solution is it aims to scalable edge technologies [4] to support
extensive data analysis and modelling as well as to improve the cyber-resilience by adopting an heuristic approach,
that combines misuse detection in real-time with the building intelligence module using NN and DL.

Current modelling approach using DL techniques [3]:
LSTM (vanilla, stacked, bidirectional, seq2seq encoder/decoder), GRU, CNN, and MLP


**References**

[1]: Bhattacharyya, D.K. and Kalita, J.K., 2013. Network anomaly detection: A machine learning perspective. Chapman and Hall/CRC.

[2]: Dua, S. and Du, X., 2016. Data mining and machine learning in cybersecurity. Auerbach Publications.

[3]: Yann LeCun, Yoshua Bengio, and Geofrey Hinton. [Deep learning](https://www.cs.toronto.edu/~hinton/absps/NatureDeepReview.pdf). Nature, 521(7553):436–444, may 2015.

[4]: Nguyen, G., Nguyen, B.M., Tran, D. and Hluchy, L., 2018. A heuristics approach to mine behavioural data logs in mobile malware detection system. Data & Knowledge Engineering, 115, pp.129-151.

[5]: Tran, N., Nguyen, T., Nguyen, B.M. and Nguyen, G., 2018. A Multivariate Fuzzy Time Series Resource Forecast Model for Clouds using LSTM and Data Correlation Analysis. Procedia Computer Science, 126, pp.636-645.
