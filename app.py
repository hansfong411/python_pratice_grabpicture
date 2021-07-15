from bs4 import BeautifulSoup
import requests
import os
import urllib.parse

# 明里
avname = input ("AV 女優關鍵字?  ")
if not os.path.exists(avname):
    os.mkdir(avname)  # 建立資料夾
urlencode= 'https://javfree.me/?s='+urllib.parse.quote_plus(avname)+"'"
#response2 = requests.get(f"https://javfree.me/?s="%E6%98%8E%E9%87%8C"")
response2 = requests.get(urlencode)
soup2 = BeautifulSoup(response2.text, "lxml")
results2 = soup2.find_all("h2",{"class": "entry-title"})
for title in results2:
    link = title.a.get('href')
    text = title.a.text
    print("現在處理:" +text)
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "lxml")
    results = soup.find_all("img")
    image_links = [result.get("src") for result in results]  # 取得圖片來源連結
    subDir_path = '/'+avname+'/'+text+'/'
    for index, link in enumerate(image_links):
        if not os.path.exists(subDir_path):
            os.mkdir(subDir_path)  # 建立資料夾
        try:
            print(link)
            img = requests.get(link)  # 下載圖片
            with open(subDir_path+"\\" +str(index+1) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
                file.write(img.content)  # 寫入圖片的二進位碼
        except:
            continue;
    print("下載完成")

