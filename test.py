import mediapipe as mp
import cv2
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
# Initialize MediaPipe Hands
hands = mp_hands.Hands()

# Read an image or frame
frame = cv2.imread("your_image.jpg")  # Replace with your actual image or frame

# Convert the image to RGB
frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Process the image and get hand landmarks
results = hands.process(frame_rgb)

# Draw landmarks on the image
if results.multi_hand_landmarks:
    for landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

# Display the image with landmarks
cv2.imshow("Hand Tracking", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
