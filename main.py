import os
from PIL import Image
import glob

if not os.path.isdir(f"{os.getcwd()}\\Images"):
    os.mkdir(f"{os.getcwd()}\\Images")
    print("Images folder has been created, please put the images to be cropped in that folder and restart.\nPress any "
          "key to quit.")
    input()
    exit(-1)
listOfImages = glob.glob(f"{os.getcwd()}\\Images\\*.jpeg")
if not os.path.isdir(f"{os.getcwd()}\\Result"):
    os.mkdir(f"{os.getcwd()}\\Result")
i = 0
for imagePath in listOfImages:
    print(imagePath)
    image = Image.open(imagePath)
    croppedImage = image.crop((0, 0, 384, 640))
    croppedImage.save(f"Result\\image{i}.jpeg")
    i += 1
    print("Done")
print("Images have been cropped successfully and have been saved to the 'Results' folder in the program's "
      "directory.\nPress any key to quit.")
input()
exit(0)
