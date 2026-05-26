# nlp4j-research-kit

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub](https://img.shields.io/badge/GitHub-oyahiroki%2Fnlp4j--research--kit-blue)](https://github.com/oyahiroki/nlp4j-research-kit)

NLP、検索、データ実験のための再現可能な研究プロジェクト構造

**リポジトリ**: https://github.com/oyahiroki/nlp4j-research-kit

**[English](README.md)** | 日本語

`nlp4j-research-kit`は、研究プロセス全体を管理するための標準化されたディレクトリ構造とワークフローを提供します：

- データセット
- 前処理
- 埋め込み
- 検索インデックス
- 実験
- メトリクス
- 来歴管理
- レポート

このプロジェクトは以下の方々を対象としています：

- 大学院生
- NLP研究者
- 検索エンジニア
- OSSリサーチャー
- 再現可能な実験管理

---

# 目標

研究プロジェクトは以下の理由で管理が困難になりがちです：

- データセットが散在している
- 前処理スクリプトが失われる
- 実験条件が不明確
- メトリクスが再現できない
- ノートブックが実際の実行と乖離する
- 依存関係が時間とともに変化する

このプロジェクトは以下を提供することで、これらの問題を解決することを目指しています：

- 再現可能な実験構造
- 標準化された実験ドキュメント
- 来歴管理
- Java/Python混在言語サポート
- 実験履歴管理
- 軽量なOSSフレンドリーなワークフロー

---

# 特徴

## 再現可能な実験

各実験は以下を保存します：

- 設定
- スクリプト
- 依存関係
- 実行環境
- メトリクス
- 生成された成果物

---

## 標準化されたディレクトリ構造

研究プロジェクトは統一された構造に従います。

```text
project/
├── docs/
├── data/
├── src/
├── tools/
├── configs/
├── experiments/
├── notebooks/
├── reports/
├── logs/
└── archive/
```

---

## 実験中心のワークフロー

各実験は独立しており、自己文書化されています。

```text
experiments/
  exp001/
    README.md
    hypothesis.md
    config.yaml
    manifest.json

    scripts/
    tools_snapshot/

    input/
    output/
    logs/
    metrics/
    figures/
```

---

## 来歴管理

システムは以下を保存します：

- ソースURL
- ダウンロードタイムスタンプ
- ライセンス
- ハッシュ
- 実行環境
- gitコミット

---

## Java + Python混在環境

混在言語研究環境をサポートします。

```text
src/
  java/
  python/
```

---

# 推奨ワークフロー

## 1. データの準備

元のデータセットを以下に配置：

```text
data/raw/
```

例：

```text
data/raw/jawiki-20260401.xml.bz2
```

---

## 2. データの前処理

中間データと処理済みデータセットを生成。

```text
data/interim/
data/processed/
```

---

## 3. 実験の作成

新しい実験を作成：

```text
experiments/exp001/
```

---

## 4. 仮説の記録

例：

```markdown
Wiktionaryベースの正規化が埋め込み検索性能を向上させる。
```

---

## 5. 実験の実行

以下を保存：

- スクリプト
- 設定
- メトリクス
- ログ
- 生成された図表

---

## 6. 再現性の保持

以下を保存：

- requirements.txt
- pip-freeze.txt
- pom.xml
- gitコミットハッシュ
- ランタイムバージョン

---

# ディレクトリ構造の例

```text
nlp4j-research-kit/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── docs/
│   ├── architecture/
│   ├── papers/
│   │   ├── drafts/          # 論文ドラフト (Word/LaTeX)
│   │   ├── published/       # 公開済み論文
│   │   └── reviews/         # 査読コメント
│   ├── presentations/       # プレゼン資料 (PowerPoint)
│   ├── meeting-notes/
│   └── references/
│
├── data/
│   ├── raw/
│   ├── external/
│   ├── interim/
│   ├── processed/
│   ├── embeddings/
│   ├── indexes/
│   └── metadata/
│
├── src/
│   ├── java/
│   ├── python/
│   ├── shell/
│   └── sql/
│
├── tools/
│   ├── java/
│   ├── python/
│   ├── docker/
│   └── scripts/
│
├── configs/
│   ├── datasets/
│   ├── experiments/
│   ├── models/
│   └── pipelines/
│
├── experiments/
│   ├── exp001/
│   ├── exp002/
│   └── exp003/
│
├── notebooks/
│
├── reports/
│   ├── figures/             # 図表 (PNG/PDF)
│   ├── tables/              # 表データ (Excel/CSV)
│   ├── drafts/              # レポートドラフト
│   ├── submissions/         # 投稿用ファイル
│   ├── presentations/       # 発表資料
│   └── reviews/             # レビュー資料
│
├── logs/
│
├── tmp/
│
└── archive/
```

---

# 実験README例

例：

```markdown
# exp001

## 目的

Wiktionaryベースの正規化が埋め込み検索品質を向上させるかを評価する。

---

## 仮説

レンマ正規化がMRRを改善する。

---

## データセット

- jawiki-20260401
- サンプルサイズ: 100000

---

## 結果

| metric | baseline | proposed |
|---|---:|---:|
| MRR | 0.612 | 0.644 |

---

## 観察

正規化により表記ゆれに対する頑健性が向上した。

---

## 次のアクション

語彙フィルタリングを評価する。
```

---

# manifest.json例

```json
{
  "experiment_id": "exp001",
  "created_at": "2026-05-26T10:30:00+09:00",

  "git": {
    "branch": "main",
    "commit": "abc1234",
    "dirty": true
  },

  "runtime": {
    "python": "3.11.8",
    "java": "17.0.10"
  },

  "commands": [
    "python scripts/prepare_data.py",
    "java -cp app.jar nlp4j.ExperimentRunner"
  ]
}
```

---

# 設計原則

## 不変の生データ

決して変更しない：

```text
data/raw/
```

---

## 実験 = コード + データ + 仮説

実験は以下を保存すべき：

- コード
- データセット
- 仮説
- メトリクス
- 観察
- レポート

---

## 失敗の保存

失敗した実験は貴重な研究資産です。

---

## 来歴の保存

常に以下を保存：

- ソースURL
- ライセンス
- タイムスタンプ
- ハッシュ

---

# 推奨技術

このテンプレートは以下と相性が良いです：

- Python
- Java
- Jupyter Notebook
- Apache Lucene
- OpenSearch
- Elasticsearch
- MLflow
- Docker
- JSONLデータセット

---

# 将来の拡張

可能な将来の拡張：

- 実験DAGの可視化
- 実験系譜の追跡
- 埋め込みの可視化
- 自動README生成
- 自動論文表生成
- Lucene/OpenSearch統合
- JSONL系譜管理

---

# クイックスタート

このセクションでは、GitHubに慣れていない研究者の方でも、このプロジェクトを使い始められるように、ステップバイステップで説明します。

---

## 前提条件

以下のソフトウェアをインストールしてください：

1. **Git** - バージョン管理システム
   - Windows: https://git-scm.com/download/win
   - Mac: `brew install git` または https://git-scm.com/download/mac
   - Linux: `sudo apt-get install git` (Ubuntu/Debian)

2. **Python 3.8以上**
   - https://www.python.org/downloads/

3. **Java 11以上**（Javaコンポーネントを使う場合）
   - https://adoptium.net/

---

## ステップ1: リポジトリのクローン

GitHubからプロジェクトをダウンロード（クローン）します。

### コマンドラインの場合

```bash
# プロジェクトをクローン
git clone https://github.com/oyahiroki/nlp4j-research-kit.git

# プロジェクトディレクトリに移動
cd nlp4j-research-kit
```

### GitHub Desktopの場合

1. GitHub Desktopをインストール: https://desktop.github.com/
2. File → Clone Repository
3. URL: `https://github.com/oyahiroki/nlp4j-research-kit.git`
4. ローカルパスを選択
5. Clone をクリック

---

## ステップ2: Python環境のセットアップ

### 仮想環境の作成

```bash
# 仮想環境を作成
python -m venv venv

# 仮想環境を有効化
# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Windows (コマンドプロンプト)
venv\Scripts\activate.bat

# Mac/Linux
source venv/bin/activate
```

### 依存パッケージのインストール

```bash
# 必要なパッケージをインストール
pip install -r requirements.txt
```

---

## ステップ3: プロジェクト構造の確認

```bash
# ディレクトリ構造を確認
# Windows
tree /F

# Mac/Linux
tree
```

主要なディレクトリ：
- `data/` - データセット
- `src/` - ソースコード
- `experiments/` - 実験
- `docs/` - ドキュメント
- `reports/` - レポート・図表

---

## ステップ4: サンプルスクリプトの実行

### Pythonサンプルの実行

```bash
# サンプルスクリプトを実行
python src/python/examples/run_sample.py
```

実行結果が表示されれば成功です！

### データ準備スクリプトの実行

```bash
# データ準備スクリプトを実行
python src/python/data/prepare_data.py
```

---

## ステップ5: 新しい実験の作成

### 実験ディレクトリの作成

```bash
# 新しい実験用ディレクトリを作成
# Windows
mkdir experiments\exp002\scripts experiments\exp002\input experiments\exp002\output experiments\exp002\logs experiments\exp002\metrics experiments\exp002\figures

# Mac/Linux
mkdir -p experiments/exp002/{scripts,input,output,logs,metrics,figures}
```

### 実験ドキュメントの作成

```bash
# エディタでREADME.mdを作成
# Windows
notepad experiments\exp002\README.md

# Mac/Linux
nano experiments/exp002/README.md
```

以下の内容をコピー＆ペースト：

```markdown
# exp002

## 目的

[実験の目的を記述]

## 仮説

[仮説を記述]

## データセット

- データセット名
- サンプルサイズ

## 結果

| metric | baseline | proposed |
|---|---:|---:|
| - | - | - |

## 観察

[観察結果を記述]

## 次のアクション

[次のアクションを記述]
```

---

## ステップ6: 変更の保存（Git操作）

### 基本的なGitワークフロー

```bash
# 1. 変更されたファイルを確認
git status

# 2. 変更をステージング（追加）
git add experiments/exp002/

# 3. 変更をコミット（記録）
git commit -m "Add exp002 experiment"

# 4. GitHubにプッシュ（アップロード）
git push origin main
```

### よく使うGitコマンド

```bash
# 現在の状態を確認
git status

# 変更履歴を確認
git log --oneline

# 特定のファイルを追加
git add path/to/file

# すべての変更を追加
git add .

# コミット
git commit -m "説明メッセージ"

# リモートから最新版を取得
git pull origin main

# リモートにプッシュ
git push origin main
```

---

## ステップ7: データの配置

### 生データの配置

```bash
# data/raw/ディレクトリにデータを配置
# 例: Wikipediaダンプファイル
cp /path/to/jawiki-20260401.xml.bz2 data/raw/
```

### データの前処理

```bash
# 前処理スクリプトを実行
python src/python/data/prepare_data.py
```

処理済みデータは以下に保存されます：
- `data/interim/` - 中間データ
- `data/processed/` - 最終処理済みデータ

---

## よくある質問（FAQ）

### Q1: Gitのインストール確認方法は？

```bash
git --version
```

バージョンが表示されればOKです。

### Q2: Python環境が正しく設定されているか確認するには？

```bash
python --version
pip list
```

### Q3: 仮想環境が有効になっているか確認するには？

コマンドプロンプトの先頭に `(venv)` が表示されていればOKです。

```
(venv) C:\Users\username\nlp4j-research-kit>
```

### Q4: GitHubにプッシュできない場合は？

認証が必要です。以下のいずれかを設定してください：

1. **Personal Access Token（推奨）**
   - GitHub → Settings → Developer settings → Personal access tokens
   - トークンを生成してパスワードの代わりに使用

2. **SSH Key**
   - SSH鍵を生成してGitHubに登録
   - 詳細: https://docs.github.com/ja/authentication

### Q5: エラーが出た場合は？

```bash
# 詳細なエラーメッセージを確認
python -v src/python/examples/run_sample.py

# ログファイルを確認
cat logs/error.log  # Mac/Linux
type logs\error.log  # Windows
```

---

## 次のステップ

1. [詳細なクイックスタートガイド](docs/QUICKSTART.md)を読む
2. [サンプル実験（exp001）](experiments/exp001/)を確認する
3. [Officeファイル管理ガイド](docs/OFFICE_FILES_GUIDE.md)を読む
4. 独自の実験を作成する

---

## サポート・コミュニティ

- **Issues**: https://github.com/oyahiroki/nlp4j-research-kit/issues
- **Discussions**: https://github.com/oyahiroki/nlp4j-research-kit/discussions
- **Wiki**: https://github.com/oyahiroki/nlp4j-research-kit/wiki

質問や問題があれば、遠慮なくIssuesで報告してください！

---

# Officeファイル管理

## ドキュメント整理

### 論文・出版物

論文執筆に関連するファイルは以下のように管理します：

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

### プレゼンテーション

プレゼンテーション資料は以下に配置します：

```text
docs/presentations/
├── conference_2026_slides.pptx
├── lab_meeting_20260526.pptx
└── poster_session.pptx
```

### レポート・分析

実験レポートや分析資料は以下に配置します：

```text
reports/
├── drafts/              # レポートドラフト
│   ├── monthly_report.docx
│   └── analysis_draft.docx
├── submissions/         # 投稿用ファイル
│   ├── final_report.pdf
│   └── supplementary.xlsx
├── presentations/       # 発表用資料
│   └── results_presentation.pptx
├── tables/              # 表データ
│   ├── experiment_results.xlsx
│   ├── metrics_comparison.xlsx
│   └── statistics.csv
└── figures/             # 図表
    ├── figure1.png
    └── chart1.pdf
```

---

## ファイル命名規則

### 論文

```text
[type]_[venue]_[year]_[version].docx
例: paper_icml_2026_v3.docx
```

### プレゼンテーション

```text
[event]_[date]_[topic].pptx
例: lab_meeting_20260526_results.pptx
```

### レポート

```text
[type]_[period]_[version].docx
例: monthly_report_202605_final.docx
```

### 表

```text
[content]_[experiment]_[date].xlsx
例: metrics_exp001_20260526.xlsx
```

---

## バージョン管理戦略

### テキスト文書（Word/PowerPoint）

1. **メジャーバージョン**: ファイル名にバージョン番号を使用
   - `paper_v1.docx`, `paper_v2.docx`, `paper_v3.docx`

2. **最終版**: `_final`サフィックスを付ける
   - `paper_final.docx`, `report_final.docx`

3. **日付版**: ISO日付形式を使用
   - `slides_20260526.pptx`

### データファイル（Excel）

1. **生データは別管理**: `data/raw/`に保存
2. **処理済み表**: `reports/tables/`に保存
3. **バージョン管理にはCSVを使用**: 可能な限りCSVに変換

---

## ベストプラクティス

### Word文書

- 一貫したフォーマットのためにスタイルを使用
- 共同編集のために変更履歴を有効化
- 最終版はPDFでエクスポート
- `archive/`にバックアップコピーを保持

### Excelファイル

- 重要なデータには名前付き範囲を使用
- 数式と計算を文書化
- バージョン管理のために主要な表をCSVでエクスポート
- 論理的な表ごとに1シート

### PowerPointファイル

- 一貫性のためにマスタースライドを使用
- 図を高解像度画像としてエクスポート
- プレゼンターノートを別途保存
- 古いバージョンを定期的にアーカイブ

---

## 実験との統合

実験ごとにOfficeファイルを管理する場合：

```text
experiments/exp001/
├── README.md
├── figures/
│   ├── result_chart.xlsx    # 図表作成用データ
│   └── result_chart.png     # 生成された図
├── metrics/
│   └── metrics_summary.xlsx # メトリクス集計
└── reports/
    └── experiment_report.docx  # 実験レポート
```

---

# 哲学

研究は以下であるべきです：

- 再現可能
- 追跡可能
- 説明可能
- 整理されている
- 共有可能

このプロジェクトは、研究プロジェクトを長期間にわたって維持しやすくすることを目指しています。

---

# ライセンス

Apache License 2.0