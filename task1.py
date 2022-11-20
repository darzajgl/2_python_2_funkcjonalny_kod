# Uzupelnij deklarację funkcji `simple_adder` tak, aby
# przyjomowała dwa argumenty i zwracała ich sumę.


def simple_adder(x: int, y: int) -> None:
    outcome = x + y
    return outcome


# Uzupełnij deklarację funkcji `simple_subtractor` tak,
# aby przymowała dwa `keyword arguments` o nazwach `x` i `y`
# i zwracała ich różnicę. Niech `x` będzie odjemną.


def simple_subtractor(x: int, y: int) -> None:
    outcome = x - y
    return outcome


# Uzupełnij deklarację funkcji `simple_calculator` tak,
# aby przyjmowała dwa argumenty pozycyjne i jeden `keyword`.
# Dwa argumenty pozycyjne mają być operandami operacji zdefiniowanej
# jako `keyword` `operation`. Jeśli `operation` nie zostanie
# przekazane jako parametr wywołania, funkcja powinna wykonać
# operację dodawania. `operation` może być jednym z '+', '-', '*',
# '**', '|' lub '&'.
#
# Przykład 1:
# simple_calculator(1, 2) == 3
#
# Przykład 2:
# simple_calculator(2, 1, operation='-') == 1


def simple_calculator(x: int, y: int, operation: str = '+') -> None:
    if operation == '+':
        return x + y
    if operation == '-':
        return x - y
    if operation == '*':
        return x * y
    if operation == '**':
        return x ** y
    if operation == '|':
        return x | y
    if operation == '&':
        return x & y

