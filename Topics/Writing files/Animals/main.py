animals = ['rabbit ', 'cat ', 'turtle']
animal_file = open('animals.txt', 'r')
animal_new_file = open('animals_new.txt', 'w')
for line in animal_file.readlines():
    animal_new_file.write(line.strip('\n') + ' ')
animal_file.close()
animal_new_file.close()
