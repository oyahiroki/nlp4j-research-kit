#!/usr/bin/env python3
"""
Data preparation script for nlp4j-research-kit

This script handles:
- Data loading from raw sources
- Data cleaning and preprocessing
- Data transformation
- Saving processed data
"""

import os
import json
from pathlib import Path
from typing import List, Dict, Any


class DataPreparator:
    """Data preparation class for research experiments."""
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize DataPreparator.
        
        Args:
            config: Configuration dictionary containing data paths and parameters
        """
        self.config = config
        self.project_root = Path(__file__).parent.parent.parent.parent
        
    def load_raw_data(self, data_path: str) -> List[Dict[str, Any]]:
        """
        Load raw data from file.
        
        Args:
            data_path: Path to raw data file
            
        Returns:
            List of data records
        """
        print(f"Loading raw data from: {data_path}")
        
        # Example: Load JSONL data
        data = []
        file_path = self.project_root / data_path
        
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        data.append(json.loads(line))
        else:
            print(f"Warning: File not found: {file_path}")
            print("Using sample data for demonstration.")
            data = self._generate_sample_data()
        
        print(f"Loaded {len(data)} records")
        return data
    
    def _generate_sample_data(self) -> List[Dict[str, Any]]:
        """Generate sample data for demonstration."""
        return [
            {"id": 1, "text": "これはサンプルテキストです。", "label": "sample"},
            {"id": 2, "text": "自然言語処理の研究を行います。", "label": "nlp"},
            {"id": 3, "text": "検索システムの評価実験です。", "label": "search"},
        ]
    
    def clean_data(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Clean and filter data.
        
        Args:
            data: Raw data records
            
        Returns:
            Cleaned data records
        """
        print("Cleaning data...")
        
        cleaned_data = []
        for record in data:
            # Example cleaning: remove empty texts
            if record.get('text', '').strip():
                cleaned_data.append(record)
        
        print(f"Cleaned data: {len(cleaned_data)} records (removed {len(data) - len(cleaned_data)})")
        return cleaned_data
    
    def transform_data(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Transform data for experiment.
        
        Args:
            data: Cleaned data records
            
        Returns:
            Transformed data records
        """
        print("Transforming data...")
        
        transformed_data = []
        for record in data:
            # Example transformation: add metadata
            transformed_record = {
                **record,
                "processed": True,
                "length": len(record.get('text', ''))
            }
            transformed_data.append(transformed_record)
        
        print(f"Transformed {len(transformed_data)} records")
        return transformed_data
    
    def save_processed_data(self, data: List[Dict[str, Any]], output_path: str) -> None:
        """
        Save processed data to file.
        
        Args:
            data: Processed data records
            output_path: Path to save processed data
        """
        file_path = self.project_root / output_path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        print(f"Saving processed data to: {file_path}")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            for record in data:
                f.write(json.dumps(record, ensure_ascii=False) + '\n')
        
        print(f"Saved {len(data)} records")
    
    def run(self) -> None:
        """Execute the full data preparation pipeline."""
        print("=" * 60)
        print("Data Preparation Pipeline")
        print("=" * 60)
        print()
        
        # Load raw data
        raw_data_path = self.config.get('raw_data_path', 'data/raw/sample.jsonl')
        data = self.load_raw_data(raw_data_path)
        print()
        
        # Clean data
        data = self.clean_data(data)
        print()
        
        # Transform data
        data = self.transform_data(data)
        print()
        
        # Save processed data
        processed_data_path = self.config.get('processed_data_path', 'data/processed/sample.jsonl')
        self.save_processed_data(data, processed_data_path)
        print()
        
        print("=" * 60)
        print("Data preparation completed successfully!")
        print("=" * 60)


def main():
    """Main execution function."""
    # Example configuration
    config = {
        'raw_data_path': 'data/raw/sample.jsonl',
        'processed_data_path': 'data/processed/sample.jsonl'
    }
    
    preparator = DataPreparator(config)
    preparator.run()


if __name__ == "__main__":
    main()

# Made with Bob
