class Pokemon:
    def __init__(self, num, name, t1, t2, total, hp, attack, defense, spAttk, spDef, speed, gen, legendary):
        self.num = num
        self.name = name
        self.t1 = t1
        self.t2 = t2
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense 
        self.spAttk = spAttk
        self.spDef = spDef
        self.speed = speed
        self.gen = gen
        self.legendary = legendary
    
    # Overriding the to string method 
    def __str__(self):
        str1 = ""
        str1 += str(self.num) + " : " + self.name
        return str1


pokemon_file = open("pokemon.csv", "r")
lst_pokemon = []

first = True

for line in pokemon_file:
    if first: # To check for header in csv
        first = False
        continue

    lst = line.split(",")  # lst will be the pokemon in list form
    pokemon = Pokemon(int(lst[0]), lst[1], lst[2], lst[3], int(lst[4]), \
        int(lst[5]), int(lst[6]), int(lst[7]), int(lst[8]), int(lst[9]), int(lst[10]), int(lst[11]), lst[12])
    lst_pokemon.append(pokemon)


# This will find the pokemon with the highest attack value
def find_highest_attack(lst_pokemon):
    max_attk = 0
    max_pokemon = None

    for pokemon in lst_pokemon:
        if pokemon.attack > max_attk:
            max_attk = pokemon.attack
            max_pokemon = pokemon

    return max_pokemon
    

print(find_highest_attack(lst_pokemon))
print(find_highest_attack(lst_pokemon).attack)

