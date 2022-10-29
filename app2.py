import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek

filename = "model2.sv"
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model

Sex_d = {0:"Female", 1:"Male"}
ChestPainType_d = {0:"ASY", 1:"ATA", 2:"NAP", 3:"TA" }
RestingECG_d = {0:"LVH", 1:"Normal", 2:"ST"}
ExerciseAngina_d = {0:"No", 1:"Yes"}
ST_Slope_d = {0:"Down", 1:"Flat", 2:"Up"}

# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem

def main():

	st.set_page_config(page_title="Sprawdź zdrowie twojego serca!")
	overview = st.container()
	left, right = st.columns(2)
	prediction = st.container()

	st.image("https://sennik.club/wp-content/uploads/2018/02/sennik-Serce.jpg")

	with overview:
		st.title("Sprawdź zdrowie twojego serca!")

	with left:
		Sex_radio = st.radio( "Sex", list(Sex_d.keys()), format_func=lambda x : Sex_d[x] )
		ChestPainType_radio = st.radio( "Chest Pain Type", list(ChestPainType_d.keys()), index=2, format_func= lambda x: ChestPainType_d[x] )
		RestingECG_radio = st.radio( "Resting ECG", list(RestingECG_d.keys()), format_func=lambda x : RestingECG_d[x] )
		ExerciseAngina_radio = st.radio( "Exercise Angina", list(ExerciseAngina_d.keys()), format_func=lambda x : ExerciseAngina_d[x] )
		ST_Slope_radio = st.radio( "ST Slope", list(ST_Slope_d.keys()), format_func=lambda x : ST_Slope_d[x] )

	with right:
		Age_slider = st.slider("Age", value=1, min_value=28, max_value=77)
		RestingBP_slider = st.slider("Resting BP", min_value=0, max_value=200)
		Cholesterol_slider = st.slider("Cholesterol", min_value=0, max_value=603)
		FastingBS_slider = st.slider("Fasting BS", min_value=0, max_value=1)
		MaxHR_slider = st.slider("Max HR", min_value=60, max_value=202)
		#Oldpeak_slider = st.slider("Oldpeak", min_value=-2, max_value=7)


	data = [[Sex_radio, ChestPainType_radio,  RestingECG_radio, ExerciseAngina_radio, ST_Slope_radio, Age_slider, RestingBP_slider,Cholesterol_slider, FastingBS_slider, MaxHR_slider]]
	survival = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.subheader("Czy masz chorobę serca?")
		st.subheader(("Tak" if survival[0] == 1 else "Nie"))
		st.write("Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100))

if __name__ == "__main__":
    main()
