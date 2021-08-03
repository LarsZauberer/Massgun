from src.GameObjects.DynamicObject import DynamicObject
from Content.Scripts.Button import Button
from panda3d.core import Vec3


class Door(DynamicObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.startPos = self.node.getPos()
        self.openingSpeed = 0.1
        self.openingHeight = 10
    
    def update(self, task):
        super().update(task)
        
        log = self.app.getLogger(self.update)
        
        if self.checkButtons():
            if self.node.getPos().z < self.openingHeight + self.startPos.z:
                self.node.setPos(Vec3(self.startPos.x, self.startPos.y, self.node.getPos().z + self.openingSpeed))
        else:
            if self.node.getPos().z > self.startPos.z:
                self.node.setPos(Vec3(self.startPos.x, self.startPos.y, self.node.getPos().z - self.openingSpeed))
        
        return task.cont
    
    # Check if all button in map is pressed
    def checkButtons(self):
        allButtons = []
        for i in self.app.objectRegistry:
            if issubclass(type(i), Button):
                allButtons.append(i)
        
        notAll = False
        for i in allButtons:
            if i.bt.state == False:
                notAll = True
        return not notAll
