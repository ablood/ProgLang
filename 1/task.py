
import csv
import sys
from math import *

import re
_re_cell_ex = re.compile(r"([a-z]+)(\d+)", re.IGNORECASE)

def _re_cell_repl(m):
    col, row = m.groups()
    return cell_to_rowcol(col, row, 'data')

def col_by_name(colname):
    col = 0
    power = 1
    for i in range(len(colname) - 1, -1, -1):
        ch = colname[i]
        col += (ord(ch) - ord('A') + 1) * power
        power *= 26
    return col - 1

def cell_to_rowcol(col, row, dataStr):
    row = int(row) - 1
    col = col_by_name(col.upper())
    return dataStr + '[' + str(row) + '][' + str(col) + ']'

def adjust_cell(cell_value):
    return re.sub(_re_cell_ex, _re_cell_repl, cell_value)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemError
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if len(sys.argv) == 4:
        load_module = sys.argv[3]
        exec('from ' + load_module + ' import *')
    
    data = []

    with open(input_file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    for row in range(len(data)):
        for cell in range(len(data[row])):
            cell_value = data[row][cell]
            if (cell_value[0] != '=' and re.match("^\d*(\.\d*)?$", cell_value) is not None):
                data[row][cell] = eval(cell_value)

    for row in range(len(data)):
        for cell in range(len(data[row])):
            cell_value = data[row][cell]
            if (type(cell_value) == str and cell_value[0] == '='):
                try:
                    data[row][cell] = eval(adjust_cell(cell_value[1:]))
                except BaseException:
                    data[row][cell] = 'Error'
                    
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

