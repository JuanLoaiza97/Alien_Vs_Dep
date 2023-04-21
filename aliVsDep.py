import random

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.down = None
        self.up = None

class LinkedList:
    def __init__(self,n ):
        self.n = n
        r = random.randrange(3)
        if r == 1:
            self.head = Node("+")
        elif r == 2:
            self.head = Node("-")
        else:
            self.head = Node("")
        self.size_hor = 1
        self.size_ver = 1
        self.lifeA = 50
        self.lifeD = 50

    def add(self):
        current = self.head
        n = self.n
        i = 1
        while i <= n:
            r = random.randrange(3)
            if r == 1:
                new_hor = current.right = Node("+")
            elif r == 2:
                new_hor = current.right = Node("-")
            else:
                new_hor = current.right = Node("")
            new_hor.left = current
            k = 1
            curd = current
            while k < n:
                r = random.randrange(3)
                if r == 1:
                    new_ver = curd.down = Node("+")
                elif r == 2:
                    new_ver = curd.down = Node("-")
                else:
                    new_ver = curd.down = Node("")
                new_ver.up = curd
                curd = curd.down
                k += 1
                self.size_ver += 1
            current = current.right
            i += 1
            self.size_hor += 1
        current.value = " "
        current = None

    def ordernar_der(self):
            current = self.head
            while current.right != None:
                down =  current.down
                donwr = current.right.down
                while down != None:
                    if donwr != None:
                        down.right = donwr
                        down = down.down
                        donwr = donwr.down
                    else:
                        break
                current = current.right

    def ordernar_izq(self):
        current = self.head.right
        while current.right != None:
            down =  current.down
            donwr = current.left.down
            while down != None:
                if donwr != None:
                    down.left = donwr
                    down = down.down
                    donwr = donwr.down
                else:
                    break
            current = current.right

    def pos_dep(self, l):
        current = self.head
        x = 0
        y = 0 
        if current.value != "👽":
            while x <= l[0]:
                if x ==  l[0]:
                    break
                current = current.right
                x += 1
            currentc = current
            if l[1] != 0: 
                while y <= l[1]:
                    if y == l[1]:
                        break
                    y += 1
                    currentc = currentc.down
            if l[0] == 0 and l[1] == 0:
                current.value = "🤖"
            else:
                currentc.value = "🤖"
        else:
            pass


    def pos_alien(self, x, y):
        current = self.head
        i = 0
        j = 0 
        while i <= x:
            if i == x:
                break
            current = current.right
            i += 1
        currentc = current
        if y != 0: 
            while j <= y:
                if j == y:
                    break
                j += 1
                currentc = currentc.down
        if x == 0 and y == 0:
            current.value = "👽"
        else:
            currentc.value = "👽"

    def move_rightA(self):
        current = self.head
        while current.right != None:
            if current.value == "👽":
                if current.right.value == "+":
                    self.lifeA += 10
                elif current.right.value == "-":
                    self.lifeA -= 10
                elif current.right.value == "🤖":
                    self.lifeA -= 25
                    current.right.value += current.value
                    current.value = " "
                    return 
                current.right.value = current.value
                current.value = " "
                return
            elif current.value == "🤖👽":
                if current.right.value == "+":
                    self.lifeA += 10
                elif current.right.value == "-":
                    self.lifeA -= 10
                current.right.value = "👽"
                current.value = "🤖"
                return
            col = current
            while col != None:
                if col.value == "👽":
                    if col.right.value == "+":
                        self.lifeA += 10
                    elif col.right.value == "-":
                        self.lifeA -= 10
                    elif col.right.value == "🤖":
                        self.lifeA -= 25
                        col.right.value += col.value
                        col.value = " "
                        return 
                    col.right.value = col.value
                    col.value = " "
                    return
                elif col.value == "🤖👽":
                    if col.right.value == "+":
                        self.lifeA += 10
                    elif col.right.value == "-":
                        self.lifeA -= 10
                    col.right.value = "👽"
                    col.value = "🤖"
                    return
                col = col.down
            current = current.right
        
    def move_leftA(self):
        current = self.head
        while current.right != None:
                if current.value == "👽":
                    if current.left.value == "+":
                        self.lifeA += 10
                    elif current.left.value == "-":
                        self.lifeA -= 10
                    elif current.left.value == "🤖":
                        self.lifeA -= 25
                        current.left.value += current.value
                        current.value = " "
                        return 
                    current.left.value = current.value
                    current.value = " "
                    return
                elif current.value == "🤖👽":
                    if current.left.value == "+":
                        self.lifeA += 10
                    elif current.left.value == "-":
                        self.lifeA -= 10
                    current.left.value = "👽"
                    current.value = "🤖"
                    return
                col = current
                while col != None:
                    if col.value == "👽":
                        if col.left.value == "+":
                            self.lifeA += 10
                        elif col.left.value == "-":
                            self.lifeA -= 10
                        elif col.left.value == "🤖":
                            self.lifeA -= 25
                            col.left.value += col.value
                            col.value = " "
                            return 
                        col.left.value = col.value
                        col.value = " "
                        return
                    elif col.value == "🤖👽":
                        if col.left.value == "+":
                            self.lifeA += 10
                        elif col.left.value == "-":
                            self.lifeA -= 10
                        col.left.value = "👽"
                        col.value = "🤖"
                        return
                    col = col.down
                current = current.right

    def move_upA(self):
        current = self.head
        while current.right != None:
            if current.value == "👽":
                if current.up.value == "+":
                    self.lifeA += 10
                elif current.up.value == "-":
                    self.lifeA -= 10
                elif current.up.value == "🤖":
                    self.lifeA -= 25
                    current.up.value += current.value
                    current.value = " "
                    return 
                current.up.value = current.value
                current.value = " " 
                return
            elif current.value == "🤖👽":
                if current.up.value == "+":
                    self.lifeA += 10
                elif current.up.value == "-":
                    self.lifeA -= 10
                current.up.value = "👽"
                current.value = "🤖"
                return
            col = current
            while col != None:
                if col.value == "👽":
                    if col.up.value == "+":
                        self.lifeA += 10
                    elif col.up.value == "-":
                        self.lifeA -= 10
                    elif col.up.value == "🤖":
                        self.lifeA -= 25
                        col.up.value += col.value
                        col.value = " "
                        return 
                    col.up.value = col.value
                    col.value = " "
                    return
                elif col.value == "🤖👽":
                    if col.up.value == "+":
                        self.lifeA += 10
                    elif col.up.value == "-":
                        self.lifeA -= 10
                    col.up.value = "👽"
                    col.value = "🤖"
                    return
                col = col.down
            current = current.right

    def move_downA(self):
        current = self.head
        while current.right != None:
            if current.value == "👽":
                if current.down.value == "+":
                    self.lifeA += 10
                elif current.down.value == "-":
                    self.lifeA -= 10
                elif current.down.value == "🤖":
                    self.lifeA -= 25
                    current.down.value += current.value
                    current.value = " "
                    return
                current.down.value = "👽"
                current.value = " "
                return
            elif current.value == "🤖👽":
                    if current.down.value == "+":
                        self.lifeA += 10
                    elif current.down.value == "-":
                        self.lifeA -= 10
                    current.down.value = "👽"
                    current.value = "🤖"
                    return
            col = current
            while col != None:
                if col.value == "👽":
                    if col.down.value == "+":
                        self.lifeA += 10
                    elif col.down.value == "-":
                        self.lifeA -= 10
                    elif col.down.value == "🤖":
                        self.lifeA -= 25
                        col.down.value += col.value
                        col.value = " "
                        return 
                    col.down.value = "👽"
                    col.value = " "
                    return
                elif col.value == "🤖👽":
                    if col.down.value == "+":
                        self.lifeA += 10
                    elif col.down.value == "-":
                        self.lifeA -= 10
                    col.down.value = "👽"
                    col.value = "🤖"
                    return
                col = col.down
            current = current.right
        
            
    def traverse2(self):
        current = self.head
        col = current
        row = current
        for i in range(0,self.n):
            while current != None:
                print(current.value, ", ", end = " ")
                current = current.right
            row = row.down
            current = row
            print("\n")


turn = 1
while turn != 0:
    print("Bienvenido")
    n = int(input("Ingrese numero de elementos de la matriz:  "))
    ll = LinkedList(n)
    ll.add()
    ll.ordernar_der()
    ll.ordernar_izq()
    def pos_arb():
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        pos = [i, j]
        return pos
    pos = pos_arb()
    ll.pos_dep(pos)
    ll.traverse2()
    x = int(input("Ingrese posicion AlienX:  "))
    y = int(input("Ingrese posicion AlienY:  "))
    ll.pos_alien(x, y)
    ll.traverse2()
    while ll.lifeA >= 0:
        print("1 para mover derecha")
        print("2 para mover izquierda")
        print("3 para mover arriba")
        print("4 para mover abajo")
        print("5 para salir")
        move = int(input("Ingrese Movimiento:  "))
        if move == 1:
            ll.move_rightA()
        elif(move == 2):
            ll.move_leftA()
        elif(move == 3):
            ll.move_upA()
        elif(move == 4):
            ll.move_downA()
        elif(move == 5):
            turn = 0
            break
        ll.traverse2()
        print()
        print(ll.lifeA)
        if ll.lifeA <= 0:
            print("Perdiste mostro 💀")