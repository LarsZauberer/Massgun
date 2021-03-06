from src.Application import Application
from src.functionDecorators import tryFunc
from src.MapLoader import MapLoader
from src.InterfaceManager import InterfaceManager
from pathlib import Path

class App(Application):
    @tryFunc
    def __init__(self, name, debug=False, rpdebugger=False):
        super().__init__(name, debug, rpdebugger)
        log = self.getLogger(self.__init__)
        # Mousecatching
        self.catchMouse(True)
        
        # Map Management
        maps = {"testing": Path("Content/maps/map.json"), "test2": Path("Content/test.json")}
        self.mapLoader = MapLoader(self, maps)
        log.debug(f"Created Maploader")
        self.mapLoader.loadMap("testing")
        
        # Interface Management
        interfaces = {}
        self.interfaceManager = InterfaceManager(self, interfaces)
        # self.interfaceManager.load("hud")
        
        # Other important stuff for your game
    
    @tryFunc
    def keybinds(self, disable=False):
        log = self.getLogger(self.keybinds)
        if disable:
            # Disableing is important to don't accept input while in developer console
            log.debug(f"Disabling Key Input")
            self.ignore("w")
            self.ignore("w-up")
            self.ignore("s")
            self.ignore("s-up")
            self.ignore("d")
            self.ignore("d-up")
            self.ignore("a")
            self.ignore("a-up")
            self.ignore("space")
            self.ignore("space-up")
            self.ignore("mouse1")
            self.ignore("mouse1-up")
            self.ignore("mouse3")
            self.ignore("mouse3-up")
        else:
            log.debug(f"Enableing Key Input")
            self.accept("w", self.keys.append, ["w"])
            self.accept("w-up", self.keys.remove, ["w"])
            self.accept("s", self.keys.append, ["s"])
            self.accept("s-up", self.keys.remove, ["s"])
            self.accept("d", self.keys.append, ["d"])
            self.accept("d-up", self.keys.remove, ["d"])
            self.accept("a", self.keys.append, ["a"])
            self.accept("a-up", self.keys.remove, ["a"])
            self.accept("space", self.keys.append, ["space"])
            self.accept("space-up", self.keys.remove, ["space"])
            self.accept("mouse1", self.keys.append, ["mouse1"])
            self.accept("mouse1-up", self.keys.remove, ["mouse1"])
            self.accept("mouse3", self.keys.append, ["mouse3"])
            self.accept("mouse3-up", self.keys.remove, ["mouse3"])
    
    @tryFunc
    def update(self, task):
        super().update(task)
        return task.cont
        
app = App("Test", True, True)

app.run()