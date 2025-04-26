class TuringMachine:
    def __init__(self, tape, initial_state, transitions, accept_state):
        self.tape = list(tape)  # Лента преобразуется в список символов
        self.state = initial_state  # Начальное состояние
        self.transitions = transitions  # Переходы машины Тьюринга
        self.accept_state = accept_state  # Принимающее состояние
        self.head = 0  # Начальная позиция головки на ленте

    def step(self):
        """Выполнение одного шага машины Тьюринга."""
        if self.state == self.accept_state:  # Если достигли принимающего состояния
            return False

        # Находим переход для текущего состояния и символа на ленте
        current_symbol = self.tape[self.head]
        if (self.state, current_symbol) not in self.transitions:
            return False

        # Получаем информацию о переходе
        next_state, write_symbol, move_direction = self.transitions[(self.state, current_symbol)]

        # Записываем символ на ленту
        self.tape[self.head] = write_symbol

        # Двигаем головку
        if move_direction == 'r':
            self.head += 1
        elif move_direction == 'l':
            self.head -= 1

        # Переходим в новое состояние
        self.state = next_state
        return True

    def run(self):
        """Запускает машину Тьюринга до достижения принимающего состояния."""
        while self.step():
            pass
        return ''.join(self.tape)  # Возвращаем итоговое состояние ленты


def parse_transitions():
    transitions = {}
    print("Введите переходы в формате:")
    print("состояние символ новое_состояние символ_для_записи направление (r или l)")
    print("Пример: q1 0 q2 0 r")
    print("Для завершения ввода переходов введите 'end'")
    while True:
        transition = input()
        if transition.strip().lower() == 'end':
            break
        parts = transition.split()
        if len(parts) == 5:
            state, symbol, next_state, write_symbol, direction = parts
            transitions[(state, symbol)] = (next_state, write_symbol, direction)
        else:
            print("Некорректный формат перехода, попробуйте снова.")
    return transitions


def main():
    initial_state = input("Введите начальное состояние: ")
    accept_state = input("Введите конечное состояние: ")
    tape = input("Введите начальную ленту: ")

    transitions = parse_transitions()

    tm = TuringMachine(tape, initial_state, transitions, accept_state)
    final_tape = tm.run()

    print("Итоговая лента:", final_tape)


if __name__ == "__main__":
    main()
