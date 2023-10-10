# automatically generated by the FlatBuffers compiler, do not modify

# namespace: data

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class View(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = View()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsView(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # View
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # View
    def Edges(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from agroproto.data.Edge import Edge
            obj = Edge()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # View
    def EdgesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # View
    def EdgesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # View
    def Obstacles(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from agroproto.data.Obstacle import Obstacle
            obj = Obstacle()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # View
    def ObstaclesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # View
    def ObstaclesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # View
    def Windrows(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from agroproto.data.Windrow import Windrow
            obj = Windrow()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # View
    def WindrowsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # View
    def WindrowsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # View
    def Image(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from agroproto.data.Image import Image
            obj = Image()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # View
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # View
    def AlarmType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # View
    def TooMuchDust(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def Start(builder): builder.StartObject(7)
def ViewStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddEdges(builder, edges): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(edges), 0)
def ViewAddEdges(builder, edges):
    """This method is deprecated. Please switch to AddEdges."""
    return AddEdges(builder, edges)
def StartEdgesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ViewStartEdgesVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartEdgesVector(builder, numElems)
def AddObstacles(builder, obstacles): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(obstacles), 0)
def ViewAddObstacles(builder, obstacles):
    """This method is deprecated. Please switch to AddObstacles."""
    return AddObstacles(builder, obstacles)
def StartObstaclesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ViewStartObstaclesVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartObstaclesVector(builder, numElems)
def AddWindrows(builder, windrows): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(windrows), 0)
def ViewAddWindrows(builder, windrows):
    """This method is deprecated. Please switch to AddWindrows."""
    return AddWindrows(builder, windrows)
def StartWindrowsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ViewStartWindrowsVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartWindrowsVector(builder, numElems)
def AddImage(builder, image): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(image), 0)
def ViewAddImage(builder, image):
    """This method is deprecated. Please switch to AddImage."""
    return AddImage(builder, image)
def AddType(builder, type): builder.PrependInt8Slot(4, type, 0)
def ViewAddType(builder, type):
    """This method is deprecated. Please switch to AddType."""
    return AddType(builder, type)
def AddAlarmType(builder, alarmType): builder.PrependInt8Slot(5, alarmType, 0)
def ViewAddAlarmType(builder, alarmType):
    """This method is deprecated. Please switch to AddAlarmType."""
    return AddAlarmType(builder, alarmType)
def AddTooMuchDust(builder, tooMuchDust): builder.PrependBoolSlot(6, tooMuchDust, 0)
def ViewAddTooMuchDust(builder, tooMuchDust):
    """This method is deprecated. Please switch to AddTooMuchDust."""
    return AddTooMuchDust(builder, tooMuchDust)
def End(builder): return builder.EndObject()
def ViewEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)
import agroproto.data.Edge
import agroproto.data.Image
import agroproto.data.Obstacle
import agroproto.data.Windrow
try:
    from typing import List, Optional
except:
    pass

class ViewT(object):

    # ViewT
    def __init__(self):
        self.edges = None  # type: List[agroproto.data.Edge.EdgeT]
        self.obstacles = None  # type: List[agroproto.data.Obstacle.ObstacleT]
        self.windrows = None  # type: List[agroproto.data.Windrow.WindrowT]
        self.image = None  # type: Optional[agroproto.data.Image.ImageT]
        self.type = 0  # type: int
        self.alarmType = 0  # type: int
        self.tooMuchDust = False  # type: bool

    @classmethod
    def InitFromBuf(cls, buf, pos):
        view = View()
        view.Init(buf, pos)
        return cls.InitFromObj(view)

    @classmethod
    def InitFromObj(cls, view):
        x = ViewT()
        x._UnPack(view)
        return x

    # ViewT
    def _UnPack(self, view):
        if view is None:
            return
        if not view.EdgesIsNone():
            self.edges = []
            for i in range(view.EdgesLength()):
                if view.Edges(i) is None:
                    self.edges.append(None)
                else:
                    edge_ = agroproto.data.Edge.EdgeT.InitFromObj(view.Edges(i))
                    self.edges.append(edge_)
        if not view.ObstaclesIsNone():
            self.obstacles = []
            for i in range(view.ObstaclesLength()):
                if view.Obstacles(i) is None:
                    self.obstacles.append(None)
                else:
                    obstacle_ = agroproto.data.Obstacle.ObstacleT.InitFromObj(view.Obstacles(i))
                    self.obstacles.append(obstacle_)
        if not view.WindrowsIsNone():
            self.windrows = []
            for i in range(view.WindrowsLength()):
                if view.Windrows(i) is None:
                    self.windrows.append(None)
                else:
                    windrow_ = agroproto.data.Windrow.WindrowT.InitFromObj(view.Windrows(i))
                    self.windrows.append(windrow_)
        if view.Image() is not None:
            self.image = agroproto.data.Image.ImageT.InitFromObj(view.Image())
        self.type = view.Type()
        self.alarmType = view.AlarmType()
        self.tooMuchDust = view.TooMuchDust()

    # ViewT
    def Pack(self, builder):
        if self.edges is not None:
            edgeslist = []
            for i in range(len(self.edges)):
                edgeslist.append(self.edges[i].Pack(builder))
            StartEdgesVector(builder, len(self.edges))
            for i in reversed(range(len(self.edges))):
                builder.PrependUOffsetTRelative(edgeslist[i])
            edges = builder.EndVector()
        if self.obstacles is not None:
            obstacleslist = []
            for i in range(len(self.obstacles)):
                obstacleslist.append(self.obstacles[i].Pack(builder))
            StartObstaclesVector(builder, len(self.obstacles))
            for i in reversed(range(len(self.obstacles))):
                builder.PrependUOffsetTRelative(obstacleslist[i])
            obstacles = builder.EndVector()
        if self.windrows is not None:
            windrowslist = []
            for i in range(len(self.windrows)):
                windrowslist.append(self.windrows[i].Pack(builder))
            StartWindrowsVector(builder, len(self.windrows))
            for i in reversed(range(len(self.windrows))):
                builder.PrependUOffsetTRelative(windrowslist[i])
            windrows = builder.EndVector()
        if self.image is not None:
            image = self.image.Pack(builder)
        Start(builder)
        if self.edges is not None:
            AddEdges(builder, edges)
        if self.obstacles is not None:
            AddObstacles(builder, obstacles)
        if self.windrows is not None:
            AddWindrows(builder, windrows)
        if self.image is not None:
            AddImage(builder, image)
        AddType(builder, self.type)
        AddAlarmType(builder, self.alarmType)
        AddTooMuchDust(builder, self.tooMuchDust)
        view = End(builder)
        return view
