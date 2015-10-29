---
layout: post
title: "Motif directionality"
date: 2015-08-07 17:37:11 -0700
comments: true
categories: 
---

A motif in a DNA sequence represents a short, recurring pattern that often has biological
implications[1]. They often play role as specific binding sites for transcription factors and other 
proteins. 

While investigating motifs and their sites generated using MEME and FIMO[2], I came across a trivial issue.
MEME is a tool for motif discovery while FIMO outputs the sites where a particular motif is found.

Examplei(this is a modified form of the original FIMO output):


```
chrom	start   stop    strand  score   p-value q-value sequence
chr19	8386315	8386328	+	100	3.04e-07	0.0008	TGGTATCGCGAGAC
chr19	8386317	8386330	-	100	3.05e-08	0.006	CCGTCTCGCGATAC	
```
Motifs are generally described using position weight matrix where each base A,T,G,C takes
a value for 0 to 1, depending on how frequently that base occurs at that position.

If you ignore the strand information, the two sites are not in sync, which should be apparent from their
start and stop coordinates. 

the case of '+' strand is pretty straightforward, but to decipher the start and stop cooridnates for '-' 
strand, required me to draw this diagram:


```                     
                        -->
           0123456789012345
+  5'------TGGTATCGCGAGACGG-------3'
           ||||||||||||||||
-  3'------ACCATAGCGCTCTGCC-------5'
           5432109876543210
           <--

```

To elaborate:

```
0 on the far left of + is position 8386315
0 and the far right of - is position 8386330
The arrows indicate the directionality of motif, yes there is one!
```



# Reference

1. [What are DNA sequence motifs?] (http://www.nature.com/nbt/journal/v24/n4/full/nbt0406-423.html)
2. [MEME Suite: Tools for motif discovery and searching](http://nar.oxfordjournals.org/content/37/suppl_2/W202.full) 
