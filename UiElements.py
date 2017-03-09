class UiRegistry(object):

    __instance__ = None

    def __new__(cls):
        """
        Re-implement the __new__ method to make sure we create a true singleton.
        """
        if not cls.__instance__:
            cls.__instance__ = object.__new__(cls)
        return cls.__instance__

    @classmethod
    def create(cls):
        """
        The constructor for the component registry providing a single registry of objects.
        """
        registry = cls()
        return registry


    def addWindow(self, window):
        self.mainwindow = window

    def getWindow(self):
        return self.mainwindow
