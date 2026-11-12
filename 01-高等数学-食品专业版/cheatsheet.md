# 速查表

## 基本导数

| 函数 | 导数 |
|---|---|
| $C$ | 0 |
| $x^n$ | $nx^{n-1}$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $e^x$ | $e^x$ |
| $a^x$ | $a^x\ln a$ |
| $\ln x$ | $1/x$ |
| $\arctan x$ | $1/(1+x^2)$ |
| $\arcsin x$ | $1/\sqrt{1-x^2}$ |

## 求导法则

| 法则 | 公式 |
|---|---|
| 和差 | $(u\pm v)'=u'\pm v'$ |
| 乘积 | $(uv)'=u'v+uv'$ |
| 商 | $(u/v)'=(u'v-uv')/v^2$ |
| 链式 | $(f(g(x)))'=f'(g(x))g'(x)$ |
| 参数方程 | $dy/dx=(dy/dt)/(dx/dt)$ |
| 隐函数 | 两边求导，解出 $y'$ |

## 基本积分

| 被积函数 | 原函数 |
|---|---|
| $x^n\ (n\ne-1)$ | $x^{n+1}/(n+1)+C$ |
| $1/x$ | $\ln\lvert x\rvert+C$ |
| $e^x$ | $e^x+C$ |
| $\sin x$ | $-\cos x+C$ |
| $\cos x$ | $\sin x+C$ |
| $\sec^2x$ | $\tan x+C$ |
| $1/(1+x^2)$ | $\arctan x+C$ |
| $1/\sqrt{1-x^2}$ | $\arcsin x+C$ |

## 泰勒展开（$x_0=0$）

| 函数 | 展开 | 收敛范围 |
|---|---|---|
| $e^x$ | $1+x+x^2/2!+x^3/3!+\cdots$ | 全体实数 |
| $\sin x$ | $x-x^3/3!+x^5/5!-\cdots$ | 全体实数 |
| $\cos x$ | $1-x^2/2!+x^4/4!-\cdots$ | 全体实数 |
| $\ln(1+x)$ | $x-x^2/2+x^3/3-\cdots$ | $-1<x\le1$ |
| $1/(1-x)$ | $1+x+x^2+\cdots$ | $\lvert x\rvert<1$ |

## 定积分与反常积分

| 场景 | 结论 |
|---|---|
| 牛顿—莱布尼茨 | $\int_a^bf=F(b)-F(a)$ |
| 换元 | $x=\varphi(t)$ 时上下限同步换成 $\alpha,\beta$ |
| 分部 | $\int_a^bu\,dv=[uv]_a^b-\int_a^bv\,du$ |
| $\int_1^\infty x^{-p}$ | $p>1$ 收敛，$p\le1$ 发散 |
| $\int_0^1 x^{-p}$ | $p<1$ 收敛，$p\ge1$ 发散 |
| 旋转体体积 | $V=\pi\int_a^bf^2dx$ |
| 平均值 | $\bar f=\frac{1}{b-a}\int_a^bfdx$ |

## 微分方程

| 类型 | 解法 |
|---|---|
| 可分离 $y'=f(x)g(y)$ | 分离后两边积分 |
| 齐次 $y'=\varphi(y/x)$ | 令 $u=y/x$ |
| 一阶线性 $y'+Py=Q$ | 积分因子 $e^{\int Pdx}$ |
| 二阶齐次 | 特征方程三种情形 |
| 二阶非齐次 | 齐次通解 + 待定特解 |

## 二阶特征方程

| 判别式 | 通解 |
|---|---|
| $p^2-4q>0$ | $C_1e^{r_1x}+C_2e^{r_2x}$ |
| $p^2-4q=0$ | $(C_1+C_2x)e^{rx}$ |
| $p^2-4q<0$ | $e^{\alpha x}(C_1\cos\beta x+C_2\sin\beta x)$ |

## 二重积分

| 区域 | 公式 |
|---|---|
| X 型 | $\int_a^bdx\int_{y_1(x)}^{y_2(x)}f\,dy$ |
| Y 型 | $\int_c^ddy\int_{x_1(y)}^{x_2(y)}f\,dx$ |
| 极坐标 | $\int_{\theta_1}^{\theta_2}d\theta\int_{r_1}^{r_2}f\,r\,dr$ |
| 质量 | $m=\iint\rho\,d\sigma$ |
| 平均值 | $\bar f=\frac{1}{A}\iint f\,d\sigma$ |

## 级数判别

| 判别法 | 判据 |
|---|---|
| 必要条件 | $u_n\to0$；不满足则发散 |
| 几何级数 | $\sum aq^{n-1}=a/(1-q)$，$\lvert q\rvert<1$ |
| p 级数 | $p>1$ 收敛 |
| 比值 | $L<1$ 收敛，$L>1$ 发散，$L=1$ 失效 |
| 根值 | 同上 |
| 莱布尼茨 | $u_n$ 递减趋于 0 |
| 幂级数半径 | $R=\lim\lvert a_n/a_{n+1}\rvert$ |

## 食品常用模型

| 过程 | 模型 | 解 |
|---|---|---|
| 一级反应/降解 | $C'=-kC$ | $C=C_0e^{-kt}$ |
| 细菌指数增长 | $N'=rN$ | $N=N_0e^{rt}$ |
| 有上限增长 | $N'=rN(1-N/K)$ | $N=K/[1+(K/N_0-1)e^{-rt}]$ |
| 牛顿冷却 | $T'=-k(T-T_m)$ | $T=T_m+(T_0-T_m)e^{-kt}$ |
| 半衰期 | $C=C_0/2$ | $t=\ln2/k$ |

## 误差

| 量 | 公式 |
|---|---|
| 绝对误差 | $\Delta y\approx\lvert f'(x)\rvert\Delta x$ |
| 相对误差 | $\Delta y/y\approx\lvert f'/f\rvert\Delta x$ |
| 多元误差 | $\Delta z\approx\lvert f_x\rvert\Delta x+\lvert f_y\rvert\Delta y$ |
| 有效数字 | 从第一个非零数字起算 |
| 数值微分 | 中心差商，误差 $O(h^2)$ |
| 数值积分 | 辛普森法，误差 $O(h^4)$ |
