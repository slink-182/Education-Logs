# purpose of this file it to test the use of an inventory with using items that heal the player

def main():
    '''
    main will be used to run the menu for actions
    '''
    userInfo = {
            'name' : 'mark', 
            'desc' : 'a goofy goober',
            'health' : 9,
            'attack' : 3,
        }
    
    i = userInfo

    inventory = [
        {'name' : 'orange', 'desc' : 'a round orange citrus fruit', "heal" : 5},
        {'name' : 'apple','desc' : 'a firm red sweet fruit', "heal" : 5},
        {'name' : 'banana','desc' : 'long yellow fruit', "heal" : 5},
    ]
    j = inventory

    UseItem(i, j)

def UseItem(i, j):
    
    while (True):
        # print the full inventory,
        for row in j:
            print(f"{row['name']} : {row['desc']}")

        # select item to use
        c = input("select item to use\n: ")
        
        for row in j:
            if row['name'] == c:
                j.remove(row)
                # calculate how item will effect stats
                i['health'] += row['heal']
                break

        # print player stats
        print(f"{i['name']} : {i['health']}")
        
        if c == "q":
            break

    
main()

'''
incorporate main select menu for actions

plug in use item 

'''