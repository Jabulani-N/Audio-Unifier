#!/usr/bin/env python3
"""
summons selection box scripts to determine settings,
then runs input_to_output to convert relevant files
"""

format_picker = __import__('pick_desired_format').pick_format

#user selects target format
target_format = format_picker()
