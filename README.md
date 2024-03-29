# PixelMenu
A python project that processes pixels from a frame and then edits it

# Functions

### 1) ChangePixels(im, col, col2, out="out.png", tolerance=10, save=True):


Replace pixels having a **RGB** value of **col** with pixels having a **RGB** value of **col2**

`im` - PIL image instance

`col`- A tuple which contains the RGB values of the pixels that are to be edited

`col2` - A tuple with RGB values of a pixel that would be replacing the originial pixels

`out` - Output File Location

`tolerance` - An int value that decides how many variations of the selected color should be replaced

`save` - If set to **True**, image will automatically save and return **True** if save was successful. Setting the value to **False** would return the PIL image instance of the edited image.

# Practical Usage

Changing information from frames and re-rendering them

### 1) Extracting Frames from original clip

![](input.gif)

### 2) Processing Frames

Process frames and then edit them

### 3) Rendering the edited frames

![](output.gif)

#### The above example was made with just 10 lines of code and took less than a few seconds to render.

