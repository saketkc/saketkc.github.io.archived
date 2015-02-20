---
layout: post
title: "library size, fragment size, insert size"
date: 2014-10-12 13:51:01 -0700
comments: true
categories: bioinformatics, tutorial
---

Bioinformatics has always been plagued with terms with multi-definitions for the same term. The FastQ format for example remained undocumented until Peter Cock et al. published [The Sanger FASTQ file format for sequences with quality scores, and the Solexa/Illumina FASTQ variants](http://nar.oxfordjournals.org/content/38/6/1767.long) 

I will try to cover a detailed explanation of the following terms , which I have often found to be confusing, thanks to the lack of cohesiveness in Bioinformatics:

* library size
* fragment size
* insert size



[SAMv1 specification](http://samtools.github.io/hts-specs/SAMv1.pdf) defines a 'TLEN' term in the alignment section:
> TLEN: signed observed Template LENgth. If all segments are mapped to the same reference, the unsigned observed template length equals the number of bases from the leftmost mapped base to the rightmost mapped base. The leftmost segment has a plus sign and the rightmost has a minus sign. The sign of segments in the middle is undefined. It is set as 0 for single-segment template or when the information is unavailable.

Going by this definition the 'insert size' *should* mean: The total length of the original *piece*  being sequenced(without adapters!).
Let's pick an example from [Seqanswers](http://seqanswers.com/forums/showthread.php?t=13098), slightly modified here. Reads R_1 and R_2 are paired end reads, sequencing the same sequence from two opposite ends. We want to sequence the '*Piece to be Sequenced*'.

    Piece to be Sequenced:                       |=====50=====|==========150==========|=====50=====|
    Fragment=Piece + Sequencing Adapters: |~~20~~|=====50=====|==========150==========|=====50=====|~~20~~|    
    Reads(Paired End):                           |----------->|                       |<-----------|    
                                                      R_1                                  R_2
    Inner Mate Distance:                                      |==========150==========|         

 Sequencing chops the DNA into shorter *pieces*, and these *pieces* are ligated with adapter sequences.Though we started with ```Piece to be sequenced``` it was ligated with sequencing adapters on both sides.  
The original sequence that was supposed to be sequenced was (50+150+50=) 250 bp long. However while the DNA was cut, the ligation step added extra bases at both ends of this *piece* so that it is now (20+50+150+50+20=) 290 bp long and this 'piece+ligated sequence adapters' are called 'Fragment'(This is the reason I chose the word *'piece'* to denote the part of DNA to be sequenced). Generally sequencing begins after adapter sequences. This is the reason R_1 and R_2 do not cover the 20 bp adapter sequences. In any case I assume the reads have been trimmed to remove the adapter sequences. The 150 bp sequence that is left *unsequenced* here is the distance between mate pairs, or the Inner Mate Distance.

Summarizing with respect to the above example:

        Insert Size      = 50+150+50        = 250
        Fragment Size    = 20+50+150+50+20  = 290 
        Library Size     = 20+50+150+50+20  = 290
        Inner Mate Distance                 = 150            

Condensing:
        
        Insert           = Sequence without the adapters(The original DNA chunk)
        Fragment         = Insert Size + Right/Left flanking adapters
        Inner Mate       = Gap between the mate pair reads

Reference:
[Seqanswers](http://seqanswers.com/forums/showthread.php?t=13098)
