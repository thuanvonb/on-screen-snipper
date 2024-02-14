## On-screen Snipper

Getting tired of switching back and forth between windows to retrieve information? This tool can help you!
This is a simple Python program you can use to capture important information and keep it on-screen for instant access.

### Installation
1. Clone the repository using `git clone https://github.com/thuanvonb/on-screen-snipper.git`.
2. Install required libraries `pip install -r requirements.txt`.

### How to use
- Launch the program using `python main.py` and wait for the message `App started` appears.
- To capture screenshot, use hotkey `Ctrl + Alt + Z`.
- A screenshot will be spawned on the capture position and can be moved around freely using LMB.
- To destroy a screenshot, press-and-release RMB.
- You can also use hotkey `Ctrl + Alt + D` to destroy all screenshots.
- There is no UI, in order to quit the program, use `Ctrl + Alt + Q`.
- Feel free to modify the hotkeys in the file `main.py` at line 15-17 if you need.

### Future works
- Static capturing: Right now, when screenshot mode is activated, what happening on the screen is continued as it is. It may be a feature or bug, but static capturing should also be possible
- User interface: Create a user interface instead of only hotkeys with some interesting things but currently I cannot think of any.
- Resizable screeshot: Maybe useful?
