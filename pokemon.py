import mysql.connector
import getpass

try:
    pw = getpass.getpass('password: ')

    cnx = mysql.connector.connect(
        user='lx1107',
        password=pw,
        host='127.0.0.1',
        database='lx1107_pokemon'
    )
    cnx.autocommit = True
    choice="A"
    
    while choice != "q" or choice != "Q":

        print("Welcome to pokemon dictionary! What do you want to do?")
        print("1. Search pokemon by name")
        print("2. Search pokemon by region")
        print("3. Search pokemon by type")
        print("4. Check my team")
        print("Q for quit")

        choice = input("Please enter the number represent your choice\n")
        cursor = cnx.cursor(buffered = True)

        if choice == "1":
            pokemon = input("Which pokemon you would like to know about ;)\n")
            query = """SELECT Pokemon.id,Pokemon.Name, Pokemon.typeName, Region.Name AS region
                        From Pokemon
                        INNER JOIN Region ON Pokemon.regionId = Region.id
                        WHERE Pokemon.Name LIKE "%s";"""%pokemon
            cursor.execute(query)
            for(id,Name,typeName, region) in cursor:
                print("Pokemon Id: ",id,"Pokemon name: ", Name, ", Type name: ", typeName,", Region name: ", region, sep="")
            haha=input("Do you want add any of those pokemon to your team?(y/n)\n")
            if haha == "y":
                pokId=input("please give me the pokemon id you want to add in :)))\n")
                query = """SELECT pokemonId FROM MyTeam WHERE pokemonId = %s;"""%pokId
                cursor.execute(query)
                if cursor.rowcount != 0:
                    print("You can't be this greedy to have two same pokemon in your team. Allison said no. Sorry you but deserve this.\n")
                else:
                    query = """SELECT Pokemon.id,Pokemon.Name, Pokemon.typeName, Region.name AS region
                        From Pokemon
                        INNER JOIN Region ON Pokemon.regionId= Region.id
                        WHERE Pokemon.Name LIKE "%s" AND Pokemon.id = %s;"""%(pokemon,pokId)
                    cursor.execute(query)
                    if cursor.rowcount == 0:
                        print("HUH THIS IS NOT IN THE POKEMON ABOVE I MEAN I UNDERSTAND YOU WANT TO ADD IT THERE BUT WHY YOU DO THIS IT HURTS\n")
                    else:
                        query = """SELECT * FROM MyTeam;"""
                        cursor.execute(query)
                        if cursor.rowcount >= 6:
                            print("BUT YOU ALREADY GOT 6 POKEMONS I THOUGHT THIS IS ENGOUGH FOR YOU\n I'll tell mom if you keep more 6 pokemons. That's the rule.\n")
                        else:
                            query = """INSERT INTO MyTeam (pokemonId) VALUES (%s);"""%pokId
                            cursor.execute(query)
                            print("Pokemon is successfully added!\n")
            else:
                print("OK nvm")
        elif choice == "2":
            regionName=input("Which region you would like to know about :D\n")
            query = """SELECT Pokemon.id, Pokemon.Name, Pokemon.typeName, Region.name AS region
                        From Pokemon
                        INNER JOIN Region ON Pokemon.regionId = Region.id
                        WHERE Region.Name LIKE "%s";"""%regionName
            cursor.execute(query)
            for(id,Name,typeName, region) in cursor:
                print("Pokemon Id: ", id ,", Pokemon name: ", Name, ", Type name: ", typeName,", Region name: ", region, sep="")
            go=input("Do you want add any of those pokemon to your team?(y/n)\n")
            if go == "y":
                pokId=input("please give me the pokemon id you want to add in :)))\n")
                query = """SELECT pokemonId FROM MyTeam WHERE pokemonId = %s;"""%pokId
                cursor.execute(query)
                if cursor.rowcount != 0:
                    print("You can't be this greedy to have two same pokemon in your team. Allison said no. Sorry you but deserve this.\n")
                else:
                    query = """SELECT Pokemon.id,Pokemon.Name, Pokemon.typeName, Region.name AS region
                        From Pokemon
                        INNER JOIN Region ON Pokemon.regionId= Region.id
                        WHERE Region.Name LIKE "%s" AND Pokemon.id = %s;"""%(regionName,pokId)
                    cursor.execute(query)
                    if cursor.rowcount == 0:
                        print("HUH THIS IS NOT IN THE POKEMON ABOVE I MEAN I UNDERSTAND YOU WANT TO ADD IT THERE BUT WHY YOU DO THIS IT HURTS\n")
                    else:
                        query = """SELECT * FROM MyTeam;"""
                        cursor.execute(query)
                        if cursor.rowcount >= 6:
                            print("BUT YOU ALREADY GOT 6 POKEMONS I THOUGHT THIS IS ENGOUGH FOR YOU\n I'll tell mom if you keep more 6 pokemons. That's the rule.\n")
                        else:
                            query = """INSERT INTO MyTeam (pokemonId) VALUES (%s);"""%pokId
                            cursor.execute(query)
                            print("Pokemon is successfully added!\n")

            else:
                print("OK nvm")

        elif choice == "3":
            type = input("Which type you would like to know about :P\n")
            typeNameNew = "%" + type + "%"
            query = """SELECT Pokemon.id,Pokemon.Name, Pokemon.typeName, Region.name AS region
                        From Pokemon
                        INNER JOIN Region ON Pokemon.regionId= Region.id
                        WHERE Pokemon.typeName LIKE "%s";""" %typeNameNew
            cursor.execute(query)
            for(id,Name,typeName, region) in cursor:
                print("Pokemon Id: ",id,", Pokemon name: ", Name, ", Type name: ", typeName,", Region name: ",region,sep="")
            huh=input("Do you want add any of those pokemon to your team?(y/n)\n")
            if huh == "y":
                pokId=input("please give me the pokemon id you want to add in :)))\n")
                query = """SELECT pokemonId FROM MyTeam WHERE pokemonId = %s;"""%pokId
                cursor.execute(query)
                if cursor.rowcount != 0:
                    print("You can't be this greedy to have two same pokemon in your team. Allison said no. Sorry you but deserve this.\n")
                else:
                    query = """SELECT Pokemon.id,Pokemon.Name, Pokemon.typeName, Region.name AS region
                        From Pokemon
                        INNER JOIN Region ON Pokemon.regionId= Region.id
                        WHERE Pokemon.typeName LIKE "%s" AND Pokemon.id = %s;"""%(typeNameNew,pokId)
                    cursor.execute(query)
                    if cursor.rowcount == 0:
                        print("HUH THIS IS NOT IN THE POKEMON ABOVE I MEAN I UNDERSTAND YOU WANT TO ADD IT THERE BUT WHY YOU DO THIS IT HURTS\n")
                    else:
                        query = """SELECT * FROM MyTeam;"""
                        cursor.execute(query)
                        if cursor.rowcount >= 6:
                            print("BUT YOU ALREADY GOT 6 POKEMONS I THOUGHT THIS IS ENGOUGH FOR YOU\n I'll tell mom if you keep more 6 pokemons. That's the rule.\n")
                        else:
                            query = """INSERT INTO MyTeam (pokemonId) VALUES (%s);"""%pokId
                            cursor.execute(query)
                            print("Pokemon is successfully added!\n")
            else:
                print("OK nvm")

        elif choice == "4":
            i = 1;
            query = """SELECT Pokemon.id,Pokemon.Name, Pokemon.typeName, Region.Name AS region
                        FROM Pokemon
                        INNER JOIN Region ON Pokemon.regionId = Region.id
                        WHERE Pokemon.id IN (SELECT pokemonId FROM MyTeam);"""
            cursor.execute(query)
            for(id,Name,typeName, region) in cursor:
                print(i,". ", "Pokemon Id: ", id, " ,Pokemon name: ", Name, ", Type name: ", typeName,", Region name: ",region,sep="")
                i = i+1

        elif choice == "Q" or choice == "q":
            break

        else:
            print("It's not a valid command, please try agaiiiin?\n")

except mysql.connector.Error as err:
    print(err)
else:
    #Invoked if no exception was thrown
    cnx.close()
