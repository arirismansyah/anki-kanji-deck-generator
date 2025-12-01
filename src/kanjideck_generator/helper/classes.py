from pydantic import BaseModel
from enum import Enum


class LevelType(str, Enum):
    JLPT = "jlpt"
    GRADE = "grade"


class JLPTLevel(str, Enum):
    N1 = "n1"
    N2 = "n2"
    N3 = "n3"
    N4 = "n4"
    N5 = "n5"


class GradeLevel(int, Enum):
    G1 = 1
    G2 = 2
    G3 = 3
    G4 = 4
    G5 = 5
    G6 = 6


GRADE_TO_JLPT_MAP: dict[GradeLevel, JLPTLevel] = {
    GradeLevel.G1: JLPTLevel.N5,
    GradeLevel.G2: JLPTLevel.N5,
    GradeLevel.G3: JLPTLevel.N4,
    GradeLevel.G4: JLPTLevel.N3,
    GradeLevel.G5: JLPTLevel.N3,
    GradeLevel.G6: JLPTLevel.N2,
}

JLPT_TO_GRADE_MAP: dict[JLPTLevel, list[GradeLevel]] = {
    JLPTLevel.N5: [GradeLevel.G1, GradeLevel.G2],
    JLPTLevel.N4: [GradeLevel.G3],
    JLPTLevel.N3: [GradeLevel.G4, GradeLevel.G5],
    JLPTLevel.N2: [GradeLevel.G6],
    JLPTLevel.N1: [],
}
