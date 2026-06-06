'''
This project was coded myself
use of AI for examples to understand and deepen learning
'''


# imports
import time;
import random;

# constants
LINE_BREAKS = 44


# define main()
def main():
    stats = {
        "name" : "jimmy jawn",
        "health" : 100,
        "attack" : 3,
    }

    inventory = [
        {
            "name":"orange",
            "desc":"A round orange citrus fruit.",
            "health":50,
            "damage":5
        },
        {
            "name":"rope",
            "desc":"thick strand material used to bind, tie and whack things.",
            "ability":"tie",
            "health":0,
            "damage":5,
        },
        {
            "name":"bomb",
            "desc":"Ignitable device capable of explosive release.",
            "health":0,
            "damage":90,
        },
        {
            "name":"action figure",
            "desc":"Chuck Norris action figure capable of guaranteeing a perfect childhood.",
            "health":0,
            "damage":100,
        },
    ]

    enemyStats = [
        {
            "name": "goblin",
            "health": 12, 
            "attack": 4,
        },
        {
            "name": "frog",
            "health": 12, 
            "attack": 2,
        },
        {
            "name": "grandma",
            "health": 12, 
            "attack": 5,
        },
        {
            "name": "tadpole",
            "health": 1, 
            "attack": 0,
        }
    ]


    while (True):
        c = input(f">{"-"*LINE_BREAKS}\nMenu\n| 1. Profile\n| 2. Inventory\n| 3. Attack\n| 4. Quit\n: ")
        random_index = random.randint(0, len(enemyStats) - 1)
        if not c.isdigit():
            print("Enter integer between 1 and 4.")
            continue
        c = int(c)
        if c < 1 or c > 4:
            print("Enter integer between 1 and 4.")

        if c == 1:
            CheckStats(stats)
        elif c == 2:
            CheckInventory(inventory, stats)
        elif c == 3: 
            Attack(stats, enemyStats[random_index])
        elif c == 4:
            print(f">{"-"*LINE_BREAKS}\nThank you for playing.")
            break


# by creating one time delay function and plugging it into the end of each function, we can tweak in one place and have it change for all places.
def TimeDelay(s):
    primary = 1.5
    secondary = primary+1
    tertiary = primary+2

    if s == 1:
        time.sleep(primary)
    elif s == 2:
        time.sleep(secondary)
    elif s == 3:
        time.sleep(tertiary)


def CheckStats(stats):
    print(f"{"-"*LINE_BREAKS}\nUser Stats <3\n| name: {stats["name"]}\n| health: {stats["health"]}\n| attack: {stats["attack"]}")
    TimeDelay(1)
    

def CheckInventory(inventory, stats):
    while (True):
        found = False
        # print(f"Inventory\n| {", ".join(inventory["name"])}\n>{("-")*LINE_BREAKS}")
        print(f"{'-' * LINE_BREAKS}\nInventory\n| {', '.join(item['name'] for item in inventory)}\n>{'-' * LINE_BREAKS}")
        c = input("Select Item\n: ")

        if c == "" or c == " " or c == "done" or c == "n/a" or c == "na":
            break
        else:
            for i in inventory:
                if c == i["name"]:
                    found = True
                    inventory.remove(i)
                    UpdateStats(i, stats)

            if not found:
                print("Item not found.")
        TimeDelay(1)


def UpdateStats(i, stats):
    stats["health"] += i["health"]
    CheckStats(stats)
    # if the item is used on someone else, I'll need to code in their stats and the shift of health by damage recieved

def Attack(stats, enemyStats):
        print(f">{"-"*LINE_BREAKS}\nA {enemyStats["name"]} appeared!\n| Health: {enemyStats["health"]} -- Attack: {enemyStats["attack"]}")
        while (True):
            c = input("Attack?\n(y/n): ")

            if c == "y":
                enemyStats["health"] = enemyStats["health"] - stats["attack"]
                print(f"{enemyStats["name"]}\n| Health: {enemyStats["health"]}")
                if (enemyStats["health"]<=0):
                    print(f"{enemyStats["name"]} defeated!")
                    break
                TimeDelay(1)
                print(f"{enemyStats["name"]} attacks! - {enemyStats["attack"]}")
                stats["health"] = stats["health"] - enemyStats["attack"]
                print(f"{stats["name"]}\n| Health: {stats["health"]}")
                if (stats["health"]<=0):
                    print(f"GAME OVER")
                    break
                TimeDelay(1)
            else:
                print("You left them alone.")
                break   


# main function to call the whole program
main()

'''
ISSUES

Once all enemies are at 0 health or lower, the list loops back around and reuses the dead ones.

Inability to use items on enemies (likely update the choice from fight or flight to a multi select battle menu, also have to figure out how to access item select menu from within the attack func.)

''' 
