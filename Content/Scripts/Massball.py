from panda3d.core import Vec3
from src.GameObjects.DynamicObject import DynamicObject
from src.functionDecorators import tryFunc


class Massball(DynamicObject):
    @tryFunc
    def __init__(self, direction, *args, **kwargs):
        super().__init__(model="models/Massball/Massball.bam", mass=5, *args, **kwargs)
        self.collided = False
        self.speed = 100
        self.attractForce = 10
        self.dir = direction
        self.shouldDestroy = False
        self.destroySpeed = 0.01
    
    @tryFunc
    def update(self, task):
        super().update(task)
        
        # Destroy Animation
        if self.shouldDestroy:
            if self.node.getScale().getX() < 0.1:
                self._destroy()
            else:
                self.node.setScale(self.node.getScale()-self.destroySpeed)
            return task.cont
        
        # Flying
        if not self.collided:
            self.node.node().setLinearVelocity(self.dir * self.speed)
        else:
            # Is on the wall
            # Stop at spot
            self.node.node().setLinearVelocity(Vec3(0, 0, 0))
            self.node.node().setMass(0)
            
            # Attract Objects
            self.attractObjects()
        
        return task.cont

    @tryFunc
    def onCollisionEnter(self, other):
        super().onCollisionEnter(other)
        if other.name != "Player":
            self.collided = True
    
    # Function to attract all gameobjects to the massball which have a mass higher than 0
    @tryFunc
    def attractObjects(self):
        log = self.app.getLogger(self.attractObjects)
        for obj in self.app.objectRegistry:
            try:
                if obj.node.node().mass > 0:
                    vel = obj.node.node().getLinearVelocity()
                    direction = self.node.getPos() - obj.node.getPos()
                    direction.normalize()
                    direction *= self.attractForce
                    obj.node.node().setLinearVelocity(vel + direction)
            except AttributeError:
                continue
    
    @tryFunc
    def _destroy(self):
        self.shouldDestroy = True
        self.app.taskMgr.remove(self.name + "_update")
        self.app.world.remove(self.node.node())
        # TODO: If actor actor cleanup
        self.node.removeNode()
        self.app.objectRegistry.remove(self)

    @tryFunc
    def destroy(self):
        self.shouldDestroy = True
