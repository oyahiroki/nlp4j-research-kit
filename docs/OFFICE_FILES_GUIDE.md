# Office Files Management Guide

このガイドでは、Word、Excel、PowerPointファイルの管理方法について説明します。

## 目次

1. [ディレクトリ構造](#ディレクトリ構造)
2. [ファイル命名規則](#ファイル命名規則)
3. [バージョン管理](#バージョン管理)
4. [ベストプラクティス](#ベストプラクティス)
5. [実験との統合](#実験との統合)

---

## ディレクトリ構造

### 論文・出版物

```text
docs/papers/
├── drafts/          # 執筆中の論文ドラフト
│   ├── paper_v1.docx
│   ├── paper_v2.docx
│   └── paper_final.docx
├── published/       # 公開済み論文
│   ├── conference_2026.pdf
│   └── journal_2026.pdf
└── reviews/         # 査読コメント・レビュー
    ├── reviewer1_comments.docx
    └── response_to_reviewers.docx
```

**用途:**
- `drafts/`: 執筆中の論文、複数バージョンの管理
- `published/`: 最終版、公開済みPDF
- `reviews/`: 査読コメント、返答文書

### プレゼンテーション

```text
docs/presentations/
├── conferences/
│   ├── icml_2026_presentation.pptx
│   └── acl_2026_poster.pptx
├── lab_meetings/
│   ├── 20260526_progress_report.pptx
│   └── 20260612_results_discussion.pptx
└── templates/
    └── lab_template.potx
```

**用途:**
- `conferences/`: 学会発表資料
- `lab_meetings/`: ラボミーティング資料
- `templates/`: 再利用可能なテンプレート

### レポート・分析

```text
reports/
├── drafts/              # レポートドラフト
│   ├── monthly_report_202605.docx
│   └── analysis_draft.docx
├── submissions/         # 投稿用ファイル
│   ├── final_report.pdf
│   └── supplementary_materials.xlsx
├── presentations/       # 発表用資料
│   └── results_presentation.pptx
├── tables/              # 表データ
│   ├── experiment_results.xlsx
│   ├── metrics_comparison.xlsx
│   └── statistics.csv
└── figures/             # 図表
    ├── figure1.png
    ├── chart1.pdf
    └── diagram1.svg
```

---

## ファイル命名規則

### 論文ファイル

**形式:** `[type]_[venue]_[year]_[version].[ext]`

**例:**
```
paper_icml_2026_v1.docx
paper_icml_2026_v2.docx
paper_icml_2026_final.docx
paper_icml_2026_final.pdf
```

**要素:**
- `type`: paper, poster, abstract
- `venue`: 学会名・ジャーナル名
- `year`: 年
- `version`: v1, v2, final

### プレゼンテーションファイル

**形式:** `[event]_[date]_[topic].[ext]`

**例:**
```
lab_meeting_20260526_results.pptx
icml_2026_oral_presentation.pptx
seminar_20260610_introduction.pptx
```

### レポートファイル

**形式:** `[type]_[period]_[version].[ext]`

**例:**
```
monthly_report_202605_draft.docx
monthly_report_202605_final.docx
quarterly_report_2026Q2.docx
```

### データ・表ファイル

**形式:** `[content]_[experiment]_[date].[ext]`

**例:**
```
metrics_exp001_20260526.xlsx
results_comparison_20260526.xlsx
statistics_summary.csv
```

---

## バージョン管理

### Word/PowerPointファイル

#### 方法1: ファイル名でバージョン管理

```text
paper_v1.docx
paper_v2.docx
paper_v3.docx
paper_final.docx
```

**メリット:**
- シンプルで分かりやすい
- 過去バージョンへの参照が容易

**デメリット:**
- ファイル数が増える
- ディスク容量を消費

#### 方法2: 日付でバージョン管理

```text
paper_20260501.docx
paper_20260515.docx
paper_20260526.docx
```

**メリット:**
- 時系列が明確
- 自動的にソート可能

#### 方法3: Git LFS（推奨）

大きなバイナリファイルはGit LFSで管理：

```bash
# Git LFSのセットアップ
git lfs install

# 追跡するファイルタイプを指定
git lfs track "*.docx"
git lfs track "*.xlsx"
git lfs track "*.pptx"

# .gitattributesが作成される
git add .gitattributes
git commit -m "Add Git LFS tracking"
```

### Excelファイル

#### CSVへの変換（推奨）

重要なデータはCSVに変換してGitで管理：

```bash
# Pythonでの変換例
import pandas as pd

# Excelを読み込み
df = pd.read_excel('data.xlsx', sheet_name='Results')

# CSVとして保存
df.to_csv('data.csv', index=False)
```

#### バージョン管理のベストプラクティス

1. **生データは別管理**: `data/raw/`に配置
2. **処理済みデータ**: `data/processed/`に配置
3. **分析結果**: `reports/tables/`に配置
4. **CSV優先**: 可能な限りCSV形式で保存

---

## ベストプラクティス

### Word文書

#### 1. スタイルの使用

```
見出し1: タイトル
見出し2: セクション
見出し3: サブセクション
本文: 通常のテキスト
```

#### 2. 変更履歴の有効化

- 共同編集時は「変更履歴の記録」を有効化
- レビュー時にコメント機能を活用
- 最終版作成時に変更を確定

#### 3. PDFエクスポート

```
最終版は必ずPDFでエクスポート:
- ファイル → エクスポート → PDF/XPS
- フォント埋め込みを確認
- ハイパーリンクを保持
```

#### 4. バックアップ

```text
archive/
└── papers/
    └── 2026/
        ├── paper_v1_20260501.docx
        ├── paper_v2_20260515.docx
        └── paper_v3_20260520.docx
```

### Excelファイル

#### 1. 名前付き範囲の使用

```
重要なデータ範囲に名前を付ける:
- 数式 → 名前の定義
- 例: "ExperimentResults", "MetricsSummary"
```

#### 2. 数式の文書化

```
A1: =AVERAGE(B2:B100)  // 平均値の計算
C1: =STDEV(B2:B100)    // 標準偏差の計算
```

#### 3. シート構成

```
Sheet1: RawData      # 生データ
Sheet2: Processed    # 処理済みデータ
Sheet3: Analysis     # 分析結果
Sheet4: Charts       # グラフ
Sheet5: Summary      # サマリー
```

#### 4. CSVエクスポート

```
重要なテーブルはCSVでもエクスポート:
- ファイル → 名前を付けて保存 → CSV
- バージョン管理に含める
```

### PowerPointファイル

#### 1. マスタースライドの使用

```
表示 → スライドマスター
- 統一されたデザイン
- フォント・色の一貫性
- ロゴ・ヘッダーの配置
```

#### 2. 図表のエクスポート

```
高解像度画像としてエクスポート:
- ファイル → エクスポート → 画像として保存
- PNG形式、300dpi以上
- reports/figures/に保存
```

#### 3. ノートの活用

```
スライドノートに以下を記録:
- 発表原稿
- 補足説明
- 参考文献
- タイミング情報
```

---

## 実験との統合

### 実験ディレクトリでのOfficeファイル管理

```text
experiments/exp001/
├── README.md
├── hypothesis.md
├── config.yaml
├── manifest.json
├── figures/
│   ├── result_chart.xlsx      # 図表作成用データ
│   ├── result_chart.png       # 生成された図
│   └── comparison_table.xlsx  # 比較表
├── metrics/
│   ├── metrics_summary.xlsx   # メトリクス集計
│   └── metrics_summary.csv    # CSV版（Git管理）
└── reports/
    ├── experiment_report.docx # 実験レポート
    └── experiment_report.pdf  # PDF版
```

### ワークフロー例

#### 1. 実験実行

```bash
# 実験を実行
python experiments/exp001/scripts/run_experiment.py

# 結果をExcelで集計
# → experiments/exp001/metrics/metrics_summary.xlsx
```

#### 2. 図表作成

```bash
# Excelで図表を作成
# → experiments/exp001/figures/result_chart.xlsx

# 図をエクスポート
# → experiments/exp001/figures/result_chart.png
```

#### 3. レポート作成

```bash
# Wordでレポート作成
# → experiments/exp001/reports/experiment_report.docx

# 図表を挿入
# PDFでエクスポート
# → experiments/exp001/reports/experiment_report.pdf
```

#### 4. バージョン管理

```bash
# CSVに変換
python tools/scripts/excel_to_csv.py \
  experiments/exp001/metrics/metrics_summary.xlsx

# Gitにコミット
git add experiments/exp001/metrics/metrics_summary.csv
git add experiments/exp001/figures/result_chart.png
git add experiments/exp001/reports/experiment_report.pdf
git commit -m "Add exp001 results and report"
```

---

## 自動化スクリプト例

### Excel → CSV変換

```python
# tools/scripts/excel_to_csv.py
import pandas as pd
import sys
from pathlib import Path

def convert_excel_to_csv(excel_path):
    """Convert all sheets in Excel to CSV files."""
    excel_file = Path(excel_path)
    output_dir = excel_file.parent
    
    # Read all sheets
    excel_data = pd.read_excel(excel_path, sheet_name=None)
    
    # Convert each sheet
    for sheet_name, df in excel_data.items():
        csv_path = output_dir / f"{excel_file.stem}_{sheet_name}.csv"
        df.to_csv(csv_path, index=False)
        print(f"Converted: {csv_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python excel_to_csv.py <excel_file>")
        sys.exit(1)
    
    convert_excel_to_csv(sys.argv[1])
```

### 図表の一括エクスポート

```python
# tools/scripts/export_figures.py
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

def export_figures_from_excel(excel_path, output_dir):
    """Export charts from Excel data as PNG files."""
    df = pd.read_excel(excel_path)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Create and save figures
    fig, ax = plt.subplots(figsize=(10, 6))
    df.plot(ax=ax)
    plt.savefig(output_path / 'chart.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Exported figures to: {output_dir}")
```

---

## トラブルシューティング

### ファイルが開けない

```bash
# ファイルの破損チェック
# Wordの場合: 「開いて修復」を試す
# Excelの場合: 別のシートから参照してみる
```

### バージョン競合

```bash
# 複数人で編集時の競合
1. 最新版をダウンロード
2. 自分の変更を別ファイルに保存
3. 差分を手動でマージ
4. 新しいバージョンとして保存
```

### ファイルサイズが大きい

```bash
# 画像の圧縮
# Word/PowerPoint: ファイル → 図の圧縮

# 不要なデータの削除
# Excel: 使用していないシートを削除

# Git LFSの使用
git lfs track "*.xlsx"
```

---

## まとめ

- **構造化**: 目的別にディレクトリを分ける
- **命名規則**: 一貫した命名規則を使用
- **バージョン管理**: ファイル名または日付で管理
- **CSV変換**: 重要なデータはCSVでも保存
- **PDF化**: 最終版はPDFでエクスポート
- **バックアップ**: 定期的にarchiveに保存

これらのプラクティスに従うことで、Officeファイルも含めた研究プロジェクト全体を効率的に管理できます。