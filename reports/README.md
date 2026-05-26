# Reports Directory

このディレクトリには、実験レポート、分析結果、図表などを管理します。

## ディレクトリ構造

```
reports/
├── drafts/              # レポートドラフト
├── submissions/         # 投稿用ファイル
├── presentations/       # 発表用資料
├── tables/              # 表データ (Excel/CSV)
├── figures/             # 図表 (PNG/PDF)
└── reviews/             # レビュー資料
```

## 各ディレクトリの用途

### drafts/
執筆中のレポート、分析文書

**ファイル例:**
```
monthly_report_202605_draft.docx
analysis_draft.docx
summary_v1.docx
```

### submissions/
投稿・提出用の最終版ファイル

**ファイル例:**
```
final_report.pdf
supplementary_materials.xlsx
appendix.pdf
```

### presentations/
発表用のプレゼンテーション資料

**ファイル例:**
```
results_presentation.pptx
poster_session.pptx
demo_slides.pptx
```

### tables/
実験結果の表データ

**ファイル例:**
```
experiment_results.xlsx
metrics_comparison.xlsx
statistics_summary.csv
```

**ベストプラクティス:**
- Excelで作成・編集
- 重要なテーブルはCSVでもエクスポート
- CSVファイルをGitで管理

### figures/
グラフ、図、チャート

**ファイル例:**
```
figure1_accuracy_comparison.png
figure2_performance_chart.pdf
diagram_architecture.svg
```

**推奨形式:**
- PNG: 300dpi以上（論文用）
- PDF: ベクター形式（拡大可能）
- SVG: 編集可能なベクター形式

### reviews/
レビュー資料、フィードバック

**ファイル例:**
```
peer_review_comments.docx
revision_notes.docx
feedback_summary.xlsx
```

## ファイル命名規則

### レポート

```
[type]_[period]_[version].docx

例:
- monthly_report_202605_draft.docx
- monthly_report_202605_final.docx
- quarterly_report_2026Q2.docx
```

### 表データ

```
[content]_[experiment]_[date].xlsx

例:
- metrics_exp001_20260526.xlsx
- results_comparison_20260526.xlsx
- statistics_all_experiments.xlsx
```

### 図表

```
figure[number]_[description].[ext]

例:
- figure1_accuracy_comparison.png
- figure2_loss_curve.pdf
- chart_performance_overview.png
```

## ワークフロー例

### 1. 実験結果の集計

```bash
# 実験を実行
python experiments/exp001/scripts/run_experiment.py

# 結果をExcelで集計
# → reports/tables/metrics_exp001.xlsx
```

### 2. 図表の作成

```bash
# Excelまたはスクリプトで図表を作成
python tools/scripts/create_figures.py

# 図をエクスポート
# → reports/figures/figure1.png
```

### 3. レポート作成

```bash
# Wordでレポート作成
# → reports/drafts/monthly_report.docx

# 図表を挿入
# 最終版をPDFでエクスポート
# → reports/submissions/monthly_report.pdf
```

### 4. バージョン管理

```bash
# ExcelをCSVに変換
python tools/scripts/excel_to_csv.py reports/tables/metrics_exp001.xlsx

# Gitにコミット
git add reports/tables/metrics_exp001.csv
git add reports/figures/figure1.png
git add reports/submissions/monthly_report.pdf
git commit -m "Add monthly report and results"
```

## Excel → CSV 変換

重要なデータはCSV形式でもバージョン管理します：

```bash
# 単一ファイルの変換
python tools/scripts/excel_to_csv.py reports/tables/results.xlsx

# 特定のシートのみ変換
python tools/scripts/excel_to_csv.py reports/tables/results.xlsx --sheet Summary

# 出力先を指定
python tools/scripts/excel_to_csv.py reports/tables/results.xlsx --output-dir data/processed/
```

## ベストプラクティス

### Excelファイル

1. **シート構成を明確に**
   - Sheet1: RawData
   - Sheet2: Processed
   - Sheet3: Summary

2. **名前付き範囲を使用**
   - 重要なデータ範囲に名前を付ける
   - 数式で参照しやすくする

3. **CSVでもエクスポート**
   - バージョン管理のため
   - 他のツールとの互換性

### 図表

1. **高解像度で保存**
   - PNG: 300dpi以上
   - PDF: ベクター形式

2. **ファイル名を明確に**
   - 内容が分かる名前
   - 連番を使用

3. **複数形式で保存**
   - 編集用: .xlsx, .pptx
   - 配布用: .png, .pdf

### レポート

1. **バージョン管理**
   - ドラフト版: `_draft`, `_v1`, `_v2`
   - 最終版: `_final`

2. **PDF化**
   - 最終版は必ずPDF
   - フォント埋め込みを確認

3. **バックアップ**
   - 定期的に`archive/`に保存
   - 重要なバージョンを保持

## 関連ドキュメント

- [Office Files Guide](../docs/OFFICE_FILES_GUIDE.md) - 詳細なガイド
- [Quick Start](../docs/QUICKSTART.md) - クイックスタート
- [Architecture Overview](../docs/architecture/overview.md) - アーキテクチャ

## トラブルシューティング

### Excelファイルが大きすぎる

```bash
# 不要なシートを削除
# 画像を圧縮
# 使用していないセルをクリア
```

### 図表の解像度が低い

```bash
# PowerPoint/Excelでエクスポート時に解像度を指定
# ファイル → エクスポート → 画像として保存 → 解像度: 300dpi
```

### CSVの文字化け

```bash
# UTF-8 with BOM形式で保存
# Excelで開く場合は「データ → テキストから」を使用