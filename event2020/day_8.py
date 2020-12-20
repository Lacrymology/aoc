from os import path
from parser import parse

curdir = path.dirname(__file__)


class InfiniteLoopError(Exception):
    """
    To be raised when a program detects an infinite loop
    """


class Process:
    def __init__(self, code: list):
        self._code = code

        self._accum = 0
        self._cp = 0
        self._visited_instrs = set()

        self._fixed = False

    def __iter__(self):
        while 0 <= self._cp < len(self._code):
            if self._cp in self._visited_instrs:
                raise InfiniteLoopError(
                    f"Infinite Loop Detected: instr: {self._code[self._cp]} cp: {self._cp}, acc: {self._accum}, visited instructions: {self._visited_instrs}"
                )

            self._visited_instrs.add(self._cp)
            self.execute()
            yield self._accum, self._cp
        yield self._accum, -1

    def execute(self):
        instr, param = self._code[self._cp]
        # print(f"{self._cp:0>3d}: {instr} {param}")

        if instr == "nop":
            self._cp += 1
        elif instr == "acc":
            self._accum += param
            self._cp += 1
        elif instr == "jmp":
            self._cp += param

    @classmethod
    def parse_instr(cls, line):
        # print(line)
        instr, param = line.split()
        return [instr, int(param)]


with open(path.join(curdir, "day_8.input")) as f:
    code = parse(f, Process.parse_instr)

try:
    process = Process(code)
    # will either run the whole program, or raise InfiniteLoopError
    list(process)
except InfiniteLoopError as e:
    print(f"Part 1: {e}")


def flip(instr):
    if instr == "nop":
        return "jmp"
    elif instr == "jmp":
        return "nop"
    else:
        raise ValueError(instr)


for idx, instr in enumerate(code):
    if instr[0] in ("nop", "jmp"):
        old = instr[0]
        code[idx][0] = flip(old)
        process = Process(code)
        try:
            print(f"Part 2: {list(process)}")
            break
        except InfiniteLoopError:
            code[idx][0] = old