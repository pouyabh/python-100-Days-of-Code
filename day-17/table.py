from prettytable import PrettyTable

table = PrettyTable()
table.add_column('names', ['ali', 'reza', 'mahdi'])
table.align = 'l'

print(table )
