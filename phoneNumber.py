import re,pyperclip
Passregex = re.compile(r'([A-Z])+([a-z])+(\d)+')
store = []
message  = str(pyperclip.paste())

if len(message)>=8:
    mess = Passregex.search(message)
    if mess != None:
        print("Strong password detected")
        print(mess.group())
    else:
        print("Try again")


