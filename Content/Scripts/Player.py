from src.GameObjects.Player.FirstPersonPlayer import FirstPersonPlayer
from Content.Scripts.Massball import Massball
from panda3d.core import Vec3
from src.functionDecorators import tryFunc

class Player(FirstPersonPlayer):
    @tryFunc
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed = 25
        self.jumpForce = 5
        self.shooted = False
        self.massballs = []
        self.maxBalls = 0
    
    @tryFunc
    def update(self, task):
        super().update(task)
        
        self.shooting()
        self.deactivateMassballs()
        
        return task.cont
    
    @tryFunc
    def shooting(self):
        if "mouse1" in self.app.keys and len(self.massballs) < self.maxBalls:
            if self.shooted == False:
                pos = self.node.getPos()
                rot = self.node.getHpr()
                self.massballs.append(Massball(self.app.render.getRelativeVector(self.app.camera, Vec3(0, 1, 0)),
                                               self.app,
                                               x=pos.x,
                                               y=pos.y,
                                               z=pos.z+3,
                                               rx=rot.x,
                                               ry=rot.y,
                                               rz=rot.z,
                                               name="Massball" + str(len(self.massballs) + 1),
                                               ))
                self.shooted = True
        else:
            self.shooted = False
    
    @tryFunc
    def deactivateMassballs(self):
        if "mouse3" in self.app.keys:
            m = self.massballs.copy()
            for ball in self.massballs:
                ball.destroy()
                m.remove(ball)
            self.massballs = m
                
