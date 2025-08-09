@echo off
pyinstaller --noconfirm --onefile --add-data "templates;templates" --add-data "static;static" desktop_app.py
pause
