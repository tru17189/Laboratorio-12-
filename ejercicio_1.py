import psycopg2

con = psycopg2.connect(
            host="localhost",
            database="laboratorio12",
            user="postgres",
            password="pokopo"
)

cur = con.cursor()
###Inciso a###
print("Inciso a)")
precio = float(input('Escribe un precio: '))
cur.execute('SELECT "price" as price1 FROM "PC" GROUP BY "price" ORDER BY "price" desc')
rows = cur.fetchall()
resultado1 = 10000
for r in rows:
    precio_querry = float(r[0])
    resultado = precio_querry - precio
    if resultado1 > resultado*-1:
        resultado1 = resultado
        a = resultado1 + (precio_querry-resultado1)
    else:
        print('No existe nada con esta descripción')

cur.execute('SELECT "model", "speed", "ram", "hd" FROM "PC" WHERE "price" = (%s)',(a,))
rows_1 = cur.fetchall()
for r in rows_1:
    print('\tmodel: ',r[0])
    print('\tspeed: ',r[1])
    print('\tram: ',r[2])
    print('\thd: ',r[3])


###Inciso b###
print("\nInciso b)")
speed = float(input('Escribe la velocidad minima de la laptop: '))
ram = float(input('Escribe la ram minima de la laptop: '))
hd = float(input('Escribe el disco duro minimo de la laptop: '))
cur.execute('SELECT "speed", "ram", "hd" FROM laptop GROUP BY "speed", "ram", "hd" ORDER BY "speed", "ram" desc')
rows_2 = cur.fetchall()
for r in rows_2:
    a = float(r[0])
    b = float(r[1])
    c = float(r[2])
    if a <= speed and b <= ram and c <= hd:
        speed = r[0]
        ram = r[1]
        hd = r[2]
        cur.execute('SELECT "speed", "ram", "hd" FROM laptop WHERE speed = (%s) and ram = (%s) and hd = (%s)',(speed,ram,hd,))
        rows_3 = cur.fetchall()
        print('No existe nada con esta descripción')
        for r in rows_3:
            print('\tspeed: ',r[0])
            print('\tram: ',r[1])
            print('\thd: ',r[2])
    else:
        print('No existe nada con esta descripción')

###Inciso c###


cur.close()
con.close()
