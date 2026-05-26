# exp001

## Purpose / 目的 / 目的

Evaluate whether Wiktionary-based normalization improves embedding search quality.

Wiktionaryベースの正規化が埋め込み検索品質を向上させるかを評価する。

评估基于Wiktionary的规范化是否能提高嵌入搜索质量。

---

## Hypothesis / 仮説 / 假设

Lemma normalization improves MRR.

見出し語正規化がMRRを向上させる。

词元规范化可以提高MRR。

---

## Setup / セットアップ / 设置

### Data Preparation / データ準備 / 数据准备

```bash
# Step 7: Data Placement
# ステップ7: データの配置
# 步骤7：数据放置

# Copy external data to experiment directory
# 外部データを実験用ディレクトリにコピー
# 将外部数据复制到实验目录
cp data/external/jawiki-20260401.txt experiments/exp001/input/

# Extract sample data (if needed)
# サンプルデータの抽出（必要に応じて）
# 提取样本数据（如需要）
head -n 100000 experiments/exp001/input/jawiki-20260401.txt > experiments/exp001/input/sample.txt
```

---

## Dataset / データセット / 数据集

- jawiki-20260401
- sample size / サンプルサイズ / 样本大小: 100000

---

## Result / 結果 / 结果

| metric / 指標 / 指标 | baseline / ベースライン / 基线 | proposed / 提案手法 / 提议方法 |
|---|---:|---:|
| MRR | 0.612 | 0.644 |

---

## Observation / 観察 / 观察

Normalization improved robustness against orthographic variations.

正規化により表記ゆれに対する頑健性が向上した。

规范化提高了对拼写变体的鲁棒性。

---

## Next Actions / 次のアクション / 下一步行动

Evaluate vocabulary filtering.

語彙フィルタリングを評価する。

评估词汇过滤。