
'''1) Un hombre desea saber cuanto dinero se genera por
 concepto de intereses sobre la cantidad que tiene en inversión
  en el banco. El decidirá reinvertir los intereses siempre y
cuando estos excedan a $7000, y en ese caso desea saber cuanto
 dinero tendrá finalmente en su cuenta.Inicio'''

p_int=float(input("digite interes "))
capital=float(input("digite la capital"))
interes= capital *p_int
if interes>7000:
        capfinal= capital+interes
        print(f"la capital fnal es:{capfinal}")

'''2) Determinar si un alumno aprueba a reprueba un curso, 
sabiendo que aprobara si su
promedio de tres calificaciones 
es mayor o igual a 70; reprueba en caso contrario.'''
calific1=float(input("digite nota1"))
calific2=float(input("digite nota2"))
calific3=float(input("digite nota3"))
promedio=(calific1+calific2+calific3)/3
print(f"promedio de la tres notas es :{promedio}")
if promedio>=70:
    print("alumno aprobo")
else:
    print("el alumno reprobo")

'''3) En un almacén se hace un 20% de descuento a los clientes 
    cuya compra supere los $1000
¿ Cual será la cantidad que pagara una persona por su compra?'''

compra=float(input("digite precio de la compra:"))
if compra>1000:
    descuento=compra * 0.20
else:
    descuento=0
totalpag= compra-descuento
print(f"el valor a pagar es:{totalpag}")

'''4) Un obrero necesita calcular su salario semanal, 
el cual se obtiene 
de la sig. manera:
Si trabaja 40 horas o menos se le paga $16 por hora
Si trabaja mas de 40 horas se le paga $16 por cada una de las primeras 40 horas y
$20 por cada hora extra.'''

hrstrabajadas=float(input("digite la horas trabajadas :"))
if hrstrabajadas>40:
    hrsextra=hrstrabajadas-40
    salario= hrsextra*20+40 *16
else:
    salario=hrstrabajadas*16

    print(f"el salario semanal es :{salario}")

'''6) Que lea dos números y los imprima en forma ascendente
Inicio'''
num1=int(input("digite numero1 :"))
num2=int(input("digite numero2 :"))
if num1<num2:
    print(num1,num2)
else:
    print(num2,num1)

'''7) Una persona enferma, que pesa 70 kg, se encuentra en reposo
 y desea saber cuantas calorías consume su cuerpo durante todo el 
 tiempo que realice una misma actividad. Las actividades que tiene
permitido realizar son únicamente dormir o estar sentado en reposo.
Los datos que tiene son que estando dormido consume 1.08 calorías 
por minuto y estando sentado en reposo consume 1.66 calorías por 
minuto.'''

actividad=input("digite la activida a realizar :")
tiempo=float(input("digite el tiempo de actividad"))
if actividad =='dormido':
    calorias=1.8*tiempo
else:
    calorias=1.66*tiempo
print(calorias)

'''8) Hacer un algoritmo que imprima el nombre de un articulo, 
clave, precio original y su precio con descuento. El descuento 
lo hace en base a la clave, si la clave es 01 el descuento
es del 10% y si la clave es 02 el descuento en del 20% (solo existen 
dos claves).'''
nom_articulo=input("digite el nombre del articulo :")
art_clave=int(input("digite clave de articulo :"))
precio_orig=int(input("digite el precio original:"))
if art_clave==1:
    precio_des=precio_orig-precio_orig*0.10
else:
    precio_des=precio_orig-precio_orig*0.20

print(f"el nombre del articulo es:{nom_articulo}"
      f" con la clave: {art_clave} con el valor original{precio_orig}"
      f"y con el valor descuento {precio_des} " )
print(f"el nombre de articulo es {nom_articulo}")
print(f"la clave del articulo es:{art_clave}")
print(f"el precio original es:{precio_orig}")
print(f"el precio original es:{precio_des}")

'''9 Hacer un algoritmo que calcule el total a pagar por la compra de camisas. Si se compran
tres camisas o mas se aplica un descuento del 20% sobre el total de la compra y si son
menos de tres camisas un descuento del 10%'''

num_camisas=int(input("ingrese numero de camisas"))
precio_cam=int(input("ingrese el precio de las camisas"))
tot_comp=num_camisas*precio_cam
if num_camisas>=3:
    totalpag=tot_comp-tot_comp*0.20
else:
    totalpagt=tot_comp-tot_comp*0.10
print(f"el total a pagar es : {totalpag}")

'''10) Una empresa quiere hacer una compra de varias piezas de la misma clase a una fabrica
de refacciones. La empresa, dependiendo del monto total de la compra, decidirá que hacer
para pagar al fabricante.
Si el monto total de la compra excede de $500 000 la empresa tendrá la capacidad
de invertir de su propio dinero un 55% del monto de la compra, pedir prestado al banco un
30% y el resto lo pagara solicitando un crédito al fabricante.
Si el monto total de la compra no excede de $500 000 la empresa tendrá capacidad
de invertir de su propio dinero un 70% y el restante 30% lo pagara solicitando crédito al
fabricante.
El fabricante cobra por concepto de intereses un 20% sobre la cantidad que se le pague a'''

costopza=int(input("digite el valor de la pizza :"))
num_pza=int(input("digite el numero de pizza"))
totcomp=costopza*num_pza
if totcomp>500000:
    cantven=totcomp*0.55
    prestamo=totcomp*0.30
    credito=totcomp*0.15
else:
    cantven=totcomp*0.70
    credito=totcomp*0.30
    prestamo=0
interes= credito*0.20

print("la cantidad vendida es ",cantven)
print("el prestamo es",prestamo)
print("el credito es",credito)
print("el interes es",interes)





