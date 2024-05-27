import pyautogui
import time

def autoclick(interval):
    try:
        while True:
            pyautogui.click()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Autoclicker stopped.")

if __name__ == "__main__":
    interval = float(input("Enter click interval:"))
    print("Press Ctrl+C to stop the autoclicker.")
    autoclick(interval)
