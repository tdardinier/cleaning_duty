python3 generate.py html 21 > html/table.html
cat html/start.html html/table.html html/end.html > cleaning_duty.html

if [ "$(uname)" == "Darwin" ]; then
    /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless --screenshot=cleaning_duty.png --window-size=2000,1414 --default-background-color=0 cleaning_duty.html
    open -a Preview cleaning_duty.png
else
    google-chrome --headless --screenshot=cleaning_duty.png  --window-size=2000,1414 --default-background-color=0 --hide-scrollbars cleaning_duty.html
    eog cleaning_duty.png
fi
