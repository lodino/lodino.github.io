---
title: "Crab: Learning Certifiably Fair Predictive Models in the Presence of Selection Bias."
collection: publications
permalink: /publication/crab
excerpt: ''
date: 2022-12-01
venue: 'arXiv'
---
**Jiongli Zhu**, Nazanin Sabri, Sainyam Galhotra, Babak Salimi.<br>

<font size=2>A recent explosion of research focuses on developing methods and tools for building fair predictive models. However, most of this work relies on the assumption that the training and testing data are representative of the target population on which the model will be deployed. However, real-world training data often suffer from selection bias and are not representative of the target population for many reasons, including the cost and feasibility of collecting and labeling data, historical discrimination, and individual biases. In this paper, we introduce a new framework for certifying and ensuring the fairness of predictive models trained on biased data. We take inspiration from query answering over incomplete and inconsistent databases to present and formalize the problem of consistent range approximation (CRA) of answers to queries about aggregate information for the target population. We aim to leverage background knowledge about the data collection process, biased data, and limited or no auxiliary data sources to compute a range of answers for aggregate queries over the target population that are consistent with available information. We then develop methods that use CRA of such aggregate queries to build predictive models that are certifiably fair on the target population even when no external information about that population is available during training. We evaluate our methods on real data and demonstrate improvements over state of the art. Significantly, we show that enforcing fairness using our methods can lead to predictive models that are not only fair, but more accurate on the target population.</font>
<br>
[Paper](https://arxiv.org/abs/2212.10839)