import os
import random
import json

MUSIC_DIR = r'D:/ProgrammingProjects/Chen-Dasheng.github.io/musicplayer/music'

def random_hex_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def get_music_files(directory):
    exts = ('.mp3', '.flac', '.wav', '.m4a', '.ogg')
    return [f for f in os.listdir(directory) if f.lower().endswith(exts)]

def find_file_with_same_name(directory, basename, exts):
    for ext in exts:
        candidate = os.path.join(directory, basename + ext)
        if os.path.isfile(candidate):
            return candidate
    return None

def build_music_list(directory):
    music_list = []
    files = get_music_files(directory)
    for filename in files:
        name, ext = os.path.splitext(filename)
        # 作者-歌名
        if '-' in name:
            artist, song_name = name.split('-', 1)
            artist = artist.strip()
            song_name = song_name.strip()
        else:
            artist = "未知"
            song_name = name
        # url（修改为指定格式）
        url = f"/musicplayer/music/{filename}"
        # 封面（查找同名jpg/png文件）
        cover = find_file_with_same_name(directory, name, ['.jpg', '.png', '.jpeg'])
        cover = cover.replace("\\", "/") if cover else ""
        # 歌词（查找同名lrc文件）
        lrc = find_file_with_same_name(directory, name, ['.lrc'])
        lrc = lrc.replace("\\", "/") if lrc else ""
        # theme
        theme = random_hex_color()
        music_list.append({
            "name": song_name,
            "artist": artist,
            "url": url,
            "cover": cover,
            "lrc": lrc,
            "theme": theme
        })
    return {"audio": music_list}

if __name__ == "__main__":
    music_list = build_music_list(MUSIC_DIR)
    # 输出为json文件
    with open("musiclist.json", "w", encoding="utf-8") as f:
        json.dump(music_list, f, ensure_ascii=False, indent=2)
    print("音乐列表已生成，共{}首。".format(len(music_list["audio"])))