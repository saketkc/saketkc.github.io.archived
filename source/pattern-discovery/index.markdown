---
layout: page
title: "pattern discovery"
date: 2015-03-15 19:21
comments: true
sharing: true
footer: true
---
Pattern: Set of items/subsequences that occur frequently in a dataset.
Intrinsic property of the dataset

- Absoulte Support: Frequency of X in dataset
- Relative Support: Absolute Support/ Total # of records


## Itemsets to association rules
- Association Rule: $X \Longrightarrow Y(S, c)$
- Support(s): Probability that a transaction contains $X \cup Y$
- Confidence(c): The conditional probability that a transaction containing X also contains Y: $c = \frac{Sup(X \cup Y)}{sup(X)}
- Association rule mining: Find all the rules $X \Longrightarrow Y$ with minimum support and confidence


## Closed Patterns
- Too many frequent patterns(all possible subsets): $2^n-11$
- Closed Patterns: X is closed if X is frequent(it satisfies the minsup threshold) and there exists
no supper pattern $X \subset Y$ with same support as X


