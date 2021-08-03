from src.GameObjects.DynamicObject import DynamicObject
from src.GameObjects.GameObject import GameObject
from src.functionDecorators import tryFunc

from Content.Scripts.buttonTrigger import buttonTrigger


class Button(DynamicObject):
    @tryFunc
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.baseModel = GameObject(self.app, name="base", x=kwargs["x"], y=kwargs["y"], z=kwargs["z"], model="models/button/Button_off.bam", ground=True)
        self.bt = buttonTrigger(self.app, x=kwargs["x"], y=kwargs["y"], z=kwargs["z"]+1.2, name="buttonTrigger", sx=2, sy=2)
        self.app.world.remove(self.node.node())
        self.node.hide()
        
        self.models = [self.app.loader.loadModel("Content/models/button/Button_off.bam"), self.app.loader.loadModel("Content/models/button/Button_on.bam")]
        
        self.on = False
        
        self.models[0].reparentTo(self.app.render)
        self.models[0].setPosHprScale(self.node.getPos(), self.node.getHpr(), self.node.getScale())
        self.models[0].show()
        self.models[1].reparentTo(self.app.render)
        self.models[1].setPosHprScale(self.node.getPos(), self.node.getHpr(), self.node.getScale())
        self.models[1].hide()
        
        self.baseModel.node.hide()
    
    @tryFunc
    def update(self, task):
        super().update(task)
        
        log = self.app.getLogger(self.update)
        
        if self.bt.state:
            if not self.on:
                log.debug(f"Changing model to on")
                self.models[1].show()
                self.models[0].hide()
                self.on = True
        else:
            if self.on:
                log.debug(f"Changing model to off")
                self.models[0].show()
                self.models[1].hide()
                self.on = False
        
        return task.cont
