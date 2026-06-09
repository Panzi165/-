"""
電流急急棒遊戲 - Flask 版本
使用 Flask 作為後端伺服器
"""

from Flask import Flask, render_template, jsonify, request
import json
import os
import logging

app = Flask(__name__)

# 配置
app.config['STATIC_FOLDER'] = os.path.join(os.path.dirname(__file__), 'static')

# 設置日誌
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 遊戲數據
game_scores = []

@app.route('/')
def index():
    """主頁 - 返回遊戲頁面"""
    return render_template('index.html')

@app.route('/api/get-scores', methods=['GET'])
def get_scores():
    """獲取遊戲成績排行榜"""
    try:
        return jsonify({
            'scores': sorted(game_scores, reverse=True)[:10],
            'total_games': len(game_scores)
        })
    except Exception as e:
        logger.error(f'獲取成績出錯: {e}')
        return jsonify({'error': '獲取成績失敗'}), 500

@app.route('/api/save-score', methods=['POST'])
def save_score():
    """保存遊戲成績"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': '無效的請求數據'}), 400
        
        score = data.get('score', 0)
        game_scores.append(score)
        
        logger.info(f'新成績已保存: {score}')
        
        return jsonify({
            'success': True,
            'message': '成績已保存',
            'score': score
        })
    except Exception as e:
        logger.error(f'保存成績出錯: {e}')
        return jsonify({'error': '保存成績失敗'}), 500

@app.route('/api/check-music', methods=['GET'])
def check_music():
    """檢查音樂文件是否存在"""
    try:
        music_folder = os.path.join(app.config['STATIC_FOLDER'], 'music')
        music_data = {
            'background': [],
            'success': [],
            'scare': [],
            'all_available': False
        }
        
        if os.path.exists(music_folder):
            for file in os.listdir(music_folder):
                file_lower = file.lower()
                
                # 背景音樂
                if file_lower.startswith('background') and file_lower.endswith('.mp3'):
                    music_data['background'].append(file)
                # 成功音樂
                elif file_lower.startswith('success') and file_lower.endswith('.mp3'):
                    music_data['success'].append(file)
                # 驚嚇音樂
                elif file_lower.startswith('scare') and file_lower.endswith('.mp3'):
                    music_data['scare'].append(file)
            
            music_data['all_available'] = (
                len(music_data['background']) > 0 and
                len(music_data['success']) > 0 and
                len(music_data['scare']) > 0
            )
            
            logger.info(f'音樂文件檢查: 背景={len(music_data["background"])}, 成功={len(music_data["success"])}, 驚嚇={len(music_data["scare"])}')
        
        return jsonify(music_data)
    except Exception as e:
        logger.error(f'檢查音樂出錯: {e}')
        return jsonify({'error': '檢查音樂失敗'}), 500

@app.route('/api/health', methods=['GET'])
def health():
    """健康檢查"""
    return jsonify({'status': 'ok', 'message': '遊戲伺服器運行中'})

@app.errorhandler(404)
def not_found(error):
    """404 錯誤處理"""
    return jsonify({'error': '找不到該資源'}), 404

@app.errorhandler(500)
def server_error(error):
    """500 錯誤處理"""
    logger.error(f'伺服器內部錯誤: {error}')
    return jsonify({'error': '伺服器內部錯誤'}), 500

if __name__ == '__main__':
    print("=" * 60)
    print("🎮 電流急急棒遊戲 - Flask 伺服器")
    print("=" * 60)
    print(" 訪問地址: http://127.0.0.1:5000")
    print(" 音樂配置:")
    print("   位置: static/music/ 資料夾")
    print("   - 背景音樂: background.mp3")
    print("   - 成功音樂: success.mp3")
    print("   - 驚嚇音樂: scare.mp3")
    print("\n🖼️  圖案配置:")
    print("   位置: static/images/ 資料夾")
    print("   - 失敗圖案: fail.png (或 fail.jpg, fail.gif)")
    print("\n⚠️  提示:")
    print("   - 音樂格式必須是 MP3")
    print("   - 音樂不能同時撥放（系統自動管理）")
    print("   - 背景音樂會在遊戲開始時迴圈撥放")
    print("   - 驚嚇音樂在失敗時撥放")
    print("   - 成功音樂在過關時撥放")
    print("\n按 Ctrl+C 停止伺服器\n")
    print("=" * 60)
    
    # 以調試模式運行
    app.run(debug=True, host='127.0.0.1', port=5000)
