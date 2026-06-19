class Weapon:
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack
        
    def __str__(self):
        return f"{self.name} - Attack: {self.attack}"

class Warrior:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def __str__(self):
        return f"{self.name}"
    

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"Warrior equipped {weapon.name}!")

    def show_weapon(self):
        if self.weapon:
            print(f"{self.name.lower()} is holding a {self.weapon.name.lower()}")
        else:
            print(f"{self.name.lower()} is unarmed")

sword = Weapon("Sword", 5)
warrior = Warrior("Conan")

warrior.equip_weapon(sword)
warrior.show_weapon()