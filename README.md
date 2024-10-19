# ☕ Virtual Coffee Machine with Hand Gesture Recognition

This project simulates a **virtual coffee machine interface** using hand gestures to select and customize coffee options. Leveraging **computer vision** and **AI techniques**, users can interact with the interface without touching physical buttons, offering a futuristic and hygienic coffee-ordering experience.

---

## 🚀 Features
- ✋ **Hand Gesture Recognition**: Simple hand gestures to interact with the coffee machine.
- ☕ **Coffee Selection**: Choose from a variety of coffee options like Espresso, Latte, and more.
- 🎛️ **Customization**: Adjust coffee strength, milk, and sugar levels with ease.
- 🤖 **AI-Powered Detection**: Uses **Mediapipe** for accurate hand detection and gesture recognition.
- 🔄 **Real-Time Feedback**: Immediate, live feedback for each selection.

---

## 🛠️ Technology Stack
- **Python**: Core programming language used.
- **OpenCV**: For video capture and real-time image processing.
- **Mediapipe**: Hand tracking and gesture recognition.
- **CVZone**: Simplified hand gesture detection.
- **GUI**: Virtual interface for a seamless user experience.

---

## 📝 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/Deepak-Vasoya/OrderCoffeeUsingHandGesture.git 
cd OrderCoffeeUsingHandGesture
```

### 2. Run the Project
```bash
python main.py
```

---

## 🔍 How It Works
- **Hand Gesture Detection**: The system tracks your hand using a webcam, detecting gestures like one, two, or three fingers, each representing a different selection or customization option.
- **Virtual Interface**: The real-time video feed overlays icons to simulate coffee-making selections.
- **Selection & Customization**: Customize your coffee by holding up different fingers for strength, milk, and sugar options.
- **Visual Feedback**: Every selection is visually confirmed on the interface, providing an intuitive and smooth user experience.

---

## 📂 Project Structure
```bash
.
├── Resources/
│   ├── Background.png  # Background image of the coffee machine
│   ├── Modes/          # Different interface modes for selection
│   └── Icons/          # Icons for various coffee options
├── main.py             # Main script for the project
└── README.md           # Project documentation
```

---

## 🔧 Future Enhancements
- Add more coffee customization options.
- Improve gesture recognition for more accurate and smooth interaction.
- Implement voice commands for an even more immersive user experience.

---

## 📝 License
This project is licensed under the MIT License.

---

## 🙏 Acknowledgements
- [OpenCV](https://opencv.org/) for real-time video processing.
- [Mediapipe](https://google.github.io/mediapipe/) for hand tracking.
- [CVZone](https://github.com/cvzone/cvzone) for simplifying hand gesture recognition.

---
Happy Brewing! ☕
