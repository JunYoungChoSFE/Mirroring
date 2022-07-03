@Echo off
call "%HOMEPATH%\Anaconda3\Scripts\activate.bat" py37_64
call python "%~dp0/../ai_filter2.py" %1 %2
call python "%~dp0/../ai_filter3.py" %1 %2
