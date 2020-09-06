python3 generate.py html 9 > html/table.html
cat html/start.html html/table.html html/end.html > cleaning_duty.html
google-chrome --headless --screenshot --window-size=2300,800 --default-background-color=0 cleaning_duty.html
mv screenshot.png cleaning_duty.png
eog cleaning_duty.png
