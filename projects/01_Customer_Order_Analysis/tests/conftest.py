"""
Pytest configuration for Customer Order Analysis tests.
Adds src directory to Python path so tests can import modules.
"""

import sys
from pathlib import Path

# Add src directory to Python path
project_root = Path(__file__).parent.parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))
