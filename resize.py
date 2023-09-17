#resize input image to height 512 and width 1024.

from PIL import Image

input_image_path = 'static\IMG_20230509_113401_00_359_seg.png'
output_image_path = 'static\IMG_20230509_113401_00_359_seg_resized.png'  # Replace with the desired output file path

# Open the input image
input_image = Image.open(input_image_path)

# Resize the image to the desired dimensions (width x height)
new_width = 1024
new_height = 512
resized_image = input_image.resize((new_width, new_height), Image.ANTIALIAS)

# Save the resized image
resized_image.save(output_image_path)

# Close the input and resized images
input_image.close()
resized_image.close()

print(f"Image resized and saved to {output_image_path}")
