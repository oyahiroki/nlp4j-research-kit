# Papers Directory

このディレクトリには、論文執筆に関連するファイルを管理します。

## ディレクトリ構造

```
papers/
├── drafts/          # 執筆中の論文ドラフト
├── published/       # 公開済み論文
└── reviews/         # 査読コメント・レビュー
```

## ファイル命名規則

### ドラフト

```
[type]_[venue]_[year]_[version].docx

例:
- paper_icml_2026_v1.docx
- paper_icml_2026_v2.docx
- paper_icml_2026_final.docx
```

### 公開済み論文

```
[venue]_[year]_[title].pdf

例:
- icml_2026_embedding_search.pdf
- acl_2026_normalization_study.pdf
```

### 査読コメント

```
[venue]_[year]_[type].docx

例:
- icml_2026_reviewer_comments.docx
- icml_2026_response_to_reviewers.docx
```

## ワークフロー

1. **ドラフト作成**: `drafts/`で執筆
2. **バージョン管理**: v1, v2, v3...と番号を付ける
3. **最終版**: `_final`サフィックスを付ける
4. **PDF化**: 最終版をPDFでエクスポート
5. **公開**: `published/`に移動

## ベストプラクティス

- 変更履歴を有効にして共同編集
- 定期的にバックアップを作成
- 最終版は必ずPDFでエクスポート
- 査読コメントは別ファイルで管理

詳細は [Office Files Guide](../OFFICE_FILES_GUIDE.md) を参照してください。