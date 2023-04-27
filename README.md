# Drought_predict

## 가뭄을 예측하는 API서비스 개발

### 설명
 - '기상자료개방포털'에서 제공되는 '종관기상관측자료'와 '표준강수지수' 데이터를 학습에 사용하여 알고자 하는 지역의 월별 예상 누적강수량과 예상 평균기온을 입력하면 예상 가뭄지수를 보여주는 딥러닝 모델을 개발하고자 함.
 - 위 개발을 통해 국내 농가에게 가뭄에 대비하고 피해를 줄일 수 있도록 하기 위함.
 - 종관기상관측자료 수가 약 60만개가 존재하고 일자료이기때문에 누적강수량 정보가 없어, 최종적으로는 기상자료개방포털에서 제공되는 월별자료 최근 3년치를 다운받아 표준강수지수 데이터와 합쳐서 사용하였음.
 

### 과정
 + **데이터수집**
   + '기상자료개방포털'에서 제공되는 '종관기상관측자료'와 '표준강수지수' 데이터 활용
   + 스크래핑을 이용하여 데이터 수집
   + sql을 활용하여 DB에 적재한 뒤 불러와서 사용하였음.

 + **모델링**
   + 위 데이터에서 월 평균기온과 월 누적강수량을 사용하여 SPI1을 예측하는 모델을 만듦.
   + 증발산량, 풍속 등도 주요한 요소이긴하나, 유저들이 쉽게 파악할 수 없는 정보이기 떄문에 사용하지 않고 평년 자료를 바탕으로 한 예상 평균기온과 예상 누적강수량은 비교적 찾아보기 쉽기 때문에 이 두가지 특성을 가지고 모델링을 진행하게 됨.
   + 랜덤포레스트 모델과 오디널인코딩, 파이프라인, 랜더마이즈서치 CV를 이용하여 최적의 하이퍼파라미터를 구하고 튜닝한 모델을 피클화 하였음.

 + **대시보드**
   + 도커와 연결한 메타베이스 툴을 이용하여 db와 연결해 SQL쿼리로 시각화 자료를 만들어주고 대시보드를 구성하였음.
   + 연월별 평균기온과 평균증발산량, 연월별 평균SPI1와 평균월누적강수량을 구성하였으며, 이는 강수량과 SPI지수의 관계성을 보기 쉽게 해줌.
 
 + **웹서비스 구현(flask, 배포는 진행하지 않음)**
   + flask를 통해 웹을 구현하였으며, blueprint를 사용하지 않고 jinja로 구성해, 모델과 대시보드를 연동해주었음.
   
### 회고
 - 프로젝트가 끝난 뒤 찾아보니 수문기상가뭄정보시스템 포털에 개월수별 누적강수량과 그에따른 SPI지수 데이터가 있었음.
 - 도메인에 대한 정보가 있었지만 충분하지 않았다는 점 그리고 내가 원하는 데이터가 있을거란 보장이 없다는 것을 알게되었고, 도메인 정보와 데이터를 더 찾아보았다면하는 아쉬움이 나는다.
 - 위의 내용을 토대로 새롭게 데이터 크롤링을 통해서 보다 정확한 데이터를 수집할 수 있을 것 같다.

---

### 사용한 프로그래밍 언어 및 라이브러리
<img src="https://img.shields.io/badge/Python-yellow?style=flat"/> <img src="https://img.shields.io/badge/pandas-red?style=flat"/> <img src="https://img.shields.io/badge/sqlite3-blue?style=flat"/> <img src="https://img.shields.io/badge/sklearn-lightgrey?style=flat"/> <img src="https://img.shields.io/badge/pickle-green?style=flat"/> <img src="https://img.shields.io/badge/flask-orange?style=flat"/> 



### 데이터 정보 및 참고 사이트
 - **데이터**
   - 종관기상관측(ASOS) : https://data.kma.go.kr/data/grnd/selectAsosRltmList.do?pgmNo=36
   - 표준강수지수(SPI) : https://data.kma.go.kr/data/gaw/selectSpiRltmList.do?pgmNo=734
 - **참고 사이트**
   - 국가가뭄정보포털 : https://www.drought.go.kr/menu/m30/m31.do
   - 수문기상 가뭄정보 시스템 : https://hydro.kma.go.kr/index.do
