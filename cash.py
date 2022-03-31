#!/usr/bin/python
import time#se usa para agregar retardos en el dia
import random
global clase,color,pais#vairables para la dificultad
global valor,impuestos,dinero_anterior,monto,excusa,contador
global cafe,limonada,oregano,azucar,piedra,insulina,petroleo,almas
global clase,cafe,cantidad,desicion,dinero,producto,vc,mvc,vl,mvl,s,y
global vc,vl,vo,va,vp,vi,vP,vA,vm
global mvc,mcl,mvo,mva,mvp,mvP,mvA,vm
global cafe,limonada,oregano,azucar,piedra,insulina
global x,i,y,cg,vc,vca,vm,ancho,alto#valores para la funcion graficadora
global co,ca,cp,ci,cA,diabetes#valores para sindrome de abstinencia
impulso_de_idiotez = 0
contador = 0#simboliza la persona que lleva tus cuentas de impuestos
excusa = 0
monto = 0
impuestos = 0
dinero_anterior = 0
dinero=100
clase = 15
color = 15
pais = 15
producto = " "
desicion = 0
cafe = 15
almas = 1
limonada = 0
oregano = 0
azucar = 5
piedra = 0
insulina = 0
petroleo = 0
valor = 0# lo uso para pasar mas facil los valores de cada producto
co = 0
ca = 0#consumo azucar
cp = 0
ci = 0
cA = 0#consumo almas
diabetes = 0
vida = 1#si llega a 0 te mueres
ciclos = 0# lo uso para contar dias
vm=0 #valor maximo usado para escalar el grafico
altura=0 #alto del grafico
ancho=0 #ancho del graifco
a=1 #valor que uso para trabajar lo aleatorio
maximo=100 #valor maximo para cambiar lo aleatorio aumentarlo aumenta la clase
mvc=10 #valor maximo variable en % para cafe
mvl=10 #valor maximo variable en % para limonada
mvo=10 #valor maximo variable en % para oregano
mva=10 #valor maximo variable en % para azucar
mvp=10 #valor maximo variable en % para piedra
mvi=10 #valor maximo variable en % para insulina
mvP=10 #valor maximo variable en % para petroleo
mvA=1 #valor maximo variable en % para almas
vc=1 #valor inicial del cafe
vl=1 #valor inicial limonada
vo=100 #valor inicial oregano
va=1000 #valor inicial azucar
vp=200 #valor inicial piedra
vi=500 #valor inicial insulina
vP=20000 #valor inicial petroleo
vA=4000000 #valor almas
cantidad = 0    #se usa para medir cantidad a comprar o vender
dia = 0
cafeina_recolectada = 0
acido_citrico_recolectado = 0
especias_recolectadas = 0
diabetes_granular_recolectada = 0
diabetes_granular_que_ingeriste = 0
piedras_recolectadas = 0
piedra_hinalada = 0
var=0#lo uso para mitigar UnboundLocalError: local variable 'cafe' referenced before assignment
dinero2 = 100#se usa para mitigar bugs al autoreferenciar la variable
cg = 0#contador grafico lo uso para cordinar el dia con el grafico
s=[["$ ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","  ","  ","  ","7 ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","0 ","0 ","  ","  ","  ","0 ","0 ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","0 ","  ","0 ","  ","0 ","  ","0 ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","0 ","  ","  ","0 ","  ","  ","0 ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","0 ","  ","  ","  ","  ","  ","0 ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","0 ","  ","  ","  ","  ","  ","0 ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","0 ","  ","  ","  ","  ","  ","0 ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","0 ","  ","  ","  ","0 ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","0 ","  ","0 ","  ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","  ","0 ","  ","  ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"],
   ["  ","  ","  ","  ","  ","  ","  ","  ","  ","8 ","  ","  ","  ","  ","  ","i ","  ","8","  ","  ","  ","  ","  ","  ","  ","8","  ","  ","  ","  ","  ","7","  ","  ","8","  ","  ","  ","  ","  ","7"]
   ]
