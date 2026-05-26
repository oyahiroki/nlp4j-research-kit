# Hypothesis

Wiktionary-based normalization improves embedding retrieval performance.

## Background

Orthographic variations in Japanese text (e.g., ひらがな/カタカナ variations, kanji variants) can reduce the effectiveness of embedding-based search systems.

## Proposed Solution

Apply lemma normalization using Wiktionary data before generating embeddings.

## Expected Outcome

- Improved MRR (Mean Reciprocal Rank)
- Better handling of orthographic variations
- More robust search results

## Success Criteria

- MRR improvement of at least 3%
- Consistent performance across different query types