height = 500
width = 500
nx = 6
ny = 6
l = 60
s = 0

def setup():
    size(width, height)
    stroke(255)
    noFill()
    frameRate(1)
 
def draw():
    global s
    background(0)
    for i in range(ny):
        for k in range(nx): 
            x = ((k+1)*width/nx)-((width/nx)/2)
            y = ((i+1)*height/ny)-((height/ny)/2)
            if s == 0:
                line(x, y-(l/2), x, y+(l/2))
            if s == 1:
                rect(x-l/2, y-l/2, l, l)
            if s == 2:
                ellipse(x, y, l, l)
    s = (s + 1)%3