i=20
x=0
y=0
vca=1#valor cafe anterior
int(dinero)
int(cafe)
int(cantidad)
int(var)
def mercado():
    global clase,vc,vl,vo,va,vp,vi,vP,vA,vm
    global cafe,limonada,oregano,azucar,piedra,insulina,almas
    global cantidad,desicion,dinero,producto,vc,mvc,vl,mvl
    global mvc,mcl,mvo,mva,mp,mvp,mvP,mvA,vm# maximos valores
    global x,i,y,cg,vc,vca,vm
    #a=random.randint(-60,100)
    #b = b+(b*(a/100))devuelve una suma de un porcentaje proporcional al valor del producto
    if clase > 9:
        a=random.randint(-1,mvA)#subida o bajada de almas
        vA = vA+(vA*(a/100))
        if vA < 1:
            vA=1

    if clase > 8:
        a=random.randint(-5,mvP)#subida o bajada de petroleo
        vP = vP+(vP*(a/100))
        if vP < 1:
            vP=1


    a=random.randint(-6,mvc)#subida o bajada de precio del cafe
    vc = vc+(vc*(a/100))
    if vc < 1:
        vc=1


    a=random.randint(-4,mvl)#subida o bajada de la limonada
    vl = vl+(vl*(a/100))
    if vl < 1:
        vl=1

    if clase > 6:#esto limita el procesamiento en niveles que no lo requieren
     a=random.randint(-5,mvo)#subida o bajada del oregano
     vo = vo+(vo*(a/100))
     if vo < 1:
         vo=1

     a=random.randint(-5,mva)#subida o bajada del azucar
     va = va+(va*(a/100))
     if va < 1:
         va=1
     a=random.randint(-5,mvp)#subida o bajada de la piedra
     vp = vp+(vp*(a/100))
     if vp < 1:
         vp=1
     a=random.randint(-5,mvi)#subida o bajada de insulina
     vi = vi+(vi*(a/100))
     if vi < 1:
         vi=1


def transaccion():
    global valor,impuestos
    global vc,vl,vo,va,vp,vi,vP,vA,vm
    global cafe,limonada,oregano,azucar,piedra,insulina,almas
    global cantidad,desicion,dinero,producto,vc,mvc,vl,mvl
    global mvc,mcl,mvo,mva,mp,mvp,mvP,mvA,vm# maximos valores
    global cafe,limonada,cantidad,desicion,dinero,producto,vc,vl
    cantidad = input("cantidad: ")
    try:
        cantidad=int(cantidad)
    except ValueError:
        print ("Escribe un numero, no una letra.")
        cantidad = 0
        input("presiona enter para continuar")


    if desicion == 2:#venta
        desicion = 0
        if cantidad <= producto:
            dinero = dinero+(cantidad*valor)
            producto = producto-cantidad
            print("+","{:,.2f}".format(cantidad*valor),"$")
            print('dinero restante:  ',"{:,.2f}".format(dinero),"$")
            #if (pais = 1):
            #if (pais = 1):
            #if (pais = 1):
            impuestos = ((cantidad*valor)/100)*60
            #valor = valor-((valor/10)*(cantidad/2))
        else:
            print("no tienes suficiente en stock")
            input("presione enter para continuar")


    if desicion == 1:#compra
        desicion = 0
        if (dinero-(cantidad*valor)>=0):
            producto=producto+cantidad
            dinero = dinero-(cantidad*valor)
            print("-","{:,.2f}".format(cantidad*valor),"$")
            print('dinero restante:  ',"{:,.2f}".format(dinero),"$")
            valor = valor+((valor/100000)*(cantidad/2))
        else:
            print("no tienes suficientes fondos")
            input("presione enter para continuar")

#$ valor de dinero
#C cafe
#L limonada
#O oregano
#A azucar
#P piedra
#I insulina
#V petroleo
#@ almas

