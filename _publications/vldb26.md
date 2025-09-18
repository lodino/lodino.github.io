---
title: "Stress-Testing ML Pipelines with Adversarial Data Corruption."
collection: publications
permalink: /publication/vldb26
excerpt: ''
date: 2026-01-01
venue: 'VLDB'
authors: '<strong>Jiongli Zhu</strong>, Geyang Xu, Felipe Lorenzi, Boris Glavic, Babak Salimi'
---
**Jiongli Zhu**, Geyang Xu, Felipe Lorenzi, Boris Glavic, Babak Salimi.<br>

<font size=2>Structured data-quality issues—such as missing values correlated with demographics, culturally biased labels, or systemic selection biases—routinely degrade the reliability of machine-learning pipelines. Regulators now increasingly demand evidence that high-stakes systems can withstand these realistic, interdependent errors, yet current robustness evaluations typically use random or overly simplistic corruptions, leaving worst-case scenarios unexplored.

We introduce SAVAGE, a causally inspired framework that (i) formally models realistic data-quality issues through dependency graphs and flexible corruption templates, and (ii) systematically discovers corruption patterns that maximally degrade a target performance metric. SAVAGE employs a bi-level optimization approach to efficiently identify vulnerable data subpopulations and fine-tune corruption severity, treating the full ML pipeline, including preprocessing and potentially non-differentiable models, as a black box. Extensive experiments across multiple datasets and ML tasks (data cleaning, fairness-aware learning, uncertainty quantification) demonstrate that even a small fraction (around 5\%) of structured corruptions identified by SAVAGE severely impacts model performance, far exceeding random or manually crafted errors, and invalidating core assumptions of existing techniques. Thus, SAVAGE provides a practical tool for rigorous pipeline stress-testing, a benchmark for evaluating robustness methods, and actionable guidance for designing more resilient data workflows.</font>
<br>
[Paper](https://arxiv.org/pdf/2506.01230)