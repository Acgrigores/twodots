from PIL import Image, ImageDraw
import random
import math

IMAGES = []
NUM_POINTS = 10
image = Image.open("map.jpg")
WIDTH, HEIGHT = image.size
WORKING_POINTS = []
CORRESPONDING_COLORS = []
PREV_POINTS = []
WEIGHT = 1

def display():
    image = Image.open("map.jpg")
    draw = ImageDraw.Draw(image)
    for i in range(NUM_POINTS):
        draw.circle(WORKING_POINTS[i], radius=10, fill=CORRESPONDING_COLORS[i])
        draw.line([WORKING_POINTS[i], PREV_POINTS[i]], fill = CORRESPONDING_COLORS[i])
    image.save("image_with_dot.jpg")
    IMAGES.append(image)

def displayFirst():
    image = Image.open("map.jpg")
    draw = ImageDraw.Draw(image)
    for i in range(NUM_POINTS):
        draw.circle(WORKING_POINTS[i], radius=10, fill=CORRESPONDING_COLORS[i])
    image.save("image_with_dot.jpg")
    IMAGES.append(image)

def closeness(points):
    total = 0
    for i in range(NUM_POINTS):
        for j in range(i + 1, NUM_POINTS):
            dist = math.dist(points[i], points[j])
            total += dist
    return total

def add(original, toAdd):
    x = original[0] + toAdd[0] - HEIGHT * math.floor((original[0] + toAdd[0])/HEIGHT)
    y = original[1] + toAdd[1] - HEIGHT * math.floor((original[1] + toAdd[1])/HEIGHT)
    return (x, y)

def randX():
    return random.randint(-WIDTH, WIDTH) * WEIGHT
def randY():
    return random.randint(-HEIGHT, HEIGHT) * WEIGHT

def defineWorkingPoints():
    for point in range(NUM_POINTS):
        P1 = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        WORKING_POINTS.append(P1)
        r = random.randint(0, 150)
        g = random.randint(0, 150)
        b = random.randint(0, 150)
        CORRESPONDING_COLORS.append((r, g, b))
def copyWorkingToPrev():
    global PREV_POINTS
    PREV_POINTS = []
    for i in range(NUM_POINTS):
        PREV_POINTS.append(WORKING_POINTS[i])

defineWorkingPoints()
copyWorkingToPrev()
displayFirst()
while closeness(WORKING_POINTS) > 350 * NUM_POINTS:
    closest = closeness(WORKING_POINTS)
    attempt_points = []
    for i in range(NUM_POINTS):
        attempt_points.append(add(WORKING_POINTS[i], (randX(), randY())))
    if(closeness(attempt_points) < closest):
        WORKING_POINTS = attempt_points.copy()
        copyWorkingToPrev()
        display()
    WEIGHT = max(WEIGHT * 0.97, 0.05)
IMAGES[0].save('map.gif', save_all=True, append_images=IMAGES[1:], duration=100, loop=0)