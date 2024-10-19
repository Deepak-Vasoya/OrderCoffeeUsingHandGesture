import os
from cvzone.HandTrackingModule import HandDetector
import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)  # Try with 0 instead of 1 if only one camera
cap.set(3, 640)
cap.set(4, 480)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# Load the background image
imgBackground = cv2.imread("Resources/Background.png")

# Import all the mode images to a list
folderPathModes = "Resources/Modes"
listImgModesPath = os.listdir(folderPathModes)
listImgModes = [cv2.imread(os.path.join(folderPathModes, imgModePath)) for imgModePath in listImgModesPath]

# Import all the icons to a list
folderPathIcons = "Resources/Icons"
listImgIconsPath = os.listdir(folderPathIcons)
listImgIcons = [cv2.imread(os.path.join(folderPathIcons, imgIconsPath)) for imgIconsPath in listImgIconsPath]

# Initialize HandDetector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Mode and selection initialization
modeType = 0  # For changing selection mode
selection = -1
counter = 0
selectionSpeed = 7
modePositions = [(1136, 196), (1000, 384), (1136, 581)]
counterPause = 0
selectionList = [-1, -1, -1]

# Main loop
while True:
    success, img = cap.read()

    # Check if image was successfully captured
    if not success or img is None:
        print("Failed to capture image")
        continue  # Skip this frame

    # Find the hand and its landmarks
    hands, img = detector.findHands(img)  # With draw

    # Overlay webcam feed on the background image
    imgBackground[139:139 + 480, 50:50 + 640] = img
    imgBackground[0:720, 847: 1280] = listImgModes[modeType]

    if hands and counterPause == 0 and modeType < 3:
        hand1 = hands[0]
        fingers1 = detector.fingersUp(hand1)
        print(fingers1)

        # Check for different finger gestures
        if fingers1 == [0, 1, 0, 0, 0]:  # Index finger
            if selection != 1:
                counter = 1
            selection = 1
        elif fingers1 == [0, 1, 1, 0, 0]:  # Index and middle fingers
            if selection != 2:
                counter = 1
            selection = 2
        elif fingers1 == [0, 1, 1, 1, 0]:  # Index, middle, and ring fingers
            if selection != 3:
                counter = 1
            selection = 3
        else:
            selection = -1
            counter = 0

        # Handle selection
        if counter > 0:
            counter += 1
            print(counter)
            cv2.ellipse(imgBackground, modePositions[selection - 1], (103, 103), 0, 0,
                        counter * selectionSpeed, (0, 255, 0), 20)
            if counter * selectionSpeed > 360:
                selectionList[modeType] = selection
                modeType += 1
                counter = 0
                selection = -1
                counterPause = 1

    # Pause after each selection is made
    if counterPause > 0:
        counterPause += 1
        if counterPause > 60:
            counterPause = 0

    # Add selection icon at the bottom
    if selectionList[0] != -1:
        imgBackground[636:636 + 65, 133:133 + 65] = listImgIcons[selectionList[0] - 1]
    if selectionList[1] != -1:
        imgBackground[636:636 + 65, 340:340 + 65] = listImgIcons[2 + selectionList[1]]
    if selectionList[2] != -1:
        imgBackground[636:636 + 65, 542:542 + 65] = listImgIcons[5 + selectionList[2]]

    # Display the background with overlay
    cv2.imshow("Background", imgBackground)

    # Wait for 1 ms between frames
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
