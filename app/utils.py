from typing import List
from random import choice
from json import dumps


class Field:
    field: List[List[int]]
    width: int
    length: int

    def __init__(self, width: int = 50, length: int = 50):
        self.width = width
        self.length = length

        # randomly choose from two states
        self.field = [[choice((0, 1)) for x in range(width)] for j in range(length)]

    @staticmethod
    def new_cell(old_cell: int, alive_neighbors: int) -> int:
        """
        Returning new cell by checking rule 4 and 5
        Returning 1 if new cell is alive 0 if new cell is dead
        """
        if old_cell:  # if cell is alive
            if alive_neighbors in (2, 3):
                return 1
            else:
                return 0
        elif alive_neighbors == 3:  # if cell is dead and alive neighbors is 3
            return 1
        else:  # if cell is dead and alive neighbors not equal to 3
            return 0

    def step(self):
        """Generate new field from past state"""
        new_field = []
        for i in range(self.length):  # for each row
            new_row = []
            for j in range(self.width):  # for each cell in row
                next_column_index = j + 1 if j != self.width - 1 else 0  # checking is it last column
                next_row_index = i + 1 if i != self.length - 1 else 0  # checking is it last row

                # summing alive neighbors for each row
                previous_row = self.field[i - 1][j - 1] + self.field[i - 1][j] + self.field[i - 1][next_column_index]
                current_row = self.field[i][j - 1] + self.field[i][next_column_index]
                next_row = self.field[next_row_index][j - 1] + self.field[next_row_index][j] + \
                           self.field[next_row_index][
                               next_column_index]
                alive_neighbors = previous_row + current_row + next_row

                new_row.append(self.new_cell(self.field[i][j], alive_neighbors))  # append new cell to new row

            new_field.append(new_row)
        self.field = new_field

    def __str__(self):
        result = ""
        for row in self.field:
            result = result + " ".join(map(str, row)) + "\n"
        return result

