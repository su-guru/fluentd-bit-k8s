import time
import json
import random
import logging
from datetime import datetime

# ログの設定
logging.basicConfig(
    filename='/logs/app.log',
    level=logging.INFO,
    format='%(message)s'
)

# ログメッセージの生成
def generate_log():
    log_types = ['INFO', 'WARNING', 'ERROR']
    messages = [
        'User logged in',
        'Failed login attempt',
        'Data processing completed',
        'System health check',
        'Database connection lost'
    ]
    
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'type': random.choice(log_types),
        'message': random.choice(messages),
        'user_id': random.randint(1000, 9999)
    }
    
    return json.dumps(log_entry)

# メイン処理
if __name__ == "__main__":
    while True:
        log_message = generate_log()
        logging.info(log_message)
        time.sleep(random.uniform(0.1, 2))  # 0.1秒から2秒の間隔でログを生成