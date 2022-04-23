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
      if inp < 501 and inp > 0:
        return inp
    except ValueError:
      print("Invalid input")
    else:
      print("Please input a number between 1 and 500")

def run_mag(mag_size):
  
  print(mag_size)
      
def main():
  print("Welcome to 'x'")
  
  
  avg_choice = get_YN_input("Would you like to use your average magnification preset? [Y/N]: ")
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
    run_mag(avg)
  elif avg_choice == False:
    file = open('mags.txt', 'a')
    magni = get_magnification()
    file.write(str(magni))
    file.write("\n")
    run_mag(magni)
  file.close()
main()