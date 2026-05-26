#!/usr/bin/env python3
"""
Excel to CSV Converter

This script converts Excel files to CSV format for better version control.
It can convert all sheets in an Excel file to separate CSV files.

Usage:
    python excel_to_csv.py <excel_file>
    python excel_to_csv.py <excel_file> --output-dir <output_directory>
    python excel_to_csv.py <excel_file> --sheet <sheet_name>
"""

import argparse
import sys
from pathlib import Path
from typing import Optional


def convert_excel_to_csv(
    excel_path: str,
    output_dir: Optional[str] = None,
    sheet_name: Optional[str] = None
) -> None:
    """
    Convert Excel file to CSV format.
    
    Args:
        excel_path: Path to Excel file
        output_dir: Output directory for CSV files (default: same as Excel file)
        sheet_name: Specific sheet to convert (default: all sheets)
    """
    try:
        import pandas as pd
    except ImportError:
        print("Error: pandas is required. Install it with: pip install pandas openpyxl")
        sys.exit(1)
    
    excel_file = Path(excel_path)
    
    if not excel_file.exists():
        print(f"Error: File not found: {excel_path}")
        sys.exit(1)
    
    # Determine output directory
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path = excel_file.parent
    
    print(f"Converting: {excel_file}")
    print(f"Output directory: {output_path}")
    print()
    
    try:
        # Read Excel file
        if sheet_name:
            # Convert specific sheet
            df = pd.read_excel(excel_path, sheet_name=sheet_name)
            csv_path = output_path / f"{excel_file.stem}_{sheet_name}.csv"
            df.to_csv(csv_path, index=False, encoding='utf-8-sig')
            print(f"✓ Converted sheet '{sheet_name}' to: {csv_path}")
        else:
            # Convert all sheets
            excel_data = pd.read_excel(excel_path, sheet_name=None)
            
            if len(excel_data) == 1:
                # Single sheet: use simple filename
                sheet_name, df = list(excel_data.items())[0]
                csv_path = output_path / f"{excel_file.stem}.csv"
                df.to_csv(csv_path, index=False, encoding='utf-8-sig')
                print(f"✓ Converted to: {csv_path}")
            else:
                # Multiple sheets: include sheet name in filename
                for sheet_name, df in excel_data.items():
                    # Sanitize sheet name for filename
                    safe_sheet_name = "".join(
                        c for c in sheet_name if c.isalnum() or c in (' ', '-', '_')
                    ).strip()
                    csv_path = output_path / f"{excel_file.stem}_{safe_sheet_name}.csv"
                    df.to_csv(csv_path, index=False, encoding='utf-8-sig')
                    print(f"✓ Converted sheet '{sheet_name}' to: {csv_path}")
        
        print()
        print("Conversion completed successfully!")
        
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description="Convert Excel files to CSV format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert all sheets
  python excel_to_csv.py data.xlsx
  
  # Convert to specific directory
  python excel_to_csv.py data.xlsx --output-dir output/
  
  # Convert specific sheet
  python excel_to_csv.py data.xlsx --sheet Results
        """
    )
    
    parser.add_argument(
        'excel_file',
        help='Path to Excel file (.xlsx or .xls)'
    )
    
    parser.add_argument(
        '-o', '--output-dir',
        help='Output directory for CSV files (default: same as Excel file)',
        default=None
    )
    
    parser.add_argument(
        '-s', '--sheet',
        help='Specific sheet name to convert (default: all sheets)',
        default=None
    )
    
    args = parser.parse_args()
    
    convert_excel_to_csv(
        excel_path=args.excel_file,
        output_dir=args.output_dir,
        sheet_name=args.sheet
    )


if __name__ == "__main__":
    main()

# Made with Bob
