import os
import json

WAREHOUSE_DIR = r'D:/ProgrammingProjects/Chen-Dasheng.github.io/upload'

def get_all_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def build_warehouse_list(directory):
    file_list = []
    files = get_all_files(directory)
    for filename in files:
        name, ext = os.path.splitext(filename)
        file_info = {
            "name": name,
            "path": f"TeraBox/warehouse/{filename}",
            "type": ext.lstrip('.').lower()
        }
        file_list.append(file_info)
    return {"filelist": file_list}

# ...existing code...

if __name__ == "__main__":
    mode = input("请选择操作模式：1-添加项目 2-覆写文件（输入1或2）：").strip()
    warehouse_list = build_warehouse_list(WAREHOUSE_DIR)

    if mode == "1" and os.path.exists("warehouselist.json"):
        with open("warehouselist.json", "r", encoding="utf-8") as f:
            existing = json.load(f)
        # 合并文件列表，避免重复
        existing_names = {item["name"] for item in existing.get("filelist", [])}
        new_files = [item for item in warehouse_list["filelist"] if item["name"] not in existing_names]
        existing["filelist"].extend(new_files)
        with open("warehouselist.json", "w", encoding="utf-8") as f:
            json.dump(existing, f, ensure_ascii=False, indent=2)
        print("已添加{}个新项目，当前总文件数：{}。".format(len(new_files), len(existing["filelist"])))
    else:
        with open("warehouselist.json", "w", encoding="utf-8") as f:
            json.dump(warehouse_list, f, ensure_ascii=False, indent=2)
        print("仓库文件列表已生成，共{}个文件。".format(len(warehouse_list["filelist"])))
# ...existing code...