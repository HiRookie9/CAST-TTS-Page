import os
import json
import shutil

# 定义源文件夹和目标文件夹的对应关系
folders = [
    ('/mnt/petrelfs/zhengzihao/workspace/accel_hydra/examples/f5tts_new/exp/f5_x1_ecapa_stage3_v1_copy/inference_400k_caption_new', "/mnt/petrelfs/zhengzihao/workspace/demo_page/CAST-TTS-Page/static/audio/text/cast"),
    ('/mnt/petrelfs/zhengzihao/workspace/CapSpeech/capspeech/output_fix', "/mnt/petrelfs/zhengzihao/workspace/demo_page/CAST-TTS-Page/static/audio/text/capspeech"),
    ('/mnt/petrelfs/zhengzihao/workspace/parler-tts/output_caps', "/mnt/petrelfs/zhengzihao/workspace/demo_page/CAST-TTS-Page/static/audio/text/parlertts")
]

jsonl_file = '/mnt/petrelfs/zhengzihao/workspace/demo_page/CAST-TTS-Page/static/audio/text/text.jsonl'  # 你的jsonl文件名

with open(jsonl_file, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            item = json.loads(line)
            wav_path = item['location']
            filename = os.path.basename(wav_path)
        except Exception:
            continue
        # 遍历每个文件夹对
        for src_folder, dst_folder in folders:
            src_path = os.path.join(src_folder, filename)
            dst_path = os.path.join(dst_folder, filename)
            # 文件存在再复制，避免报错
            if os.path.exists(src_path):
                os.makedirs(dst_folder, exist_ok=True)
                shutil.copy2(src_path, dst_path)
                print(f"Copied {src_path} -> {dst_path}")