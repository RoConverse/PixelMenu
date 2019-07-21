# PixelMenu
A python project that processes pixels from a frame and then edits it

#Functions
####ChangePixels(im, col, col2, out, tolerance):
Replace pixels having a **RGB** value of **col** with pixels having a **RGB** value of **col2**
`im` - PIL image instance

`col`- A tuple which contains the RGB values of the pixels that are to be edited

`col2` - A tuple with RGB values of a pixel that would be replacing the originial pixels

`out` - Output File Location

`tolerance` - An int value that decides how many variations of **col** should be replaced
