import gradio as gr
import joblib
import pandas as pd 
PATH_MODEL = "random_forest_best_model.joblib"
model = joblib.load(PATH_MODEL)
with gr.Blocks() as demo:
    gr.Markdown(
    """
    # Obesity Level Prediction!
    """)
    with gr.Row():
        gender = gr.Dropdown(choices=["Male", "Female"], label="Gender")
        age = gr.Number(label="Age")
    with gr.Row():
        family_history = gr.Dropdown(choices=["Yes", "No"], label="Family History with Overweight")
        frequent_consumption = gr.Dropdown(choices=["Yes", "No"], label="Frequent Consumption of High Caloric Food")
    frequent_vegetables = gr.Slider(1, 3, step=1, label="Frequent Consumption of Vegetables (times per week)")
    num_meals = gr.Slider(1, 4, step=1, label="Number of Main Meals")
    with gr.Row():
        food_between_meals = gr.Dropdown(choices=["Always", "Frequently", "Sometimes", "no"], label="Consumption of Food between Meals")
        smoke = gr.Dropdown(choices=["Yes", "No"], label="Smoking")
    ch2o = gr.Slider(1, 3, label="Consumption of Water daily (Liters)")
    scc = gr.Dropdown(choices=["Yes", "No"], label="Calories Consumption Monitoring")
    physical_activity = gr.Slider(0, 3, step=1, label="Physical Activity Frequency (times per week)")
    time_using_tech = gr.Slider(0, 3, label="Time using Technology Devices")
    alcohol_consumption = gr.Dropdown(choices=["Always", "Frequently", "Sometimes", "no"], label="Alcohol Consumption")
    transportation = gr.Dropdown(choices=["Automobile", "Motorbike", "Bike", "Public Transportation", "Walking"], label="Transportation used")
    
    calc_btn = gr.Button("Calculate Obesity Level")
    output = gr.Textbox(label="Predicted Obesity Level")
    def predict_obesity(gender, age, family_history, frequent_consumption, frequent_vegetables, num_meals, food_between_meals, smoke, ch2o, scc, physical_activity, time_using_tech, alcohol_consumption, transportation):
        input_data = pd.DataFrame({
            "Gender": gender,
            "Age": age,
            "family_history_with_overweight": family_history,
            "FAVC": frequent_consumption,
            "FCVC": frequent_vegetables,
            "NCP": num_meals,
            "CAEC": food_between_meals,
            "SMOKE": smoke,
            "CH2O": ch2o,
            "SCC": scc,
            "FAF": physical_activity,
            "TUE": time_using_tech,
            "CALC": alcohol_consumption,
            "MTRANS": transportation
        }, index=[0])

        return model.predict(input_data)[0]

    calc_btn.click(fn=predict_obesity, inputs=[gender, age, family_history, frequent_consumption, frequent_vegetables, num_meals, food_between_meals, smoke, ch2o, scc, physical_activity, time_using_tech, alcohol_consumption, transportation], outputs=output)

demo.launch(share=True)