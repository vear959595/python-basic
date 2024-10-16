from pathlib import Path

practice_files = Path.home() / "practice_files"
practice_files.mkdir(exist_ok=True)

images = practice_files / "images"
images.mkdir(exist_ok=True)

documents = practice_files / "documents"
documents.mkdir(exist_ok=True)

paths = [documents / "image1.png", documents / "image2.gif", documents / "image3.png", documents / "image4.jpg"]

for path in paths:
    path.touch()

for find_word in documents.rglob("*.*"):
        if find_word.suffix.lower() in  [".png", ".jpg", ".gif"]:
            find_word.replace(images/ find_word.name)
