import streamlit as st
import pickle
model=pickle.load(open('HI_model.pkl','rb'))

st.markdown("<h2 style='font-size:22px;'>Health Insurance Predictor</h2>", unsafe_allow_html=True)


age = st.number_input('Age:',min_value=18,max_value=100,value=18,step=1)

gender=st.selectbox('Gender',['Select Gender','female','male',])

bmi=st.text_input( "BMI", key="bmi_text")
def update_bmi():
    st.session_state.bmi_text = str(st.session_state.bmi_slider)
if "bmi_text" not in st.session_state:
    st.session_state.bmi_text = ""
st.slider("Select BMI", min_value=10.0,max_value=50.0,value=None,step=0.1,key="bmi_slider",on_change=update_bmi)

children = st.number_input('No. of Children:',min_value=0,max_value=10,value=0,step=1)

def update_smoker():
    st.session_state.smoker_text = st.session_state.smoker_radio
if "smoker_text" not in st.session_state:
    st.session_state.smoker_text = "yes"
smoker=st.text_input("Smoker",key="smoker_text")
st.radio('',["yes", "no"],key="smoker_radio",on_change=update_smoker)

if st.button('Submit'):
    age=int(age)
    bmi=float(bmi)
    children=int(children)
    gender_enc=1 if gender=='female' else 0
    smoker_enc=1 if smoker=='yes' else 0
    q=[[age,gender_enc,bmi,children,smoker_enc]]
    yp=round(model.predict(q)[0],2)
    st.markdown(
    f"""
    <h1 style="font-size: 50px; font-weight: 900; color: white;">
        Your Premium: ₹{yp:,.2f}
    </h1>
    """,
    unsafe_allow_html=True
)
    
   
    


