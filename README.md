# --ZhiHu-Answer-Video-Question-Article-Column
知乎回答、視頻、提問、文章、專欄抓取-ZhiHu-Answer-Video-Question-Article-Column

# 系統條件

可在terminal中使用![yt-dlp](https://github.com/yt-dlp/yt-dlp)，並且M$WIN需要修改加上.exe後綴名。

可在terminal中使用![google-chrome](https://www.google.com/chrome/)，並且M$WIN需要修改加上.exe後綴名。

# 使用教程

1.python -m pip install -r requirements.txt或pip install -r requirements.txt。

2.安裝好![geckodriver](https://github.com/mozilla/geckodriver)，參照![geckodriver](https://github.com/mozilla/geckodriver)的使用教程。

3.安裝好![chromedriver](https://chromedriver.chromium.org/downloads)，參照![chromedriver](https://chromedriver.chromium.org/downloads)的使用教程。

4.輸入命令![google-chrome](https://www.google.com/chrome/) --remote-debugging-port=9222 --user-data-dir="/home/a/chrome_debugging"（請根據M$WIN添加.exe並更換NTFS等文件系統的路徑格式），以運行允許被chromedriver操縱的最新版本原生瀏覽器。（除此以外不能爬取知乎的絕大多數用戶數據。）

5.修改get_index.py中的lao-liang-83-95修改為你所要抓取的知乎用戶的HTTP TOKEN。

6.python get_index.py，抓取A.V.Q.A.C.索引文件。

7.安裝好![yt-dlp](https://github.com/yt-dlp/yt-dlp)（在![GitHub](https://github.com/yt-dlp/yt-dlp)下載）。

8.python download.py，包括本體無JS網頁和圖片完全下載用戶內回答、視頻、提問、文章、專欄。
