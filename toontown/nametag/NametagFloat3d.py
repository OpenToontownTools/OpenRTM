from direct.task.Task import Task

from toontown.nametag.Nametag3d import Nametag3d


class NametagFloat3d(Nametag3d):
    def tick(self, task):
        return Task.done
