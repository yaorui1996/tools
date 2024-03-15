import os
import glob


os.chdir(r"C:\Users\yaorui\Downloads\temp2")

videos = glob.glob("*.MP4")
images = glob.glob("*.JPG")

for fn in images:
    print(fn, end='\t')
    name = ''
    res = os.popen(f"exiftool -b -m -ImageDescription {fn}").readlines()
    if len(res) > 0:
        name = res[0].replace("DCIM\\100GOPRO\\","")
        os.popen(f"rename {fn} {name}").readlines()
    print(name)

for fn in videos:
    print(fn, end='\t')
    model = ''
    gps = ''
    res = os.popen(f"exiftool -b -m -GoPro:Model {fn}").readlines()
    if len(res) > 0:
        model = res[0]
        os.popen(f"exiftool -n -m -P -overwrite_original_in_place -Keys:Model=\"{model}\" {fn}").readlines()
    res = os.popen(f"exiftool -b -m -UserData:GPSCoordinates {fn}").readlines()
    if len(res) > 0:
        gps = res[0]
        os.popen(f"exiftool -n -m -P -overwrite_original_in_place -Keys:GPSCoordinates=\"{gps}\" {fn}").readlines()
    print(f"{model}\t{gps}")
