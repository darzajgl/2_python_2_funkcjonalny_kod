# Uzupełnij funkcję `adder` tak, aby przyjmowała jeden argument
# pozycyjny i zwracała funkcję. Zwrócona funkcja powinna przyjmować
# jeden argument pozycyjny i zwracać sumę otrzymanego argumentu i
# argumentu przekazanego wcześniej do funkcji adder
#
# Przykład:
# adder(1)(2) == 3


def adder(n: int) -> int:
    if n == 0:
        return 0
    else:
        return (n + adder(n - 1))
