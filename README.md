# This PC Folders

A Python script for hiding and showing the folders under "This PC" on Windows 10.

![An example of the script hiding and showing folders under This PC.](screenshots/usage-example.gif)

## Getting Started

Ensure you have Python 3+ installed.

You pass "hide" or "show" when running the script to set the visibility for the folders. Relaunch the Explorer after running the command for it to take effect.

```bash
$ python this_pc_folders.py hide
$ python this_pc_folders.py show
```

## Details

For this all to work, the script modifies the Windows registry. Each folder under "This PC" has a corresponding registry key with a `ThisPCPolicy` value.

Changing the value of this key between `Show` and `Hide` sets the visibility for the folders, and that is the extent of the registry modifications.

If you're concerned about something going wrong, open `regedit` and export `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions` before using this script.

## Caveats

This implementation is not guaranteed to work on your version of Windows. This script was tested and working on Windows 10 64bit, version 1607, OS Build 14393.576 and working as of December 30, 2016.

It should work on all versions of Windows 10, but could potentially break in future major releases.
