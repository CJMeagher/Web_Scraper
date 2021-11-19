planets = ['Mercury',
           'Venus',
           'Earth',
           'Mars',
           'Jupiter',
           'Saturn',
           'Uranus',
           'Neptune']
file = open('planets.txt', 'w', encoding='utf-8')
file.write('\n'.join(planets))
file.close()
