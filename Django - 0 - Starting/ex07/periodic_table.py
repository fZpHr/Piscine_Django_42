import sys

def main():
    with open('periodic_table.txt', 'r') as f:
        lines = f.readlines()

    elements = []
    for line in lines:
        element_name, element_properties = line.split(' = ')
        element_dict = dict(item.split(':') for item in element_properties.strip().split(', '))
        element_dict['name'] = element_name
        elements.append(element_dict)
    table = [['' for _ in range(18)] for _ in range(7)]
    first = 0
    for element in elements:
        position = int(element['position'])
        row_offset = 0
        color = "DarkRed"
        for i in range(7):
            if (position == 1):
                row_offset = 1
            elif(position in range (2, 12)):
                row_offset = 3
                color = "DarkGoldenRod"
            elif(position in range (12, 17)):
                row_offset = 1
                color = "DarkGreen"
            if (position == 17):
                first += 1
                if (first == 1):
                    row_offset = 0
                else:
                    row_offset = first - 1
                    color = "DarkGreen"
            if table[i + row_offset][position] == '':
                table[i + row_offset][position] = f"""<td style='background-color: {color};'>
                <span class='style1'>{element['number']}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{element['molar']}</span>
                <br><span class='style3'>{element['small']}</span>
                <br><h4>{element['name']}</h4><span class='style4'>{element['electron']}</span></td>"""
                break
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == '':
               table[i][j] = '<td></td>'
    rows = ['<tr>' + ''.join(cell for cell in row) + '</tr>' for row in table]
    content = '\n'.join(rows)
    

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Table de Mendeleïev</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: black;
        }}
        h4 {{
            font-size: 10px;
            text-align: center;
        }}
        table {{
            border-collapse: collapse;
            margin: auto;
        }}
        td:empty {{
            border: none;
            background-color: transparent;
        }}
        th, td {{
            font-weight: bold;
            border: 5px solid rgb(0, 0, 0);
            color: rgb(255, 255, 255);
            padding: 8px;
            background-color: gray;
            font-size: 15px;
        }}
        td:hover {{
            background-color: white;
            cursor: pointer;
        }}
        .style1 {{ 

            font-size: 10px;
            color: white;
            justify-content: center;
            display: flex;
        }}
        .style2 {{ 
            font-size: 10px;
            color: white;
            justify-content: center;
            display: flex;
        }}
        .style3 {{ 
            font-size: 15px;
            color: white;
            justify-content: center;
            display: flex;
        }}
        .style4 {{ 
            font-size: 7px;
            color: white;
            justify-content: center;
            display: flex;
        }}
    </style>
</head>
<body>
    <table>
        {content}
    </table>
</body>
</html>
"""

    with open('periodic_table.html', 'w') as f:
        f.write(html)

if __name__ == "__main__":
    main()