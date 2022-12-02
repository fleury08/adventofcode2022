import uuid
from dataclasses import dataclass, field
from typing import List


@dataclass
class Elf:
    id = uuid.uuid4()
    total_calories = 0

    def add_calories(self, amount):
        self.total_calories += amount

    def __repr__(self):
        return f"id {self.id}: {self.total_calories} cal"

@dataclass
class Elves:
    last_elf: Elf = field(default_factory=Elf)
    elves_list: List[Elf] = field(default_factory=list)
    sorted_elves: List[Elf] = field(default_factory=list)

    def add_elf(self, elf: Elf):
        self.elves_list.append(elf)
        self.sorted_elves = self.sort_elves()
        self.last_elf = elf

    def sort_elves(self):
        return sorted(self.elves_list, key=lambda x: x.total_calories, reverse=True)