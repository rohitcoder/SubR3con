import os
import subprocess
# importing basic modules
import urllib2
import fileinput
import sys
import socket
import ssl
# Check if we are running this on windows platform
is_windows = sys.platform.startswith('win')
context = ssl._create_unverified_context()
# Console Colors
if is_windows:
    # Windows deserves coloring too :D
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white
    try:
        import win_unicode_console , colorama
        win_unicode_console.enable()
        colorama.init()
        #Now the unicode will work ^_^
    except:
        print("[!] Error: Coloring libraries not installed, no coloring will be used [Check the readme]")
        G = Y = B = R = W = G = Y = B = R = W = ''


else:
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white


def banner():
    print("""%s
 _______           ______   _______  ______   _______  _______   
(  ____ \|\     /|(  ___ \ (  ____ )/ ___  \ (  ____ \(  ___  )( (    /|
| (    \/| )   ( || (   ) )| (    )|\/   \  \| (    \/| (   ) ||  \  ( |
| (_____ | |   | || (__/ / | (____)|   ___) /| |      | |   | ||   \ | |
(_____  )| |   | ||  __ (  |     __)  (___ ( | |      | |   | || (\ \) |
      ) || |   | || (  \ \ | (\ (         ) \| |      | |   | || | \   |
/\____) || (___) || )___) )| ) \ \__/\___/  /| (____/\| (___) || )  \  |
\_______)(_______)|/ \___/ |/   \__/\______/ (_______/(_______)|/    )_)
                                                                        %s%s
          ##--- SUBDOMAIN RECON AND TAKEOVER,Information Gathering TOOL ---##
                # Coded By Rohit Kumar - @rohitcoder
    """ % (R, W, G))
banner() 
target = raw_input("Enter Target link witout http:// or https:// ")
base_file = "report/"+target;
log_file = "logs/"+target;
print(">Please wait fetching all subdomains using Sublist3r...")
subprocess.call("python sublist3r/sublist3r.py -v -d "+target+" -o "+log_file+".txt", shell=True)
print(">Subdomain fetched Succesfully...")
print(">Sepearting All Subdomains of 404,200,403,401 etc Response codes in different file...")
for line in fileinput.input([log_file+'.txt']):
     if not line.strip():
                continue
     else:
           link = 'http://'+line
           print(">Working with: " + link)
           # req = Request(link) 
           try:
               fetch = urllib2.urlopen(link, timeout=5)
               response = fetch.read().decode('utf-8')
               resp_code = fetch.getcode() 
               print("Response for "+link+" is "+str(resp_code))
               hs = open(base_file+"_200.txt","a+")
               hs.write(link + "\n")
               hs.close()
           except urllib2.URLError as e:
              print("Error")
           except socket.timeout as e:
              print("Error")