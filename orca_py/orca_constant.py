from enum import IntEnum


class ORCA_MODE(IntEnum):
    SleepMode = 1
    ForceMode = 2
    PositionMode = 3
    HapticMode = 4
    KinematicMode = 5


class ORCA_MODE_SUBCODE(IntEnum):
    ForceControlStream = 0x1C
    PositionControlStream = 0x1E
    KinematicDataStream = 0x20
    HapticDataStream = 0x22
    SleepDataStream = 0x00  # all else
