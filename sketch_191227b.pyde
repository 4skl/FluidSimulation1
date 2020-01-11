add_library('peasycam')
class Sphere:
    def __init__  (self, coords):
        self.originalCoords = coords
        self.coords = coords
    def next(self):
        self.compare()
        self.update(5,[])
        return self.coords
    def compare(self):
        nextcoords = [self.coords[0] ,self.coords[1]+9 ,self.coords[2]]
        self.todonextcompare = {'coords': nextcoords}
                    
    def update(self,time,objectList):
        #if self.todonextcompâre  
        self.coords = self.todonextcompare['coords']
    def reset(self):
        self.coords = self.originalCoords

def init(lo,La,ha,ra):
    grid = []
    
    for i in range(lo):
        for j in range(La):
            for k in range(ha):
                grid.append(Sphere([i*20,j*20,k*20]))
             
    return grid




r = 10
l = 3
L = 3
h = 3

focusCam  = [20,20,20]
pos = [100,100,100]
objects  = init(l,L,h,r)

def setup():
    size(400,400,P3D)
    cam = PeasyCam(this, 100)
    cam.setMinimumDistance(50)
    cam.setMaximumDistance(500)
    
def draw():
    clear()
    for object in objects:
        
        pushMatrix()
        noStroke()
        lights()
        
        translate(object.coords[0], object.coords[1], object.coords[2])
        
        sphere(r)
        popMatrix()        
    #camera(pos[0], pos[1],pos[2], focusCam[0], focusCam[1], focusCam[2], 1.0, 0.0, 0.0)
    #
    if keyPressed:
        """
        if key=='z':
            pos[0] += (focusCam[0]-pos[0])*0.01
            pos[1] += (focusCam[1]-pos[1])*0.01
            pos[2] += (focusCam[2]-pos[2])*0.01
        if key=='s':
            pos[0] -= (focusCam[0]-pos[0])*0.01
            pos[1] -= (focusCam[1]-pos[1])*0.01
            pos[2] -= (focusCam[2]-pos[2])*0.01
        if key=='q':
            pos[0] -= PI
        if key=='d':
            pos[0] += PI
        if key=='a':
            focusCam[2] -= PI
        if key=='e':
            focusCam[2] += PI
        """
        if key=='b':
            for object in objects:
                object.next()
        if key=='r':
            for object in objects:
                object.reset()
            """
            focusCam[0] = 20
            focusCam[1] = 20
            focusCam[2] = 20
            pos[0] = 100
            pos[1] = 100
            pos[2] = 100
            """
