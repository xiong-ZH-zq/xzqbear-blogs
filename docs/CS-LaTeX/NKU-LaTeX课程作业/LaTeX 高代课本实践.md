---
comments: true
---
# LaTeX 课程 —— 高代课本复现

NKU 数学科学学院的 LaTeX 课程期末作业的形式为：复现数学分析或者高等代数课本的某几页，由老师按学号指定。

我被抽中的部分是《高等代数》王萼芳本的 98-100 页，综合来看省时省力的做法是：

- 使用 mathpix 或者 simpleTeX 来 OCR 电子书，得到全部的内容代码，注意微调一些内容就行；
- 接下来解决格式问题就好，目前来看格式有些问题也没关系，分数都会在 90 以上，如果要 95 及以上就要好好调格式了，我的分数就是 95.

如下图片展示效果：

![](https://raw.githubusercontent.com/xiong-ZH-zq/My-PicGO-Img/main/blog/LaTeX%20P1.jpg)

![](https://raw.githubusercontent.com/xiong-ZH-zq/My-PicGO-Img/main/blog/LaTeX%20P2.jpg)

![](https://raw.githubusercontent.com/xiong-ZH-zq/My-PicGO-Img/main/blog/LaTeX%20P3.jpg)

完整代码：

```latex
\documentclass{ctexbook}
\usepackage{amsmath}
\usepackage{amsthm} 
\usepackage{indentfirst} 
\usepackage{xeCJKfntef}
\usepackage{endnotes}    % 带圈数字脚注实现所需宏包
\usepackage{xpatch}
\usepackage{xunicode-addon}
\usepackage[textwidth=16cm,hcentering,a4paper,top=3cm,bottom=3cm]{geometry}

\setlength{\parindent}{2em}
\setcounter{page}{98}



% 带圈数字脚注的实现
\AtBeginUTFCommand[\textcircled]{\begingroup\normalsize\EnclosedNumbers}
\AtEndUTFCommand[\textcircled]{\endgroup}
\xeCJKDeclareCharClass{Default}{"24EA, "2460->"2473, "3251->"32BF}
\newfontfamily\EnclosedNumbers{Garamond-Math.otf}
\makeatletter
\renewcommand\thefootnote{\textcircled{\@arabic\c@footnote}}
\xpatchcmd\@makefntext
{{\hss\@makefnmark}}
{{\hss\@makefnmark@nosuperscript}\space}
{}{\fail}
\def\@makefnmark@nosuperscript{\lower .3ex \hbox{\normalfont\@thefnmark}}
\xpatchcmd\footnoterule
{.4\columnwidth}
{1in}
{}{\fail}
\protected\def\textcircled@protected{\textcircled}
\xpatchcmd\enoteformat
{\makeenmark}
{\makeenmark@nosuperscript}
{}{\fail}
\def\makeenmark@nosuperscript{%
	\lower .3ex \hbox{\normalfont\@theenmark\space}}
\makeatother





\begin{document}
\[
\boldsymbol{\gamma}=\boldsymbol{\gamma}_0+\boldsymbol{\eta},\tag{10}
\]
\CJKunderdot{其中 $\boldsymbol{\eta}$ 是导出组 (1) 的一个解. 因此, 对于方程组 (9) 的任一个特解 $\gamma_0$, 当 $\boldsymbol{\eta}$ 取遍它的导出组的全部解时, (10) 就给出 (9) 的全部解.}
证明
\[
\gamma=\gamma_0+\left(\boldsymbol{\gamma}-\gamma_0\right),
\]
由上面的 $1, \boldsymbol{\gamma}-\boldsymbol{\gamma}_0$ 是导出组 (1) 的一个解, 令
\[
\boldsymbol{\gamma}-\boldsymbol{\gamma}_0=\boldsymbol{\eta},
\]
就得到定理的结论.既然 (9) 的任一个解都能表成 (10) 的形式, 由 2 , 在 $\boldsymbol{\eta}$ 取遍 (1) 的全 部解的时候,
\[
\gamma=\gamma_0+\boldsymbol{\eta}
\]
就取遍 (9) 的全部解. \rule{3pt}{10pt}    % 证毕符号

定理 9 说明了, 为了找出一线性方程组的全部解, 我们只要找出它的一个特殊的 解以及它的导出组的全部解就行了. 导出组是一个齐次方程组, 在上面我们已经看到, 一个齐次线性方程组的解的全体可以用基础解系来表出. 因此, 根据定理我们可以用 导出组的基础解系来表出一般方程组的一般解: 如果 $\gamma_0$ 是方程组 (9) 的一个特解, $\boldsymbol{\eta}_1$, $\boldsymbol{\eta}_2, \cdots, \boldsymbol{\eta}_{n-r}$ 是其导出组的一个基础解系,那么 (9) 的任一个解 $\gamma$ 都可以表成
\[
\boldsymbol{\gamma}=\boldsymbol{\gamma}_0+k_1 \boldsymbol{\eta}_1+k_2 \boldsymbol{\eta}_2+\cdots+k_{n-r} \boldsymbol{\eta}_{n-r} \text {. }
\]

\textbf{推论} \quad 在方程组 (9) 有解的条件下, 解是唯一的充分必要条件是它的导出组 (1) 只有零解.

\textbf{证明} \quad 充分性. 如果方程组 (9) 有两个不同的解, 那么它的差就是导出组的一个非 零解. 因之, 如果导出组只有零解, 那么方程组有唯一解.

必要性. 如果导出组有非零解, 那么这个解与方程组 (9) 的一个解 (因为它有解) 的 和就是 (9) 的另一个解, 也就是说, (9) 不止一个解. 因之, 如果方程 (9) 有唯一的解, 那 么它的导出组只有零解.\rule{3pt}{10pt}

线性方程组的理论与解析几何中关于平面与直线的讨论有密切的关系. 我们来看线性方程组

\[
\left\{\begin{array}{l}
	a_{11} x_1+a_{12} x_2+a_{13} x_3=b_1 \\
	a_{21} x_1+a_{22} x_2+a_{23} x_3=b_2 .
\end{array}\right.\tag{11}\label{平面线性方程组}
\]

(\ref{平面线性方程组}) 中每一个方程表示一个平面, 线性方程组 (\ref{平面线性方程组}) 有没有解的问题就相当于这两个 平面有没有交点的问题. 我们知道, 两个平面只有在平行而不重合的情形没有交点. (\ref{平面线性方程组}) 的系数矩阵与增广矩阵分别是

\[
\boldsymbol{A}=\left(\begin{array}{lll}
	a_{11} & a_{12} & a_{13} \\
	a_{21} & a_{22} & a_{23}
\end{array}\right), \quad \overline{\boldsymbol{A}}=\left(\begin{array}{llll}
	a_{11} & a_{12} & a_{13} & b_1 \\
	a_{21} & a_{22} & a_{23} & b_2
\end{array}\right),
\]
它们的秩可能是 1 或者 2. 有三个可能的情形:
\begin{enumerate}
	\item  $\boldsymbol{A}$ 的秩 $=1, \overline{\boldsymbol{A}}$ 的秩 $=1$. 这就是 $\boldsymbol{A}$ 的两行成比例, 因而这两个平面平行. 又因为 $\bar{A}$ 的两行也成比例, 所以这两个平面重合. 方程组有解.
	\item  $\boldsymbol{A}$ 的秩 $=1, \overline{\boldsymbol{A}}$ 的秩 $=2$. 这就是说, 两个平面平行而不重合. 方程组无解.
	\item  $\boldsymbol{A}$ 的秩 $=2$. 这时 $\overline{\boldsymbol{A}}$ 的秩一定也是 2. 在几何上就是这两个平面不平行, 因而一定 相交. 方程组有解.
\end{enumerate}

下面再来看看线性方程组的解的几何意义. 设矩阵 $\boldsymbol{A}$ 的秩为 2 , 这时一般解中有一 个自由未知量,譬如说是 $x_3$,一般解的形式为
\[
\left\{\begin{array}{l}
	x_1=d_1+c_1 x_3, \\
	x_2=d_2+c_2 x_3
\end{array} .\right. \label{一般解的形式}\tag{12}
\]
从几何上看,两个不平行的平面相交成一条直线. 把 (12) 改写一下就是直线的点向式 方程
\[
\frac{x_1-d_1}{c_1}=\frac{x_2-d_2}{c_2}=x_3 .
\]
如果引人参数 $t$, 令 $x_3=t,(12)$ 就成为
\[
\left\{\begin{array}{l}
	x_1=d_1+c_1 t, \\
	x_2=d_2+c_2 t, \\
	x_3=t .
\end{array}\right.  \tag{13}\label{点向式方程一般解}
\]
这就是直线的参数方程.
(\ref{平面线性方程组}) 的导出方程组是
\[
\left\{\begin{array}{l}
	a_{11} x_1+a_{12} x_2+a_{13} x_3=0, \\
	a_{21} x_1+a_{22} x_2+a_{23} x_3=0 .
\end{array}\right. \tag{14}\label{导出方程组}
\]
从几何上看, 这是两个分别与 (\ref{平面线性方程组}) 中平面平行的且过原点的平面, 因而它们的交线过 原点且与直线 (12) 平行. 既然与直线 (12) 平行, 也就是有相同的方向, 所以这条直线的 参数方程就是
\[
\left\{\begin{array}{l}
	x_1=c_1 t, \\
	x_2=c_2 t, \\
	x_3=t .
\end{array}\right. \tag{15}\label{曲线参数方程组}
\]
(13) 与 (15) 正说明了线性方程组 (\ref{平面线性方程组}) 与它导出方程组 (14) 的解之间的关系.



\section*{\S 7. 二元高次方程组}


现在我们利用已经建立起来的线性方程组的理论给出一个解二元高次方程组的 一般方法. 为了这个目的, 我们先讨论一下两个一元多项式有非常数的公因式的条件.
根据第一章的结果, 可以证明:

\textbf{引理}\quad \CJKunderdot{设
\begin{align}
	& f(x)=a_0 x^n+a_1 x^{n-1}+\cdots+a_n, \\
	& g(x)=b_0 x^m+b_1 x^{m-1}+\cdots+b_m
\end{align}
是数域 $P$ 上的两个非零的多项式, 它们的系数 $a_0, b_0$ 不全为零. 于是 $f(x)$ 与 $g(x)$ 在 $P[x]$ 中有非常数的公因式的充分必要条件是, 在 $P[x]$ 中存在非零的次数小于 $m$ 的多 项式 $u(x)$ 与次数小于 $n$ 的多项式 $v(x)$, 使}
\[
u(x) f(x)=v(x) g(x) .
\]


\textbf{证明}\quad 先证必要性. 如果 $f(x)$ 与 $g(x)$ 有非常数的公因式 $d(x)$, 即
\[
f(x)=d(x) f_1(x), \quad g(x)=d(x) g_1(x),
\]

其中 $\partial\left(f_1(x)\right)<n, \partial\left(g_1(x)\right)<m$, 那么取 $u(x)=g_1(x), v(x)=f_1(x)$, 显然就有
\[
u(x) f(x)=d(x) f_1(x) g_1(x)=v(x) g(x) .
\]

再证充分性. 为了确定起见, 不妨设 $a_0 \neq 0$, 也就是说, $f(x)$ 是一 $n$ 次多项式. 假定有 $u(x), v(x)$ 使
\begin{equation}
	u(x) f(x)=v(x) g(x),
\end{equation}

其中 $\partial(u(x))<m, \partial(v(x))<n$. 令
\[
(f(x), v(x))=d(x),
\]

于是
\[
f(x)=d(x) f_1(x), \quad v(x)=d(x) v_1(x) .
\]

代入 (3) 式,得
\[
d(x) u(x) f_1(x)=d(x) v_1(x) g(x),
\]

消去 $d(x)$, 有
\begin{equation}
	u(x) f_1(x)=v_1(x) g(x) .
\end{equation}



因为 $d(x) \mid v(x)$, 所以 $d(x)$ 的次数小于 $n$, 因而 $f_1(x)$ 的次数大于零. 我们知道 $\left(f_1(x)\right.$, $\left.v_1(x)\right)=1$\footnote{参看第一章习题 10.}, 于是由 $(4)$, 即
\[
f_1(x) \mid v_1(x) g(x),
\]

得
\[
f_1(x) \mid g(x) .
\]

这就是说 $f(x)$ 与 $g(x)$ 有一非常数的公因式 $f_1(x)$. \rule{3pt}{10pt}

下面再来把引理中的条件改变一下. 令
\[
u(x)=u_0 x^{m-1}+u_1 x^{m-2}+\cdots+u_{m-1}, \quad v(x)=v_0 x^{n-1}+v_1 x^{n-2}+\cdots+v_{n-1} .
\]
由多项式相等的定义, 等式
\begin{equation}
	u(x) f(x)=v(x) g(x)
\end{equation}
就是左右两端对应系数相等, 即
\begin{equation}
\left\{\begin{aligned}
	&a_0 u_0 \phantom{+a_1 u_1+a_0 u_2}  =b_0 v_0, \\
	&a_1 u_0+a_0 u_1 \phantom{+a_0 u_2} =b_1 v_0+b_0 v_1, \\
	&a_2 u_0+a_1 u_1+a_0 u_2  =b_2 v_0+b_1 v_1+b_0 v_2, \\
	&\qquad\qquad\qquad\ldots \ldots \ldots \ldots  \\
	&a_n u_{m-2}+a_{n-1} u_{m-1}  =b_{m-2} v_{n-2}+b_{m-1} v_{n-1}, \\
	&\qquad\qquad\qquad a_n u_{m-1}  =b_m v_{n-1} .
\end{aligned}\right.
\end{equation}
如果把 (6) 看成一个关于未知量 $u_0, u_1, \cdots, u_{m-1}, v_0, v_1, \cdots, v_{n-1}$ 的方程组,那么它是一个含 $m+n$ 个未知量, $m+n$ 个方程的齐次线性方程组. 显然,引理中的条件: “在 $P[x]$ 中存在非零的次数小于 $m$ 的多项式 $u(x)$ 与次数小于 $n$ 的多项式 $v(x)$ 使 (5) 式成立" 就相当于说, 齐次线性方程组 (6) 有非零解.




\end{document}
```