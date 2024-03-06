---
comments: true
description: The note of Havard STAT 110 Lecture 2
tags:
  - "Probability Theory"
date: 2024-02-18
---

# Havard Stat 110 Lecture 2

## Story Proofs, Axioms of Probability

### Some hints
Some hints and comments:

- [00:09](https://www.youtube.com/watch?v=FJd_1H3rZGg&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=2#t=9.658512) Don't lose your common sense (And not only rely on them).
- [02:38](https://www.youtube.com/watch?v=FJd_1H3rZGg&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=2#t=158.25955602479553) Do check answer (By doing simple and extreme cases).
- [04:05](https://www.youtube.com/watch?v=FJd_1H3rZGg&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=2#t=245.4278630500679) Label people and objects.

<!-- more -->
###  Order does not matter with replacement
[13:15](https://www.youtube.com/watch?v=FJd_1H3rZGg&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=2#t=795.316193859333) 

> Pick $k$ times from set of $n$ objects where order does not matter with replacement.

There are about $\binom{n+k-1}{k}$ ways to pick.

[22:40](https://www.youtube.com/watch?v=FJd_1H3rZGg&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=2#t=1360.1499519904633)  Imagine put $k$ balls into $n$ boxes. 

[29:30](https://www.youtube.com/watch?v=FJd_1H3rZGg&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=2#t=1770.6932009570846) Extra: Bose-Einstein condensate (Bose-Einstein 凝聚态) 


### Story Proof
[31:16](https://www.youtube.com/watch?v=FJd_1H3rZGg&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=2#t=1876.189528040531) 
>[!note] Example 1
> Use story proof to prove $\displaystyle\binom{n}{k} = \binom{n}{n-k}$

This is easy as we can consider divide $n$ people into two teams: one contains $k$ people and the other one contains $n-k$ people.

[32:14](https://www.youtube.com/watch?v=FJd_1H3rZGg&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=2#t=1934.9023430977516) 
>[!note] example 2
>Prove 
> $$ n\binom{n-1}{k-1} = k\binom{n}{k} $$

Consider the story below:
> Pick $k$ people out of $n$ , with $1$ designated as President.

The solution is obviously

$$
k\binom{n}{k}
$$

And transform the view of the problem:

- First choose $1$ President, which has $n$ ways.
- Then choose $k-1$ people from $n-1$ people.

[35:06](https://www.youtube.com/watch?v=FJd_1H3rZGg&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=2#t=2106.862381) 
>[!note] Example 3 (Vander Monde)
>Prove
> $$ \binom{m+n}{k} = \sum\limits_{j=0}^k \binom{m}{j}\binom{n}{k-j} $$

The left annotation means: choose $k$ people from $m+n$ people. 

Then we consider divide $m+n$ people into two groups: first contains $m$ people and second contains $n$ people. Next choose $j$ people from first one and $k-j$ people second one.

### Non-naive Probability Axioms
[39:15](https://www.youtube.com/watch?v=FJd_1H3rZGg&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=2#t=2355.103309830723) Non-naive definition
>[!note] Non-naive Definition of Probability
>A **Probability Sample** consists of $S$ and $P$, where $S$ is a sample space and $P$ is a function which takes an event $A\subset S$ as input, returns $P(A)\in [0,1]$ as outputs such that:
>1. $P(\varnothing) = 0$ , $P(S)=1$ .
>2. $\displaystyle P\left(\bigcup_{n=1}^\infty A_n\right) = \sum\limits_{n=1}^\infty P(A_n)$ if $A_j$ are disjoint.