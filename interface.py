from  operacoes.somar import Somar
from  operacoes.dividir import Dividir

class Interface:
    def __init__(self):
        pass 
    def execute():
        print("Qual é o cálculo que quer efetuar? x + - /")  
        res:str = input()
        print("Preciso que introduza dois valores:")
        x:float = float(input("x="))
        y:float = float(input("y="))
        if res =="+":
            s:object = Somar(x,y)
            res = s.executar()
            print("O valor da operação somar é:", res)
        elif res =="/":
            s:object = Dividir(x,y)
            res = s.executar()
            if type(res)==str:
                print (res)
            else:
                print("O valor da operação divisão é:",res)

        