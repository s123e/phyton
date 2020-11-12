height = 500
width = 500
nx = 6
ny = 6
l = 60
slide = 0

def setup():
    size(width, height)
    stroke(0, 102, 0) #цвет рамки
    fill(0, 102, 0)   #цвет закраски 
    frameRate(5) #скорость прокрутки
 
def draw():
    global slide
    background(0)
    for i in range(ny):
        for k in range(nx): 
            x = ((k+1)*width/nx)-((width/nx)/2)
            y = ((i+1)*height/ny)-((height/ny)/2)
            if slide == 0:
                line(x, y-(l/2), x, y+(l/2))
            if slide == 1:
                rect(x-l/2, y-l/2, l, l)
            if slide == 2:
                ellipse(x, y, l, l)
                #triangle(x-2, y-2, 100+x, 20+y, 40+x, 90+y)
    slide = (slide + 1)%3
