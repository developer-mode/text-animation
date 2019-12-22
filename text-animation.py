# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~ Project Name: Text Animation ~
# ~ Author: Developer Mode       ~
# ~ Instagram: /developermode    ~
# ~ GitHub: /developer-mode      ~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from time import sleep

def animate(input_text):
    text_length = int(len(input_text))+1
    text = 2 * (input_text + '  ')
    for i in range(0,text_length+1):
        print("\033c")
        print("\t┌─────────────────────────────┐")
        print('\t│  ' + text[i:i+25] + '  │')
        print("\t└─────────────────────────────┘")
        print("\n\n")
        sleep(0.2) # Moves a character to the left every 0.2 seconds
    
    animate(input_text) # Function Recursion | Repeats the Animation

animate("Welcome to DeveloperMode!")

