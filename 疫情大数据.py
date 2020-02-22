
import requests
import json
 
def Down_data():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36'
    }
    r = requests.get(url, headers)
    res = json.loads(r.text)
    data_res = json.loads(res['data'])
    return data_res
 
def Parse_data1():
    data = Down_data()
    list = ['截至时间：'+str(data['lastUpdateTime'])+'\n'
          '全国确诊人数：'+str(data['chinaTotal']['confirm'])+'\n'
          '今日新增确诊：'+str(data['chinaAdd']['confirm'])+'\n'
          '全国疑似：'+str(data['chinaTotal']['suspect'])+'\n'
          '今日新增疑似：'+str(data['chinaAdd']['suspect'])+'\n'
          '全国治愈：'+str(data['chinaTotal']['heal'])+'\n'
          '今日新增治愈：'+str(data['chinaAdd']['heal'])+'\n'
          '全国死亡：'+str(data['chinaTotal']['dead'])+'\n'
          '今日新增死亡：'+str(data['chinaAdd']['dead'])+'\n']
    result = ''.join(list)
    with open('疫情查询.txt', 'a+', encoding="utf-8") as f:
        f.write(result + '\n')
 
def Parse_data2():
    data = Down_data()['areaTree'][0]['children']
    path = str(input('请输入你要查询的省份：'))
    for i in data:
        if path in i['name']:
            for item in i['children']:
                list_city = [
                    '地区: '+str(item['name']) + '\n'
                    ' 确诊人数：' + str(item['total']['confirm']) ,
                    ' 新增确诊：' + str(item['today']['confirm']) ,
                    ' 治愈：' + str(item['total']['heal']) ,
                    ' 新增治愈：' + str(item['today']['heal']) ,
                    ' 死亡：' + str(item['total']['dead']) ,
                    ' 新增死亡：' + str(item['today']['dead']) + '\n'
                            ]
                res_city = ''.join(list_city)
                with open('疫情查询.txt', 'a+', encoding="utf-8") as f:
                    f.write(res_city)
 
Down_data()
Parse_data1()
Parse_data2()
