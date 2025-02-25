# 🚀 Transport Classification Model

![Streamlit App](https://img.shields.io/badge/Streamlit-Deployed-brightgreen)
![FastAI](https://img.shields.io/badge/FastAI-Enabled-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-yellowgreen)

Welcome to the **Transport Classification Model**, a deep learning-based web application built using **Streamlit** and **FastAI**. This model classifies images of different types of transport, such as cars, planes, boats, and more! 🚗🚁🚢

### 🌐 Live Demo
Check out the live deployed version: [Transport Classifier](https://transports-classification.streamlit.app/)

---

## 📌 Features
✅ Upload an image of a transport vehicle
✅ Get an AI-based classification result
✅ View prediction confidence score
✅ Interactive and responsive UI using **Streamlit**
✅ Optimized for deployment on **Streamlit Cloud**

---

## 📂 Project Structure
```
├── transport_model.pkl       # Trained FastAI model
├── app.py                    # Streamlit app script
├── requirements.txt          # Dependencies
├── README.md                 # Project Documentation
```

---

## 🚀 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/transport-classifier.git
cd transport-classifier
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit App Locally
```bash
streamlit run app.py
```

---

## 🛠 Model Details
This project uses **FastAI** for deep learning-based image classification. The model was trained on a dataset containing different types of transport vehicles. The pre-trained **ResNet** model was fine-tuned for optimal accuracy.

### 🔧 Tech Stack
- **Python 3.8+**
- **FastAI**
- **Streamlit**
- **PyTorch**

---

## 🚀 Deployment on Streamlit Cloud
Want to deploy your own version? Follow these steps:
1. Push your code to a public GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Connect your GitHub repository and deploy the app.

---

## 🤝 Contributing
Contributions are welcome! If you'd like to enhance this project, feel free to submit a pull request.

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

---

