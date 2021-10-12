@echo off

set fn=%1
set flag=%2
cd /d %~dp0

If "%1"=="" (
    echo Please Provide the Name of the Repository
) else ( 
    if "%2"=="" (
        python push-pr.py %fn% %flag%
        ) else (
            if "%2"=="l" (
               python C:\Users\wired\pycmd\Scripts\push-pr.py %fn%
            )
        )
    )