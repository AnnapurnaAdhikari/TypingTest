
# Typing Speed Test App

A simple Typing Speed Test built using **Streamlit**.
The app allows users to test their typing speed and accuracy with randomly selected sample texts.

## Features

- Displays random text to type
- Calculates:
    - Time taken
    - Words per minute (WPM)
    - Accuracy (%)
- Simple and easy-to-use interface (powered by **Streamlit**)

## 🛠 Setup Instructions

### 1️⃣ Clone or download the repository
```bash 
git clone https://github.com/AnnapurnaAdhikari/TypingTest.git
cd typing-test-app
```

### 2️⃣ Create and activate virtual environment
- Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```
- macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install streamlit
```
### 4️⃣ Run the Streamlit app
```bash
streamlit run app.py
```
- The app will open automatically in your browser.

## 📸 Screenshot
* ![Home Page](image.png)
* ![After taking test](image-1.png)

## 🔮 Future Improvements

- Real-time WPM calculation

- Countdown timer

- Highlight incorrect words

- Leaderboard