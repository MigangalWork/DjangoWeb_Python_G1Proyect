# impresión de datos

# constantes de alineación de columna
class Align:
    LEFT = 0
    RIGHT = 1


# definición de columna
class Column:
    def __init__(self, name, align=Align.LEFT):
        self.name = name
        self.align = align


# imprimir tabla
def print_table(columns, data, column_sep='  ', padding=' '):
    # ancho de separador
    column_sep_width = len(column_sep)

    # ancho de padding
    padding_width = len(padding)

    # obtener ancho de cada columna

    column_widths = []
    for column_index in range(len(columns)):
        column_name = columns[column_index].name

        column_width = len(column_name)

        for row in data:
            column_width = max(column_width, len(row[column_index]))

        column_widths.append(column_width)

    # ancho de tabla, incluyendo separación entre columnas y padding
    table_width = (
            padding_width
            + sum(column_widths)
            + column_sep_width * (len(columns) - 1)
            + padding_width
    )

    # borde de tabla horizontal
    horizontal_border = '+' + ('-' * table_width) + '+'

    # crear cadena de formato

    row_format_string_parts = [
        '|',
        padding
    ]

    next_column_sep = ''
    for column, column_width in zip(columns, column_widths):
        row_format_string_parts += next_column_sep

        if column.align == Align.LEFT:
            row_format_string_parts.append('{:<')
        elif column.align == Align.RIGHT:
            row_format_string_parts.append('{:>')
        else:
            raise ValueError('align no válido')

        row_format_string_parts.append(str(column_width))
        row_format_string_parts.append('}')
        next_column_sep = column_sep

    row_format_string_parts.append(padding)
    row_format_string_parts.append('|')

    row_format_string = ''.join(row_format_string_parts)

    # imprimir tabla

    print(horizontal_border)

    # imprimir nombres de columnas
    column_names = [column.name for column in columns]
    print(row_format_string.format(*column_names))

    print(horizontal_border)

    # imprimir filas
    for row in data:
        print(row_format_string.format(*row))

    print(horizontal_border)


# test
def _test():
    columns = [
        Column('a'),
        Column('aaa', Align.LEFT),
        Column('aaa', Align.RIGHT)
    ]

    data = [
        ('1', '2', '3'),
        ('12', '34', '34'),
        ['23', '5', '67'],
    ]

    print_table(columns, data)
    print_table(columns, data, '|', '*')


if __name__ == '__main__':
    _test()
