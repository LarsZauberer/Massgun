from src.Console import Command


class Test(Command):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.executor = "test"
    
    def execute(self, cmd):
        print(cmd)

class maxBalls(Command):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.executor = "maxballs"
    
    def execute(self, cmd):
        log = self.app.getLogger(self.execute)
        try:
            self.app.player.maxBalls = int(cmd)
            log.info(f"New maxball count: {int(cmd)}")
        except Exception:
            log.exception(f"Error while setting max ball count")
