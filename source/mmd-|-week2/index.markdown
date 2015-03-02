---
layout: page
title: "mmd | week2"
date: 2015-02-15 18:24
comments: true
sharing: true
footer: true
---

## Set Simialarity
- Many data mining problems boil down to finding similar sets

## Document Simialarity
- Document => Shingling(Set of strings of length k) => Minhashing(Signtaures, short integeres representing words) => LSH
- shingles: K-shingle = Sequence of k characters that appears in the document
- k = 2, abcab = {ab, bc, ca}i
- Changing a word affects only k shingles within k distance from the word
- Reordering paragraphs also would affect the 2k si


## Simarilty
- Jaccard similarity: Sim(C1,C2) =$$\frac{C1 \cap C2}{C1 \cup C2 }
- Rows =elements of universal set(set of all k-shingles)
- Columns=setssi
- 1 in (i,j) if i is a member of j
- Column similarity = Jaccard similarity of sets of rows with entry 1
- E.g C1=[0,1,1,1,1,0] C2=[1,0,0,1,1,1]. sim(C1,C2)=2/5
- Type of rows:
    row C1 C2
    a 1 1
    b 1 0
    c 0 1
    d 0 0
- Sim (C1,C2)= a/a+b+c

##Minhashing

- Minhash = h(C) = Number of first row (among permuted rows) such that Column ‘C’ has 1
- Signaure of a column = Use several hash functions to create a signature for each column
- Signaure Matrix: Rows represent min hash values of columns represented 

## Minhashing example
3 1 0 0 1
2 0 1 1 0
1 1 0 0 0
4 0 1 1 1

Think!
Minhash 1 2 2 3

