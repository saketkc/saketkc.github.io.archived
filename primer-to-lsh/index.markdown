$$D_2 statistic for alignment free searches$$

The $$D_2$$ statistic is characterized by number of matches of length k between any two sequences $$A$$ and $$B$$ allowing upto $$t$$ mis
matches. Sequences A and B are represented as $$(A_1, A_2, A_3, ... A_n_A) and (B_1, B_2, B_3, ...., B_n_B)$$ respectively.

More generally $$D_2$$ is characterized by $$(n_A, n_B, k, t, \eta)$$ where:
$$n_A$$ = Total length of nucleotides in sequence A
$$n_B$$ = Total length of nucleotides in sequence B
k = length of matches
t = length of allowable mismatches



## LSH

Jaccard similarity: Notion of similarity that associates similarity of sets with the relative size of their intersection
A comman example would be determining if a document is a plagiarised copy of another, if not identical. The technique 
used to convert these documents to a set intersection problem is referred to as “shingling”



### Jaccard Similarity
Jaccard similarity = $$jSIM(S,T) = \frac{|S \cap T|}{|S \cup T|}$$

Let $$S=[1,2,3]$$ and $$T=[2,3,4,5,6]$$ then $$SIM(S,T)=\frac{2}{6}$$


#### Jacard distance  
$$D_J(A,B) = 1 - jSIM(A,B)$$ and is a distance metric.

### Cosine Similarity

As the name suggests, cosine similarity relies on taking cosines between two given vectors to infer the similarity.
The range for cosine is [-1,1] When used in positive space it is [0,1]

Thinking in terms of document matching, a document can be represented as a vector of words, where the “words” form the unit vectorsand the 
associated scalar is the frequency of the word.

####Cosine distance

$$D_C(A,B)=1-S_C(A,B)$$ but is not a metric since it does not follow the triangular inequality $$d(x,z) \leq d(x,y)+d(y,z)$$, neither does it
follow the coincidence axiom $$d(x,y)=0 iff\ x=y$$$ since cosine(x,y)=0 if $$x \perp y$$

$$cSIM(A,B) = cos(\theta) =  \frac{A.B}{|A||B|}$$

$$Range(cSIM(A,B))=[-1,1]$$ where -1 means entirely opposite, 1 means ‘exactly similar’. In a positive space, such as when using the frequencies of
words, the range is limited to $$[0,1]$$.

### Angular similarity
For vectors in positive+negative space: 

$$aSIM(A,B)=1-\frac{cos^{-1}(cSIM(A,B))}{\pi}$$


For vectors in positive space(only): 

$$aSIM(A,B)=1-\frac{2.cos^{-1}(cSIM(A,B))}{\pi}$$


#### Angular difference coefficient
$$D_A(A,B) = 1-aSIM(A,B)$$ and *is* a distance metric


### Tanimoto similarity

[A computer program for Classifying plants](http://www.sciencemag.org/content/132/3434/1115) describes Tanimoto similairty 

 




