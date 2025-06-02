import os
import json

WAREHOUSE_DIR = r'D:/ProgrammingProjects/Chen-Dasheng.github.io/warehouse'

def get_all_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def build_warehouse_list(directory):
    file_list = []
    files = get_all_files(directory)
    for filename in files:
        name, ext = os.path.splitext(filename)
        file_info = {
            "name": name,
            "path": f"/warehouse/{filename}",
            "type": ext.lstrip('.').lower()
        }
        file_list.append(file_info)
    return {"filelist": file_list}

if __name__ == "__main__":
    warehouse_list = build_warehouse_list(WAREHOUSE_DIR)
    with open("warehouselist.json", "w", encoding="utf-8") as f:
        json.dump(warehouse_list, f, ensure_ascii=False, indent=2)
    print("仓库文件列表已生成，共{}个文件。".format(len(warehouse_list["filelist"])))