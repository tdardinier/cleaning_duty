set PYTHONIOENCODING=utf-8
python generate.py html 20 > html/table.html
wsl cat html/start.html html/table.html html/end.html > cleaning_duty.html
"C:\Program Files\Google\Chrome\Application\chrome.exe" --headless --screenshot="%cd%\cleaning_duty.png" --disable-gpu --window-size=2000,1433 --default-background-color=0 --hide-scrollbars "%cd%\cleaning_duty.html"
