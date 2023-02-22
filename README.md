# PROJECT3-dought-predict

## 가뭄을 예측하는 API서비스 개발

### 1. 데이터셋
 - OpenAPI에서 제공되는 종관기상관측자료
 - 기상자료개방포털에서 제공되는 표준가뭄지수
 - 위 두 데이터를 합쳐주고 DB에 저장하여 진행하였음.
 - 종관기상관측자료 수가 약 60만개가 존재하고 일자료이기때문에 누적강수량 정보가 없어, 최종적으로는 기상자료개방포털에서 제공되는 월별자료 최근 3년치를 다운받아 표준가뭄지수 데이터와 합쳐서 사용하였음.
 - 프로젝트가 끝난 뒤 찾아보니 수문기상가뭄정보시스템 포털에 개월수별 누적강수량과 그에따른 SPI지수 데이터가 있었음.(나중에 다시 하게 된다면 이 포털에서 스크래핑을 할 수 있을 듯.)
 
### 2. 모델링
 - 위 데이터에서 월 평균기온과 월 누적강수량을 사용하여 SPI1을 예측하는 모델을 만듦.
 - 증발산량, 풍속 등도 주요한 요소이긴하나, 유저들이 쉽게 파악할 수 없는 정보이기 떄문에 사용하지 않고 평년 자료를 바탕으로 한 예상 평균기온과 예상 누적강수량은 비교적 찾아보기 쉽기 때문에 이 두가지 특성을 가지고 모델링을 진행하게 됨.
 - 랜덤포레스트 모델과 오디널인코딩, 파이프라인, 랜더마이즈서치 CV를 이용하여 최적의 하이퍼파라미터를 구하고 튜닝한 모델을 피클화 하였음.

### 3. 대시보드
 - 도커와 연결한 메타베이스 툴을 이용하여 db와 연결해 SQL쿼리로 시각화 자료를 만들어주고 대시보드를 구성하였음.
 - 연월별 평균기온과 평균증발산량, 연월별 평균SPI1와 평균월누적강수량을 구성하였으며, 이는 강수량과 SPI지수의 관계성을 보기 쉽게 해줌.
 
### 4. 웹서비스 구현(flask, 배포는 진행하지 않음)
 - flask를 통해 웹을 구현하였으며, blueprint를 사용하지 않고 jinja로 구성해, 모델과 대시보드를 연동해주었음.
