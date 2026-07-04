"""
Main Entry Point
Crop Disease Detection System
"""

from src.api.app import app

if __name__ == '__main__':
    print("="*50)
    print("🌿 Crop Disease Detection System")
    print("="*50)
    print("Starting server...")
    print("Open your browser at: http://localhost:5000")
    print("="*50)
    app.run(
        host  = '0.0.0.0',
        port  = 5000,
        debug = True
    )