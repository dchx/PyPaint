from utils import *
from fill_color import fill_color
imgname = 'example.png'

# create image
img = np.ones([5, 5, 3]) # create a 5x5 white image
coor_tocolor = [[2, 2], [1, 2], [3, 2], [2, 1], [2, 3], [1, 3]]
for coor in coor_tocolor: img[coor[0], coor[1]] = [0., 0., 0.]
mpimg.imsave(imgname, img); print('Saved: %s'%imgname)
plt.imshow(img); plt.show() # show image

# read image
img = mpimg.imread(imgname)
# show image, pick a coordinate
plt.imshow(img); plt.show()

# fill color
coor = [2, 2]
tofill = img[2, 2] * 0.5
img_fill = fill_color(img, coor, tofill)
plt.imshow(img_fill); plt.show()
