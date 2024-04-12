---
comments: true
description: Notes for Havard Stat 110 Lecture 3
tags:
  - Probability Theory
  - 数学
date: 2024-02-19
---
# Havard Stat 110 Lecture 3
## Birthday Problem
[00:49](https://www.youtube.com/watch?v=LZ5Wergp_PA&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=3#t=49.0381900667572) 
$K$ people, find probability that share same birthday. Exclude Feb. 29th and assume other 365 days equally likely and independence.
<!-- more -->
Obviously if $K>365$ , the probability is $1$.

Let $K\leqslant 365$ , consider $P(\text{no match})$ :

$$
P(\text{no match}) = \dfrac{365\times 364\times \cdots (365-K+1)}{365^K}
$$

So $1-P(\text{no match}) = P(\text{match})$ .

Compute this result and we can get that:

$$
P(\text{match}) = 
\begin{cases}50.7\% , &K=23 \\ 97\% , &K=50 \\ 99.999\% , &K=100 \end{cases}
$$

## Properties of Probability
[22:46](https://www.youtube.com/watch?v=LZ5Wergp_PA&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=3#t=1366.4243181296997) 

1. $P(\overline{A}) = 1-P(A)$ .
2. If $A\subseteq B$ (If $A$ occurs that $B$ occurs), then $P(A)\leqslant P(B)$ .
3. $P(A\cup B) = P(A)+P(B)-P(A\cap B)$ . (For proof, consider $P(A\cup B) = P(A)+P(B\cap \overline{A})$) .
4. $$ \begin{aligned}P(A\cup B\cup C) &= P(A)+P(B)+P(C) \\ &- P(A\cap B)-P(A\cap C)-P(B\cap C)\\ &+P(A\cap B\cap C)\end{aligned} $$ 

## de Montmort's Problem
[38:48](https://www.youtube.com/watch?v=LZ5Wergp_PA&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=3#t=2328.5419208226167) 
$n$ cards, labeled $1,2,\cdots,n$ . Let $A_j$ be the event "$j$-th card matches".
So we need to compute $P(A_1\cup A_2\cdots \cup A_n)$ .

$P(A_j) = \dfrac{1}{n}$ since all position equally likely for card labled $j$ .

$P(A_1\cap A_2) = \dfrac{(n-2)!}{n!}$ as we can consider the first and the second one are fixed.

So $\displaystyle P\left(\bigcap_{k=1}^n A_k\right) = \dfrac{(n-k)!}{n!}$ .  

Thus we can compute that:

$$
\begin{aligned}
P(A_1\cup A_2\cdots \cup A_n)  &= n\frac{1}{n}- \frac{n(n-1)}{2!}\frac{1}{n(n-1)}\cdots+(-1)^{n+1}\binom{n}{n}\frac{(n-n)!}{n!} \\
&= 1- \frac{1}{2!}+ \frac{1}{3!}-\cdots+(-1)^{n+1} \frac{1}{n!} \\
&\approx 1-\frac{1}{\mathrm{e}}
\end{aligned}
$$


