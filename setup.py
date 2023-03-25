import os, math, sys

# installing dependencies for firefox
os.system("sudo apt-get install python3-pip && sudo apt-get install tor")
os.system("pip install -U selenium")
os.system("pip install Pysocks")
os.system("pip install pyvirtualdisplay && apt-get install xvfb")

#printing the core values of the OS
import platform
OS_bit = int(platform.architecture()[0][:2])

# get firefox version
try:
    os.system('firefox -v > /tmp/firefox_version.txt')
    with open('/tmp/firefox_version.txt', 'r') as f:
        result = f.read()
    os.remove('/tmp/firefox_version.txt')
    marker = result.find('Firefox') + 8
    version = result[marker:].split()[0]
    a,b,c = version.split(".")
    FirefoxVersion = int(a)
except:
    print("Error getting Firefox version")
    sys.exit(1)

# set geckodriver version based on firefox version
if FirefoxVersion < 102:
    first = 0
    second = 24
    OS_bit = 64
elif FirefoxVersion == 102:
    first = 8
    second = 0
    OS_bit = 64
elif FirefoxVersion > 102:
    first = 9
    second = 0

# fetch and install geckodriver
os.system("sudo wget https://github.com/mozilla/geckodriver/releases/download/v0.32.2/geckodriver-v0.32.2-linux64.tar.gz".format(OS_bit))
os.system("sudo tar -xvzf geckodriver-v0.32.2-linux64.tar.gz".format(OS_bit))
os.system("sudo rm geckodriver-v0.32.2-linux64.tar.gz")
os.system("sudo chmod +x geckodriver")
os.system("sudo mv geckodriver /usr/local/bin/")
os.system("sudo chmod +x faitagram && chmod +x setup.py")
