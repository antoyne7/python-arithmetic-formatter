class Problem:
    show_result = False
    spaces = 4
    
    def __init__(self, operand_1, operator, operand_2):
        self.operand_1 = operand_1
        self.operator = operator
        self.operand_2 = operand_2

    @classmethod
    def from_string(cls, problem):
        return cls(
            operand_1=problem.split(' ')[0],
            operator=problem.split(' ')[1],
            operand_2=problem.split(' ')[2]
        )

    def get_size(self):
        if len(self.operand_1) > len(self.operand_2):
            return len(self.operand_1) + 2
        else:
            return len(self.operand_2) + 2

    def get_result(self):
        if self.operator == '+':
            return int(self.operand_1) + int(self.operand_2)
        else:
            return int(self.operand_1) - int(self.operand_2)

    def get_left_space(self, rvalue):
        return self.get_size() - len(rvalue)

    def get_lines(self):
        lines =  [
            ' ' * self.get_left_space(self.operand_1) + self.operand_1,
            self.operator + ' ' * (self.get_left_space(self.operand_2)-1) + self.operand_2,
            '-' * self.get_size()
        ]

        if self.show_result:
            lines.append(' ' * self.get_left_space(str(self.get_result())) + str(self.get_result()))
            
        return lines

    def add_to_lines(self, l):
        for index, line in enumerate(self.get_lines()):
            l[index] += line + self.spaces*' '
        return l