def consumir():
    global cafe,limonada,oregano,azucar,piedra,insulina,petroleo,almas
    global clase,vc,vl,vo,va,vp,vi,vP,vA
    global co,ca,cp,ci,cA,diabetes
    print("elije un producto")

    if clase > 6:
        print("o oregano")
        print("a azucar")
        print("p piedra")
        print("i insulina")
    if clase > 9:
        print("@ alma")

    producto = input()
    if producto == "o":
        if oregano == 0:
            print("no tienes oregano")
        if oregano > 0:
            oregano = oregano-1
            print("hamon del bueno")
            impulso_de_idiotez=random.randint(1,10)#probabilidad de que hagas una pendejada
            if impulso_de_idiotez > 5:
                print("la mercancia era de la buena y sientes que tu pie te mira feo")
                print("estupidamente te disparas a ti en el pie")
                print("te llevan al hospital paramedicos")
                print("la factura del hospital es de 1000")
                input("presione enter para continuar")
                dinero = dinero-1000
                print("-1,000$")


    if producto == "a":
        if azucar == 0:
            print("no tienes azucar")
        if azucar > 0:
            azucar = azucar-1
            print("te dieron ganas de bailar un p***** cumbion bien loco")
            input("presione enter para continuar")
            impulso_de_idiotez=random.randint(1,10)#probabilidad de que hagas una pendejada
            if impulso_de_idiotez > 5:
                print("mientras caminas por la calle gritas:¡QUE SE ARMEN LOS P*****S CHING***ZOS!. y golpeas a un adulto mayor de 80 años")
                print("te arrestan. la fianza es de 10,000$")
                input("presione enter para continuar")
                dinero = dinero-10000
                print("-10,000$")


            if impulso_de_idiotez > 1:
              print("que se armen los p******* c******dazos")

    if producto == "p":
        if piedra == 0:
            print("no tienes piedra")
        if piedra > 0:
            piedra = piedra-1
            print("tan duro como el amor de papa :'v")
            input("presione enter para continuar")
    if producto == "i":
        if insulina == 0:
            print("no tienes insulina")
        if insulina > 0:
            insulina = insulina-1
            print("ella te desea dulces sueños(pero eres diabetico)>:D")
            input("presione enter para continuar")
    if producto == "@":
        if almas == 0:
            print("no tienes mas almas")
        if almas > 0:
            almas = almas-1
            cA = cA+1
            print("para llenar el vacio que ella te dejo al irse con otro")
            input("presione enter para continuar")

def productos():
    global valor
    global cafe,limonada,oregano,azucar,piedra,insulina,petroleo,almas
    global clase,vc,vl,vo,va,vp,vi,vP,vA
    global cantidad,desicion,dinero,producto,vc,mvc,vl,mvl
    global mvc,mcl,mvo,mva,mvp,mvP,mvA,vm# maximos valores
    global cafe,limonada,cantidad,desicion,dinero,producto,vc,vl
    print("elije un producto")
    print("c cafe")
    print("l limonada")
    if clase > 6:
        print("o oregano")
        print("a azucar")
        print("p piedra")
        print("i insulina")
    if clase > 8:
        print("v petroleo")
    if clase > 9:
        print("@ alma")
    producto = input()
    if producto == "c":
        producto = cafe
        valor = vc#vc = valor cafe
        transaccion()
        vc = valor
        cafe = producto
    if producto == "l":
        producto = limonada
        valor = vl
        transaccion()#vl = valor limonada
        vl = valor
        limonada = producto
    if producto == "o":
        producto = oregano
        valor = vo
        transaccion()#vo = valor oregano
        vo = valor
        oregano = producto
    if producto == "a":
        producto = azucar
        valor = va
        transaccion()#va = valor azucar
        va = valor
        azucar = producto
    if producto == "p":
        producto = piedra
        valor = vp
        transaccion()#vp = valor piedra
        vp = valor
        piedra = producto
    if producto == "i":
        producto = insulina
        valor = vi
        transaccion()#vi = valor insulina
        vi = valor
        insulina = producto
    if producto == "v":
        producto = petroleo
        valor = vP
        transaccion()#vP = valor petroleo
        vP = valor
        petroleo = producto
    if producto == "@":
        producto = almas
        valor = vA
        transaccion()#vA = valor Alma
        vA = valor
        almas = producto

