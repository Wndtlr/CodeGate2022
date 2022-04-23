import keyboard
import pyautogui
from PIL import Image 


position = pyautogui.position()
#While toggle is on,
while (keyboard.is_pressed("ctrl+shift+m")):
    position = pyautogui.position()
    

    