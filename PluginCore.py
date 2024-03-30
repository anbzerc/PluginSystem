from abc import ABC, abstractmethod, ABCMeta


# TODO plugin.yaml
class PluginSample(ABC):
    #Abstract method and classe to force plugin to define these methods
    @classmethod
    @abstractmethod
    def nourrir(self):
        pass