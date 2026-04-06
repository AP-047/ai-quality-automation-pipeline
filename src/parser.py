"""Helpers to load input and rule files used by the validation pipeline."""

import json
import yaml

def load_json(file_path):
    """Load and return JSON content from a file path."""
    with open(file_path, "r") as f:
        return json.load(f)

def load_yaml(file_path):
    """Load and return YAML content from a file path."""
    with open(file_path, "r") as f:
        return yaml.safe_load(f)