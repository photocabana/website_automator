# to import a updated pip [pip install webbrowser] C:\Users\rinnn\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip

import sys
import webbrowser


# These are the URLs that will be used in the script
URLS = {
    "work": ["https://www.github.com", "https://www.google.com"],
    "personal": ["https://www.facebook.com", "https://www.spotify.com", "https://www.youtube.com"]
}


def open_webpages(urls):
    for url in urls:
        webbrowser.open_new_tab(url)


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in URLS:
        print("Usage: python script.py <set_name>")
        print("Available sets:")
        for set_name in URLS.keys():
            print(f"- {set_name}")
        sys.exit(1)

    set_name = sys.argv[1]
    urls = URLS[set_name]
    open_webpages(urls)
