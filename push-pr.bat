@echo off

set fn=%1
set flag=%2
cd /d %~dp0

If "%1"=="" (
    python push-pr.py
) else ( 
    if "%2"=="" (
        python push-pr.py %fn% %flag%
        ) else (
            if "%2"=="l" (
               python push-pr.py %fn%
            )
        )
    )
