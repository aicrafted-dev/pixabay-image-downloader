# pixabay-image-downloader
基于 Pixabay 官方 API 的 Python 图片采集工具，支持关键词搜索、批量下载和本地化管理。Demonstrates RESTful API integration, JSON data parsing, and file I/O operations.  #Python #API #ImageDownloader

🌙 Pixabay 月亮图片采集工具
一个基于 Python 的图片采集工具，通过 Pixabay 官方 API 批量搜索并下载月亮主题的高质量图片。

✨ 功能特点
🔍 通过关键词搜索 Pixabay 图片库

📥 批量下载高清图片到本地

📁 自动创建文件夹管理图片

⚡ 代码简洁易懂，适合初学者学习

🛠️ 技术栈
Python 3.6+

Requests 库（HTTP 请求）

JSON 数据处理

文件 I/O 操作

📦 安装与使用
1. 克隆项目
git clone https://github.com/你的用户名/pixabay-image-downloader.git
cd pixabay-image-downloader
2. 安装依赖
pip install requests
3. 获取 API 密钥
访问 Pixabay API 文档，注册账号后即可获取你的专属 API 密钥。
4. 配置并运行
在 pixabay_moon.py 中替换你的 API 密钥：
API_KEY = "你的API密钥"  # 替换为实际密钥
运行脚本：
python pixabay_moon.py
5. 查看结果
下载的图片会自动保存在项目目录下的 moon_photos/ 文件夹中。

📁 项目结构
text
pixabay-image-downloader/
├── pixabay_moon.py      # 主程序
├── moon_photos/         # 图片保存目录（自动生成）
└── README.md            # 项目说明
🚀 进阶优化方向
□ 支持命令行参数（自定义关键词、下载数量）
□ 多线程并发下载，提升速度
□ 将图片信息（标题、作者、点赞数）保存为 CSV 文件
□ 添加图形用户界面（GUI）
⚠️注意事项
请遵守 Pixabay API 的使用条款，控制请求频率

免费 API 有每日请求次数限制，请合理使用

本工具仅供学习交流使用

📄 开源协议
本项目采用 MIT 协议，欢迎自由使用和修改。

🙏 致谢
感谢 Pixabay 提供的免费图片 API 服务。

