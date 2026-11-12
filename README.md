# 高等数学 · 食品专业贯通学习系统

面向食品类专业专科起点的交互式高数学习站。以教学大纲与专业后续课程需求为主线，不绑定单一教材，重点强化基础运算与熟练应用。

## 入口

- 在线站点：部署后访问 `https://<用户名>.github.io/advanced-math-zhishu/`
- 本地：双击根目录 `index.html`
- 单书伴侣：`01-高等数学-食品专业版/food-math学习伴侣.html`

## 内容

| 模块 | 数量 |
|---|---|
| 章节精讲 | 10 章（极限 → 微分 → 积分 → 微分方程 → 多元 → 二重积分 → 级数 → 数学实验） |
| 概念页 | 32 个，带依赖关系 |
| 第一性原理深度推导 | 6 篇（ε-N、中值定理、微积分基本定理、一阶线性、二阶常系数、泰勒） |
| 测验 | 56 题（50 道分章 + 6 道综合），答错沿依赖链倒推根因 |
| 抽认卡 | 60 张 |
| 术语 | 75 条 |
| 食品案例 | 冷却、降解、发酵、烤盘质量、配方优化、营养标签误差 |

## 目录结构

```
.
├── index.html                  # 总学习手册（单文件，统一入口）
├── index.md                    # Markdown 导航
├── .nojekyll                   # GitHub Pages 关闭 Jekyll
├── 00-学习总览/                # 专业定位、学习节奏、综合检验
├── 01-高等数学-食品专业版/
│   ├── SKILL.md                # 学习总纲
│   ├── chapters/               # 10 章精讲
│   ├── concepts/               # 32 个概念 + 6 篇深度推导
│   ├── paths/learn.md          # 学习路径详版
│   ├── quiz.md / flashcards.md / glossary.md
│   ├── patterns.md / cheatsheet.md
│   ├── manifest.json           # 结构化清单（驱动交互）
│   ├── food-math学习伴侣.html  # 单书学习伴侣
│   └── _work/                  # 生成脚本与过程产物（full 包才含）
```

## 本地使用

双击 `index.html`，浏览器打开即可。公式与 Mermaid 图走 CDN，联网时正常渲染；完全离线时公式显示源码、图显示文本，不影响阅读与导航。

## 部署到 GitHub Pages

```bash
git init
git add -A
git commit -m "高等数学 · 食品专业贯通学习系统"
git branch -M main
git remote add origin https://github.com/<用户名>/advanced-math-zhishu.git
git push -u origin main
```

仓库 Settings → Pages → Source 选 `Deploy from a branch`，Branch 选 `main`，目录选 `/ (root)`，保存后等 1–2 分钟。

## 说明

- 内容按教学大纲与食品专业需求自编，不对应某一本教材，章节编号仅用于本站导航。
- 例题中的数值均经过手算核对，个别为便于计算做了取整。
- 进度保存在浏览器 localStorage，换设备不互通。
