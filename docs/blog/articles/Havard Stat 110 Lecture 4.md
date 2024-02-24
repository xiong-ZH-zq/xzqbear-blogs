---
comments: true
description: 
tags:
  - Probability Theory
date: 2024-02-20
---
# Havard Stat 101 Lecture 4 - Conditional Probability

## Independence
[10:49](https://www.youtube.com/watch?v=P7NE4WF8j-Q#t=649.6844439732971) 
>[!note] Definition: Independence
>Events $A$, $B$ are independent if $P(A\cap B) = P(A)P(B)$ .

<!-- more -->

>[!danger] Note
>It is completely different from disjointness.

$A,B,C$ are independent if

$$
\begin{aligned}
&P(AB) = P(A)P(B), \\
&P(BC) = P(B)P(C), \\
&P(AC) = P(A)P(C), \\
&P(ABC) = P(A)P(B)P(C).
\end{aligned}
$$

Similarly for events $A_1,A_2,\cdots,A_n$ , means all multiply rules hold.

## Newton-Pepys Problem (1693)
[18:22](https://www.youtube.com/watch?v=P7NE4WF8j-Q#t=1102.50909)  
We have a fair dice, which is most likely below?

1. A. At least one $6$ with $6$ dices;
2. B. At least two $6$ with $12$ dices;
3. C. At least three $6$ with $18$ dices;

The answer is A. Here is the calculation:

$$
P(A) = 1-\left(\frac{5}{6}\right)^6 \approx 0.665
$$

$$
P(B) = 1-\left(\frac{5}{6}\right)^{12} - 12\left(\frac{5}{6}\right)^{11} \frac{1}{6}\approx 0.619
$$

$$
P(C) = 1- \sum\limits_{k=0}^2 \binom{18}{k}\left( \frac{1}{6}\right)^k \left(\frac{5}{6}\right)^{18-k} \approx 0.597
$$

## Conditional Probability
[32:35](https://www.youtube.com/watch?v=P7NE4WF8j-Q#t=1955.8446588817444) 
>[!note] Definition: Conditional Probability
>$$P(A|B) = \dfrac{P(A\cap B)}{P(B)}$$


