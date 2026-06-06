# build a list of dictionaries that the user can select how to search for each person

def main():
    items = [
        {"name":"James Smith", "age":22, "id":1234},
        {"name":"Mando Lore", "age":24, "id":4321},
        {"name":"True Falls", "age":26, "id":1122},
        {"name":"Hope Loss", "age":28, "id":2211},
        {"name":"Jake State", "age":30, "id":2233},
        {"name":"Mason Mercy", "age":32, "id":3322},
        {"name":"Drake Mine", "age":34, "id":3344},
    ]
    while (True):
        select = int(input("Search by\n| 1. name\n| 2. age\n| 3. id\n| 4. quit\n: "))
        if select == 1:
            search = input("SEARCH NAME: ").lower()
        elif select == 2:
            search = int(input("SEARCH BY AGE: "))
            insertType = "age"
        elif select == 3:
            search = int(input("SEARCH BY ID: "))
            insertType = "id"
        elif select == 4:
            break
            
        for row in items:
            if row["name"].lower() == search:
                print(f"Name: {row["name"]} | Age: {row["age"]} | ID: {row["id"]}")

            elif row[insertType] == search:
                print(f"Name: {row["name"]} | Age: {row["age"]} | ID: {row["id"]}")

main()