def decidir():
    global impúestos,contador
    global clase,vc,vl,vo,va,vp,vi,vP,vA,vm
    global cafe,limonada,oregano,azucar,piedra,insulina,petroleo,almas
    global cantidad,desicion,dinero,producto,vc,mvc,vl,mvl
    global mvc,mcl,mvo,mva,mvp,mvP,mvA,vm# maximos valores
    #print('%.2f' % valor)redondea los decimales a solo 2
    #print("{:,}".format(valor))#escribe decimales en los valores grandes
    #print("{:,.2f}".format(valor))#convina redondeo y comas decimales
    #print("Total cost is: ${:,.2f}".format(total_amount))
    print('cafe:    ',"{:,.2f}".format(vc),'$')
    print('limonada:',"{:,.2f}".format(vl),'$')#print '%.2f' % vc esto redondea el valor
    if clase > 6:
        print('oregano: ',"{:,.2f}".format(vo),'$')
        print('azucar:  ',"{:,.2f}".format(va),'$')
        print('piedra:  ',"{:,.2f}".format(vp),'$')
        print('insulina:',"{:,.2f}".format(vi),'$')
    if clase > 8:
        print('petroleo:',"{:,.2f}".format(vP),"$")
    if clase > 9:
        print('almas:   ', "{:,.2f}".format(vA),"$")

    print('limonada restante:',"{:,}".format(limonada))
    if clase > 6:
        print('oregano restante: ',"{:,}".format(oregano))
        print('azucar restante:  ',"{:,}".format(azucar))
        print('piedra restante:  ',"{:,}".format(piedra))
        print('insulina restante:',"{:,}".format(insulina))
    if clase > 9:
        print('petroleo restante:',"{:,}".format(petroleo))
        print('almas restantes:  ',almas,' PD:se consume 1 cada 100 dias si llega a 0 mueres')

    print('cafe restante:    ',cafe,' PD:se consume 1 al dia si llega a 0 mueres')
    print('dinero restante:  ',"{:,.2f}".format(dinero),"$",'...tu billullo')
    print('dia:',dia)
    print('escribe: 1 = comprar, 2 = vender,3 = no hacer nada','4 = impirmir grafico')
    if clase > 6:
        print("5 = consumir")
    if clase > 1:
        print("6 = consultar deuda de impuestos, 7 = pagarle al contador")
    while desicion == 0:
        desicion = input()
        try:
            desicion=int(desicion)

        except ValueError:
            print ("Escribe un numero, no una letra.")
            input("presiona enter para continuar")
    if desicion == 7:
        print("le pagaste al contador")
        print("- 100.00 $")
        dinero = dinero - 100
        contador = contador + 30
        input("presione enter para continuar")
    if desicion == 6:
        print("deves:",impuestos)
        print("NOTA: los impuestos equivalen al 25% de todos tus ingresos")
        print("NOTA: puedes pagarle a un contador 100$ al mes para que te diga cuanto debes de impuestos cuando mas lo necesitas")
        input("presione enter para continuar")
    if desicion == 4:
        screen()
        input("presione enter para continuar")
    if desicion == 3:#nada
        print("sigamos")
    if desicion == 5:
        consumir()
    if desicion == 1:#compra
        productos()
    if desicion == 2:#venta
        productos()

    desicion = 0
def clases():
    print ("elije un personaje")
    print ("-1 comunista")
    print ("0 bagabundo")#cafe
    print ("1 pasante")#cafe
    print ("2 godinez")#cafe, impuestos
    print ("3 supervisor")# cafe, impuestos, empleados
    print ("4 empresario")#cafe, limonada, impuestos, empleados,
    print ("5 politico")#cafe, impuestos + y -,empleados, corrupcion(lavado)
    print ("6 banquero")#crea creditos y genera ganancias cafe, impuestos, corrupcion
    print ("7 traficante")#cafe, impuestos, oregano, azucar, piedra, insulina, sindrome de abstinencia
    print ("8 mafioso")#cafe, impuestos, oregano, azucar, sal, insulina, empleados, corrupcion
    print ("9 wuachicolero")#cafe, pero solo genera petroleo, impuestos,
    print ("9 creyente")#cafe, pero solo genera petroleo, impuestos,
    print ("9 sectario")#cafe, pero solo genera petroleo, impuestos,
    print ("10 la parca")#acceso total productos, almas, impuestos,
    print ("11 el diablo mismo")#acesso total productos, almas, empleados,impuestos


