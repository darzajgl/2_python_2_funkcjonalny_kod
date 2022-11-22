# Uzupełnij deklarację funkcji `multi_calculator` tak,
# aby funkcja działała analogicznie do funkcji `simple_calculator`,
# z tą różnicą, że obsługuje więcej niż dwa argumenty pozycyjne.
#
# * Jeśli funkcja nie otrzyma żadnych argumentów powinna
#   zwrócić `0` niezależnie od `operation`
# * Jeśli funckja otrzyma jeden argument pozycyjny powinna
#   zwrócić jego wartość niezależnie od `operation`
# * Domyślną operacją jest dodawanie
#
# Przykład 1:
# multi_calculator(1, 1, 1, 1, 1, 1) == 6
#
# Przykład 2:
# multi_calculator(10, 1, 1, operation='-') == 8
#
# Przykład 3:
# multi_calculator(operation='|') == 0
#
# Przykład 4:
# multi_calculator(3) == 3


def multi_calculator(*args: int, operation: str = '+') -> None:
    # print(args)
    if args == tuple():
        return 0
    if len(args) == 0:
        return 0
    if len(args) == 1:
        return args[0]

    if operation == '+':
        return sum(args)

    if operation == '-':
        subtraction = args[0]
        for arg in args[1:]:
            subtraction -= arg
        return subtraction

    if operation == '*':
        multiplication = 1
        for arg in args:
            multiplication *= arg
        return multiplication

    if operation == '**':
        power = args[0]
        for arg in args:
            power **= arg
        return power

    if operation == '|':
        div = args[0]
        for arg in args:
            div |= arg
        return div

    if operation == '&':
        andd = args[0]
        for arg in args:
            andd &= arg
        return andd


print("12 = " + str(multi_calculator(4, 4, 4)))
print("3 = " + str(multi_calculator(1, 1, 1)))
print("4 = " + str(multi_calculator(10, 1, 1, 1, 1, 1, 1, operation='-')))
print("24 = " + str(multi_calculator(2, 3, 4, operation='*')))
print("0 = " + str(multi_calculator(tuple(), operation="**")))
print("2 = " + str(multi_calculator(2, operation="**")))
print("4 = " + str(multi_calculator(2, 2, operation="**")))
print("3071 = " + str(multi_calculator(235, 2345, 623, 123, operation="|")))
print("663 = " + str(multi_calculator(663, operation="&")))
