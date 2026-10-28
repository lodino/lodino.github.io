---
title: "UClean: Uncertainty-Aware Data Cleaning for Machine Learning"
collection: publications
permalink: /publication/uclean27
excerpt: ''
date: 2027-01-01
venue: 'SIGMOD'
featured: true
authors: 'Kaiyuan Hu*, <strong>Jiongli Zhu*</strong>, Boris Glavic, Babak Salimi'
content_heading: 'Abstract'
---

Data cleaning is a costly step in ML pipelines, and in many real settings, corrupted or missing training values cannot be uniquely recovered. Instead, each dirty cell may only be constrained to a feasible range, and revealing its true value requires an external oracle. Cleaning is therefore a budgeted decision problem. A natural idea is to directly optimize for validation performance. However, using held-out validation labels to choose training-data values can severely overfit to the validation set. We instead study uncertainty-aware cleaning: under a fixed oracle budget, our framework UClean determines which uncertain training cells should be resolved to maximally reduce validation-loss uncertainty. UClean models dirty training data with possible-world semantics, where different feasible repairs can induce different trained models and validation outcomes. To avoid enumerating this space, UClean uses abstract interpretation to propagate uncertainty through learning to obtain a symbolic validation-loss expression. It then performs sensitivity analysis on this symbolic objective to estimate each cell's contribution to validation-loss uncertainty, yielding an objective-aware cleaning order without repeated retraining. Experiments on multiple datasets show that UClean recovers test AUC faster than representative baselines.
