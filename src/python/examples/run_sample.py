#!/usr/bin/env python3
"""
Sample script for nlp4j-research-kit

This script demonstrates the basic workflow of the research kit:
1. Load configuration
2. Prepare data
3. Run experiment
4. Save results
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path


def load_config(config_path: str) -> dict:
    """Load experiment configuration from YAML file."""
    print(f"Loading configuration from: {config_path}")
    # In a real implementation, use PyYAML
    # For now, return a sample config
    return {
        "experiment_id": "sample",
        "dataset": "sample_data",
        "model": "sample_model"
    }


def prepare_data(config: dict) -> None:
    """Prepare data for the experiment."""
    print("Preparing data...")
    print(f"  Dataset: {config.get('dataset', 'N/A')}")
    print("  Data preparation complete.")


def run_experiment(config: dict) -> dict:
    """Run the experiment and return results."""
    print("Running experiment...")
    print(f"  Experiment ID: {config.get('experiment_id', 'N/A')}")
    print(f"  Model: {config.get('model', 'N/A')}")
    
    # Simulate experiment results
    results = {
        "experiment_id": config.get("experiment_id"),
        "timestamp": datetime.now().isoformat(),
        "metrics": {
            "accuracy": 0.85,
            "precision": 0.82,
            "recall": 0.88
        },
        "status": "completed"
    }
    
    print("  Experiment complete.")
    return results


def save_results(results: dict, output_dir: str) -> None:
    """Save experiment results to file."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    results_file = output_path / "results.json"
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"Results saved to: {results_file}")


def main():
    """Main execution function."""
    print("=" * 60)
    print("nlp4j-research-kit - Sample Script")
    print("=" * 60)
    print()
    
    # Get project root directory
    project_root = Path(__file__).parent.parent.parent.parent
    print(f"Project root: {project_root}")
    print()
    
    # Load configuration
    config_path = project_root / "configs" / "experiments" / "sample.yaml"
    config = load_config(str(config_path))
    print()
    
    # Prepare data
    prepare_data(config)
    print()
    
    # Run experiment
    results = run_experiment(config)
    print()
    
    # Save results
    output_dir = project_root / "experiments" / "sample" / "output"
    save_results(results, str(output_dir))
    print()
    
    print("=" * 60)
    print("Sample script completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()

# Made with Bob
