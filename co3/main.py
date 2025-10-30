from graphics import rectangle,circle
from graphics.threeDgraphics import cuboid, sphere

print("Rectangle Area:", rectangle.area(10,5))
print("Rectangle Perimeter:", rectangle.perimeter(10,5))

print("Circle Area:", circle.area(7))
print("Circle Perimeter:", circle.perimeter(7))

print("Cuboid Surface Area:", cuboid.surface_area(2, 3, 4))
print("Cuboid Perimeter:", cuboid.perimeter(2, 3, 4))

print("Sphere Surface Area:", sphere.surface_area(5))
print("Sphere Volume:", sphere.volume(5))
