# automatically generated by the FlatBuffers compiler, do not modify

# namespace: types

import flatbuffers

class Levels(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsLevels(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Levels()
        x.Init(buf, n + offset)
        return x

    # Levels
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Levels
    def Data(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 8
            from .Level import Level
            obj = Level()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Levels
    def DataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def LevelsStart(builder): builder.StartObject(1)
def LevelsAddData(builder, Data): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(Data), 0)
def LevelsStartDataVector(builder, numElems): return builder.StartVector(8, numElems, 4)
def LevelsEnd(builder): return builder.EndObject()
