import streamlit as st
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="Iris Classification Dashboard",
    page_icon="🌸",
    layout="wide"
)



# --------------------------------
# THEME
# --------------------------------

theme = st.sidebar.radio(
    "🎨 Select Theme",
    ["Dark", "Light"]
)


if theme == "Dark":

    bg_color = "#0b1120"
    card_bg = "#1e293b"
    text_color = "#f8fafc"
    sidebar_bg = "#111827"

    table_bg = "#111827"
    table_header = "#334155"
    table_text = "#ffffff"

else:

    bg_color = "#f5f7fa"
    card_bg = "#ffffff"
    text_color = "#111111"
    sidebar_bg = "#e5e7eb"

    table_bg = "#ffffff"
    table_header = "#dbeafe"
    table_text = "#111111"



# --------------------------------
# CSS
# --------------------------------

st.markdown(f"""

<style>


.stApp {{
background:{bg_color};
color:{text_color};
}}



section[data-testid="stSidebar"] {{
background:{sidebar_bg};
}}


section[data-testid="stSidebar"] * {{
color: {"white" if theme=="Dark" else "#111"} !important;
}}



.custom-card {{

background:{card_bg};
color:{text_color};

padding:25px;
border-radius:20px;

transition:0.3s;

text-align:center;

margin-bottom:15px;

}}



.custom-card:hover {{

transform:translateY(-8px);

box-shadow:
0px 10px 30px rgba(0,255,255,0.3);

}}




.stButton > button {{

width:100%;

background:
linear-gradient(90deg,#00c6ff,#0072ff);

color:white;

border:none;

border-radius:12px;

padding:12px;

font-size:18px;

font-weight:bold;

}}



.stButton > button:hover {{

transform:scale(1.05);

box-shadow:0px 0px 20px #00c6ff;

}}




/* STREAMLIT TABLE */

.stDataFrame {{

border-radius:15px;

overflow:hidden;

}}



.stDataFrame [role="grid"] {{

background:{table_bg} !important;

}}



.stDataFrame [role="columnheader"] {{

background:{table_header} !important;

color:{table_text} !important;

font-weight:bold;

}}



.stDataFrame [role="gridcell"] {{

background:{table_bg} !important;

color:{table_text} !important;

}}



.stDataFrame [role="row"]:hover [role="gridcell"] {{

background:#334155 !important;

color:white !important;

}}



h1,h2,h3 {{

text-align:center;

}}



</style>


""", unsafe_allow_html=True)




# --------------------------------
# TITLE
# --------------------------------

st.title("🌸 Iris Flower Classification Dashboard")


st.markdown(
"""
<h4 style="text-align:center">
Machine Learning Classification Project using KNN
</h4>
""",
unsafe_allow_html=True
)




# --------------------------------
# DATASET
# --------------------------------

iris = load_iris()


X = iris.data
y = iris.target


feature_names = iris.feature_names
target_names = iris.target_names



df = pd.DataFrame(
    X,
    columns=feature_names
)


df["Species"] = y




# --------------------------------
# TRAIN MODEL
# --------------------------------

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,
    test_size=0.2,
    random_state=42

)



model = KNeighborsClassifier(
    n_neighbors=3
)


model.fit(
    X_train,
    y_train
)



accuracy = accuracy_score(
    y_test,
    model.predict(X_test)
)




# --------------------------------
# CARDS
# --------------------------------

c1,c2,c3 = st.columns(3)



with c1:

    st.markdown(
    f"""
    <div class="custom-card">

    <h3>📊 Dataset Size</h3>

    <h1>{len(df)}</h1>

    </div>
    """,
    unsafe_allow_html=True
    )



with c2:

    st.markdown(
    """
    <div class="custom-card">

    <h3>🌸 Classes</h3>

    <h1>3</h1>

    </div>
    """,
    unsafe_allow_html=True
    )



with c3:

    st.markdown(
    f"""
    <div class="custom-card">

    <h3>🎯 Accuracy</h3>

    <h1>{accuracy*100:.2f}%</h1>

    </div>
    """,
    unsafe_allow_html=True
    )





# --------------------------------
# DATASET TABLE
# --------------------------------

st.subheader("📋 Dataset Preview")


st.dataframe(

    df.head(10),

    use_container_width=True,

    height=400

)




# --------------------------------
# SIDEBAR INPUT
# --------------------------------

st.sidebar.markdown(
"## 🌿 Flower Measurements"
)



sepal_length = st.sidebar.slider(
"Sepal Length",
4.0,
8.0,
5.1
)


sepal_width = st.sidebar.slider(
"Sepal Width",
2.0,
5.0,
3.5
)


petal_length = st.sidebar.slider(
"Petal Length",
1.0,
7.0,
1.4
)


petal_width = st.sidebar.slider(
"Petal Width",
0.1,
3.0,
0.2
)





# --------------------------------
# PREDICTION
# --------------------------------

input_data = [[

sepal_length,
sepal_width,
petal_length,
petal_width

]]



prediction = model.predict(
input_data
)


result = target_names[prediction[0]]




# --------------------------------
# INPUT TABLE
# --------------------------------

st.subheader("📌 Current Input Values")



input_df = pd.DataFrame(

input_data,

columns=feature_names

)



st.dataframe(

input_df,

use_container_width=True

)





# --------------------------------
# BUTTON
# --------------------------------


if st.button("🔍 Predict Flower Species"):


    st.markdown(

    f"""
    <div class="custom-card">

    <h2>Prediction Result</h2>

    <h1 style="color:#38bdf8">

    {result.upper()}

    </h1>

    </div>

    """,

    unsafe_allow_html=True

    )



    if result=="setosa":

        st.balloons()





# --------------------------------
# INFO
# --------------------------------


st.subheader("🤖 Model Information")


st.info(

f"""

Algorithm: K-Nearest Neighbors (KNN)


Training Samples: {len(X_train)}


Testing Samples: {len(X_test)}


Accuracy: {accuracy*100:.2f}%

"""

)



st.markdown("---")


st.markdown(

"""

<center>



</center>

""",

unsafe_allow_html=True

)