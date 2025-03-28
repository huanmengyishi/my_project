import requests

url = "http://cl2.hno3.cn/get_classrooms"
url2 = "http://cl2.hno3.cn/get_available_buildings"
params = {
    "campus_code": "0101",
    "building_code": "010102",
    "start_time": 1,
    "end_time": 9
}
params2 = {
    "campus_code": "0101",
    "start_time": 1,
    "end_time": 9
}
headers = {
    "accept": "application/json"
}

try:
    response = requests.get(url, params=params)
    response2 = requests.get(url2, params=params2)
    response.raise_for_status()  # 检查 HTTP 错误
    response2.raise_for_status()
    # 解析 JSON 响应
    response_data = response.json()
    response_data2 = response2.json()
    data_list = response_data["data"]
    data_list2 = response_data2["data"]
    print("所有数据:", data_list)
    print("所有数据:", data_list2)
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
except ValueError as e:
    print(f"JSON 解析失败: {e}")

