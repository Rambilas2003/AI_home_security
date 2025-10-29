from playsound import playsound
import random
import time
NORMAL_TEMP = 10.0 
TEMP_TOLERANCE = 5.0 
def get_current_temperature():
    return round(random.uniform(24, 31), 2)
def check_temperature(temp):
    if abs(temp - NORMAL_TEMP) > TEMP_TOLERANCE:
        print(f"[ALERT] Temperature fluctuation detected: {temp}°C")
        playsound("knock.mp3")
    else:
        print(f"[OK] Temperature stable: {temp}°C")
        
        
def main():
    print("Starting Resilient AI-IoT Result Analysis Simulation...\n")
    for _ in range(5): 
        temp = get_current_temperature()
        check_temperature(temp)
        print("-" * 60)
        time.sleep(2)

if __name__ == "__main__":
    main()
