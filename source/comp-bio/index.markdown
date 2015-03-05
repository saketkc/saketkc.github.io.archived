---
layout: page
title: "comp bio"
date: 2015-03-04 17:21
comments: true
sharing: true
footer: true
---

## Tries
- Each edge labelled with a character coming from a set of alphabets
- Each node has atmost one outgoing edge labelled ‘x’. In other words, outgoing
edges from each node have a unique label
- To reconstruct the suffix read from root to the leaf

We generally add a special character ‘$’ that is included when constructing the suffix trie

## Why add  a terminating character

Without adding a terminating character if we were to walk down
from root to track a suffix, we would not end on a leaf but maybe
somewhere in the middle of internal nodes. So there won’t be a one
to one mapping.

The nodes can beimagined to have some kind of a lable themselves
that spells out the suffix till that point

## Check if some string is a substring of T?

- If S is a substring of T, it is a prefix of some suffix of T
- Search: Start at root -> go to child -> check if next incoming character of S matches
to any children -> Go ahead or fall off
- If you fall off, you fall off for life! S does not occur in T
- If all characters exhausted -> Done!

## Checking if some string is a suffix of T?

- Walk as if searching for a string
- Additional constraint: Last node before exhausitng should be a ‘$’

## Counting number of times
- If we don’t fall off: Number of times = # of lead nodes subrooted at n
- To count number of leaf nodes = DFS

## Finding longest repeated substring of T
- Look for deepest node with more than one child! [DFS again, keep count of number of leaf nodes per node[Not ecaxtly per node though]]
