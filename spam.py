# This program is for spamming messages in any links or apps.

# Importing necessasary modules.
import pyautogui
import time
import webbrowser

## Use this code before executing the whole program to find the position of where to write and enter the messages in the wanted link.
## Put the values gotten in coordinate variable.
# currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX,"and ",currentMouseY)

coordinate=(1000, 969)

# Give the url of the site you want to spam on. By default its given whatsapp.
# Dont use this step if the intention is to spam in an app. Manually select the app.
url = 'https://web.whatsapp.com'
webbrowser.open(url)

# Some time is given to select the chat to spam on.
time.sleep(10)

repeats=2  # No of times spam.txt is to be repeated.
with open("pythonfiles\spam.txt",encoding='utf8') as f:    # Opening spam.txt containing words to spam. By default its given Lorem Ipsum.
    text=f.readlines()  
    for repeat in range(repeats):
        pyautogui.click(coordinate)
        for sentence in text:
            for words in sentence:
                pyautogui.write(words, interval=0)        # Writes every letters of the spam.txt 
                pyautogui.press('enter')                  # And sends it.
        repeat+=1
				
# End of program.
