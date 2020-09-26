from utils import *

def within_img(img, coor):
	'''
	check if coor (y, x) is within img
	'''
	edge = img.shape[:2]
	for axis in [0, 1]:
		if coor[axis] < 0 or coor[axis] >= edge[axis]: return False
	return True

def neighbors(coor):
	out = []
	out.append([coor[0] - 1, coor[1]])
	out.append([coor[0] + 1, coor[1]])
	out.append([coor[0], coor[1] - 1])
	out.append([coor[0], coor[1] + 1])
	return out

def fill_color(img, coor, tofill, visited=None):
	'''
	apply paint bucket for img at pixel coor
	search for neighbor pixels with same color and replace with color
	coor - [y, x] coordinate to apply paint bucket
	tofill - a color, should to the same shape as img[0, 0].shape
	'''
	if type(visited)==type(None):
		first_iter = True
		img = img.copy()
		visited = np.zeros(img.shape[:2], dtype=bool)
	else: first_iter = False
	visited[coor[0], coor[1]] = True
	color = img[coor[0], coor[1]].copy()
	img[coor[0], coor[1]] = tofill
	for nbr in neighbors(coor):
		if within_img(img, nbr) and not visited[nbr[0], nbr[1]] and np.all(img[nbr[0], nbr[1]]==color):
			fill_color(img, nbr, tofill, visited)
	if first_iter: return img
