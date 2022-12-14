'''
Manipulate the keyboard to press the specified shortcut key by judging the  `recognizer.now_ges`
'''
from recognition.recognition import recognizer
import keyboard
import yaml
import time
from threading import Thread
from GlobalStates import MyGlobalStates, resource_path


def load(file=resource_path("assets/bind.yml")) -> dict:
    with open(file, 'r', encoding='utf-8') as f:
        binds = yaml.load(f.read(), Loader=yaml.FullLoader)
        f.close()
    return binds


binds = load()


def reloads():
    global binds
    binds = load()


def waiting_to_press_and_release():
    global binds
    while True:
        if MyGlobalStates.__run__:
            if recognizer.now_ges in binds.keys():
                if binds[recognizer.now_ges] != 'nothing':
                    keyboard.press_and_release(binds[recognizer.now_ges])
            time.sleep(0.35)
        else:
            break


# waiting
def start_in_thread():
    Thread(target=waiting_to_press_and_release).start()
