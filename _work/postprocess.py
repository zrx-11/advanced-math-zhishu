#!/usr/bin/env python3
"""构建后处理：把通用标题替换成本站标题。重建 index.html 后需重跑。"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
idx = ROOT / "index.html"
s = idx.read_text(encoding="utf-8")

s = s.replace("<title>学习总手册</title>",
              "<title>高等数学 · 食品专业贯通学习系统</title>")
s = s.replace("'<h1>学习总手册</h1>'",
              "'<h1>高等数学 · 食品专业贯通学习系统</h1>'")
s = s.replace('<span class="brand">学习总手册<span>点化学习系统 · 统一入口',
              '<span class="brand">高等数学 · 食品专业<span>知枢学习系统 · 统一入口')
if '<meta name="description"' not in s:
    s = s.replace("<title>高等数学 · 食品专业贯通学习系统</title>",
                  '<title>高等数学 · 食品专业贯通学习系统</title>\n'
                  '<meta name="description" content="食品专业高等数学：10 章精讲、32 个概念、6 篇从零推导、56 道测验，按依赖链诊断根因。">')
idx.write_text(s, encoding="utf-8")

md = ROOT / "index.md"
if md.exists():
    t = md.read_text(encoding="utf-8")
    t = t.replace("# 学习总手册", "# 高等数学 · 食品专业贯通学习系统", 1)
    md.write_text(t, encoding="utf-8")

print("标题已替换：", "<title>高等数学 · 食品专业贯通学习系统</title>" in s)
