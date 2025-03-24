## Next Word Prediction using the LSTM RNN

# **LSTM Model Deployment with Streamlit**

## **📌 Project Overview**
This project deploys an **LSTM-based text classification model** using **Streamlit**. The web app allows users to enter text and get predictions from a trained LSTM model.

---
## **📂 Project Structure**
```
├── app.py                  # Streamlit app
├── lstm_model.h5           # Trained LSTM model
├── tokenizer.pkl           # Saved tokenizer
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---
## **🔹 Installation**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-repo/streamlit-lstm.git
cd streamlit-lstm
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

---
## **🚀 Run the Streamlit App**
```bash
streamlit run app.py
```

## **🔹 Deploying on Cloud**
### **1️⃣ Deploy on Streamlit Community Cloud**
1. Create a **GitHub repository** with your project files.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Connect your GitHub repo and deploy.

### **2️⃣ Deploy on Heroku**
1. Create a `requirements.txt` file.
2. Use `Procfile` to define the Streamlit command.
3. Deploy using **Heroku CLI**.

---
## **📌 Dependencies (`requirements.txt`)**
```txt
streamlit
tensorflow
numpy
pickle-mixin
```

---
## **🎯 Summary**
✅ **Train an LSTM model** for text classification.  
✅ **Deploy it using Streamlit** with an interactive UI.  
✅ **Use a tokenizer** to process text inputs.  
✅ **Deploy on cloud platforms** (Streamlit Cloud, Heroku, etc.).  

🚀 **Enjoy building AI-powered web apps with Streamlit!**



Deploy link:  https://next-word-prediction-using-lstm-rnn-01.streamlit.app