def nivel_de_dificultad():
    print ("elije dificultad social")
    print ("1 primer  mundo")
    print ("2 segundo mundo")
    print ("3 tercer  mundo")

def color_de_piel():
    print ("elije dificultad genetica")
    print ("1 color piel")# random
    print ("2 color crotolamo")# random
    print ("3 ¿que es crotolamo?")# random
    print ("4 color popo de perro")# random
    print ("5 color olimpico")#random
    print ("6 color cientifico")#random
    print ("7 color patriota")#random
    print ("8 color letz meic ameryka greit agein")#blanco
    print ("9 color piedra")#blanco whitexican # te falta vitamina D
    print ("10 color maderus")#tostado tirandole a chicano
    print ("11 color chocolate indecizo")#cafe
    print ("12 color politicamente correcto")#negro invisible de noche
def resumen_dificultad():
    print ("resumen de dificultad:","pais =",pais,"color de piel =",color,"clase social =",clase)
def seleccion_de_dificultad():
    global clase,color,pais
    while clase !=range(-1,11):
        #nivel_de_dificultad()
        clases()
        clase = input()
        print("clase =",clase)
        try:
            clase=int(clase)
            break
            #return (clase)
        except ValueError:
            print ("Escribe un numero, no una letra.")
            input("presione enter para continuar")
            #time.sleep(1)
            #return
    while pais !=range(0,3):
        nivel_de_dificultad()
        pais = input()
        print("pais =",pais)
        try:
            pais=int(pais)
            break
        except ValueError:
            print ("Escribe un numero, no una letra.")
            input("presione enter para continuar")
            #time.sleep(1)
            #return
    while color !=range(1,12):
        #nivel_de_dificultad()
        color_de_piel()
        color = input()
        print("color =",color)
        try:
            color=int(color)
            break
        except ValueError:
            print ("Escribe un numero, no una letra.")
            input("presione enter para continuar")
            #time.sleep(1)
            #return
    resumen_dificultad()
def comparar():
    global clase,vc,vl,vo,va,vp,vi,vP,vA
    if clase == 1:
        print(" ")
    if clase == 2:
        print(" ")
    if clase == 3:
        print(" ")
def comparar2():
    global clase,vc,vl,vo,va,vp,vi,vP,vA,vm
    if vc>vm:
        vm=vc
    if vc>10000000000:
        vc=10000000000
    if vl>10000000000:
        vl=10000000000
    if vo>10000000000:
        vo=10000000000
    if va>10000000000:
        va=10000000000
    if vp>10000000000:
        vp=10000000000
    if vi>10000000000:
        vi=10000000000
    if vP>10000000000:
       vP=10000000000
    if vA>10000000000:
       vA=10000000000
def screen():#screen

    #global s,y
    #print(s[0][0])
    print("vca:",vca,"vc:",vc)
    for y in range(0, 29, 1):
             print(s[y][0],s[y][1],s[y][2],s[y][3],s[y][4],s[y][5],s[y][6],s[y][7],s[y][8],s[y][9],s[y][10],s[y][11],s[y][12],s[y][13],s[y][14],s[y][15],s[y][16],s[y][17],s[y][18],s[y][19],s[y][20],s[y][21],s[y][22],s[y][23],s[y][24],s[y][25],s[y][26],s[y][27],s[y][28],s[y][29],s[y][30],s[y][31],s[y][32],s[y][33],s[y][34],s[y][35],s[y][36],s[y][37],s[y][38])
