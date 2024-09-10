# from turtle import Turtle,Screen
# timmy=Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('green')
# timmy.forward(200)
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Anime name",['Naruto', 'Attack on titan' , 'Demon slayer'])
table.add_column('Main character',['Uzumaki Naruto','Eran','Tanjero'])
table.add_column('Power',['Rasangun','Rumbling','Sun breathing'])
table.align='l'
print(table)

