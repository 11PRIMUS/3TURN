import sqlite3
import json
from datetime import datetime
from typing import Dict, List
import logging

logger= logging.getLogger(__name__)

def init_db(db_path: str):
    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS creations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            original_prompt TEXT,
            enhanced_prompt TEXT,
            image_path TEXT,
            model_3d_path TEXT,
            metadata TEXT
        )
    ''')
    conn.commit()
    conn.close()
    logger.info("db init")

def save_creation(db_path: str, original_prompt: str, enhanced_prompt: str, image_path: str=None, mode_3d_path: str=None, metadata: Dict=None) ->int:
    """new creation"""
    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()

    cursor.execute('''
        INSERT INTO creations 
        (timestamp, original_prompt, enhanced_prompt, image_path, model_3d_path, metadata)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        datetime.now().isoformat(),
        original_prompt,
        enhanced_prompt,
        image_path,
        model_3d_path,
        json.dumps(metadata) if metadata else None
    ))
    conn.commit()
    creation_id=cursor.lastroiwid
    conn.close()

    return creation_id

