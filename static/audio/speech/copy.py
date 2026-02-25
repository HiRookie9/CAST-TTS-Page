import os
import json
import shutil

# 定义源文件夹和目标文件夹的对应关系
folders = [
    ('/mnt/petrelfs/zhengzihao/workspace/mos/experiments/cast_experment/audio/speech/cast', "/mnt/petrelfs/zhengzihao/workspace/demo_page/CAST-TTS-Page/static/audio/speech/cast"),
    ('/mnt/petrelfs/zhengzihao/workspace/mos/experiments/cast_experment/audio/speech/f5tts', "/mnt/petrelfs/zhengzihao/workspace/demo_page/CAST-TTS-Page/static/audio/speech/f5tts"),
    ('/mnt/petrelfs/zhengzihao/workspace/mos/experiments/cast_experment/audio/speech/maskgct', "/mnt/petrelfs/zhengzihao/workspace/demo_page/CAST-TTS-Page/static/audio/speech/maskgct"),
    ('/mnt/petrelfs/zhengzihao/workspace/mos/experiments/cast_experment/audio/speech/prompt', "/mnt/petrelfs/zhengzihao/workspace/demo_page/CAST-TTS-Page/static/audio/speech/prompt"),
    ('/mnt/petrelfs/zhengzihao/workspace/mos/experiments/cast_experment/audio/speech/zipvoice', "/mnt/petrelfs/zhengzihao/workspace/demo_page/CAST-TTS-Page/static/audio/speech/zipvoice"),
]
txt_file = "/mnt/petrelfs/zhengzihao/workspace/demo_page/CAST-TTS-Page/static/audio/speech/speech.txt"
with open(txt_file, 'r', encoding='utf-8') as f:
    for line in f:
        id_ = line.strip()
        for ext in ['.wav', '.flac']:
            filename = f"{id_}{ext}"
            for src_folder, dst_folder in folders:
                src_path = os.path.join(src_folder, filename)
                dst_path = os.path.join(dst_folder, filename)
                # 文件存在再复制，避免报错
                if os.path.exists(src_path):
                    os.makedirs(dst_folder, exist_ok=True)
                    shutil.copy2(src_path, dst_path)
                    print(f"Copied {src_path} -> {dst_path}")