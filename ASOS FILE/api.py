from urllib.parse import urlencode
import requests
import json
from bs4 import BeautifulSoup
import os,json
import time
import xmltodict
import pandas as pd
import sqlite3

# conn = sqlite3.connect('weather.db')
# cur = conn.cursor()
# cur.execute("DROP TABLE IF EXISTS ASOS;")
# conn.commit()
# cur.execute("""CREATE TABLE ASOS ( 
# 				tm VARCHAR(32),
# 				stnNm VARCHAR(32),
#                                 avgTa VARCHAR(32),
#                                 maxTa VARCHAR(32),
#                                 sumRn VARCHAR(32),
#                                 avgWs VARCHAR(32),
#                                 avgRhm VARCHAR(32),
#                                 avgPv VARCHAR(32),
#                                 sumGsr VARCHAR(32)
#                                 );
# 	        """)
# conn.commit()

# query = ("INSERT INTO ASOS (tm, stnNm, avgTa, maxTa, sumRn, avgWs, avgRhm, avgPv, sumGsr) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)")



url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'

pageNo = '1'
max_page = 9
numOfRows = '100'
dataType = "JSON"
dataCd = "ASOS"
dateCd = "DAY"
startDt = '20200101'
endDt = '20211231'

stnIds = [90, 100, 101, 105, 108, 112, 114, 127, 129, 130, 131, 133, 138, 140, 143, 146, 152, 156, 159, 162, 165, 168, 170, 184, 188, 189, 192, 201, 202, 203, 211, 212, 221, 226, 232, 235, 236, 238, 243, 244, 245, 247, 248, 260, 261, 262, 272, 273, 277, 279, 281, 284, 285, 288, 289, 294, 295]


key = 'F4oVuqC4eXrB7lFM3x0BgN+t2WmjBwhDI1Mtj0agmifYaipbsFbzGCZOIGmEvJN+BbeMsyKD1zlvmtapNPTsCQ=='

df = pd.DataFrame()
for i in range(len(stnIds)):
    for j in range(1, max_page):
        params = {
                'serviceKey' : key,
                'pageNo':j,
                'numOfRows':numOfRows,
                'dataType':dataType,
                'dataCd':dataCd,
                'dateCd':dateCd,
                'startDt':startDt,
                'endDt':endDt,
                'stnIds':stnIds[i]}
        response = requests.get(url, params = urlencode(params))
        data = json.loads(response.text)
        parsed_data = data['response']['body']['items']['item']
        df_list = pd.DataFrame(parsed_data)
        for idx, row in df_list.iterrows():
                # cur.execute(query, (row['tm'], row['stnNm'], row['avgTa'], row['maxTa'], row['sumRn'], row['avgWs'], row['avgRhm'], row['avgPv'], row['sumGsr']))
                # conn.commit()

                print(row['tm'], row['stnNm'], row['avgTa'], row['maxTa'], row['sumRn'], row['avgWs'], row['avgRhm'], row['avgPv'], row['sumGsr'])
        # try:
        # cur.execute(query, (row['tm'], row['stnNm'], row['avgTa'], row['maxTa'], row['sumRn'], row['avgWs'], row['avgRhm'], row['avgPv'], row['sumGsr']))
        # except Exception as e:
        #         print(e)
# conn.close()