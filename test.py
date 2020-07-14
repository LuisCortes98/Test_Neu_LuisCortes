import pyodbc

Cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-BJB95UB;UID=luis;PWD=1234')
Cursor = Cnxn.cursor()
inp = ""
dato= ""

print("Este programa le permite consultar la poblacion por ciudades segun el nivel que se consulte, si se busca un pais, se debería mostrara sus estados y cada estado sus ciudades con su respectiva poblacion; sí se consulta un estado se mostrara el estado con todas sus ciudades y su respectiva poblacion; y por ultimo si se consulta una ciudad se mostrara su poblacion. \n")

while 1:
    inp = input("Escriba 1 si desea consultar por pais, 2 si desea consultar por estado y 3 si desea consultar por ciudad: \n")

    if inp == 1:
        dato = raw_input("Ingrese el pais: ")
        Cursor.execute("SELECT [Name_Country], [Name_State], [Name_City], [Population_City] FROM [Test_Poblacion].[dbo].[Population_City] WHERE Name_Country = (?) order by Id_country, Id_state, Id_City", dato)
        Table = Cursor.fetchall()
        if Table != None:
            for item in Table:
                print ("Pais:" + item[0] + " | " + "Estado:" + item[1] + " | " + "Ciudad:" + item[2] + " | " + "Poblacion:" + item[3])
                print ("\n")
        else:
            print ("No se encuentra el pais")
        break

    if inp == 2:
        dato = raw_input("Ingrese el estado: ")
        Cursor.execute("SELECT [Name_Country], [Name_State], [Name_City], [Population_City] FROM [Test_Poblacion].[dbo].[Population_City] WHERE Name_State = (?) order by Id_country, Id_state, Id_City", dato)
        Table = Cursor.fetchall()
        if Table != None:
            for item in Table:
                print ("Pais:" + item[0] + " | " + "Estado:" + item[1] + " | " + "Ciudad:" + item[2] + " | " + "Poblacion:" + item[3])
                print ("\n")
        else:
            print ("No se encuentra el estado")
        break

    if inp == 3:
        dato = raw_input("Ingrese la ciudad: ")
        Cursor.execute("SELECT [Name_Country], [Name_State], [Name_City], [Population_City] FROM [Test_Poblacion].[dbo].[Population_City] WHERE Name_City = (?) order by Id_country, Id_state, Id_City", dato)
        Table = Cursor.fetchall()
        if Table != None:
            for item in Table:
                print ("Pais:" + item[0] + " | " + "Estado:" + item[1] + " | " + "Ciudad:" + item[2] + " | " + "Poblacion:" + item[3])
                print ("\n")
        else:
            print ("No se encuentra la ciudad")
        break

    if inp > 3:
        print("Opcion no valida")
        break


    
    
    
