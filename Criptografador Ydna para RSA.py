#Criptografador Ydna para RSA
#Versão: 9.17.1
#Última atualização: 09/12/2017/09:49
#Criado por: Anderson Cortez

import math
sair = 0
done_asc = 0
done_pcode = 0
done_crypt = 0
mensagem_asc = ""
mensagem = ""
mensagem_p_codificar = ""
mensagem_p_decodificar = ""
mensagem_codificada = ""
mensagem_inteira = ""
mensagem_alfabetica = ""
mensagem_inteira_alfabetica = ""
primolistar = False
listaeprimo = False
listaprimos = ""
primoinicial = ""
primofinal = ""
atende_e = ""
lista_e = ""
primop = False
primoq = False
a = ""
n = ""
e = ""
p = ""
q = ""
d = ""
fn = ""
eok = False
num = 0
poss = 0
inv_mul = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or inv_mul(n, A%n, t, s-A//n*t, N or n),-1)[n<1]
while sair == 0:
        print ("")
        print (" ----------------------------------------- ")
        print ("|                                         |")
        print ("|    O que deseja fazer?                  |")
        print ("|                                         |")
        print ("|  1- Criar um conjunto de chaves RSA     |")
        print ("|  2- Criptografar em RSA                 |")
        print ("|  3- Descriptografar em RSA              |")
        print ("|  4- Converter ASC2 em letras            |")
        print ("|  5- Hackear P e Q de uma criptografia   |")
        print ("|  6- Hackear D de uma criptografia       |")
        print ("|  7- Gerar lista de primos               |")
        print ("|  8- Resetar variáveis                   |")
        print ("|  9- Sair                                |")
        print ("|  -Criado por Anderson Cortez            |")
        print ("|                                         |")
        print (" ----------------------------------------- ")
        print ("")
        menufunc = int(input(">"))
        if(menufunc == 1):
                while primop == False:
                        print ("Digite um valor primo P")
                        p = int(input("P:"))
                        for i in range(2, p-1):
                                a = p % i
                                if a == 0:
                                        primop = False
                                        print ("")
                                        print ("O valor digitado(",p,") não é primo")
                                        break
                                else:
                                        primop = True
                while primoq == False:
                        print ("Digite um valor primo Q")
                        q = int(input("Q:"))
                        for i in range(2, q-1):
                                a = q % i
                                if a == 0:
                                        primoq = False
                                        print ("")
                                        print ("O valor digitado(",q,") não é primo")
                                        break
                                else:
                                        primoq = True
                n = p * q
                fn = (p - 1)*(q - 1)
                while eok == False:
                        print ("Digite um valor entre 1 e", fn, "que não possua múltiplos comuns com", fn)
                        print ("Digite _lista_ para listar todos os valores que atendem a essa condição")
                        e = str(input("E:"))
                        if(e == "lista"):
                                for i in range(1, fn):
                                        if math.gcd(i, fn) == 1:
                                                atende_e = i
                                                lista_e += ";" + str(atende_e)
                                        else:
                                                xxx = 0
                                print ("Lista de números que atendem a condição:", lista_e)
                        else:
                                e = int(e)
                                if inv_mul(e,fn) == -1:
                                        print ("O valor digitado(",e,") não é valido")
                                        eok = False
                                else:
                                        eok = True
                d = (inv_mul(e,fn))
                d = int(d)
                print ("Inverso multiplicativo de", e, "usando o módulo", fn, "é:", d)
                print ("")
                print ("Chaves Calculadas!")
                print ("")
                print ("")
                print ("|-------------------------------------------------------|")
                print ("| Chaves Públicas(N =", n, ";E =", e, ";                 ")
                print ("| Chaves Privadas(P =", p, ";Q =", q, ";D =", d, ";      ")
                print ("|-------------------------------------------------------|")
                print ("")
        if(menufunc == 2):
                print ("Digite o valor de N e de E")
                n = int(input("N:"))
                e = int(input("E:"))
                print ("Digite a mensagem para pré-codificar")
                mensagem = str(input("MENSAGEM:"))
                precode = [ord(c) for c in mensagem]
                print ("A pré-codificação em blocos de sua mensagem é:", precode)
                print ("")
                print ("Agora, digite a pré-codificação bloco á bloco")
                print ("Quando terminar digite _fim_")
                while(done_pcode == 0):
                        bloco = str(input("BLOCO:"))
                        if(bloco == "fim"):
                                done_pcode = 1
                        else:
                                mensagem_p_codificar = int(bloco)
                                mensagem_p_codificar = (mensagem_p_codificar**e) % n
                                mensagem_p_codificar = str(mensagem_p_codificar)
                                mensagem_codificada += " " + mensagem_p_codificar
                print ("Mensagem Codificada!")
                print ("")
                print ("A mensagem é:", mensagem_codificada)
                print ("")
        if(menufunc == 3):
                print ("Digite o valor de P")
                p = int(input("P:"))
                print ("Digite o valor de Q")
                q = int(input("Q:"))
                n = p * q
                print ("Digite o valor de D")
                d = int(input("D:"))
                print ("Digite bloco por bloco da mensagem codificada")
                while(done_crypt == 0):
                        bloco = str(input("BLOCO:"))
                        if(bloco == "fim"):
                                done_crypt = 1
                        else:
                                mensagem_p_decodificar = int(bloco)
                                mensagem_p_decodificar = (mensagem_p_decodificar ** d) % n
                                mensagem_p_decodificar = str(mensagem_p_decodificar)
                                mensagem_inteira += " " + mensagem_p_decodificar
                                mensagem_alfabetica = int(mensagem_p_decodificar)
                                mensagem_alfabetica = chr(mensagem_alfabetica)
                                mensagem_inteira_alfabetica += mensagem_alfabetica
                print ("")
                print ("Mensagem Descriptografada!")
                print ("A mensagem em ASC2 é:", mensagem_inteira)
                print ("A mensagem em letras é:", mensagem_inteira_alfabetica)
        if(menufunc == 4):
                print ("Digite bloco por bloco da mensagem")
                print ("Digite _fim_ quando terminar")
                while(done_asc == 0):
                        bloco = input("BLOCO:")
                        if(bloco == "fim"):
                                done_asc = 1
                        else:
                                bloco = int(bloco)
                                decimal = chr(bloco)
                                mensagem_asc += decimal
                print ("A mensagem é", mensagem_asc)
        if(menufunc == 5):
                print ("Digite o valor de N para tentar descobrir os valores possíveis para P e Q")
                n = int(input("N:"))
                num = 0
                while(num < n):
                        num = num +1
                        poss = n / num
                        print (poss, "with", num)
        if(menufunc == 6):
                print ("Digite o valor de P")
                p = int(input("P:"))
                print ("Digite o valor de Q")
                q = int(input("Q:"))
                print ("Digite o valor de E")
                e = int(input("E:"))
                fn = (p - 1)*(q - 1)
                d = (inv_mul(e,fn))
                print ("Inverso multiplicativo de", e, "no módulo", fn, "é:", d)
        if(menufunc == 7):
                primoinicial = int(input("Insira o valor de inicio: "))
                primofinal = int(input("Insira o valor de fim: "))
                for y in range (primoinicial, primofinal + 1):
                        if y == 2:
                               primolistar = str(y)
                               listaprimos += primolistar + " ; "
                        if y == 3:
                               primolistar = str(y)
                               listaprimos += primolistar + " ; "
                        if y % 2 == 0 and y != 2:
                                xxx = 0
                        elif y % 3 == 0 and y != 3:
                                xxx = 0
                        else:
                                primo = False
                                for i in range (3, y):
                                        if y % i == 0:
                                                listaeprimo = False
                                                break
                                        else:
                                                listaeprimo = True
                                if listaeprimo == True:
                                    primolistar = str(y)
                                    listaprimos += primolistar + " ; "
                print (listaprimos)        
        if(menufunc == 8):
                done_asc = 0
                done_pcode = 0
                done_crypt = 0
                mensagem_asc = ""
                mensagem = ""
                mensagem_inteira = ""
                mensagem_p_codificar = ""
                mensagem_p_decodificar = ""
                mensagem_codificada = ""
                mensagem_alfabetica = ""
                mensagem_real_alfabetica = ""
                mensagem_inteira_alfabetica = ""
                listaprimos = ""
                primolistar = False
                listaeprimo = False
                primoinicial = ""
                primofinal = ""
                atende_e = ""
                lista_e = ""
                eok = False
                primop = False
                primoq = False
                n = ""
                e = ""
                p = ""
                q = ""
                d = ""
                fn = ""
                num = 0
                poss = 0
                print ("")
                print ("Variáveis Resetadas!")
                print ("")                              
        if(menufunc == 9):
                sair = 1