def screen_registro():
     global x,i,y,cg,vc,vca,vm,ancho,alto
     if ancho == 1:
         for x in range(2, 15, 1):
             for alto in range(0, 29, 1):
                 s[alto][x-1] = s[alto][x]
                 s[alto][x]= " "

     y = y+2
     if y > 15:
         y = 0
         ancho = 1

     if vca > vc:
         vca = vc
         i = i+1
         if i >28:
             i = 29
     if vca < vc:
         vca = vc
         i=i-1
         if i < 1:
             i = 0


     s[i][y] = "{:,.2f}".format(vc)
     """
     for y in range(1, 29, 1):
         s[28][y] = y
     for y in range(0, 29, 1):
        s[y][0] = "{:,.2f}".format(x*i)
        i=i-1
        s[28][0] = "{:,.2f}".format(x*0)#pone un 0 en la cordenada que cartesianamente deveria ser 0,0
"""
def acienda():
    global dinero_anterior,dinero,impuestos,monto,desicion,excusa,contador
    monto = 0
    print("contador dias de contrato restantes", contador)
    #impuestos = ((dinero-dinero_anterior)/100)*25
    if impuestos < 0:
        impuestos = 0
    if contador > 1:
        print("impuestos","{:,.2f}".format(impuestos))
    if contador == 1:
        print("el contrato de tu contador ya se vencio. renuevalo pagandole")
        input("presione enter para continuar")
    if contador < 0:
        contador = 0

    if dinero-dinero_anterior >= 1000:
        while impuestos > 0:
            while desicion == 0:
                time.sleep(2)
                print("hacienda ha detectado un ingreso particularmente sospechoso en tu cuenta bancaria")
                print("requisicion de honorarios fiscales porfavor")
                print("calcule cuantos impuestos debe y paguelos")
                if excusa < 3:
                    print("1 = dar una excusa")
                    print("2 = pagar, ")
                    desicion = input()
                try:
                    desicion=int(desicion)
                except ValueError:
                    print ("Escribe un numero, no una letra.")
                    desicion = 0
                    input("presione enter para continuar")

                if desicion == 2:
                    print("calcule el monto exacto con deciamles o superior")
                    while monto == 0:
                        monto = input()
                        try:
                            monto=float(monto)
                        except ValueError:
                            print ("Escribe un numero sin puntos ni comas")
                            monto = 0
                            input("presione enter para continuar")
                    if monto < impuestos:
                        print("ERROR!!!!")
                        print("debias:","{:,.2f}".format(impuestos))
                        print("se te añadira una multa de 100$ por intento de evasion de impuestos")
                        print("- 100.00 $")
                        dinero = dinero - 100
                        print("-","{:,.2f}".format(impuestos),"$")
                        dinero = dinero - impuestos
                        impuestos = 0
                        input("presione enter para continuar")
                        desicion = 0
                        monto = 0
                        return
                    if monto >= impuestos:
                        print("...(hojeando papeles)")
                        time.sleep(3)
                        print("todo en orden. tenga buen dia.")
                        dinero = dinero - monto
                        print("debias:","{:,.2f}".format(impuestos),"$","pagaste:","{:,.2f}".format(monto),"$")
                        impuestos = 0
                        input("presione enter para continuar")
                if desicion !=2 and desicion !=1 or (desicion !=1 and excusa >1):
                    desicion = 2

                if excusa < 3:
                    if desicion == 1:
                        print("1 = ahorita no joven")
                        print("2 = mi mama dice: que no esta en casa")
                        print("3 = el dinero no es mio, es de un amigo")
                        input()
                        excusa = excusa +1
                        print("esta bien, volveremos luego")
                        input("presione enter para continuar")
                        dinero_anterior = dinero
                        desicion = 0
                        monto = 0
                        return
    dinero_anterior = dinero
    desicion = 0
    monto = 0
def GAME_OVER():
    print("GAME OVER")
    print("resultados:")
    print("clase jugada: ",clase)#poner en clase 1 el string correspondiente
    print("dias: ",dia)
    print("cafeina recolectada: ",cafeina_recolectada)
    print("acido citrico recolectado: ",acido_citrico_recolectado)
    #print("almas encaminadas: ", petroleo_usado)
    #print("almas recolectadas: ")
    #print("almas consumidas: ")

seleccion_de_dificultad()# elije un nivel de dificultad
if clase == -1:
    for i in range (0,30):
        print("")
    print("los comunistas no creen en el capitalismo bobis")
    for i in range (0,10):
        print("")
    cafe = 0
