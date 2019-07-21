from PIL import Image
def ChangePixels(im, col, col2, out="out.png", tolerance=10, save=True):
    newimdata = []
    blackcolor = col
    white=col2
    for color in tuple(im.getdata()):
        if sum(tuple(color)) in range(sum(blackcolor), sum(blackcolor)+tolerance) or sum(tuple(color)) in range(sum(blackcolor)-tolerance, sum(blackcolor)):
            newimdata.append(white)
        else:
            newimdata.append(tuple(color))
    newim = Image.new(im.mode,im.size)
    newim.putdata(tuple(newimdata))
    if save:
        try:
            newim.save(out)
            return True
        except Exception as ex:
            print(ex)
            return False
    else:
        return newim
def ChangeTransparency(im, col, out="out.png", transparency=255, tolerance=10, save=True):
    newimdata = []
    blackcolor = col
    for color in tuple(im.getdata()):
        if sum(tuple(color)) in range(sum(blackcolor), sum(blackcolor)+tolerance) or sum(tuple(color)) in range(sum(blackcolor)-tolerance, sum(blackcolor)):
            newimdata.append((255,255,255,transparency))
        else:
            newimdata.append(tuple(color))
    newim = Image.new(im.mode,im.size)
    newim.putdata(tuple(newimdata))
    if save:
        try:
            newim.save(out)
            return True
        except Exception as ex:
            print(ex)
            return False
    else:
        return newim
