python3 generate.py html 4 > html/table.html
cat html/start.html html/table.html html/end.html > cleaning_duty.html
vim -c "1,15s/Charlotte/Lisa/g | wq" cleaning_duty.html
vim -c "13,30s/Daniel/Eylul/g | wq" cleaning_duty.html
vim -c "13,30s/Haishan/Jialu/g | wq" cleaning_duty.html
vim -c "13,30s/Mike/Georg/g | wq" cleaning_duty.html
google-chrome --headless --screenshot --window-size=2200,800 --default-background-color=0 cleaning_duty.html
mv screenshot.png cleaning_duty.png
eog cleaning_duty.png
