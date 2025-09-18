---
title: "Stress-Testing ML Pipelines with Adversarial Data Corruption."
collection: publications
permalink: /publication/kairos25
excerpt: ''
date: 2025-09-01
venue: 'NeurIPS'
authors: '<strong>Jiongli Zhu</strong>*, Parjanya Prajakta Prashant*, Alex Cloninger, Babak Salimi'
---
**Jiongli Zhu**\*, Parjanya Prajakta Prashant\*, Alex Cloninger, Babak Salimi.<br>

<font size=2>Training data increasingly shapes not only model accuracy but also regulatory compliance and market valuation of AI assets. Yet existing valuation methods remain inadequate: model-based techniques depend on a single fitted model and inherit its biases, while algorithm-based approaches such as Data Shapley require costly retrainings at web scale. Recent Wasserstein-based model-agnostic methods rely on approximations that misrank examples relative to their true leave-one-out (LOO) utility. We introduce KAIROS, a scalable, model-agnostic valuation framework that assigns each example a distributional influence score: its contribution to the Maximum Mean Discrepancy (MMD) between the empirical training distribution and a clean reference set. Unlike Wasserstein surrogates, our MMD-based influence admits a closed-form solution that faithfully approximates the exact LOO ranking within O(1/N2) error, requires no retraining, and naturally extends to conditional kernels for unified label- and feature-error detection. Moreover, KAIROS supports efficient online updates: when a new batch of size m arrives, all scores can be updated in O(mN) time, delivering up to 50x speedup without compromising ranking quality. Empirical evaluations on noise, mislabeling, and poisoning benchmarks show that KAIROS consistently outperforms state-of-the-art model-, Shapley-, and Wasserstein-based baselines in both accuracy and runtime. We provide rigorous theoretical guarantees, including symmetry for reproducible rankings and density-separation for interpretable thresholds.</font>
<br>
[Paper](https://arxiv.org/pdf/2506.23799)