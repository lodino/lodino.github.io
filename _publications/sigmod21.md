---
title: " Building Fast and Compact Sketches for Approximately Multi-Set Multi-Membership Querying."
collection: publications
permalink: /publication/sigmod21
excerpt: ''
date: 2021-01-01
venue: 'SIGMOD'
# paperurl: 'http://lodino.github.io/files/sigmod21.pdf'
---
Rundong Li, Pinghui Wang, **Jiongli Zhu**, Junzhou Zhao, Jia Di, Xiaofei Yang, Kai Ye.<br>

Given a set S, Membership Querying (MQ) answers whether a query element q ∈ S. It is a fundamental task in areas like database systems and computer networks. In this paper, we consider a more general problem, Multi-Set Multi-Membership Querying (MS-MMQ). Given n sets S<sub>0</sub>, ..., S<sub>n-1</sub>, MS-MMQ answers which sets contain element q. A direct way to address MS-MMQ is to build an MQ structure (e.g., Bloom Filter) for each set. However, the query and space complexities grow linearly with n and become prohibitive for a large n. To address this challenge, we propose a novel Circular Shift and Coalesce (CSC) framework to efficiently achieve approximate MS-MMQ. Instead of building an MQ data structure for each set, the CSC index encodes all n sets into a compact sketch and retrieves only a few bytes in the sketch for a query, which achieves high memory-efficiency and boosts the query speed by several times. CSC is compatible with mainstream data structures for Approximate MQ. We conduct experiments on real-world datasets and results demonstrate that our framework is up to 91.2 times faster and up to 48.9 times more accurate than state-of-the-art methods.
<br>
[Download](http://lodino.github.io/files/sigmod21.pdf)