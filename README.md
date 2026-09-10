## https://wadesha.github.io/architecture-daily/

> GitHub Pages 地址放第一行，点击访问。

---

# 中国建筑文化档案 · Chinese Architecture Archive

一个持续积累的中国建筑文化研究档案库，涵盖 514 篇精选文章。GitHub Pages 首页随机展示其中一篇，可随时切换。

**A continuously growing archive of Chinese architectural culture — 514 articles and counting.** The GitHub Pages landing page displays a random article each visit, with a shuffle button for endless discovery.

## 四大分类 · Four Categories

| 代码 | 中文 | English | 文件数 |
|---|---|---|---|
| `01_provincial-architecture` | 省级建筑 | Provincial Architecture | 49 |
| `02_villages-and-houses` | 村落民居 | Villages & Vernacular | 101 |
| `03_overseas-architecture` | 海外研究 | Overseas Scholarship | 35 |
| `04_style-analysis` | 体风分析 | Style Analysis | 329 |

## 目录结构 · Directory Layout

```
.
|-- index.html： GitHub Pages 首页（随机展示+切换）
|-- index.json： 完整台账（首页数据源）
|-- _scripts/： 维护脚本（不发布）
| +-- gen_index.js： 重新生成台账
|-- 01_provincial-architecture/： 省级建筑研究
| |-- fujian/ hubei/ jiangsu-shanghai/ ...
|-- 02_villages-and-houses/： 村落与民居
| |-- songyang/ yanxia/ chuantong-minju/ ...
|-- 03_overseas-architecture/： 海外学者研究
| +-- 营造法式/ 喜龙仁/ 关野贞/ 沙畹/ ...
+-- 04_style-analysis/： 写作体风模仿与分析
 |-- group01-chenzhihua/ group06-wenzhou-dingjunqing/ ...
```

## 维护与同步 · Maintenance

台账 `index.json` 由脚本自动生成。当 OneDrive 源目录有新增/修改时：

```bash
# 1. 重新生成台账
node _scripts/gen_index.js

# 2. 提交并推送
git add -A
git commit -m "sync: $(date +%Y%m%d) update"
git push origin main
```

**写作方法与过程文件**存放在作者本地，不进入 GitHub Pages 发布流程。本仓库只承载可公开浏览的成品内容。

## 技术栈 · Tech Notes

- **GitHub Pages** 静态托管（无构建步骤）
- **原生 HTML/CSS/JS**，零依赖，加载迅速
- **index.json** 作为唯一数据源，首页 fetch 加载
- 文件路径即永久 URL，便于引用和分享

## License

内容归作者所有。仓库仅用于公开浏览，未经授权请勿用于商业目的。
