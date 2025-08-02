import cv2
import random
import time
import pygame
import os

# Initialize webcam
cap = cv2.VideoCapture(0)

# Load sound for rating (optional)
pygame.mixer.init()
# You can use any short beep sound (or funny effect)
sound_path = "beep.mp3"  # You must have a .mp3 or .wav in same folder
if os.path.exists(sound_path):
    beep = pygame.mixer.Sound(sound_path)
else:
    beep = None

# Outfit ratings list
ratings = [
    "10/10 – Main character energy 💃",
    "7.5/10 – Slay queen 👑",
    "3/10 – Fashion crime scene 🕵️‍♀️",
    "6/10 – Meh. Safe choice.",
    "9/10 – Looking FINEEE 😍",
    "2/10 – Sweetie... no. 😬",
    "8.5/10 – Lowkey iconic.",
    "5/10 – Midcore. But brave.",
    "0/10 – Burn it. 🔥",
    "11/10 – Heavenly look 😇"
]

font = cv2.FONT_HERSHEY_DUPLEX
show_rating = False
rating_text = ""
last_rating_time = 0
screenshot_count = 0

def get_random_rating():
    return random.choice(ratings)

def play_beep():
    if beep:
        beep.play()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture video.")
        break

    key = cv2.waitKey(1) & 0xFF

    # Show prompt to press R or S
    cv2.putText(frame, "Press 'R' to Rate, 'S' to Screenshot, 'Q' to Quit", (20, 30), font, 0.6, (0, 255, 255), 2)

    # If 'r' is pressed, show rating
    if key == ord('r'):
        show_rating = True
        rating_text = get_random_rating()
        last_rating_time = time.time()
        play_beep()

    # If 's' is pressed, take screenshot
    if key == ord('s'):
        screenshot_count += 1
        filename = f"screenshot_{screenshot_count}.png"
        cv2.imwrite(filename, frame)
        cv2.putText(frame, f"Screenshot saved as {filename}", (20, 470), font, 0.6, (0, 255, 0), 2)

    # Show rating for 5 seconds
    if show_rating and time.time() - last_rating_time < 5:
        cv2.putText(frame, rating_text, (30, 100), font, 0.9, (255, 0, 255), 2)
    elif show_rating:
        show_rating = False

    # Display frame
    cv2.imshow("👗 Dress Rating App – Rose Edition 👑", frame)

    # Quit app
    if key == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
