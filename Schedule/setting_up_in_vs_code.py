# https://stackoverflow.com/questions/73527596/how-to-execute-the-whole-current-file-in-the-vscode-python-repl

"""
1. This is the nicest option with interactive
   window on the side
   -- Good if you have horizontal space

Add #%% to start a side by side
jupyter like interface

You can click

Run cell

Or right click on the editor
and select Run in Interactive Window

Or create a keyboard shortcut
Click on the Gear (bottom left)
And select Keyboard Shortcuts
Look for Run Current File in Interactive Window
C-K C-Enter

By default the following already work
(in Jupyter like cells):
C-Enter - Run Current Cell
S-Enter - Run Current Cell and Advance

"""

#%%
x = np.arange(1,11)
print(x)

# %%
hello = 1

# %%
np.arange(1,11)

# %%
import numpy as np
np.arange(1,21)