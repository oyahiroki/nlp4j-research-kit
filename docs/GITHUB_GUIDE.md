# GitHub初心者向けガイド

このガイドでは、GitHubを初めて使う研究者の方向けに、基本的な使い方を説明します。

## 目次

1. [Gitとは？GitHubとは？](#gitとはgithubとは)
2. [初期セットアップ](#初期セットアップ)
3. [基本的なワークフロー](#基本的なワークフロー)
4. [よく使うコマンド](#よく使うコマンド)
5. [トラブルシューティング](#トラブルシューティング)

---

## Gitとは？GitHubとは？

### Git
- **バージョン管理システム**
- ファイルの変更履歴を記録
- 複数人での共同作業を支援
- ローカル（自分のPC）で動作

### GitHub
- **Gitのホスティングサービス**
- オンラインでコードを共有
- 共同作業のプラットフォーム
- バックアップとしても機能

### なぜ研究でGitを使うのか？

1. **再現性**: 過去のバージョンに戻れる
2. **追跡性**: 誰がいつ何を変更したか記録
3. **共同作業**: 複数人で同時に作業可能
4. **バックアップ**: クラウドに自動保存
5. **公開**: 研究成果を簡単に共有

---

## 初期セットアップ

### 1. Gitのインストール

#### Windows

1. https://git-scm.com/download/win からダウンロード
2. インストーラーを実行
3. デフォルト設定でOK

#### Mac

```bash
# Homebrewを使う場合
brew install git

# または
# Xcodeコマンドラインツールをインストール
xcode-select --install
```

#### Linux (Ubuntu/Debian)

```bash
sudo apt-get update
sudo apt-get install git
```

### 2. Gitの初期設定

```bash
# ユーザー名を設定
git config --global user.name "Your Name"

# メールアドレスを設定
git config --global user.email "your.email@example.com"

# 設定を確認
git config --list
```

### 3. GitHubアカウントの作成

1. https://github.com にアクセス
2. Sign up をクリック
3. メールアドレス、パスワードを入力
4. メール認証を完了

### 4. 認証の設定

#### Personal Access Token（推奨）

1. GitHub → Settings → Developer settings
2. Personal access tokens → Tokens (classic)
3. Generate new token
4. スコープを選択（repo, workflow など）
5. トークンをコピー（後で使用）

#### SSH Key（上級者向け）

```bash
# SSH鍵を生成
ssh-keygen -t ed25519 -C "your.email@example.com"

# 公開鍵をコピー
# Windows
type %USERPROFILE%\.ssh\id_ed25519.pub

# Mac/Linux
cat ~/.ssh/id_ed25519.pub

# GitHubに登録
# Settings → SSH and GPG keys → New SSH key
```

---

## 基本的なワークフロー

### ステップ1: リポジトリのクローン

```bash
# HTTPSでクローン
git clone https://github.com/oyahiroki/nlp4j-research-kit.git

# SSHでクローン（SSH鍵設定済みの場合）
git clone git@github.com:oyahiroki/nlp4j-research-kit.git

# ディレクトリに移動
cd nlp4j-research-kit
```

### ステップ2: ファイルの編集

```bash
# 新しいファイルを作成
echo "# My Experiment" > experiments/exp002/README.md

# 既存のファイルを編集
# お好みのエディタで編集
```

### ステップ3: 変更の確認

```bash
# 変更されたファイルを確認
git status

# 変更内容の詳細を確認
git diff
```

### ステップ4: 変更をステージング

```bash
# 特定のファイルを追加
git add experiments/exp002/README.md

# 複数のファイルを追加
git add experiments/exp002/

# すべての変更を追加
git add .
```

### ステップ5: 変更をコミット

```bash
# コミット（変更を記録）
git commit -m "Add exp002 experiment"

# 詳細なメッセージを書く場合
git commit
# エディタが開くので、詳細を記述
```

### ステップ6: GitHubにプッシュ

```bash
# リモートにプッシュ
git push origin main

# 初回プッシュの場合
git push -u origin main
```

### ステップ7: 最新版を取得

```bash
# リモートから最新版を取得
git pull origin main
```

---

## よく使うコマンド

### 状態確認

```bash
# 現在の状態を確認
git status

# 変更履歴を確認
git log

# 簡潔な履歴表示
git log --oneline

# グラフ表示
git log --graph --oneline --all
```

### ファイル操作

```bash
# ファイルを追加
git add <file>

# ファイルを削除
git rm <file>

# ファイル名を変更
git mv <old> <new>
```

### 変更の取り消し

```bash
# ステージングを取り消し
git reset <file>

# 変更を破棄（注意！）
git checkout -- <file>

# 最後のコミットを取り消し
git reset --soft HEAD~1

# コミットを完全に取り消し（注意！）
git reset --hard HEAD~1
```

### ブランチ操作

```bash
# ブランチ一覧
git branch

# 新しいブランチを作成
git branch <branch-name>

# ブランチを切り替え
git checkout <branch-name>

# ブランチを作成して切り替え
git checkout -b <branch-name>

# ブランチをマージ
git merge <branch-name>
```

### リモート操作

```bash
# リモートリポジトリを確認
git remote -v

# リモートから取得
git fetch origin

# リモートから取得してマージ
git pull origin main

# リモートにプッシュ
git push origin main
```

---

## 実践例：実験を追加する

### シナリオ
新しい実験（exp003）を作成して、GitHubに保存する

### 手順

```bash
# 1. 最新版を取得
git pull origin main

# 2. 実験ディレクトリを作成
mkdir -p experiments/exp003/{scripts,input,output,logs,metrics,figures}

# 3. README.mdを作成
cat > experiments/exp003/README.md << 'EOF'
# exp003

## Purpose
新しい正規化手法の評価

## Hypothesis
形態素解析ベースの正規化がMRRを改善する

## Dataset
- jawiki-20260401
- sample size: 50000
EOF

# 4. 変更を確認
git status

# 5. 変更を追加
git add experiments/exp003/

# 6. コミット
git commit -m "Add exp003: morphological normalization experiment"

# 7. プッシュ
git push origin main
```

---

## .gitignoreの使い方

### .gitignoreとは？

Gitで管理したくないファイルを指定するファイル

### よくある除外対象

```gitignore
# Python
__pycache__/
*.pyc
.venv/

# データファイル（大きいファイル）
data/raw/*.bz2
data/raw/*.gz
*.bin

# 一時ファイル
*.tmp
*.log

# OS固有
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
```

### 使い方

```bash
# .gitignoreファイルを編集
nano .gitignore

# 変更をコミット
git add .gitignore
git commit -m "Update .gitignore"
```

---

## ブランチを使った作業

### ブランチとは？

- 独立した作業スペース
- 実験的な変更を安全に試せる
- 複数の機能を並行開発できる

### 基本的な使い方

```bash
# 1. 新しいブランチを作成
git checkout -b feature/new-experiment

# 2. 作業を行う
# ファイルを編集...

# 3. 変更をコミット
git add .
git commit -m "Add new experiment"

# 4. mainブランチに戻る
git checkout main

# 5. ブランチをマージ
git merge feature/new-experiment

# 6. ブランチを削除
git branch -d feature/new-experiment
```

### ブランチ戦略の例

```
main          ← 安定版
├── develop   ← 開発版
│   ├── feature/exp001  ← 実験1
│   ├── feature/exp002  ← 実験2
│   └── feature/exp003  ← 実験3
```

---

## コミットメッセージのベストプラクティス

### 良いコミットメッセージ

```bash
# 明確で具体的
git commit -m "Add exp001: Wiktionary normalization experiment"

# 変更の理由を説明
git commit -m "Fix data preprocessing bug that caused encoding errors"

# 複数行で詳細を記述
git commit -m "Add new evaluation metrics

- Add MRR calculation
- Add Precision@K
- Add Recall@K
- Update documentation"
```

### 避けるべきコミットメッセージ

```bash
# 曖昧
git commit -m "update"
git commit -m "fix"
git commit -m "changes"

# 説明不足
git commit -m "."
git commit -m "wip"
```

### コミットメッセージの規約

```
<type>: <subject>

<body>

<footer>
```

**Type:**
- `feat`: 新機能
- `fix`: バグ修正
- `docs`: ドキュメント
- `style`: フォーマット
- `refactor`: リファクタリング
- `test`: テスト
- `chore`: その他

**例:**
```bash
git commit -m "feat: Add exp001 experiment

Implement Wiktionary-based normalization experiment.
Includes data preprocessing, model training, and evaluation.

Closes #123"
```

---

## トラブルシューティング

### Q1: コミットを間違えた

```bash
# 最後のコミットを修正
git commit --amend -m "Correct commit message"

# ファイルを追加し忘れた場合
git add forgotten_file.py
git commit --amend --no-edit
```

### Q2: 変更を破棄したい

```bash
# 特定のファイルの変更を破棄
git checkout -- <file>

# すべての変更を破棄（注意！）
git reset --hard HEAD
```

### Q3: プッシュできない

```bash
# エラー: Updates were rejected
# 原因: リモートに新しいコミットがある

# 解決方法1: プル→マージ→プッシュ
git pull origin main
# 競合を解決
git push origin main

# 解決方法2: リベース
git pull --rebase origin main
git push origin main
```

### Q4: マージ競合が発生した

```bash
# 1. 競合ファイルを確認
git status

# 2. ファイルを編集して競合を解決
# <<<<<<< HEAD
# 自分の変更
# =======
# 他人の変更
# >>>>>>> branch-name

# 3. 解決したファイルを追加
git add <resolved-file>

# 4. マージを完了
git commit
```

### Q5: 大きなファイルをプッシュできない

```bash
# Git LFSを使用
git lfs install
git lfs track "*.bin"
git lfs track "*.model"
git add .gitattributes
git commit -m "Add Git LFS tracking"
git push origin main
```

### Q6: 認証エラー

```bash
# Personal Access Tokenを使用
# ユーザー名: GitHubユーザー名
# パスワード: Personal Access Token

# または、認証情報を保存
git config --global credential.helper store
```

---

## GitHub Desktop（GUI）の使い方

### インストール

https://desktop.github.com/ からダウンロード

### 基本操作

1. **Clone**: File → Clone Repository
2. **Commit**: 変更を確認 → Summary入力 → Commit
3. **Push**: Push origin
4. **Pull**: Fetch origin → Pull origin

### メリット

- GUIで直感的
- 変更の可視化
- 競合解決が簡単
- 初心者に優しい

---

## VS Codeでの Git操作

### 拡張機能

- **GitLens**: Git履歴の可視化
- **Git Graph**: ブランチのグラフ表示
- **Git History**: ファイル履歴の表示

### 基本操作

1. **Source Control**: サイドバーのアイコン
2. **Stage**: + ボタン
3. **Commit**: メッセージ入力 → ✓ ボタン
4. **Push/Pull**: ... メニュー

---

## 参考資料

### 公式ドキュメント

- Git公式: https://git-scm.com/doc
- GitHub Docs: https://docs.github.com/ja
- Pro Git（日本語版）: https://git-scm.com/book/ja/v2

### チュートリアル

- GitHub Learning Lab: https://lab.github.com/
- Atlassian Git Tutorial: https://www.atlassian.com/git/tutorials

### チートシート

- GitHub Git Cheat Sheet: https://education.github.com/git-cheat-sheet-education.pdf

---

## まとめ

### 基本的なワークフロー

```bash
# 1. クローン（初回のみ）
git clone https://github.com/oyahiroki/nlp4j-research-kit.git

# 2. 最新版を取得
git pull origin main

# 3. 作業
# ファイルを編集...

# 4. 変更を確認
git status
git diff

# 5. 変更を追加
git add .

# 6. コミット
git commit -m "説明メッセージ"

# 7. プッシュ
git push origin main
```

### 覚えておくべきコマンド

```bash
git status    # 状態確認
git add .     # 変更を追加
git commit    # コミット
git push      # プッシュ
git pull      # プル
git log       # 履歴確認
```

これらの基本を押さえれば、研究プロジェクトでGitを効果的に使えます！