import unittest

class Test(unittest.TestCase):
  import time
  import threading
  from pynput.mouse import Button, Controller as MouseController
  from pynput.keyboard import Listener, KeyCode, Key, Controller as KeyboardController
  import random
  import errno

  # Delay variables
  delay = 0.01
  rand_delay_max = 0.1
  rand_delay_min = 0.01

  # key press variables
  start_stop_key = KeyCode(char='.')
  exit_key = KeyCode(char=',')
  toggle_key = KeyCode(char='k')
  rand_delay_key = KeyCode(char='r')

  try:
      with open('stats.txt', 'r') as file:
          # read a list of lines into data if file found 
          data = file.readlines()
  except FileNotFoundError as e:
      if e.errno == errno.ENOENT:
          # FileNotFoundError code here
          with open('stats.txt', 'a') as file:
              file.write("0")
              file.close()
      else:
          raise
  finally:
      with open('stats.txt', 'r') as file:
          # read a list of lines into data
          data = file.readlines()
  try:
      with open('mouseButton.txt', 'r') as mbfile:
          # read a list of lines into data if file found 
          mbdata = mbfile.readlines()
  except FileNotFoundError as e:
      if e.errno == errno.ENOENT:
          # FileNotFoundError code here
          with open('mouseButton.txt', 'a') as mbfile:
              mbfile.write("0")
              mbfile.write("\n")
              mbfile.write("0")
              mbfile.close()
      else:
          raise
  finally:
      with open('mouseButton.txt', 'r') as mbfile:
          # read a list of lines into data
          mbdata = mbfile.readlines()

  # saved mouse button / rand button
  pastButton = mbdata[0]
  pastButton = str(pastButton)
  if pastButton == "1" or "1\n":
      button = Button.right
      currentButton = "right"
      print("Current button: " + currentButton)
  elif pastButton == "0" or "0\n":
      button = Button.left
      currentButton = "left"
      print("Current button: " + currentButton)
  else:
      button = Button.left
      currentButton = "left"
      print("Past button not found. Defaulting to: " + currentButton + " mouse button")


  pastRand = mbdata[1]
  pastRand = str(pastRand)
  if pastRand == "1" or "1\n":
      rand_numb = True
      rand_numb_status = "true"
      print(" ")
      print("Random delay time toggled to " + rand_numb_status) 
  elif pastRand == "0" or "0\n":
      rand_numb = False
      rand_numb_status = "false"
      print(" ")
      print("Random delay time toggled to " + rand_numb_status) 
  else:
      rand_numb = False
      rand_numb_status = "false"
      print(" ")
      print("Past rand_status not found. Defaulting to: " + rand_numb_status)

  # other default variables
  times = 0
  times = int(times)
  sessionTimes = 0
  sessionTimes = int(sessionTimes)
  TotalTimes = data[0]
  TotalTimes = int(TotalTimes)
  read_lines_stats = 1
  read_lines_mbd = 2

  class ClickMouse(threading.Thread):
      def __init__(self, delay, button):
          super(ClickMouse, self).__init__()
          self.delay = delay
          self.button = button
          self.running = False
          self.program_running = True
          # rand delay
          global rand_numb
          self.rand_numb = rand_numb

      def start_clicking(self):
          self.running = True

      def stop_clicking(self):
          self.running = False

      def exit(self):
          global Totaltimes
          global past_key
          global read_lines_stats
          global read_lines_mbd
          global currentButton
          global rand_numb_status
          self.stop_clicking()
          self.program_running = False

          # define TotalTimes as a string (and data[0] as a string to be sure that it works)
          Totaltimes = str(TotalTimes)
          data[0] = TotalTimes
          data[0] = str(data[0])

          # write everything back to stats.txt
          with open('stats.txt', 'w') as file:
              # file.writelines( data )
              data_amount_stats = 0
              for x in range(read_lines_stats):
                  file.write(data[data_amount_stats])
                  data_amount_stats = data_amount_stats + 1
                  file.write("\n")
          print("wrote and/or appended " + str(data_amount_stats) + " string to file: stats.txt")
          file.close()

          # define currentButton as a string (and mbdata[0] as a string to be sure that it works)
          if currentButton == "left":
              currentButton = "0"
          elif currentButton == "right":
              currentButton = "1"
          else:
              currentButton = "0"
          currentButton = str(currentButton)
          mbdata[0] = currentButton
          mbdata[0] = str(mbdata[0])

          if self.rand_numb == True:
              rand_numb_status = "1"
          elif self.rand_numb == False:
              rand_numb_status = "0"
          else:
              rand_numb_status = "0"
          rand_numb_status = str(rand_numb_status)
          mbdata[1] = rand_numb_status
          mbdata[1] = str(mbdata[1])

          with open('mouseButton.txt', 'w') as file:
              # file.writelines( data )
              data_amount_mbd = 0
              for x in range(read_lines_mbd):
                  file.write(mbdata[data_amount_mbd]) # maybe dont do this
                  data_amount_mbd = data_amount_mbd + 1
                  if data_amount_mbd == read_lines_mbd:
                      pass
                  else:
                      file.write("\n")
          print("wrote and/or appended " + str(data_amount_mbd) + " string(s) to file: mouseButton.txt")
          file.close()
          exit

      def rand_numb_T(self):
          self.rand_numb = True

      def rand_numb_F(self):
          self.rand_numb = False

      def run(self):
          while self.program_running:
              while self.running:
                  global times
                  global TotalTimes
                  global sessionTimes
                  mouse.click(self.button)
                  times = times + 1
                  print(times)
                  sessionTimes = sessionTimes + 1
                  TotalTimes = TotalTimes + 1                
                  if self.rand_numb == False:
                      time.sleep(self.delay)
                  elif self.rand_numb == True:
                      self.rand_delay = random.uniform(rand_delay_max,rand_delay_min)
                      time.sleep(self.rand_delay)
                      print("")
                      print("random delay set to: " + str(self.rand_delay))
              time.sleep(0.1)

      # Toggle Key
      def toggleKey(self):
          global button
          global currentButton
          if self.button == Button.left:
              self.button = Button.right
              currentButton = "right"
          elif self.button == Button.right:
              self.button = Button.left
              currentButton = "left"

  keyboard = KeyboardController()
  mouse = MouseController()
  click_thread = ClickMouse(delay, button)
  click_thread.start()

  def on_press(key):
      if key == start_stop_key:
          if click_thread.running: 
              global times
              global TotalTimes
              global sessionTimes
              click_thread.stop_clicking()
              print(" ")
              print("Clicks this run: " + str(times))
              print("Clicks this session: " + str(sessionTimes))
              print("Lifetime Clicks: " + str(TotalTimes))
              print("Clearing session clicks...")
              times = 0

          else:
              click_thread.start_clicking()
      elif key == exit_key:
          click_thread.exit()
          listener.stop()


      # toggle key pressed
      elif key == toggle_key:
          global currentButton
          click_thread.toggleKey()
          print(" ")
          print("key toggled; current button: " + currentButton)


      # rand key pressed
      elif key == rand_delay_key:
          if click_thread.rand_numb == True:
              click_thread.rand_numb_F()
              rand_numb_status = "false"
          elif click_thread.rand_numb == False:
              click_thread.rand_numb_T()
              rand_numb_status = "true"
          print(" ")
          print("Random delay time toggled to " + rand_numb_status)

  with Listener(on_press=on_press) as listener:
      listener.join()
if __name__ == '__main__':
  unittest.main()
