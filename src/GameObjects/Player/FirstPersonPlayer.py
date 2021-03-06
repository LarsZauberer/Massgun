from src.GameObjects.DynamicObject import DynamicObject
from panda3d.core import Vec3, BitMask32
from panda3d.bullet import BulletCapsuleShape, ZUp, BulletBoxShape
from panda3d.bullet import BulletCharacterControllerNode
from src.functionDecorators import tryFunc


class FirstPersonPlayer(DynamicObject):
    @tryFunc
    def __init__(self, app, x=-10, y=-10, z=5, rx=0, ry=0, rz=0, sx=1, sy=1, sz=1):
        # Character
        self.speed = 50
        self.jumpForce = 20
        self.preJumpSpeed = Vec3(0, 0, 0)

        super().__init__(app, name="Player", x=x, y=y, z=z, rx=rx, ry=ry, rz=rz, sx=sx, sy=sy, sz=sz, mass=1000, model="defaultMeshes/cube.bam")
        
        # Set Camera at rotation
        self.app.camera.setHpr(rx, ry, rz)
    
    @tryFunc
    def update(self, task):
        super().update(task)
        
        self.app.camera.setPos(self.node.getPos().x, self.node.getPos().y, self.node.getPos().z+3)
        self.node.setHpr(self.app.camera.getHpr().x, 0, 0)
        
        if self.app.mv.hasMouse():
            deltaX = self.app.mv.getMouseX()
            deltaY = round(self.app.mv.getMouseY(), 2)
            deltaX *= 10
            deltaY *= 10
            
            self.app.camera.setH(self.app.camera.getH() - deltaX)
            self.app.camera.setP(self.app.camera.getP() + deltaY)
            if self.app.camera.getP() > 90:
                self.app.camera.setP(90)
            if self.app.camera.getP() < -90:
                self.app.camera.setP(-90)
        
        # Normal Movement
        speed = Vec3(0, 0, 0)
        
        if "w" in self.app.keys:
            forward = self.app.render.getRelativeVector(self.app.camera, Vec3(0,1,0))
            forward.normalize()
            forward.z = 0
            speed += forward*self.speed
        if "s" in self.app.keys:
            forward = self.app.render.getRelativeVector(self.app.camera, Vec3(0,-1,0))
            forward.normalize()
            forward.z = 0
            speed += forward*self.speed
        if "d" in self.app.keys:
            forward = self.app.render.getRelativeVector(self.app.camera, Vec3(1,0,0))
            forward.normalize()
            forward.z = 0
            speed += forward*self.speed
        if "a" in self.app.keys:
            forward = self.app.render.getRelativeVector(self.app.camera, Vec3(-1,0,0))
            forward.normalize()
            forward.z = 0
            speed += forward*self.speed
        if "space" in self.app.keys and self.isGrounded():
            speed.z += self.jumpForce
        
        if self.isGrounded():
            self.node.node().setLinearVelocity((speed.x, speed.y, self.node.node().getLinearVelocity().z + speed.z))
        else:
            self.node.node().setLinearVelocity((self.node.node().getLinearVelocity().x + speed.x/self.speed, self.node.node().getLinearVelocity().y + speed.y/self.speed, self.node.node().getLinearVelocity().z + speed.z))
            if self.node.node().getLinearVelocity().x > self.speed:
                self.node.node().setLinearVelocity((self.speed, self.node.node().getLinearVelocity().y, self.node.node().getLinearVelocity().z))
            if self.node.node().getLinearVelocity().x < -self.speed:
                self.node.node().setLinearVelocity((-self.speed, self.node.node().getLinearVelocity().y, self.node.node().getLinearVelocity().z))
            if self.node.node().getLinearVelocity().y > self.speed:
                self.node.node().setLinearVelocity((self.node.node().getLinearVelocity().x, self.speed, self.node.node().getLinearVelocity().z))
            if self.node.node().getLinearVelocity().y < -self.speed:
                self.node.node().setLinearVelocity((self.node.node().getLinearVelocity().x, -self.speed, self.node.node().getLinearVelocity().z))
            
        
        self.app.win.movePointer(0, int(self.app.win.getXSize()/2), int(self.app.win.getYSize()/2))
        
        return task.cont
    
    @tryFunc
    def isGrounded(self):
        result = self.app.world.contactTest(self.node.node())
        for i in result.getContacts():
            if i.getNode1().getTag("ground") == "True":
                return True
        return False
