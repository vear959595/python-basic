from pathlib import Path
import shutil

#Exercise 1

myfolder = Path.home() / "my_folder"

myfolder.mkdir(exist_ok=True)

#Exercise 2
file1 = myfolder / "file1.txt"
file2 = myfolder / "file2.txt"
image = myfolder / "image.png"

file1.touch()
file2.touch()
image.touch()

# Exercise 3

images = myfolder / "images"
images.mkdir(exist_ok=True)

image_dest = images/ "image.png"

image.replace(image_dest)

#Exercise 4

file1.unlink()

#Exercise 5

shutil.rmtree(myfolder)
