from typing import List

from model.elf import Elf, Elves


def main():
    elves = Elves()
    with open("input", "r", encoding="utf-8") as elfs_input:
        rows = elfs_input.readlines()
        for row in rows:
            row = row.strip()
            if not elves:
                elves.add_elf(Elf())
            if not row:
                print(elves)
                elves.add_elf(Elf())
                continue
            elves.last_elf.add_calories(int(row or 0))

    print(f"Top Elf {elves.sorted_elves[0].id} with {elves.sorted_elves[0].total_calories} cal")
    print(f"Top 3 elves: {elves.sorted_elves[0:3]}, total {sum(x.total_calories for x in elves.sorted_elves[0:3])}")


if __name__ == '__main__':
    main()