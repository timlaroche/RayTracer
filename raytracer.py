from PIL import Image, ImageDraw
from Camera import Camera
from Sphere import Sphere
import numpy as np

cam = Camera(0,0,0)
imgx = 1280
imgy = 720

img = Image.new('RGB', (imgx, imgy), color = 'black')
pixelMap = img.load()

#Place a Sphere in centre, distance 10 away.
sphere1 = Sphere(np.array([0,0,-1]), (255, 255, 255), 100)
#sphere1 (x-0)^2 + (y-0)^2 + (z+10)^2 - 25 = 0
#		 ()

for i in range(img.size[0]):
	for j in range(img.size[1]):

		u = -imgx/2 + (imgx)*(i+0.5)/imgx
		v = -imgy/2 + (imgy)*(j+0.5)/imgy


		rayDirection = -1*np.array([0,0,1]) + u*np.array([1,0,0]) + v*np.array([0,1,0])
		rayOrigin = np.array([0,0,0])
		#p(t) = rayorigin + t*raydirect
		
		#Sphere intersection
		a = np.dot(rayDirection, rayDirection)
		b = np.dot(2*rayDirection, (rayOrigin - sphere1.centre))
		c = np.dot((rayOrigin - sphere1.centre), (rayOrigin - sphere1.centre)) - sphere1.radius**2

		eminc = rayOrigin - sphere1.centre

		discrim = (np.dot(rayDirection, eminc))**2 - ((np.dot(rayDirection, rayDirection))*(np.dot(eminc, eminc))-sphere1.radius**2)
		if(discrim >= 0):
			print("intersect")
			pixelMap[i,j] = sphere1.colour
		else:
			pixelMap[i,j] = (0, 0,0)

img.save('output.png')

	