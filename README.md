# Dither

This small program creates a black and white copy of an input image using Bayer dithering.

Use:

```python dither.py [input_image_filename] [matrix_size]```

Where ```[input_image_filename]``` is the actual filename of the image you are importing and ```[matrix_size]``` is a numerical value for the size of the matrix used.

The matrix size can either be ```4```, ```16```, or ```64```. Any other value (or no value) will default to ```64```.

Example:

```python dither.py coffee_512x512.png 64```

Input image (```coffee_512x512.png```):

![A colorful image of a turtle enjoying a hot cup of coffee.](./coffee_512x512.png)

Output image (```coffee_512x512_dither_64.png```):

![A black and white dithered version of the original input image of a turtle enjoying a hot cup of coffee.](./coffee_512x512_dither_64.png)
