import argparse
import winreg

PATH = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{}\PropertyBag"

# The first part is to get this to work on 32bit Python and 64bit Windows.
# The second is just so we can do whatever we want to the key.
ACCESS_TYPES = winreg.KEY_WOW64_64KEY + winreg.KEY_ALL_ACCESS

# Keys pointing to all the folders under This PC on:
# Windows 10 version 1607, OS Build 14393.576 on December 30, 2016
FOLDER_KEYS = {
    "documents": "{f42ee2d3-909f-4907-8871-4c22fc0bf756}",
    "pictures":  "{0ddd015d-b06c-45d5-8c4c-f59713854639}",
    "videos":    "{35286a68-3c57-41a1-bbb1-0eae73d76c95}",
    "downloads": "{7d83ee9b-2244-4e70-b1f5-5393042af1e4}",
    "music":     "{a0c69a99-21c8-4671-8703-7934162fcf1d}",
    "desktop":   "{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}"
}

def set_this_pc_policy(key, value):
    winreg.SetValueEx(key, "ThisPCPolicy", 0, winreg.REG_SZ, value)

def open_key(key):
    return winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, PATH.format(key), 0,
        ACCESS_TYPES)

def set_folder_visibility(key, isShown):
    if isShown:
        set_this_pc_policy(key, "Show")
    else:
        set_this_pc_policy(key, "Hide")

def show_folders(isShown):
    for folder_key in FOLDER_KEYS.values():
        with open_key(folder_key) as key:
            set_folder_visibility(key, isShown)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("visibility", type=str, default="Hide",
        choices=["show", "hide"])

    args = parser.parse_args()

    if args.visibility == "show":
        print("Showing folders under This PC")
        show_folders(True)
    elif args.visibility == "hide":
        print("Hiding folders under This PC")
        show_folders(False)
