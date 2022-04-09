#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template


# In[2]:


app = Flask(__name__)


# In[3]:


import joblib


# In[4]:


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        age = request.form.get("income")
        loan = request.form.get("age")
        income = float(income)
        age = float(age)
        loan = float(loan)
        print(income,age,loan)

        model1 = joblib.load("CART")
        pred1 = model1.predict([[income, age, loan]])
        s1 = "The Risk of Credit Card Default based on Decision Tree is " + str(pred1[0])
        
        model2 = joblib.load("RF")
        pred2 = model2.predict([[income, age, loan]])
        s2 = "The Risk of Credit Card Default based on Random Forest is " + str(pred2[0])
        
        model3 = joblib.load("GB")
        pred3 = model3.predict([[income, age, loan]])
        s1 = "The Risk of Credit Card Default based on Gradient Boosting is " + str(pred3[0])
        
        return(render_template("index.html", result1=s1, result2=s2, result3=s3))
    else:
        return(render_template("index.html", result1= "2", result2= "2", result3= "2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




