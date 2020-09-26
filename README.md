## Python paint tools

I'm too poor to have Photoshop.  
I don't have Microsoft Paint on my Mac.  
I can't fill colors with Preview.

So, I use Python to paint.

### Tools
* The paint bucket tool  
  Change colors for connected pixels with the same color.  
  `fill_color(img, coor, tofill)`  
  - Arguments  
  `img` - array like, the image data, shape: (ny, nx, nchanel)  
  `coor` - the coordinate (y, x) to put the paint bucket on  
  `tofill` - the color of the paint bucket, should to the same shape as img[0, 0].shape  
  - Returns  
  Array like, the new image after applying the paint bucket
