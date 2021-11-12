print( "BIENVENIDOS A TU APLICATIVO LABORAL"   )

user = input("USER: ")
password=(input("PASSWORD: ") )
 

if password==("idat"): print("#######BIENVENIDOS A SYM SOLUCIONES TECNOLOGICAS ############")
else: print("ERROR DE AUTENTICAICON")
      
while password!=("idat"):
      print("ERROR DE AUTENTICAICON")
      password=(input("PASSWORD: ") )
      if password==("idat"): print("#######BANNERBIENVENIDOS A ORACLE############")
      else: print("ERROR DE AUTENTICAICON")
print("TIENES 10 INSTALACIONES 10 AVERIAS Y 10 MIGRACIONES EN TU APLICATIVO")    
def trabajos():
    averias=20
    instalaciones=40
    migraciones=15
    instalaciones=int(input("INGRESA TUS INSTALACIONES EJECUTADAS: "))
    averias=int(input("INGRESA TUS AVERIAS EJECUTADAS: "))
    migraciones=int(input("INGRESA TUS MIGRACIONES EJECUTADAS: "))
    print(instalaciones*40 + averias*20 + migraciones*15)
trabajos()
print("BUENAS TARDES MUY BUEN TRABAJO")