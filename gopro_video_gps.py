import os
import glob


fp = r"C:\Users\yaorui\Pictures\iCloud Photos\Photos"
fp1 = r"C:\Users\yaorui\Downloads\temp1"
fp2 = r"C:\Users\yaorui\Downloads\temp2"
os.chdir(fp2)


# os.popen(f"copy \"{fp1}\\*\" \"{fp2}\\*\"").readlines()

fns = glob.glob("*.MP4")
# fn = "GX010021.MP4"

for fn in fns:
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
