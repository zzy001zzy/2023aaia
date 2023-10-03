def setup(): 
    size(500,500)

def draw():
    background(0) 
    fill(255,92,15) 
    ellipse(255,255,80,80)

    a, a2 = frameCount/36.0,frameCount/36.0*365/88
    ellipse(250+200*cos(a), 250+200*sin(a),10,10)
    ellipse(250+79*cos(a2), 250+79*sin(a2),10,10)
    stroke(255)
    line(250+200*cos(a), 250+200*sin(a), 250+79*cos(a2), 250+79*sin(a2))
