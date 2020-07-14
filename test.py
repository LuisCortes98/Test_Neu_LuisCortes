import pyodbc

Cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-BJB95UB;UID=luis;PWD=1234')
Cursor = Cnxn.cursor()
inp = ""
dato= ""

print("Este programa le permite consultar la poblacion por ciudades segun el nivel que se consulte, si se busca un pais, se debería mostrara sus estados y cada estado sus ciudades con su respectiva poblacion; sí se consulta un estado se mostrara el estado con todas sus ciudades y su respectiva poblacion; y por ultimo si se consulta una ciudad se mostrara su poblacion. \n")

while 1:
    inp = input("Escriba 1 si desea consultar por pais, 2 si desea consultar por estado y 3 si desea consultar por ciudad \n")

    if inp == 1:
        dato = raw_input("Ingrese el pais ")
        Cursor.execute("SELECT Name_Country From [Test].[dbo].[Countries] where Name_Country = (?)", dato)
        Table = Cursor.fetchall()
        if Table != None:
            Cursor.execute("SELECT a.Name_Country, b.Name_State, c.Name_City, c.Population_City FROM [Test].[dbo].[Countries] as a left join [Test].[dbo].[States] as b ON a.Id_Country = b.Id_Country left join [Test].[dbo].[Cities] as c ON b.Id_State = c.Id_State WHERE a.Name_Country = (?) ORDER BY b.Id_State desc", dato)
            Table = Cursor.fetchall()
            print (Table)
        else:
            print ("No se encuentra el pais")
        break

    if inp == 2:
        dato = raw_input("Ingrese el estado ")
        Cursor.execute("SELECT Name_State From [Test].[dbo].[States] where Name_State = (?)", dato)
        Table = Cursor.fetchall()
        if Table != None:
            Cursor.execute("SELECT Name_State, Name_City, Population_City FROM [Test].[dbo].[States] as a left join [Test].[dbo].[Cities] as b ON a.Id_State = b.Id_State WHERE Name_State = (?) ORDER BY a.Id_State DESC", dato)
            Table = Cursor.fetchall()
            print (Table)
        else: 
            print ("No se encuentra el estado")
        
        break

    if inp == 3:
        dato = raw_input("Ingrese la ciudad ")
        Cursor.execute("SELECT Name_City From [Test].[dbo].[Cities] where Name_City = (?)", dato)
        Table = Cursor.fetchall()
        if Table != None:
            Cursor.execute("SELECT Name_City, Population_City FROM [Test].[dbo].[Cities] WHERE Name_City = (?)", dato)
            Table = Cursor.fetchall()
            print (Table)
        else:
            print ("No se encuentra la ciudad")
        break

    if inp > 3:
        print("Opcion no valida")
        break


    
    
    
