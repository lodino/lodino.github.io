---
title: "Fine-Tuning Without Forgetting via Loss-Adaptive Learning Rates"
collection: publications
permalink: /publication/finch26
excerpt: ''
date: 2026-05-19
venue: 'arXiv preprint'
preprint: true
authors: 'Parjanya Prajakta Prashant*, <strong>Jiongli Zhu*</strong>, Aldan Creo, Babak Salimi'
author_note: '* Equal contribution.'
paperurl: 'https://arxiv.org/abs/2605.20005'
content_heading: 'Summary'
---

FINCH adjusts the learning rate using the current training loss to limit catastrophic forgetting during language-model fine-tuning. It takes smaller steps on high-loss batches and increases the learning rate as training progresses, while retaining the original training objective. The approach is motivated by a bound relating per-step forgetting to the learning rate and training loss. Experiments cover knowledge acquisition, science, and low-resource language adaptation, evaluating both new-task performance and retention of pretrained capabilities.
