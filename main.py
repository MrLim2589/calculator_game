from enum import Enum
from math import floor


class Operation(Enum):
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    MIN = 5
    LEFT = 6
    REVERSE = 7
    APPEND = 8


class Button:
    def __init__(self, operation: Operation, num=0):
        self.operation = operation
        self.num = num

    def __str__(self):
        return f'{self.operation}|{self.num}'

    def get_info(self):
        return f'Operation: {self.operation}, Number: {self.num}'

    def operate(self, num):
        if self.operation == Operation.ADD:
            return num + self.num
        elif self.operation == Operation.SUB:
            return num - self.num
        elif self.operation == Operation.MUL:
            return num * self.num
        elif self.operation == Operation.DIV:
            return num / self.num
        elif self.operation == Operation.MIN:
            return -num
        elif self.operation == Operation.LEFT:
            return floor(num / 10)
        elif self.operation == Operation.REVERSE:
            return int(str(num)[::-1])
        elif self.operation == Operation.APPEND:
            return int(f'{num}{self.num}')


class Calculator:
    def __init__(self, start, goal, move, buttons: list = []):
        self.start = start
        self.goal = goal
        self.move = move
        self.buttons = buttons

    def print_status(self):
        print(f'Start: {self.start}, Goal: {self.goal}, Moves: {self.move}')
        for i in range(len(self.buttons)):
            print(f'Button{i}: {self.buttons[i]}')

    def add_button(self, button: Button):
        self.buttons.append(button)

    def solve(self, num=None, depth=0, path=None):
        if num is None:
            num = self.start
        if path is None:
            path = {}
        if depth > self.move:
            return False
        if num == self.goal:
            return True
        if type(num) == float:
            return False

        for button in self.buttons:
            path[depth] = button
            ans = self.solve(button.operate(num), depth + 1, path)
            if ans:
                return path
            else:
                path.popitem()

    def print_answer(self):
        buttons = self.solve()
        for i in range(len(buttons)):
            print(f'{i + 1}. {buttons[i]}')


if __name__ == '__main__':
    """
    start = int(input('Start: '))
    goal = int(input('Goal: '))
    move = int(input('Moves: '))
    calculator = Calculator(start, goal, move)
    while True:
        operation = int(
            input('Button(operation)/(0. EXIT 1. ADD, 2. SUB, 3. MUL, 4. DIV, 5. MIN, 6. LEFT, 7. RIGHT): '))
        if operation not in list(map(int, Operation)):
            break
                
        num = int(input('Button(number): '))
        calculator.add_button(Button(Operation(operation), num))

    calculator.print_status()
    print(calculator.solve())
    """
    calculator = Calculator(8, 9, 5, [Button(Operation.MUL, 3), Button(Operation.APPEND, 1), Button(Operation.DIV, 5),
                                      Button(Operation.REVERSE)])
    calculator.print_answer()
