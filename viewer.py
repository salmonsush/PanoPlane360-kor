# viewer which view png and exr file.
# display picture or display the data of each pixel on terminal.
import os
os.environ["OPENCV_IO_ENABLE_OPENEXR"]="1"
import sys
import cv2
import pyexr

def display_image(image_path):
    image = cv2.imread(image_path)
    cv2.imshow("Image Viewer", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def display_exr_pixel_data(exr_path):
    exr_data = pyexr.open(exr_path)
    header = exr_data.header()

    print(f"Image Size: {header['dataWindow'].width()} x {header['dataWindow'].height()}")
    channels = header['channels'].keys()
    
    for channel in channels:
        pixel_data = exr_data.get(channel)
        print(f"Channel: {channel}")
        for y in range(header['dataWindow'].height()):
            for x in range(header['dataWindow'].width()):
                pixel_value = pixel_data[y][x]
                print(f"Pixel ({x}, {y}): {pixel_value}")
    
def main():
    if len(sys.argv) != 3:
        print("Usage: python image_viewer.py <image/exr_path> <mode>")
        print("Mode: image or data")
        sys.exit(1)

    image_path = sys.argv[1]
    mode = sys.argv[2]

    if mode == "image":
        display_image(image_path)
    elif mode == "data":
        if image_path.endswith(".exr"):
            display_exr_pixel_data(image_path)
        else:
            print("Data mode is only supported for .exr files.")
    else:
        print("Invalid mode. Use 'image' or 'data'.")

if __name__ == "__main__":
    main()
