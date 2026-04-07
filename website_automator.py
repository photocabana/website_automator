#Imports the sys module, which gives access to command-line arguments and system functions like exiting the script.

# Imports the webbrowser module, which lets Python control and open URLs in your default browser.  -  to import a updated pip [pip install webbrowser] C:\Users\rinnn\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip

import sys
import webbrowser


# Defines a dictionary called URLS with two named sets of links — "work" and "personal". Each key maps to a list of URLs you want opened together. - These are the URLs that will be used in the script

URLS = {
    "work": ["https://www.github.com", "https://www.google.com"],
    "personal": ["https://www.facebook.com", "https://www.spotify.com", "https://www.youtube.com"]
}


# Defines a function that takes a list of URLs and loops through each one, opening it in a new browser tab.

def open_webpages(urls):
    for url in urls:
        webbrowser.open_new_tab(url)


# This is a Python convention — the code inside only runs if you execute this file directly (not if it's imported as a module by another script).

if __name__ == "__main__":
    
    # Checks two things: (1) that exactly one argument was passed when running the script (the script name itself is always sys.argv[0], so len == 2 means one extra argument), and (2) that the argument matches a key in URLS. If either check fails, it shows usage instructions.
    
    if len(sys.argv) != 2 or sys.argv[1] not in URLS:
        print("Usage: python script.py <set_name>")
        print("Available sets:")
        for set_name in URLS.keys():
            print(f"- {set_name}")
        sys.exit(1)

    set_name = sys.argv[1]
    urls = URLS[set_name]
    open_webpages(urls)
