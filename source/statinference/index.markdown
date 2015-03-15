---
layout: page
title: "statinference"
date: 2015-03-13 06:41
comments: true
sharing: true
footer: true
---

## Probability
- Population quantity summarizing the randomness of a random experiment
- Inherently when we are talking about probability we are talking about population
- Data in hand is just an aid to model this probability
- $\alpha$ quantile: $F(x_\alpha)=\alpha$ About%100(1-\alpha)$ of the observations lie above this point 

## Baye’s Rule
- $P(B|A)=\frac{P(A|B)P(B)}{P(A|B)P(B)+P(A|B^c)P(B^c)}$
- Let
    - + = Test results positive
    - - = Test results positive
    - D = Person has disease in reality
    - D^c = Person does not have disease
- Sensitivity = $P(+|D)$
- Specificity = $P(-|D^c)$
- Positive Predictive Value(PPV) = $P(D|+)$
- Negative Predictive value = $P(D^c|-)$
- Prevalence of Diseae = $P(D)$
- Likelihood ratio: $\frac{P(D|+)}{P(D^c|+)}= \frac{P(+|D)P(D)}{P(+|D^c)P(D^c)}$ 
- Post test odds of D = $DLR_+$ x Pre test odds

## Estimation
- Sample mean is itself a random variable and will have it;s own
distribution, expected value
- The center of this distribution of the sample mean is same as that of observation making
the sample mean an ‘unbiased’ estimator of population mean
- Expected values are properties of distribution
- Sample mean is an estimate of pipulation mean. 
- Center of mass of population = population mean
- Center of mass of observations - Sample mean

