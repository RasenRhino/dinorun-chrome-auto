from pynput.keyboard import Key, Controller

keyboard = Controller()


import time
st=time.time()
while True:
		keyboard.press(Key.space)

		st=time.time()
		print("ha")