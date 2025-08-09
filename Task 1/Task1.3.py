'''This is Task 1.3 of MIA Summer training for AI SUB-TEAM
Program created and programmed by: Yassin Khaled, CCE28
Required to do :
1. Create a class for each driver with their unique moves and properties. Done
2. Implement offensive and defensive moves for each driver. Done
3. Create a move selector for each driver to choose their moves intelligently. Done
4. Implement move execution logic to apply the selected moves and update driver states. Done
I did each round for each driver, and the winner is the one who has tire health above 0.
For each round only 1 driver have the absolute choice (Randomly Selected, I imported random to be fair)
'''

from abc import ABCMeta, abstractmethod
import random


class Driver(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
        self.__tirehealth = 100 #Private attribute for tire health
        self.__fuel = 500 #Private attribute for fuel
        
    @abstractmethod # Abstraction 
    def move_offensive(self):
        pass
    
    @abstractmethod
    def move_defensive(self):
        pass
    
    @abstractmethod
    def move_selector(self):
        pass
    
    @property # Encapsulation
    def tire_health(self):
        return self.__tirehealth
    
    @tire_health.setter # Encapsulation
    def tire_health(self, value):
        self.__tirehealth = max(0, value)
    
    @property
    def fuel(self):
        return self.__fuel
    
    @fuel.setter
    def fuel(self, value):
        self.__fuel = max(0, value)

    def __str__(self):
        return f"Driver: {self.name}, Tire Health: {self.__tirehealth}, Fuel: {self.__fuel}"
    
        
class Verstappen(Driver): # Inheritance
    def __init__(self):
        super().__init__("Max Verstappen")
        self.offensive_moves = {"DRS Boost": [45,12], "Red Bull Surge": [80, 20], "Percision Turn": [30, 8]}  # [fuel_cost, damage]
        self.defensive_moves = {"Brake Late": [25, 30], "ERS Deployment": [40, 50]}  # [fuel_cost, damage_reduction]
        self.ers_deployment = 3 # This is the number of times ERS can be deployed
    
    def move_offensive(self): # This is an example of a method that implements the abstract method (Polymorphism)
        return self.move_selector("offensive")
    
    def move_defensive(self): # This is the method that will be used to select the defensive move (Polymorphism)
        return self.move_selector("defensive")
    
    def move_selector(self, move_type): # This is the method that will be used to select the move (Polymorphism)
        if move_type == "offensive":
            available_moves = {}
            for k, v in self.offensive_moves.items():
                if self.fuel >= v[0]:
                    available_moves[k] = v
            if not available_moves:
                return None, None
            move = random.choice(list(available_moves.keys()))
            return move, self.offensive_moves[move]
        elif move_type == "defensive":
            available_moves = {}
            for k, v in self.defensive_moves.items(): #(k, v) is move name and its effects
                if self.fuel >= v[0]:
                    available_moves[k] = v
            # Check ERS Deployment limit
            if "ERS Deployment" in available_moves and self.ers_deployment <= 0:
                del available_moves["ERS Deployment"]
            if not available_moves:
                return None, None
            move = random.choice(list(available_moves.keys()))
            return move, self.defensive_moves[move]
        else:
            raise ValueError("Invalid move type. Choose 'offensive' or 'defensive'.")

class Mostafa(Driver): # Inheritance
    def __init__(self):
        super().__init__("Hassan Mostafa")
        self.offensive_moves = {"Turbo Start": [50, 10], "Mercedes Charge": [90, 22], "Corner Mastery": [25, 7]}  # [fuel_cost, damage]
        self.defensive_moves = {"Slipstream Cut": [20, 40], "Agressive Block": [35, 100]}  # [fuel_cost, damage_reduction]
        self.aggressive_block = 2 # This is the number of times aggressive block can be used
    
    def move_offensive(self):
        return self.move_selector("offensive")
    
    def move_defensive(self):
        return self.move_selector("defensive")
    
    def move_selector(self, move_type):
        if move_type == "offensive":
            available_moves = {}
            for k, v in self.offensive_moves.items(): # (k, v) is move name and its effects
                if self.fuel >= v[0]: # Check if the driver has enough fuel for the move
                    available_moves[k] = v
            if not available_moves:
                return None, None
            move = random.choice(list(available_moves.keys()))
            return move, self.offensive_moves[move]
        elif move_type == "defensive":
            available_moves = {}
            for k, v in self.defensive_moves.items():
                if self.fuel >= v[0]:
                    available_moves[k] = v
            # Check Aggressive Block limit
            if "Agressive Block" in available_moves and self.aggressive_block <= 0:
                del available_moves["Agressive Block"]
            if not available_moves:
                return None, None
            move = random.choice(list(available_moves.keys()))
            return move, self.defensive_moves[move]
        else:
            raise ValueError("Invalid move type. Choose 'offensive' or 'defensive'.")
        
class Race:
    def __init__(self, driver1, driver2):
        self.driver1 = driver1
        self.driver2 = driver2
        self.currentdriver = driver1
        self.rounds= 0
        
    def startturn(self):
        self.rounds += 1
        attacker = self.currentdriver
        defender = self.driver2 if self.currentdriver == self.driver1 else self.driver1
        
        print(f"Round {self.rounds}")
        print(f"{attacker.name} is attacking.")
        
        # Attacker always attacks
        attack_move, attack_effects = attacker.move_offensive()
        if attack_move is None:
            print(f"{attacker.name} has no available offensive moves!")
            return True
        
        print(f"{attacker.name} uses {attack_move} with effects: {attack_effects}")
        attacker.fuel -= attack_effects[0]
        damage = attack_effects[1]
        
        # Defender tries to defend
        defense_move, defense_effects = defender.move_defensive()
        damage_reduction = 0
        
        if defense_move is not None:
            print(f"{defender.name} defends with {defense_move}")
            defender.fuel -= defense_effects[0]
            damage_reduction = defense_effects[1]
            
            # Track limited uses
            if defense_move == "ERS Deployment" and hasattr(defender, 'ers_deployment'):
                defender.ers_deployment -= 1
            elif defense_move == "Agressive Block" and hasattr(defender, 'aggressive_block'):
                defender.aggressive_block -= 1
        else:
            print(f"{defender.name} cannot defend!")
        
        # Calculate final damage
        final_damage = max(0, damage - damage_reduction)
        defender.tire_health -= final_damage
        
        print(f"Attack damage: {damage}, Defense reduction: {damage_reduction}, Final damage: {final_damage}")
        print(f"{defender.name} - Tire Health: {defender.tire_health}, Fuel: {defender.fuel}")
        
        if defender.tire_health <= 0 or defender.fuel <= 0:
            print(f"{defender.name} has been defeated!")
            print(f"WINNER: {attacker.name}")
            return True
        
        self.currentdriver = defender  # Switch to the next driver
        return False
    
    def start_race(self):
        print("=" * 52)
        print("           F1 RACE SIMULATION STARTED")
        print("=" * 52)
        print(f"\n  Driver 1: {self.driver1.name}")
        print(f"  Driver 2: {self.driver2.name}")
        print("\n Race begins now!")
        
        winner = None
        while True:
            result = self.startturn()
            if result == True:  # Someone won
                winner = self.driver1.name if self.driver2.tire_health <= 0 or self.driver2.fuel <= 0 else self.driver2.name
                break
            elif result == "draw":  # Both can't continue
                print("\n RACE RESULT: DRAW")
                break
            elif result == "switch":  # Skip turn, try other driver
                continue
        
        print("\n" + "="*60)
        print("                   FINAL RACE RESULTS")
        print("="*60)
        
        if winner:
            loser = self.driver2.name if winner == self.driver1.name else self.driver1.name
            print(f" CHAMPION: {winner}")
            print(f" DEFEATED: {loser}")
        else:
            print(" RESULT: DRAW - Both drivers unable to continue")
            
        print(f"\n FINAL STATISTICS:")
        print(f"   Total rounds: {self.rounds}")
        print(f"   {self.driver1.name}: Tire Health {self.driver1.tire_health}, Fuel {self.driver1.fuel}")
        print(f"   {self.driver2.name}: Tire Health {self.driver2.tire_health}, Fuel {self.driver2.fuel}")
        print("\n Race simulation completed!")
        print("="*60)
        
# Main
max_verstappen = Verstappen()
hassan_mostafa = Mostafa()
race = Race(max_verstappen, hassan_mostafa)
race.start_race()
