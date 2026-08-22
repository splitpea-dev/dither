import sys
from PIL import Image


def create_map(d):
        # build matrix based on dimension (2 x 2, 4 x 4, or 8 x 8)
        if d == 2:
                m = [0, 2, 3, 1]
        elif d == 4:
                m = [0, 8, 2, 10, 12, 4, 14, 6, 3, 11, 1, 9, 15, 7, 13, 5]
        else:
                m = [0, 32, 8, 40, 2, 34, 10, 42, 48, 16, 56, 24, 50, 18, 58, 26, 12, 44, 4, 36, 14, 46, 6, 38, 60, 28, 52, 20, 62, 30, 54, 22, 3, 35, 11, 43, 1, 33, 9, 41, 51, 19, 59, 27, 49, 17, 57, 25, 15, 47, 7, 39, 13, 45, 5, 37, 63, 31, 55, 23, 61, 29, 53, 21]

        # apply threshold formula to values
        for x in range(len(m)):
                m[x] = (m[x] + 1) / (d ** 2)
                m[x] = (m[x] - 0.5)
    
        return m


def get_matrix_index(x, y, dim):
        r = y % dim
        c = x % dim
        return ((r * dim) + c)


dimension = 0
inset = {4, 16, 64}

# try to open image file from argument 1
if len(sys.argv) > 1:
        try:
                im = Image.open(sys.argv[1]).convert("L")
        except FileNotFoundError:
                print("The input file does not exist or is invalid.")
                exit()

# try to parse level of dither
if len(sys.argv) > 2:
        z = int(sys.argv[2])
        if z in inset:
                if z == 4:
                        dimension = 2
                elif z == 16:
                        dimension = 4
                else:
                        dimension = 8
        else:
                print("Valid args are: 4, 16, and 64. Default to 64.")
                z = 64
                dimension = 8

# create output file name
outname = sys.argv[1].split('.')[0] + '_dither_' + str(z) + ".png"

# prepare matrix
matrix = create_map(dimension)

# set up output image
om = Image.new("L", (im.width, im.height), 0)

# convert image
rr = 255
for y in range(im.height):
        for x in range(im.width):
                p = im.getpixel((x, y))
                m = matrix[get_matrix_index(x, y, dimension)]
                cp = float(p) + rr * m

                if (cp < 128.0):
                        # dark pixel
                        om.putpixel((x, y), 0)
                else:
                        # light pixel
                        om.putpixel((x, y), 255)

# clean-up
om.save(outname)
om.close()
im.close()