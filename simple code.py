import cv2
import random
import time
from playsound import playsound

NORMAL_TEMP = 25.0 
TEMP_TOLERANCE = 5.0  

def get_current_temperature():
    return round(random.uniform(24, 31), 2)

def check_temperature(temp):
    if abs(temp - NORMAL_TEMP) > TEMP_TOLERANCE:
        print(f"[ALERT] Temperature fluctuation detected: {temp}°C")
    else:
        print(f"[OK] Temperature stable: {temp}°C")

def detect_knock():
    knock = random.choice([True, False])
    if knock:
        print("[INFO] Delivery knock detected at the door!")
        try:
            playsound("knock.mp3")  
        except:
            print("(Sound file missing - skipping sound alert)")
    else:
        print("[INFO] No knock detected.")

def motion_detection_simulation():
    objects = ["none", "animal", "human"]
    detected = random.choice(objects)
    if detected == "animal":
        print("[ALERT] Animal movement detected in the room!")
    elif detected == "human":
        print("[ALERT] Human movement detected in the room!")
    else:
        print("[OK] No significant movement detected.")
        
def main():
    print("Starting Resilient AI-IoT Result Analysis Simulation...\n")
    for _ in range(5): 
        temp = get_current_temperature()
        check_temperature(temp)
        detect_knock()
        motion_detection_simulation()
        print("-" * 60)
        time.sleep(2)

if __name__ == "__main__":
    main()
