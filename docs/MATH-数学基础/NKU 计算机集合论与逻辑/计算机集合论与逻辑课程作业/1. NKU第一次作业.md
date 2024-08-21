---
comments: true
---
# NKU 第一次作业
>[!faq] Exercise 1.1.11
>对于任意的表达式 $\phi = s_0s_1\cdots s_k$，$\phi$ 的**恰当初始字符串**就是满足 $l<k$ 的任意序列 $s_0s_1\cdots s_l$，证明：一个语句的恰当初始字符串不会是一个语句，并用它替换引理 1.1.5 的证明中的结论 (4) 证明引理 1.1.5.

考虑语句归纳法：
设性质 $\mathcal{P}$ 为 “任何恰当初始字符串不能组成语句”.

-----
（归纳基础）
对两个字符和三个字符的情形：

- 两个字符时，即 $\neg p$ ，恰当初始字符串仅有 $\neg$ ，这显然不能成为一个语句；
- 三个字符时，即 $\bullet p_1 p_2$ ，其中 $\bullet$ 为二元连接词，此时两个恰当初始字符串 $\bullet$ 和 $\bullet p_1$ 都不能成为语句.

-----
设 $\varphi$ 和 $\psi$ 满足归纳假设（即具有性质 $\mathcal{P}$），那么：
(i) 对于 $\neg \varphi$ ，此时取恰当初始字符串 $\neg \varphi_0$ ，如果它为语句，则 $\varphi_0$ 自身也可构成 $L$-语句，这违反了归纳假设.

(ii) 对于 $\bullet \varphi \psi$ ，如果取到的恰当初始字符串形如 $\bullet \varphi \psi_0$ ，那么中缀表达式可以写为 $(\varphi) \bullet (\psi_0)$ ，$\varphi$ 为语句而 $\psi_0$ 不为语句，从而不为 $L$-语句. （实际上这里是有问题的，挖坑以后填）

因此，$\neg \varphi$ 和 $\bullet \varphi \psi$ 均具有性质 $\mathcal{P}$ . 根据语句归纳法命题成立. $\square$

下面利用该命题证明命题 1.1.5：

如果 $\theta = \bullet \varphi \psi$ 当中的 $\varphi$ 和 $\psi$ 不唯一，则有 $\bullet \varphi'\psi '$ ，其中 $\varphi',\psi'$ 均为语句，若 $\varphi'$ 的长度大于 $\varphi$ ，则由习题结论可知 $\varphi$ 不能为语句，矛盾！若 $\varphi'$ 长度小于 $\varphi$ ，则 $\varphi'$ 不能为语句，也矛盾，从而 $\varphi' = \varphi$ . $\square$

>[!faq] Exercise 1.3.19
>令 $|$ 为具有如下语义的二元连接词：
> $$ V(\phi \mid \psi) = \begin{cases} \mathrm{T},\text{if }V(\phi) = \mathrm{F} \text{ or } V(\psi) = \mathrm{F} \\ \mathrm{F},\text{Otherwise.}\end{cases} $$
> 
>这个连接词称为 nand （与非），证明：$\left\lbrace | \right\rbrace$ 是完备的.

设两个不同的原子语句为 $p,q$ ，由于 $\left\lbrace \neg , \lor \right\rbrace$ 是完备的，那么考虑表示出 $\neg$ 和 $\lor$ 即可：

$$
\neg p  = p\mid p
$$

$$
p\lor q = ((\neg p)\mid (\neg q))
$$

因此 $\left\lbrace \mid \right\rbrace$ 是完备的. $\square$

>[!faq] Exercise 1.3.21
> 证明 $\left\lbrace \neg, \leftrightarrow \right\rbrace$ 是不完备的.

考虑性质 $\mathcal{P}$ 为：对于所有原子语句为 $p_0,p_1,\cdots p_n$ 的 $L$-语句 $\psi$ ，$V(\psi)$ 在真值表当中取值为 $\mathrm{T}$ 的所有可能情形数为偶数.

考虑使用语句归纳法证明 $\left\lbrace \neg, \leftrightarrow \right\rbrace\cup \left\lbrace p_0,p_1,\cdots,p_n \right\rbrace$ 构成的语句 $\psi$ 均满足 $\mathcal{P}$ 性质：

对于基本的一阶语句情形 ，有如下的真值表：

$$
\begin{array}{ccccc}
p_0 & p_1 & \neg p_0 & \neg p_1 & p_0 \leftrightarrow p_1 \\
\hline
\mathrm{T} & \mathrm{T} &\mathrm{F}& \mathrm{F} & \mathrm{T}\\
\mathrm{T} & \mathrm{F} &\mathrm{F}& \mathrm{T} & \mathrm{F} \\
\mathrm{F} & \mathrm{T} &\mathrm{T}& \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} &\mathrm{T}& \mathrm{T} & \mathrm{T}
\end{array}
$$

可以发现所有的一阶语句都满足性质 $\mathcal{P}$ ，归纳基础成立.

对于 $n$ 阶语句 $\varphi$ 和 $\psi$ ，设归纳假设成立：
(1) $\neg \varphi$ 和 $\neg\psi$ 不改变真值情形个数的奇偶性；
(2) $\varphi\leftrightarrow \psi$ 同样不改变奇偶性；
因此均满足性质 $\mathcal{P}$ ，故可认为 $\left\lbrace \neg, \leftrightarrow \right\rbrace\cup \left\lbrace p_0,p_1,\cdots,p_n \right\rbrace$ 构成的语句均具有性质 $\mathcal{P}$ .

但是 $p_0 \land p_1$ 不具有性质 $\mathcal{P}$ ，因为在四种真值情形当中，共有 3 种情形取值为 $\mathrm{F}$ ，1 种情形取值为 $\mathrm{T}$ . 因此不完备性证毕. $\square$

