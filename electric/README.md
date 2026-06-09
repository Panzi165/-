# 🎮 電流急急棒遊戲 - Python Flask 版本

一款使用 **Python Flask** 後端和 **HTML5 Canvas** 前端的互動式遊戲。

## 📁 文件結構

```
flask_game/
├── app.py                  # Flask 主程式
├── requirements.txt        # Python 依賴包
├── templates/
│   └── index.html         # 遊戲主頁面
└── static/
    ├── music/             # 放置音樂文件夾（MP3）
    └── images/            # 放置失敗圖案文件夾
```

## 🎵 音樂配置

### 音樂文件命名與放置

1. **位置**：`static/music/` 資料夾
2. **格式**：MP3 格式
3. **建議命名**：`success.mp3`

### 支援的命名方式（任選其一）

- `success.mp3`
- `win.mp3`
- `victory.mp3`
- `celebrate.mp3`
- `applause.mp3`

系統會自動偵測並載入第一個找到的 MP3 文件。

### 📋 如何添加音樂

1. 準備你的勝利音樂 MP3 文件
2. 複製到 `static/music/` 資料夾
3. 確保檔名是 `.mp3` 格式
4. 重新啟動 Flask 伺服器
5. 過關時會自動撥放！

## 🖼️ 失敗圖案配置

### 圖案文件放置

1. **位置**：`static/images/` 資料夾
2. **支援格式**：PNG、JPG、GIF
3. **建議命名**：`fail.png` 或 `fail.jpg`

### 📋 如何添加失敗圖案

1. 準備失敗圖案圖片
2. 複製到 `static/images/` 資料夾
3. 支援的檔名：
   - `fail.png`
   - `fail.jpg`
   - `fail.gif`
4. 遊戲失敗時會自動顯示

## 🚀 啟動遊戲

### 第一步：安裝依賴

```bash
cd "c:\Users\User\Desktop\網站程式設計\flask_game"
pip install -r requirements.txt
```

### 第二步：運行伺服器

```bash
python app.py
```

### 第三步：訪問遊戲

打開瀏覽器，訪問：
```
http://127.0.0.1:5000
```

## 🎮 遊戲說明

- **開始**：點擊畫面開始遊戲
- **操作**：移動滑鼠沿著軌道（金色）移動
- **目標**：從綠色的 START 走到黃色的 END
- **危險**：碰到棕色牆壁會失敗
- **勝利**：到達終點會播放音樂！

## 🔌 API 端點

- `GET /` - 主遊戲頁面
- `GET /api/health` - 伺服器健康檢查
- `GET /api/check-music` - 檢查音樂文件
- `POST /api/save-score` - 保存遊戲成績
- `GET /api/get-scores` - 獲取成績排行榜

## 🛠️ 技術棧

- **後端**：Python Flask
- **前端**：HTML5 Canvas + JavaScript
- **音樂**：Web Audio API
- **成績管理**：JSON 數據存儲

## 💡 提示

- 伺服器首次啟動會打印設置提示
- 確保音樂和圖片檔案格式正確
- 按 `Ctrl+C` 停止伺服器
- 所有資料實時保存在伺服器記憶體中

## 📝 遊戲成績

遊戲成績會在伺服器運行期間保存，可通過 API 查詢：
```bash
curl http://127.0.0.1:5000/api/get-scores
```

---

祝你遊戲愉快！🎉
