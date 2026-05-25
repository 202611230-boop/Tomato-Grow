import streamlit as st
import pandas as pd
import joblib

# 모델 로드
rf_model = joblib.load("tomato_model.pkl")

# 제목
st.title("착과율 예측 프로그램")

# 입력
temp = st.number_input("내부온도 입력", value=25.0)
humidity = st.number_input("내부습도 입력", value=60.0)
soil_temp = st.number_input("지온 입력", value=20.0)

# 버튼
if st.button("예측하기"):

    # 입력 데이터를 DataFrame으로 변환
    input_data = pd.DataFrame(
        [[temp, humidity, soil_temp]],
        columns=['내부온도', '내부습도', '지온']
    )

    # 예측
    predicted = rf_model.predict(input_data)

    # 결과 출력
    st.write(f"### 예측 착과율 : {predicted[0]:.1f}%")
