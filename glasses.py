import pyautogui

from PIL import Image 
def run_program(mag_size):
    toggleZoom = False  
    toggleTerminate = toggleZoomrue
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
    width_total, height_total = screensize
    
    while(toggleZoom): #continue to do this
        position = pyautogui.position()
        
        box_width, box_height = width_total * .2, height_total * .2 
        left_distance = box_width // 4
        right_distance = left_distance * 3
        up_distance = box_height // 2
        down_distance = up_distance
        
        mouse_width, mouse_height = position
        if (mouse_width - left_distance < 0):
            left_distance = mouse_width
        if (mouse_width + right_distance > width_total):
            right_distance = box_width - mouse_width
        if (mouse_height + up_distance > height_total):
            up_distance = box_height - mouse_height
        if (mouse_height - down_distance < 0):
            down_distance = mouse_height
       
        left = (mouse_width - left_distance)
        down = (mouse_height - down_distance)
        up = (mouse_height + up_distance)
        right = (mouse_width + right_distance)
        
        myScreenshot = pyautogui.screenshot()
        im = Image.myScreenshot
        im = im.crop(left, up, right, down)
        
        magnify(im, mag_size)
        
        if(keyboard.is_pressed("ctrl+shift+m")):
            toggleZoom = not toggleZoom


def magnify(image, mag_size):
    
  image.show()


def get_YN_input(prompt):
  '''
  Returns true for yes and false for no
  '''
  while True:
    inp = input(prompt)
    if inp not in 'YN':
      print("Invalid input")
    elif inp == 'Y':
      return True
    elif inp == 'N':
      return False



def get_magnification():
  while True:
    inp = input("How much would you like to magnify by? ")
    try:
      inp = int(inp)
      if inp < 201 and inp > 0:
        return inp
    except ValueError:
      print("Invalid input")
    else:
      print("Please input a number between 1 and 200")
    
def main():
  print("Welcome to Magnify!")
  file = open("mags.txt", 'r')
  list = file.readlines()
  if len(list) > 5:
    avg_choice = get_YN_input("Would you like to use your average magnification preset? [Y/N]: ")
  else:
    avg_choice = False
  if avg_choice == True:
    file = open("mags.txt", "r")
    mags_list = file.readlines()
    for x in range(len(mags_list)):
      y = mags_list[x]
      y = int(y.strip('\n'))
      mags_list[x] = y
    list_sum = sum(mags_list)
    list_len = len(mags_list)
    avg = list_sum // list_len
    run_program(avg)
  elif avg_choice == False:
    file = open('mags.txt', 'a')
    magni = get_magnification()
    file.write(str(magni))
    file.write("\n")
    run_program(magni)
  file.close()


main()
