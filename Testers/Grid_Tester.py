import Grid.Grid as G

my_grid = G.Grid("Gotham")
my_grid.add_object(1, 2, "ROCK")
print(my_grid.objects)
my_grid.move_object(1, 2, 3, 4)
print(my_grid.objects)
my_grid.remove_object(3, 4)
print(my_grid.objects)