# agar `from app.main import app` selalu bisa saat pytest
import os, sys
ROOT = os.path.abspath(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
