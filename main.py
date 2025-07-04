from PIL import Image, ImageDraw
import random
import math

def display(pointOne, pointTwo, pastPointOne, pastPointTwo):
    image = Image.open("map.jpg")
    draw = ImageDraw.Draw(image)
    draw.circle(pointOne, radius=10, fill="purple")
    draw.circle(pointTwo, radius=10, fill="blue")
    draw.line([pastPointOne, pointOne], fill = "purple")
    draw.line([pastPointTwo, pointTwo], fill = "blue")
    image.save("image_with_dot.jpg")
    IMAGES.append(image)

def displayFirst(pointOne, pointTwo):
    image = Image.open("map.jpg")
    draw = ImageDraw.Draw(image)
    draw.circle(pointOne, radius=10, fill="purple")
    draw.circle(pointTwo, radius=10, fill="blue")
    image.save("image_with_dot.jpg")
    IMAGES.append(image)

def closeness(pointOne, pointTwo):
    x1, y1 = pointOne
    x2, y2 = pointTwo
    xDiff = min(abs(x1 - x2), abs(WIDTH - x1 + x2), abs(WIDTH - x2 + x1))
    yDiff = min(abs(y1 - y2), abs(HEIGHT - y1 + y2), abs(HEIGHT - y2 + y1))
    return xDiff**2+yDiff**2

def add(original, toAdd):
    x = original[0] + toAdd[0] - HEIGHT * math.floor((original[0] + toAdd[0])/HEIGHT)
    y = original[1] + toAdd[1] - HEIGHT * math.floor((original[1] + toAdd[1])/HEIGHT)
    return (x, y)

def randX():
    return random.randint(-WIDTH, WIDTH) * WEIGHT
def randY():
    return random.randint(-HEIGHT, HEIGHT) * WEIGHT

image = Image.open("map.jpg")
IMAGES = []
WIDTH, HEIGHT = image.size
P1 = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
P2 = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
prev1 = P1
prev2 = P2
displayFirst(P1, P2)
WEIGHT = 1
for i in range(300):
    closest = closeness(P1, P2)
    attempt_p1 = add((P1), (randX(), randY()))
    attempt_p2 = add((P2), (randX(), randY()))
    if(closeness(attempt_p1, attempt_p2) < closest):
        display(attempt_p1, attempt_p2, P1, P2)
        P1 = attempt_p1
        P2 = attempt_p2
    WEIGHT = WEIGHT * 0.97
IMAGES[0].save('map.gif', save_all=True, append_images=IMAGES[1:], duration=300, loop=0)