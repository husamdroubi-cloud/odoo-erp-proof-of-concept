@echo off
REM ============================================================
REM Restore script for Odoo ERP Proof of Concept repository
REM Project: master_parts_list_manager module
REM ============================================================

echo 🔄 Restoring Odoo ERP Proof of Concept...

REM Go to the directory of this script
cd /d %~dp0

REM Fetch latest from GitHub
git fetch origin

REM Switch to main branch
git checkout main

REM Reset to latest remote state
git pull origin main

echo ✅ Repository is up to date.
echo 📌 You are now at the checkpoint for:
type CHECKPOINT.md

pause
