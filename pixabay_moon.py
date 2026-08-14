import json
import requests
import os 
API_KEY = "API_KEY"  # 请替换成你从Pixabay官网获取的真实密钥
SEARCH_QUERY = "moon"    # 要搜索的关键词“月亮”
DOWNLOAD_FOLDER = "moon_photos"  # 图片将保存到这个文件夹

url = f"https://pixabay.com/api/?key={API_KEY}&q={SEARCH_QUERY}&image_type=photo&per_page=20"

print(f"正在搜索关键词 '{SEARCH_QUERY}' 的图片...")
response = requests.get(url)

if response.status_code != 200:
    print(f"请求失败，状态码: {response.status_code}")
    exit()
data = response.json() 
image_hits = data.get('hits', [])

if not image_hits:
    print("没有找到相关图片。")
    exit()

print(f"成功找到 {len(image_hits)} 张图片，准备下载...")
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# 6. 下载并保存图片
for idx, hit in enumerate(image_hits):
    # 'largeImageURL' 是高质量图片的下载地址
    image_url = hit.get('largeImageURL')
    if not image_url:
        continue
 # 构造图片的文件名，例如: moon_photo_1.jpg
    file_name = f"{SEARCH_QUERY}_photo_{idx+1}.jpg"
    file_path = os.path.join(DOWNLOAD_FOLDER, file_name)

    # 发送请求下载图片内容 (二进制数据)
    print(f"  正在下载: {file_name}")
    img_response = requests.get(image_url)

    # 将图片内容写入文件
    with open(file_path, 'wb') as f:
        f.write(img_response.content)

print("所有图片下载完成！")


