import pyautogui
from PIL import Image 
def run_program(mag_size):
    toggleZoom = false  
    toggleTerminate = true
    #While toggle is on,
    while (toggleTerminate): 
        if(keyboard.is_pressed("ctrl+shift+m")): #toggle between zooming and not
            toggleZoom = not toggleZoom

        if(toggleZoom): #check to see if it is zooming and then call the function to do so 
            zoom(mag_size, toggleZoom)

        if(keyboard.is_pressed("ctrl+shift+t")): #once the terminate keybind is pressed exit.
            toggleTerminate = false

def zoom(mag_size, toggleZoom):
    screensize = pyautogui.size() #get screensize to compare with the area we are zooming into. 

    while(toggleZoom): #continue to do thi s
        position = pyautogui.position()
        screenFile = open(screenshot.png)
        
run_program(mag_size)