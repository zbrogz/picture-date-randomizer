import os
import random
from datetime import datetime, timedelta
import piexif

picturesDir = "your/file/path"


now = datetime.now()

count = 0
filenames = os.listdir(picturesDir)
random.shuffle(filenames)
for filename in filenames:
    filePath = os.path.join(picturesDir, filename)
    timestamp = now + timedelta(seconds=count)
    exif_dict = piexif.load(filePath)
    new_date = timestamp.strftime("%Y:%m:%d %H:%M:%S")
    exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
    exif_bytes = piexif.dump(exif_dict)
    piexif.remove(filePath)
    piexif.insert(exif_bytes, filePath)
    count += 1

print(count, "files updated")
