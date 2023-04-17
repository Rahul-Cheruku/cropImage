from PIL import Image


# user input
imgURL = "C:/Users/rahul/Desktop/Pravaig Acceleration/portfolio/happy tailor services.png"

ratio='2X3'.split('X')


imgFolder = imgURL.split('/')
imgName=imgFolder[-1].split('.')[0]
imgExt=imgFolder[-1].split('.')[1]
del imgFolder[-1]
imgFolder = '/'.join(imgFolder)

# Load the original image
img = Image.open(imgURL)

# Get the width and height of the original image
width, height = img.size

# Calculate the desired height of the cropped images
crop_height = width * (int(ratio[1])//int(ratio[0]))

# Loop through the image vertically and crop it into 900x1600 images
for i in range(0, height, crop_height):
    # Calculate the y-coordinates of the crop
    top = i
    bottom = min(i + crop_height, height)

    # Crop the image
    cropped_img = img.crop((0, top, width, bottom))

    # Save the cropped image
    cropped_img.save(f'{imgFolder+"/"+imgName+str(i)+"."+imgExt}')



