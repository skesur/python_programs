import streamlit as st
import numpy as np
import datetime as dt
import time as t
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Streamlit Demo",
    page_icon="",
    layout="wide"
)

st.sidebar.title("Stramlit Topics")
page = st.sidebar.radio("Go to Section", ['UI & Layout','Input Widgets','Data Display','Buttons & Files','Program 714','Media & Status','Charts and Visualization'])

if page=="UI & Layout":
    st.title("UI Creation & Layout Fundamentals",text_alignment="center")
    st.header("Text Elements")
    st.subheader("Subheader Example")
    st.text("This is text")
    st.write("It supports text, number, table, etc.")
    st.markdown("**Bold** and _italic_")

    code = """
        # Create a class called Matrix containing constructor that initialized the number of rows and number of columns of a new 
    # Matrix object.

    # The Matrix class has methods for each of the following:
    # 1. get the number of rows
    # 2. get the number of columns
    # 3. set the elements of the matrix at given position (i,j)
    # 4. adding two matrices. If the matrices are not addable, “ Matrices cannot be added” will be displayed.
    # (Overload the addition operation to perform this)
    # 5. Multiplying the two matrices.  If the matrices are not multiplied, “ Matrices cannot be multiplied” will 
    # be displayed.(Overload the addition operation to perform this)

    import numpy as np

    class Matrix:
        def __init__(self,r,c):
            self.rows=r
            self.cols=c
            
        def getRows(self):
            return self.rows
        
        def getCols(self):
            return self.cols
        
        def setElements(self):
            self.arr = np.zeros((self.rows,self.cols),dtype=int)
            k = 0
            for i in range(self.rows):
                for j in range(self.cols):
                    k+=1
                    el = int(input(f"Enter element {k} :"))
                    self.arr[i][j]=el
                    
        def __add__(self,other):
            if self.arr.shape==other.arr.shape:
                return self.arr+other.arr
            else:
                return "Matrics cannot be added"
            
        def __mul__(self,other):
            if self.rows==other.cols:
                return np.dot(self.arr,other.arr)
            else:
                return "Matrics cannot be multiplied"
            
    a = Matrix(2,2)
    a.setElements()
    b = Matrix(2,2)
    b.setElements()
    print(a+b)
    print(a*b)
    """

    st.code(code,language="python")

    st.markdown("<div style='width:200px;height:100px;background-color:lightblue;color:crimson;border-radius:25px;display:flex;justify-content:center;align-items:center;font-size:36px;font-weight:500;margin-left:0px;'>Hello World</div>"
    "",unsafe_allow_html=True)

elif page=="Input Widgets":

    st.title("Input Widgets & Interactivity")
    name=st.text_input("Enter name: ")
    feedback=st.text_area("Enter feedback: ")
    age=st.number_input("Enter age: ",1,100,18)
    rating=st.slider("Rate session: ",1,10,5)
    course=st.selectbox("Selecct course: ",["FSD-1","FSCP-1","PS","DE"],index=None)
    days=st.multiselect("Preffered days: ",["Mon","Tue","Wed","Thu","Fri"])
    mode=st.radio("Mode",["Online","Offline"])
    subscribe=st.checkbox("Subscribe")
    exam_date=st.date_input("Date",dt.date.today())
    exam_time=st.time_input("Time",'now')

    st.markdown("### Live Output: ")
    st.write(f"Name: {name}")
    st.write(f"Feedback: {feedback}")
    st.write(f"Age: {age}")
    st.write(f"Rating: {rating}")
    st.write(f"Course: {course}")
    st.write(f"Preferred days: {days}")
    st.write(f"Mode: {mode}")
    st.write(f"Subscribed: {subscribe}")
    st.write(f"Date: {exam_date}")
    st.write(f"Time: {exam_time}")


elif page=="Data Display":
    st.title("Displaying Data")

    data = {
        "Student":["A","B","C"],
        "Marks":[95,35,66],
        "Pass":[True,False,True]
    }

    df = pd.DataFrame(data)
    st.subheader("Table")
    st.table(data)
    st.subheader("Dataframe")
    st.dataframe(data)
    st.subheader("JSON")
    st.json(data)

elif page=="Buttons & Files":
    st.title("Buttons, File upload & Download")
    u_file = st.file_uploader("Upload CSV",type=["csv"])
    if u_file:
        df=pd.read_csv(u_file)
        st.dataframe(df)    

    if st.button("Generate Sample Data"):
        data={
            "Student":["A","B","C"],
            "Marks":[95,35,66],
            "Pass":[True,False,True]
        }    
        df=pd.DataFrame(data)
        st.table(df)

        csv=df.to_csv(index=False)
        st.download_button(
            "Download CSV",
            csv,
            "marks.csv"
        )    

elif page=="Program 714":
    st.title("Program 714")
    st.markdown("""
        BMI Calculator App
        Take user inputs:
        - Weight (kg) (number input)
        - Height (cm) (number input)
        On button click, calculate BMI = weight / (height/100)^2.
        - Display:
        - BMI Value
        - A health category (Underweight, Normal, Overweight, Obese)
        - Show results in colored messages (st.success(), st.warning(), st.error())
    """)        
    weight=st.number_input("Enter weight (kg): ")
    height=st.number_input("Enter height (cm): ")
    if st.button("Calculate BMI"):
        bmi = weight/((height/100)**2)
        st.write("BMI: ",round(bmi,2))
        if bmi<18:
            st.warning("You are Underweight")
        elif bmi<24 and bmi>=18:
            st.success("You are Normal")
        elif bmi<30 and bmi>=24:
            st.warning("You are Overweight")
        else:
            st.error("You are Obese")            

elif page == "Media & Status":

    st.title("Media & Status")
    st.success("Success Status")
    st.info("Info Status")
    st.warning("Warning Status")
    st.error("Error Status")
    if st.button("Start Task") : 
        progress = st.progress(0)
        with st.spinner("Processing..."):
            for i in range(100):
                t.sleep(0.3)
                progress.progress(i+1)
        st.success("Task Completed")        

    st.divider()
    st.subheader("Media Display")
    st.image("th.jfif",caption="Python", width="stretch")
    st.image("https://picsum.photos/600/300")   
    st.audio("sampleaudio.mp3")
    st.video("samplevideo.mp4") 
    st.video("https://youtu.be/JrTwLUHOp_U?si=pZirfNHbqB6GJPP_")

elif page=="Charts and Visualization":
    st.title("Charts and Visualization")

    x=np.arange(1,101)
    y=np.random.randint(1,100,100)
    
    st.subheader("Matplotlib Line Chart")
    plt.figure()
    plt.plot(x,y,marker="*")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Line Chart")
    st.pyplot(plt)

    st.subheader('Matplotlib Histogram')
    plt.figure()
    plt.hist(y,color='red')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title("Histogram")
    st.pyplot(plt)

    st.subheader("Streamlit in-built Charts")
    data={
        "X":x,
        "Y":y
    }
    df = pd.DataFrame(data)
    st.line_chart(df["Y"],color="#ffaa0088")
    st.bar_chart(df["Y"],color="#0d00ff87")
    st.area_chart(df["Y"])

