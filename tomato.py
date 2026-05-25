temp = float(input("내부온도 입력 : "))
humidity = float(input("내부습도 입력 : "))
soil_temp = float(input("지온 입력 : "))


# DataFrame으로 변환(2차원 배열 형태로 입력)
input_data = pd.DataFrame([[temp, humidity, soil_temp]], columns=['내부온도', '내부습도', '지온'])


# 예측
predicted = rf_model.predict(input_data)

print(f"예측 착과율 : {predicted[0]:.1f}%")