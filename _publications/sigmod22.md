---
title: "Interpretable Data-Based Explanations for Fairness Debugging."
collection: publications
permalink: /publication/sigmod22
excerpt: ''
date: 2022-01-01
venue: 'SIGMOD'
---
Romila Pradhan, **Jiongli Zhu**, Boris Glavic, Babak Salimi.<br>

<font size=2>A wide variety of fairness metrics and eXplainable Artificial Intelligence (XAI) approaches have been proposed in the literature to identify bias in machine learning models that are used in critical real-life contexts. However, merely reporting on a model's bias or generating explanations using existing XAI techniques is insufficient to locate and eventually mitigate sources of bias. We introduce Gopher, a system that produces compact, interpretable, and causal explanations for bias or unexpected model behavior by identifying coherent subsets of the training data that are root-causes for this behavior. Specifically, we introduce the concept of causal responsibility that quantifies the extent to which intervening on training data by removing or updating subsets of it can resolve the bias. Building on this concept, we develop an efficient approach for generating the top-k patterns that explain model bias by utilizing techniques from the machine learning (ML) community to approximate causal responsibility, and using pruning rules to manage the large search space for patterns. Our experimental evaluation demonstrates the effectiveness of Gopher in generating interpretable explanations for identifying and debugging sources of bias.</font>
<br>
[Paper](https://dl.acm.org/doi/10.1145/3514221.3517886) | [Code](https://github.com/romilapradhan/gopher) | [Project Website](https://gopher-sys.github.io/)