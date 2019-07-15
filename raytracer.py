from PIL import Image, ImageDraw
from Sphere import Sphere
import numpy as np

imgx = 300
imgy = 300

img = Image.new('RGB', (imgx, imgy), color = 'black')
pixelMap = img.load()

#Place a Sphere in centre, distance 10 away.
sphere1 = Sphere(np.array([0,0,-20]), (255, 255, 255), 10)
sphere2 = Sphere(np.array([1,1,-20]), (255, 0, 0), 10)
#sphere1 (x-0)^2 + (y-0)^2 + (z+10)^2 - 25 = 0
#		 ()
objects = [sphere1, sphere2]

for i in range(img.size[0]):
	for j in range(img.size[1]):

		u = -imgx/2 + (imgx)*(i+0.5)/imgx
		v = -imgy/2 + (imgy)*(j+0.5)/imgy

		ndcx = (i+0.5)/imgx
		ndcy = (j+0.5)/imgy

		psx = 2 * ndcx - 1
		psy = 1- 2 * ndcy

		rayDirection = -1*np.array([0,0,1]) + psx*np.array([1,0,0]) + psy*np.array([0,1,0])
		#print(rayDirection)
		rayOrigin = np.array([0,0,0])
		#p(t) = rayorigin + t*raydirect
		
		#Sphere intersection
		for obj in objects:		
			a = np.dot(rayDirection, rayDirection)
			b = np.dot(2*rayDirection, (rayOrigin - obj.centre))
			c = np.dot((rayOrigin - obj.centre), (rayOrigin - obj.centre)) - obj.radius**2

			eminc = rayOrigin - obj.centre

			discrim = (np.dot(rayDirection, eminc))**2 - ((np.dot(rayDirection, rayDirection))*(np.dot(eminc, eminc))-obj.radius**2)
			if(discrim >= 0):
				print("intersect")
				pixelMap[i,j] = obj.colour

img.save('output.png')

	