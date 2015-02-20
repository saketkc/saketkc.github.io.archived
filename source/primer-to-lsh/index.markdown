---
layout: page
title: "Primer to LSH"
date: 2015-01-02 19:31
comments: true
sharing: true
footer: true
---

## $$D_2$$
The $$D_2$$ statistic is characterized by number of matches of length k between any two sequences $$A$$ and $$B$$ allowing upto $$t$$ mis
matches. Sequences A and B are represented as $$(A_1, A_2, A_3, ... A_n_A) and (B_1, B_2, B_3, ...., B_n_B)$$ respectively.

More generally $$D_2$$ is characterized by $$(n_A, n_B, k, t, \eta)$$ where:
$$n_A$$ = Total length of nucleotides in sequence A
$$n_B$$ = Total length of nucleotides in sequence B
k = length of matches
t = length of allowable mismatches



## Jaccard Similarity

Jaccard similarity: Notion of similarity that associates similarity of sets with the relative size of their intersection
A comman example would be determining if a document is a plagiarised copy of another, if not identical. The technique 
used to convert these documents to a set intersection problem is referred to as “shingling”


Jaccard similarity = $$ jSIM(S,T) = \frac{ |S \cap T| }{ |S \cup T| } $$

Let $$S=[1,2,3]$$ and $$T=[2,3,4,5,6]$$ then $$SIM(S,T)=\frac{2}{6}$$


#### Jaccard distance

$$D_J(A,B) = 1 - jSIM(A,B)$$ and is a distance metric.

## Cosine Similarity

As the name suggests, cosine similarity relies on taking cosines between two given vectors to infer the similarity.
The range for cosine is [-1,1] When used in positive space it is [0,1]

Thinking in terms of document matching, a document can be represented as a vector of words, where the “words” form the unit vectorsand the 
associated scalar is the frequency of the word.

### Cosine distance

$$D_C(A,B)=1-S_C(A,B)$$ but is not a metric since it does not follow the triangular inequality $$d(x,z) \leq d(x,y)+d(y,z)$$, neither does it
follow the coincidence axiom $$d(x,y)=0 iff\ x=y$$ since cosine(x,y)=0 if $$x \perp y$$

$$cSIM(A,B) = cos(\theta) =  \frac{A.B}{|A||B|}$$

$$Range(cSIM(A,B))=[-1,1]$$ where -1 means entirely opposite, 1 means ‘exactly similar’. In a positive space, such as when using the frequencies of
words, the range is limited to $$[0,1]$$

## Angular similarity
For vectors in positive+negative space: 

$$aSIM(A,B)=1-\frac{cos^{-1}(cSIM(A,B))}{\pi}$$


For vectors in positive space(only): 

$$aSIM(A,B)=1-\frac{2.cos^{-1}(cSIM(A,B))}{\pi}$$


### Angular difference coefficient
$$D_A(A,B) = 1-aSIM(A,B)$$ and *is* a distance metric


## Tanimoto similarity

[A computer program for Classifying plants](http://www.sciencemag.org/content/132/3434/1115) describes Tanimoto similarity using bit arrays
where each bit is a representative of the presence(1) or absence(0) of the plant. 

$$tSIM(A,B)=\frac{\sum_i(A_i \land B_i)}{\sum_i(A_i \lor B_i)}$$

Thus tanimato similarity is simply defined as the ratio of total number of common bits set to 1 to the total number of bits set to 1 in either(or both) of the vectors.


## Tanimato similarity v/s Jacard similarity

A = [“mary”, “little”, “girl”]
B = [“mary”, “had”, “a”, “little”, “lamb”, “which”, “bleat”]

$$jSIM(A,B) = \frac{2}{8}$$

Now just similar to the plants context for Tanimato similarity, our plants are: [“mary”, “had”, “a”, “little”, “lamb”, “which”, “bleat”, “girl”]
and thus, the corresponding bit vectors are:
A = [1,0,0,1,0,0,0,1]
B = [1,1,1,1,1,1,1,0]

$$tSIM(A,B) = \frac{1+0+0+1+0+0+0+0}{1+1+1+1+1+1+1+1} = \frac{2}{8}$$

Also note, $$ |A| = 3$$, $$|B| = 7$$, and $$|A\cap B| = 2 $$

So $$jSIM, tSIM$$ are in fact *one and the same*

In fact if jacard similarity were to be written for bit arrays:

$$jSIM(A,B) = \frac{|A \cap B|}{A \cup B|} = \frac{A .B}{|A| + |B| - |A \cap B|}$$

where $$A.B = \sum_i(A_iB_i) = A \cup B$$
denominator is trivial.

More generally, tanimato or jacard simialruty is given by:

$$SIM(A,B) = \frac{A.B}{||A||^2 + ||B||^2 - A.B}$$

### Tanimato distance

$$D_T(A,B)=-log_2(T(A,B))$$

To quote wikipedia [Wikipedia](http://en.wikipedia.org/wiki/Jaccard_index#Tanimoto_similarity_and_distance)
{% blockquote %}

This coefficient is, deliberately, not a distance metric. It is chosen to allow the possibility of two specimens, which are quite different from each other, to both be similar to a third. It is easy to construct an example which disproves the property of triangle inequality.
{% endblockquote %}

*Wrong* definition:


Tanimato distance is often confused with Jacard distance and maybe wrongly defined as $$D_T(A,B)=1-tSIM(A,B)$$, thus leading to the wrong conclusion that tanimato 
distance is indeed a distance metric, when it is not.


$$D_J(A,B) = 1-\frac{|A \cap B|}{|A \cup B|} = \frac{|A \cup B| - |A \cap B|}{A \cup B|} = \frac{|A| + |B| - 2|A \cap B|}{|A| + |B| - |A \cap B|}$$

## A warmup problem
Taken from [Chapter 3 of Ullman’s Mining Massive Datasets](http://infolab.stanford.edu/~ullman/mmds/booka.pdf)
{% blockquote %}
Suppose we have a universal set U of n elements, and we
choose two subsets S and T at random, each with m of the n elements. What
is the expected value of the Jaccard similarity of S and T
{% endblockquote %}

### Solution:


$$P(S \cap T = k) = \frac{ {m \choose k} * {(n-m) \choose (m-k)} }{ {n \choose m} * {n \choose m} }$$

$$ jSIM_k(S,T) = \frac{k}{m + (m-k)} $$

Thus $$ E(jSIM(S,T)) = \sum_k jSIM_k * P(S\cap T = k) = \sum_{k=1}^{m} \frac{k}{2m-k} *  \frac{ {m \choose k} * {(n-m) \choose (m-k)} }{ {n \choose m} * {n \choose m} }$$

### ToDO: LSH
