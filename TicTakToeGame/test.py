import sys
import time

for i in reversed(range(1, 11)):
    sys.stderr.write(f"{i:2d}\r")
    time.sleep(.1)


lst = ["Как дела?", "Что делаешь?", "Как настроение?"]
for word in lst:
    for letter in word:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.05)
    
    print('\r ') 
    time.sleep(1)