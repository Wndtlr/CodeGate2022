import pyautogui
from PIL import Image 
def run_program(mag_size):
    toggleZoom = false  
    toggleTerminate = true
    #While toggle is on,

    while (toggleTerminate): 
        if(keyboard.is_pressed("ctrl+shift+m")):
            toggleZoom = not toggleZoom

        if(toggleZoom):
            zoom(mag_size, toggleZoom)

        if(keyboard.is_pressed("ctrl+shift+t")):
            toggleTerminate = false


def zoom(mag_size, toggleZoom):
    while(toggleZoom):
        position = pyautogui.position()
        screenFile = open(screenshot.png)
run_program(mag_size)