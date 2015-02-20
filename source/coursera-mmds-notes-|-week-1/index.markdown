---
layout: page
title: "Coursera mmds notes | Week 1"
date: 2015-02-14 00:19
comments: true
sharing: true
footer: true
---

#Map Reduce
Problem: Too much data to fit into memory
So data in disk, only portion can be loaded into memory


## Solution?
Split your jobs : Cluster computing

### Cluster computing challenges
Node failures: Once in 1000 days
1M server => 1000 failures/day

Persistency: Node fails, data should still be made available if it was 
stored on the failed node

Atomicity: Fails in between computing period.

Network bottleneck: 10TB/1Gbps = 10000x8s = 24 hours
Hard: distributed computing is hard!
    

##Map-Reduce
- Store data redundantly!
- Move computation close to data
- Simple progrramming model

###Distributed file system

- Stores data across nodes, redundantly
- Data rarely updated in place
- Reads and appends are more common, updating is rare
- Data kept in chunks across nodes
- Multiple copies of each chunk, no two same chunks being on the same ndoe, 2x-3x
- Each chunk 16-64MB
- Master node stores metadata, replicated as well
- Client library for file acess, accesses files through master’s metadata

## Map-Reduce: Warmup

- Large text doc => Count number of unique words
- Case 1:Document can’t fit in memory but (words, freq) can
    - Use hashtables
- Case 2: (word, freq) also can’t
    - words(x.txt) | sort | uniq -c

## Map-Reduce: overview

- Map!
    - scan input one record at a time(words(x,txt))
    - Extract what you want to(words again in our case): keys

- Group by key
    - Sort and shuffle(sort)

- Reduce
    - Aggregate, summarize, filter, tranform(uniq -c)


## Map-Reduce: Map

- Input: (key, value)
- Intemediate Step: (key, value) $$=>$$  (key1, value1), (key2, value2) for key in keys;
- Group by key: (key1, [val1,val2,vax]); (key2, [vall1, val2])
    

## Map-Reduce: Reduce

- Reduce: (key1, [val1,val2,vax]) $$=>$$ (key1, val1+val2+val3)
- any reducing function(not just addition, of course)

## Map-Reduce: Formally
- Input: Set of (key,value) pairs
- Map: $$<k,v>\longrightarrow<k’, v’>$$*
    - One map call for rach $$<k,v>$$
- Reduce:$$<k’,<v’>> \longrightarrow <k’, v’’>$$ 
    - All values with same key $$k’$$ reduced together
    - One reduce function per unique key $k’$

## Word Counting
- Input: Text doc
- Map : (word, 1)
- Group by key: (word,1), (word,1); (word2,1), (word2,1)
- Reduce : (word, sigma(word))
- REMEMEBER: All this happens across nodes on different chunks, reading isn’t sequential, but parallel!
- Multiple map nodes, multiple reduce nodes
- Sysmte uses a hash function to hash each key such that all tuples with same keys 
land in the same reducer node. So all (word,x) intance go to node 1, (word2,y) goto node 2 etc.
- Final result also spread across different nodes, as expected
- the magic happens because rather than randomly accessing the disk, it is being 
accessed sequentially
- Sequential reads are much much more efficient than random access.
- Reading randomly would have require higher number of file.seek operations

## Psuedocode
```
map(key, value)
    @key: doc name
    @value: text in doc
    for word in value.split():
        yield((word,1))

reduce(key, value:)
    result = 0
    for each count v in values:
        result+=v
    yield((key, result))
```

##DataFlow
- Input, Output: on DFS
- Scheduler maps task close to physical storage
- Intermediate REsults: Local FS of workers
- Coordianted by Master node
    - Task status: Idle, complete, in-progress
    - Idle tasks get sheduled as workers are made available
    - on completeion of a task, the master sends the intermediate files to
    reducer
    - Pings workers to check status of failures
    - Map worker failure: Master reset status of all jobs either complete or in-progress 
    on that node to idle
    - Reduce worker faiure: Only need to reset status of in-progress tasks
    - Idle tasks rescheduled

## Number of Tasks
- M map tasks, R reduce tasks
- Rule of thumb: $$M>>n$$, n=number of nodes In fact: one task per chunk
    - Why? If 1 task/node and one task fails, it has to wait for the remaining n-1 
    to complete before getting rescheduled

- $$R<<M$$, makes sense to spread output to less number of nodes.

## Refining:Combiners
- Combiner acts after mapper to pre-process before shufflineg, also provided by the prgrammer
- Helps reduce tranfer overheads, network time
- Combiner is same as recduer$i
- Combining is intuitive and works for associative, commutative functions
- Consider reducer task of taking an average, You ask the combiner to return the (sum, count) tuple
- Calculating median: Not possible using only combiners!

## Refining: Shuffler
Used for deciding which key-value pairs goes to which reducer
- Naive approach for hashing: hash(key) mod R $$\belongsto [0,R-1]$$-

## PageRank:: Flow
- If page j with important $$r_j$$ has n outlinks, each links
get $$\frac{r_j}{n}$$ votes
- Page j’s own importantortance is sigma of it’s in-links
- It’s a cycle: Page is important if pointed to by other importatn ones

$$r_j = \sum_{i\longrightarrow j}\frac{r_i}{d_i}$$ where $$d_i$$ is the out degree of node i

## Page Rank: Matrix Formulation
- M = stochastic adj matrix,
- If $$\i \longrightarrow j$$ then $$M_{ji}=\frac{1}{d_i}$$  else $$M_{ji}$=0$i
- $$$r_i$$ is the rank of page i
- Contraint: $$\sum r_i=1$$
- $$ r = M.r$$
- Clearly, r is  a principle eign vector of M

## PageRank::Power Iteration
- $$r^{t+1}=M.r^{t}$$

## Random walk interpretation
- Surfer at time t on page i, then on t+1 at some j, an outlink of i
- Repeat
- $$p(t)$$ = vector with probability that walker is at ith coordinate at time t
- $$p(t+1)=M.p(t)$$
- Iterate till statinary condition $$p(t+1)=M.p(t)=p(t)$$

## Conditions on M
- Two main problems: Spider trap $$A \longleftrightarrow B$$
- And Dead end $$A \longrightarrow Bi$
- Randowm walker stuck at m: $$ A \longleftrightarrow B \longrightarrow m \longleftarrow $$

## Spider Trap Solution
- Jumping to i+1 is probabilistic with probability with choosing a random jump link= $$\beta$$

## Teleporting
- Keep $$M$$ stocahstic, aperiodic, irreducible
- $$A=M+a^{T}(\frac{1}{n}e)$$ a=1 if node i has out degree 0, else 0, e=unit vector
- $$r_j = \sum_{i\longrightarrow j} \beta \frac{r_i}{d_i} + (1-\beta)\frac{1}{n}$$
- $$A=\beta M+(1-\beta)\frac{1}{n}e.e^T$$, $$r^{t+1}=Ar^t$$
- Efficiently $$r_i = \sum A_{ij}. r_j$$ where $$A_{ij}=\beta M_{ij}+ \frac{1-\beta}{N}$$ $$\sum r_j=1$$.