while cafe>0:
    if cafe >15:
        print("tu cafe geneticamente modificado para pudrise rapido se ha deteriorado. solo puedes almacenar 15 unidades")
        print("PD: el cafe es vida. evita el exceso (no vivas, solo consume) ")
        cafe = 15
        input("presione enter para continuar")

    if limonada >20:
        print("tu limonada en polvo geneticamente modificada para pudrise rapido se ha deteriorado. solo puedes almacenar 20 unidades.")
        print("PD: si la vida te quita limones, sigue comprandole limonada en polvo a LEMON CORP®")
        cafe = 20
        input("presione enter para continuar")

    comparar2()

    if cg >= 29:# ayuda a regresar el contador grafico a 0 para ajustar el grafico
        cg = 0
    if clase > 9:#prueba para determinar si funciona la clase
        ciclos = ciclos+1

    if ciclos > 100:#inanicion de almas
        ciclos = 0
        if cA == 0:#consumo almas
            cafe = 0
            print("murio por inanicion de almas")
            input("presione enter para continuar")
            GAME_OVER()
    if clase > 1:
        acienda()
        contador = contador-1
    dia = dia+1#puntuacion en dias
    cg = cg+1#contador grafico
    cafe=cafe-1

    decidir()
    mercado()
    screen_registro()

    #time.sleep(1.5)

if cafe <= 0:
    GAME_OVER()

#afedo camate pofavo afedo CAMATE
def sindrome_de_abstinencia():
    global co,ca,cp,ci,cA,diabetes
    if ca >=1:
        ca = ca-1

    if ca == 0:
        print("no has bailado suficientes cumbiones locos")
        print("de la tristesa le pagas a alguien 100$ para que te de un abrazo")
        dinero = dinero-100
        input("presione enter para continuar")

def catastrofes():
    #pandemias
    #golpes de estado
    #pago de impuestos
    #asaltos
    #enfermedades
    #mandar saludar a tu madre
    sindrome_de_abstinencia()
    #catastrofes naturales terremotos inundaciones incendios meteoritos
    #


def contratos():
    rentame_tu_alma()
def info_mecanicas():
    print("sobre quien quieres saber sus mecanicas?")



def pasante():
     print("descripcion")
     """
     pasante_info =  ("pasante, debil y pobreton, no recibe pago por su trabajo como asistente a teimpo parcial,
                     "no tiene que pagar impuestos a no ser que reciba sospechosas ganancias de nose donde,
                     "su vida es simple y aburrida necesita consumir 1 taza de cafe al dia o morira ")
     print(pasante_info)
"""

def bagabundo():
    print("descripcion")
    """
    bagabundo_info =("tonto como una rocka y feo como una blasfemia la vida te ha dado la espalda y tu por tonto no le
                     "has agarrado las nalgas, estas en la calle sobreviviendo todo lo que puedes con la basura que
                     "encuentras
                     )
"""

def get_shortened_integer(number_to_shorten):
    """ Takes integer and returns a formatted string """
    trailing_zeros = floor(log10(abs(number_to_shorten)))
    if trailing_zeros < 3:
        # Ignore everything below 1000
        return trailing_zeros
    elif 3 <= trailing_zeros <= 5:
        # Truncate thousands, e.g. 1.3k
        return str(round(number_to_shorten/(10**3), 1)) + 'k'
    elif 6 <= trailing_zeros <= 8:
        # Truncate millions like 3.2M
        return str(round(number_to_shorten/(10**6), 1)) + 'M'
    else:
        raise ValueError('Values larger or equal to a billion not supported')
#>>> get_shortened_integer(2300)
#2.3k # <-- str

#>>> get_shortened_integer(1300000)
#1.3M # <-- str
def rentame_tu_alma():
    print(" ")
    """
    contrato_info = "hola que tal. soy mefistoteles bon strangl representante de SORTEAMEESTA.INC y estoy interesado en")
                    "rentar tu alma por el 1% de su valor actual con un pago de contado efectivo"
                    "en 15 dias"
    """
