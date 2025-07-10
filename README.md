# 🐾 Cats vs Dogs Image Classifier
_A Machine Learning + Web App Project built during the IBM PBEL Virtual Internship_

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)

A clean and user-friendly web application that classifies images as either a **Cat** or a **Dog** using a **Convolutional Neural Network (CNN)** built with TensorFlow and deployed through a Flask web server.
> 🎓 This project was built as part of the **IBM PBEL Virtual Internship** under the domain of AI/ML.

This project blends deep learning and web development to create a real-world AI-powered tool, ideal for showcasing machine learning deployment skills.

---

## Demo

**Interactive Demo**: Upload a cat or dog image and get an instant prediction from the model.

> **Model**: Custom CNN  
> **Accuracy**: Achieved **87.06%** validation accuracy after 10 epochs
> **Accuracy**: Trained on Cats vs Dogs dataset (binary classification)

---

## Screenshots

### Before Prediction

![Before Prediction](static/demo_before.jpg)

---

### After Prediction

![After Prediction](static/demo_after.jpg)
 
---

## How It Works

1. User uploads a JPG/PNG image of a cat or dog
2. Image is resized and normalized
3. Preprocessed image is passed to a trained CNN
4. Model predicts and displays whether it's a cat or dog

---

## Model Overview

- Built using **Keras (TensorFlow backend)**
- Binary classification: `0 = Cat`, `1 = Dog`
- Input images resized to **150x150**, normalized
- Final trained model saved as `.keras` and used in Flask app
- **Final Validation Accuracy**: **87.06%**
- Training performed over 10 epochs on the **Cats vs Dogs** dataset
- View training notebook: [cats_vs_dogs_model_training_colab.ipynb](cats_vs_dogs_model_training_colab.ipynb)

---

## Tech Stack

| Layer        | Technologies              |
|--------------|---------------------------|
| **Frontend** | HTML5, CSS3, Font Awesome |
| **Backend**  | Python, Flask             |
| **Modeling** | TensorFlow, Keras         |
| **Tools**    | VS Code, Git, GitHub      |

---

## Features

- Upload an image (JPG/PNG)
- Predict using a trained CNN
- Stylish UI with gradient background & paw prints
- Shows uploaded image and result clearly
- Includes footer with LinkedIn & GitHub links

---

## Installation

> Clone & run locally in a virtual environment

```bash
git clone https://github.com/Vipul-0503/cats-vs-dogs-classifier.git
cd cats-vs-dogs-classifier

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

---

## Run the App

Once everything is set up:

Open your browser and go to:  
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📁 Project Structure

```bash
cats-vs-dogs-webapp/
│
├── app.py                                          # Flask web server
├── cats_vs_dogs_cnn.keras                          # Trained CNN model
├── cats_vs_dogs_model_training_colab.ipynb         # Colab notebook
├── requirements.txt                                # Python dependencies
├── README.md                                       # This file
├── LICENSE                                         # Apache License 2.0
├── .gitignore
│
├── templates/
│ └── index.html                                    # Web interface (HTML)
│
├── static/
│ ├── style.css                                     # Styling for UI
│ ├── demo_before.jpg                               # Screenshot before prediction
│ ├── demo_after.jpg                                # Screenshot after prediction
│ └── uploads/                                      # User-uploaded images
```

---

## License

This project is licensed under the **Apache License 2.0**.  
See the [LICENSE](LICENSE) file for full details.
  
You are free to **use**, **modify**, **distribute**, and **fork** this project, provided that proper attribution is given and any changes are noted.

---

## 🔗 Connect with Me

Made with 💜 by **Vipul**

- 🌐 [LinkedIn](https://www.linkedin.com/in/vipul-458b70310)
- 💻 [GitHub](https://github.com/Vipul-0503)

---

## ⭐ Bonus Ideas for the Future

- Add drag-and-drop image upload
- Add webcam capture functionality
- Deploy on **Render**, **PythonAnywhere**, or **Heroku**
- Extend model to classify multiple animals (e.g. rabbit, panda)

---

> ⭐ If you like this project, consider giving it a **star** on GitHub!


