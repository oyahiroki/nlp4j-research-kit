# Quick Start Guide

このガイドでは、nlp4j-research-kitを使って最初の実験を実行する方法を説明します。

## 前提条件

- Python 3.8以上
- Java 11以上（Javaコンポーネントを使用する場合）
- Git

## セットアップ

### 1. リポジトリのクローン

```bash
git clone https://github.com/yourname/nlp4j-research-kit.git
cd nlp4j-research-kit
```

### 2. Python環境のセットアップ

```bash
# 仮想環境の作成
python -m venv venv

# 仮想環境の有効化
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# 依存パッケージのインストール（requirements.txtを作成後）
pip install -r requirements.txt
```

### 3. ディレクトリ構造の確認

```bash
# プロジェクト構造を確認
tree -L 2
```

## サンプル実験の実行

### 方法1: Pythonスクリプトの実行

```bash
python src/python/examples/run_sample.py
```

### 方法2: データ準備スクリプトの実行

```bash
python src/python/data/prepare_data.py
```

### 方法3: Javaプログラムの実行

```bash
# コンパイル
javac -d bin src/java/nlp4j/ExperimentRunner.java

# 実行
java -cp bin nlp4j.ExperimentRunner exp001
```

## 新しい実験の作成

### 1. 実験ディレクトリの作成

```bash
mkdir -p experiments/exp002/{scripts,tools_snapshot,input,output,logs,metrics,figures}
```

### 2. 実験ドキュメントの作成

```bash
# README.mdの作成
cat > experiments/exp002/README.md << 'EOF'
# exp002

## Purpose

[実験の目的を記述]

## Hypothesis

[仮説を記述]

## Dataset

- データセット名
- サンプルサイズ

## Result

| metric | baseline | proposed |
|---|---:|---:|
| MRR | - | - |

## Observation

[観察結果を記述]

## Next Actions

[次のアクションを記述]
EOF
```

### 3. 設定ファイルの作成

```bash
# config.yamlの作成
cat > experiments/exp002/config.yaml << 'EOF'
experiment:
  id: exp002
  name: "Your Experiment Name"
  description: "Experiment description"

dataset:
  name: your-dataset
  source: data/raw/your-data.jsonl
  
# その他の設定...
EOF
```

### 4. 実験の実行

```bash
# スクリプトを作成して実行
python experiments/exp002/scripts/run_experiment.py
```

## データの配置

### 生データの配置

```bash
# 生データをdata/raw/に配置
cp /path/to/your/data.jsonl data/raw/
```

### データの前処理

```bash
# 前処理スクリプトの実行
python src/python/data/prepare_data.py
```

処理済みデータは以下に保存されます：
- `data/interim/` - 中間データ
- `data/processed/` - 最終処理済みデータ

## 実験結果の確認

### メトリクスの確認

```bash
# メトリクスファイルの確認
cat experiments/exp001/metrics/results.json
```

### ログの確認

```bash
# ログファイルの確認
cat experiments/exp001/logs/experiment.log
```

### 図表の確認

```bash
# 生成された図表を確認
ls experiments/exp001/figures/
```

## ベストプラクティス

### 1. 実験前のチェックリスト

- [ ] 仮説を明確に定義
- [ ] データセットを準備
- [ ] 設定ファイルを作成
- [ ] 実験スクリプトを準備
- [ ] 評価メトリクスを定義

### 2. 実験中

- [ ] ログを記録
- [ ] 中間結果を保存
- [ ] エラーを記録
- [ ] 進捗を文書化

### 3. 実験後

- [ ] 結果を保存
- [ ] メトリクスを計算
- [ ] 図表を生成
- [ ] README.mdを更新
- [ ] manifest.jsonを作成

## トラブルシューティング

### Python環境の問題

```bash
# 仮想環境を再作成
deactivate
rm -rf venv
python -m venv venv
source venv/bin/activate  # または venv\Scripts\activate
pip install -r requirements.txt
```

### Java環境の問題

```bash
# Javaバージョンの確認
java -version
javac -version

# クラスパスの確認
echo $CLASSPATH  # Linux/Mac
echo %CLASSPATH%  # Windows
```

### データの問題

```bash
# データファイルの存在確認
ls -lh data/raw/

# データファイルの形式確認
head -n 5 data/raw/your-data.jsonl
```

## 次のステップ

1. [アーキテクチャドキュメント](architecture/overview.md)を読む
2. サンプル実験（exp001）を確認する
3. 独自の実験を作成する
4. 結果を分析する
5. レポートを作成する

## 参考資料

- [README.md](../README.md) - プロジェクト概要
- [Architecture Overview](architecture/overview.md) - アーキテクチャ詳細
- [experiments/exp001/](../experiments/exp001/) - サンプル実験

## サポート

問題が発生した場合は、GitHubのIssuesで報告してください。