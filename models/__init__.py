#!/usr/bin/python3
"""
    initializes models
"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
