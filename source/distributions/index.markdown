---
layout: page
title: "Distributions"
date: 2015-02-08 18:16
comments: true
sharing: truei
tags: distribution, continuous-distribution
footer: true
---

### Gumbel Distribution
Used to model the extreme deviations from the median of distributions.
Given the extreme(max/min) samples from an order statistic, models the
distribution of these extreme values.



####Model


$$f(x) = \frac{1}{\beta} e^{ \frac{x-\alpha}{\beta} - e^{ \frac{x-\alpha}{\beta} }$$



$$F(x) = 1-e^{ -e^{x-\alpha}{\beta} }$$


$$\alpha$$ = the location parameter

$$\beta$$ = the scale parameter

####Mean
$$\mu=\alpha-\gamma\beta$$
where $$\gamma=lim_{n\to\infty}(\sum_{k=1}^n\frac{1}{k}-ln n)$$, a.k.a Euler’s constant

####Variance

$$\sigma^2=\frac{1}{6}\pi^2\beta^2$$


####Application

[1] Given the data for past 10 years’ highest earthquake on richter scale,
model


[2] TODO: The maximum value in a sample of RVs coming from exponential distribution can be modelled using Gumbel distribuion


