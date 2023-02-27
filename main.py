from PIL import Image
import os
import config

# set the directory containing the images you want to resize
input_dir = config.input_directory

# set the directory where you want to save the resized images
output_dir = config.output_directory

# set the percentage by which you want to reduce the size of the images
percent_reduce = 50

# loop through all files in the input directory
for filename in os.listdir(input_dir):
    # check if the file is an image
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # open the image using PIL
        image = Image.open(os.path.join(input_dir, filename))
        # get the original size of the image
        original_size = image.size
        # calculate the new size of the image based on the percentage reduction
        new_size = (int(original_size[0] * percent_reduce / 100), int(original_size[1] * percent_reduce / 100))
        # resize the image
        resized_image = image.resize(new_size)
        # save the resized image to the output directory
        resized_image.save(os.path.join(output_dir, filename))
        # remove the original image from the input directory
        os.remove(os.path.join(input_dir, filename))
