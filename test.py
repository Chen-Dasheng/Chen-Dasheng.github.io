import http.client
import json

conn = http.client.HTTPSConnection("alist.snaplittlebear.top")  # 修复域名
payload = json.dumps({
    "username": "admin",
    "password": "Snap@Littlebear0909"
})
headers = {
    'Content-Type': 'application/json'
}
conn.request("POST", "/api/auth/login", payload, headers)
res = conn.getresponse()
data = res.read()
token = json.loads(data).get('data', {}).get('token')  # 新增token解析

conn = http.client.HTTPSConnection("alist.snaplittlebear.top")
payload = json.dumps({
    "path": "/TeraBox/warehouse",  # 修正路径
    "password": "Snap@Littlebear0909",
    "page": 1,
    "per_page": 0,
    "refresh": False
})
headers = {
    'Authorization': f'{token}',  # 修复token使用方式
    'Content-Type': 'application/json'
}
conn.request("POST", "/api/fs/list", payload, headers)  # 修正API路径
res = conn.getresponse()
data = res.read()
result = json.loads(data)

file_list = []
for item in result.get('data', {}).get('files', []):
    if item.get('type') == 'file':
        file_list.append({
            "name": item.get('name'),
            "path": f"/warehouse/{item['name']}",
            "type": item.get('name').split('.')[-1].lower()
        })

if __name__ == "__main__":
    with open("test.json", "w", encoding="utf-8") as f:
        json.dump({"filelist": file_list}, f, ensure_ascii=False, indent=2)
    print(f"成功获取 {len(file_list)} 个文件信息，已保存至test.json")
