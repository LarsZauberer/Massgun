from src.GameObjects.TriggerBox import TriggerBox
from src.functionDecorators import tryFunc


class buttonTrigger(TriggerBox):
    @tryFunc
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = False
        
    
    @tryFunc
    def update(self, task):
        super().update(task)
        
        self.state = len(self.touching) > 0
        
        return task.cont
