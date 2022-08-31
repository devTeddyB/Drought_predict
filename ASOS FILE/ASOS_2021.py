import pandas as pd
import sqlite3

conn = sqlite3.connect('weather1.db')
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS ASOS_2021;")

cur.execute("""CREATE TABLE ASOS_2021 (
                tm DATE,
                stnNm VARCHAR(32),
                avgTa REAL,
                avgPv REAL,
                avgRhm INTEGER,
                sumGsr REAL,
                avgWs REAL,
                sumRn REAL
                );
            """)


conn.commit()

query = ("INSERT INTO ASOS_2021 (tm, stnNm, avgTa, avgPv, avgRhm, sumGsr, avgWs, sumRn) VALUES (?, ?, ?, ?, ?, ?, ?, ?)")


stnIds = [90, 100, 101, 105, 108, 112, 114, 127, 129, 130, 131, 133, 138, 140, 143, 146, 152, 156, 159, 162, 165, 168, 170, 184, 188, 189, 192, 201, 202, 203, 211, 212, 221, 226, 232, 235, 236, 238, 243, 244, 245, 247, 248, 260, 261, 262, 272, 273, 277, 279, 281, 284, 285, 288, 289, 294, 295]


stnNm = {90:'속초', 100:'대관령', 101:'춘천', 105:'강릉', 108:'서울', 112:'인천', 114:'원주', 127:'충주',
        129:'서산', 130:'울진', 131:'청주', 133:'대전', 138:'포항', 140:'군산', 143:'대구', 146:'전주',
        152:'울산', 156:'광주', 159:'부산', 162:'통영', 165:'목포', 168:'여수', 170:'완도', 184:'제주',
        188:'성산', 189:'서귀포', 192:'진주', 201:'강화', 202:'양평', 203:'이천', 211:'인제', 212:'홍천',
        221:'제천', 226:'보은', 232:'천안', 235:'보령', 236:'부여', 238:'금산', 243:'부안', 244:'임실',
        245:'정읍', 247:'남원', 248:'장수', 260:'장흥', 261:'해남', 262:'고흥', 272:'영주', 273:'문경',
        277:'영덕', 279:'구미', 281:'영천', 284:'거창', 285:'합천', 288:'밀양', 289:'산청', 294:'거제', 295:'남해'}

date_data = {'2021-01':'2021-01-31', '2021-02':'2021-02-28', '2021-03':'2021-03-31', '2021-04':'2021-04-30', '2021-05':'2021-05-31', '2021-06':'2021-06-30',
            '2021-07':'2021-07-31', '2021-08':'2021-08-31', '2021-09':'2021-09-30', '2021-10':'2021-10-31', '2021-11':'2021-11-30', '2021-12':'2021-12-31'}

# 202~130 까지 수정

df = pd.DataFrame()
for j in stnIds:
    df_load = pd.read_csv('C:/Users/eorhk/Desktop/Section3/Project/data/월자료/2021/SURFACE_ASOS_' + f'{j}' + '_MNH_2021_2021_2022.csv', encoding='cp949', sep=',')
    # print(df_load)
    df_loads = df.append(df_load)
    df_recent = df_loads.replace({'지점':stnNm})
    df_last = df_recent.replace({'일시':date_data})
    # print(df_re)
    for idx, row in df_last.iterrows():
        cur.execute(query, (row['일시'], row['지점'], row['평균기온(°C)'], row['평균수증기압(hPa)'], row['평균상대습도(%)'], row['합계 일사량(MJ/m2)'], row['평균풍속(m/s)'], row['월합강수량(00~24h만)(mm)']))
        conn.commit()
        print(row['일시'], row['지점'], row['평균기온(°C)'], row['평균수증기압(hPa)'], row['평균상대습도(%)'], row['합계 일사량(MJ/m2)'], row['평균풍속(m/s)'], row['월합강수량(00~24h만)(mm)'])

conn.close()