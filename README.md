# PixelMenu
A python project that processes pixels from a frame and then edits it

# Functions

### 1) ChangePixels(im, col, col2, out="out.png", tolerance=10, save=True):


Replace pixels having a **RGB** value of **col** with pixels having a **RGB** value of **col2**
`im` - PIL image instance

`col`- A tuple which contains the RGB values of the pixels that are to be edited

`col2` - A tuple with RGB values of a pixel that would be replacing the originial pixels

`out` - Output File Location

`tolerance` - An int value that decides how many variations of **col** should be replaced

`save` - If set to **True**, image will automatically save and return **True** if save was successful. Setting the value to **False** would return the PIL image instance of the edited image.

### 2) ChangeTransparency(im, col, out="out.png", transparency=255, tolerance=10, save=True):


Change transparency of pixels having an **RGB** value of col
`im` - PIL image instance

`col`- A tuple which contains the RGB values of the pixels that are to be edited

`out` - Output File Location

`tolerance` - An int value that decides how many variations of **col** should be edited

`transparency` - An int value that sets the transparency, **max** is 255(opaque), **minimum** is 0(transparent)

`save` - If set to **True**, image will automatically save and return **True** if save was successful. Setting the value to **False** would return the PIL image instance of the edited image.
