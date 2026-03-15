# Python 練習：自動抓季度動畫（同步產出 TXT 與存入 MySQL)
# -Anime Scraper: Sync Output to TXT and MySQL
AMI3.0.py為爬蟲部分，爬蟲對象為"https://acgsecrets.hk/bangumi/" 的動畫資訊站。
執行後依照提示輸入年份及季度(月)，每季為3個月一論，EX：202001、202004或202107。
若需存至MySQL中並執行ANISQL.py，則需保存TXT文字檔。

ANISQL.py功用為將前述產生的文件檔引入資料庫、查詢及修改，執行後依照提示操作即可，資料庫主要構成為動畫作品的中文名、日文名及日文(英文拼音)等。

最後，需注意的是檔案路徑要正確。
