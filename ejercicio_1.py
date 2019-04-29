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
precio = float(input('Escribe un precio(Dolares): '))
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
ram = float(input('Escribe la ram minima de la laptop(GB): '))
hd = float(input('Escribe el disco duro minimo de la laptop(GB): '))
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
    cur.execute('SELECT "model", "speed", "ram", "hd" FROM laptop WHERE speed = (%s) and ram = (%s) and hd = (%s)',(speed,ram,hd,))
    rows_3 = cur.fetchall()
    print('No existe nada con esta descripción')
    for r in rows_3:
        print('\tmodel: ',r[0])
        print('\tspeed: ',r[1])
        print('\tram: ',r[1])
        print('\thd: ',r[2])
else:
    print('No existe nada con esta descripción')

###Inciso c###
print("\nInciso c)")
dinero = float(input("Con cuanto dinero cuenta(DOLARES)?"))
a = dinero*0.75
b = dinero*0.25
speed = float(input("Cuanto es la velocidad minima que necesita?"))
cur.execute('SELECT "price", (SELECT "price" FROM "printer" WHERE "price" < (%s) limit 1) FROM "PC" GROUP BY "price" ORDER BY "PC"."price" desc',(b,))
rows_4 = cur.fetchall()
for r in rows_4:
    price_1 = float(r[0])
    price_2 = float(r[1])
if price_1 <= a and price_2 <= b:
    cur.execute('SELECT "speed" FROM "PC" GROUP BY "speed" ORDER BY "speed" asc')
    rows_5 = cur.fetchall()
    for r in rows_5:
        speed_1 = float(r[0])
    if speed_1 <= speed:
        cur.execute('SELECT "PC"."model", (SELECT "printer"."model" FROM "printer" WHERE "printer"."price"<= (%s) LIMIT 1) FROM "PC" WHERE "PC"."price"<= (%s) LIMIT 1', (a,b,))
        rows_6 = cur.fetchall()
        for r in rows_6:
            r1 = r[0]
            r2 = r[1]
        print('\tPC model: ',r1)
        print ('\tPrinter model: ',r2) 
    else:
        print("No existe nada con esa descripcion")            
else:
    print("No existe nada con esa descripcion")

###Iniciso e###
print("\nInciso d)")
s = 0
money = float(input("Cuanto dinero quiere analizar(GB): "))
moneyR = money 
cur.execute('SELECT "price" FROM "PC" GROUP BY "price"')
rows_7 = cur.fetchall()
while 0 < money:
    for r in rows_7:
        moneyD = float(r[0])
        money = money - moneyD
        s = s + 1
print("\tPodrias comprar",s,"PC")

s = 0
cur.execute('SELECT "price" FROM "laptop" GROUP BY "price"')
rows_8 = cur.fetchall()
money = moneyR
while 0 < money:
    for r in rows_8:
        moneyD = float(r[0])
        money = money - moneyD
        s = s + 1
print("\tPodrias comprar",s,"laptop")

s = 0
cur.execute('SELECT "price" FROM "printer" GROUP BY "price"')
rows_9 = cur.fetchall()
money = moneyR
while 0 < money:
    for r in rows_9:
        moneyD = float(r[0])
        money = money - moneyD
        s = s + 1
print("\tPodrias comprar",s,"printer")


cur.close()
con.close()
