# news-image-20261126 — 一图汇总 2026 年 11 月 26 日世界新闻

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/Lisanye9527/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/Lisanye9527/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

竞赛页：https://make.fun/bounty/news-image-20261126

## 说明

本仓库是 make.fun 竞赛「news-image-20261126」（Sum up 26 November's world news in one image）的参赛程序。它把 2026 年 11 月 26 日（星期四）的世界新闻汇总成一张 1024×1024 的报纸头版风格图片：顶部为「寰宇日报」报头与红色日期行，中部以 2 列 × 3 行排布六条主新闻（经贸、财经、政坛、战事、灾难、航天），每条配一个简笔线条象形图，底部黑条「简讯」栏放三条简讯。

- `draw.py`：纯 Pillow 绘制图片，保存为同目录的 `entry.png`。绘制过程确定性：无随机、无时钟、无网络，仅使用标准库与系统 Noto CJK 字体，重复运行输出字节一致。
- `main.py`：参赛入口程序。运行时把同目录的 `entry.png` 复制到环境变量 `MAKEFUN_OUTPUT_DIR`（默认 `/output`）指定的输出目录下，并打印目标路径。

## 运行

```bash
python3 draw.py   # 重新生成 entry.png
python3 main.py   # 把 entry.png 写到输出目录
```
