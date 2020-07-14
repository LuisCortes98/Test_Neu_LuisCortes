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
        Cursor.execute("SELECT DISTINCT Name_State FROM [Test_Poblacion].[dbo].[Population_City] WHERE Name_Country = (?)", dato)
        Table_State = Cursor.fetchall()
        if Table_State != None:
            print (dato + "\n")
            for item in Table_State:
                print ("   " + item[0])
                print ("\n")
                Cursor.execute("SELECT [Name_City], [Population_City] FROM [Test_Poblacion].[dbo].[Population_City] WHERE Name_State = (?) order by Id_country, Id_state, Id_City", item)
                Table = Cursor.fetchall()
                for item2 in Table:
                    print ("       " + item2[0] +  " : "+ item2[1]+ "\n")
                    print ("\n")
        else:
            print ("No se encuentra el pais")
        break

    if inp == 2:
        dato = raw_input("Ingrese el estado: ")
        Cursor.execute("SELECT [Name_City], [Population_City] FROM [Test_Poblacion].[dbo].[Population_City] WHERE Name_State = (?)", dato)
        Table = Cursor.fetchall()
        print (dato + '\n')
        if Table != None:
            for item in Table:
                print ("   "+ item[0]+" : " + item[1])
                print ("\n")
        else:
            print ("No se encuentra el estado")
        break

    if inp == 3:
        dato = raw_input("Ingrese la ciudad: ")
        Cursor.execute("SELECT [Name_City], [Population_City] FROM [Test_Poblacion].[dbo].[Population_City] WHERE Name_City = (?)", dato)
        Table = Cursor.fetchone()
        if Table != None:
            print("   "+ Table[0]+" : " + Table[1])
        else:
            print ("No se encuentra la ciudad")
        break

    if inp > 3:
        print("Opcion no valida")
        break


    
    
    
