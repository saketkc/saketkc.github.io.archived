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

## Number of nodes in a suffix trie
-Motivation: Imagine `aaaa$` Then there is a branch point at each node=10 nodes in total= 2m+1 nodes=1 root, m node with outgoing to $
and m with outgoing to a => 2m+1(Linear)
- Consider `(a)^n(b)^n`: 
    - 1 root
    - n nodes for b...
    - n nodes along a-a-a chain
    - n nodes for each n noded a-a-a chain above with b
    - 2n+1 leaves(obvious 2n$+$)

    In total 2n=m 
    and Total = 2n+1+n^2+2n+1 = n^2+4n+2

## Suffix tree bound on size
- Depth = O(m) = length of longest substring = m+1
- Width  = Max Number of distinct substrings till that length  <= m
- Order of size = O(m^2)

## Problem: REduce Suffix trie size
- Compress non branching paths into single edge. The label is concatenated edgel labels. All internal nodes guaranteed 
to have more than one children
- Post edge label compression(Generate a tree(like balanced binary tree) from trie):
    - Number of leaves: m
    - Number of internal nodes(at max, since this is like a balanced binary tree): m-1
    - Total O(2m-1)? NO
    - the label lengths are still growing so still O(m^2)
    - Solution: Use information from T to encode (offset, length) information throwing away
    edge labels
    -  LEaves hold offsets of the whole suffix that the leaf corresponds to

## Edge label compressed Suffix tree
- Node depth: Number of edges from root to the destination node(Trivial)
- Label Depth: Total length of edge labels for edges on path from root to node = Summation of ‘lengths’ from (offset, length) tuple till tbhat node

## Space Caveat: O(m) is really O(m) now?
- Space taken bhy edge lables = O(m) since it is storing a integer tuple
- The integer storage is 64 bits is practical for all purposes
- 32 bits cannot store hg19 suffix tree
## Building
- 1. Build suffix trie => Merge nodes with one children, relabel. But wasting O(m^2) space!
- 2. Build  a single edge tree first for the longest suffix => Augment to include 2nd longest
=> Augment to include 3rd longest 

## Suffix tree: Searching for substring
- Kind of trivials since you need to start at root, go to next child with label matching to the first character of S
and walk down
- O(n) Stepe1: Walk down the matching path
- O(k) as it’s a balanced subtree so number of leaf nodes is same as internal noes in the subtree Step2: Match found: Visit all leafs below, reporting each leaf offset as match offset
- Order(n+k)

## Longest common substring
- S1$1S2$2
- Point to note: annoate each node depending on whether the leaves below it includesuffixes of S1, S2 or both
- The deepest node with both S1, S2 represents the longest common substring
