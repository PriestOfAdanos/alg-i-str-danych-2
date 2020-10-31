"""
Wartości które przchowuje w listach są zamieniane na zero w momencie kiedy nie należą już do listy.
Robię to dla czytelności w momencie kiedy chcemy zobaczyć które elementy są zajęte.
"""



class Stack(object):
    def __init__(self, size):
        self.size = size
        self.stack = [0]*self.size
        self.top = -1

    def push(self, x):
        if not self.top>=self.size:
            self.top+=1
            self.stack[self.top]=x
        else:
            print('overflow')

    def pop(self):
        if self.top>=0:
            self.stack[self.top]=0
            self.top-=1
            return self.stack[self.top+1]
    
    def find(self,query):
        for i in range(self.size):
            if query == self.stack[i]:
                return i


class Queue(object):
    def __init__(self, size):
        self.size = size
        self.que = [0]*self.size
        self.tail = 0
        self.head = 0

    def equeue(self,x):
        if self.tail < (self.size - 1) and self.head != self.tail + 1:
            self.que[self.tail] = x
            self.tail += 1  
        elif self.head != 0:
            self.que[self.tail] = x
            self.tail = 0
        else:
            print("Kolejka jest pełna")
    
    def dequeue(self):
        if self.head==self.size and self.tail!=0:
            self.head=0
        elif self.head==self.tail:
            print('Empty')
        else:
            self.head+=1
        x = self.que[self.head-1]
        self.que[self.head-1] = 0
        return x

    def find(self, query):
        if self.tail > self.head:
            for i in range(self.head, self.tail):
                if self.que[i] == query:
                    return i
        else:
            for i in range(0, self.size):
                if self.tail <= i < self.head:
                    continue
                if self.queue[i] > query:
                    return i
        return None

class PrirityQueue(Queue):
    def dequeue(self):
        if self.head==self.size and self.tail!=0:
            self.head=0
            print('huj')
        elif self.head==self.tail:
            print('Empty')
        else:
            self.head+=1
            print(self.head)
        current = self.head
        for index, priority in enumerate(self.que):
            if self.que[current]<priority:
                current=index
        x = self.que[current]
        self.que[current] = self.que[self.head-1]
        self.que[self.head-1] = 0
        return x


class Cell(object):
    def __init__(self, data=None,previous = None):
        self.is_guard = False
        self.data = data
        self.next = None
        self.previous = previous #previous parameter is not used in SingleLinkList


class SingleLinkList:
    def __init__(self):
        self.head = None

    def append(self, data):
        cell = Cell(data)
        if self.head is None:
            self.head = cell
        else:
            last = self.head
            while(last.next):
                last = last.next
            last.next=cell      

    def insert(self,data,index=0):
        cell = self.head
        if index<0:
            print('Wrong index')
        elif index == 0:
            cell = Cell(data)
            cell.next = self.head
            self.head = cell
        else:
            cell = self.head
            for i in range(index):
                if i+1==index:
                    cl = Cell(data)
                    cl.next = cell.next
                    cell.next = cl
                cell = cell.next
                
    def find(self, query):
        cell = self.head
        index = 0
        while cell is not None:
            if cell.data == query:
                return index
            index+=1
            cell = cell.next
                    
    def remove(self, index):
        cell = self.head
        if index<0:
            print('Wrong index')
        elif index == 0:
            self.head = self.head.next
        else:
            cell = self.head
            for i in range(index+1):
                if i+1==index:# and cell.next.next is not None:
                    cell.next = cell.next.next
                cell = cell.next

    def print_out(self):
        cell = self.head
        while cell is not None:
            if cell.data is not None:
                print(cell.data, end=',')
                if cell.next is None:
                    print("")
            cell = cell.next



class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        cell = Cell(data)
        if self.head is None:
            self.head = cell 
            self.tail = cell
        else:
            cell.previous = self.tail
            cell.previous.next = cell
            self.tail = cell
        

    def insert(self,data,index=0):
        cell = self.head
        if index<0:
            print('Wrong index')
        elif index == 0:
            cell = Cell(data)
            cell.next = self.head
            self.head = cell
        else:
            # cell = self.head
            for i in range(index):
                if i+1==index:
                    cl = Cell(data)
                    cl.next = cell.next
                    cl.previous = cell
                    cell.next = cl
                cell = cell.next
                
    def find(self, query):
        cell = self.head
        index = 0
        while cell is not None:
            if cell.data == query:
                return index
            index+=1
            cell = cell.next
                    
    def remove(self, index):
        cell = self.head
        if index<0:
            print('Wrong index')
        elif index == 0:
            self.head = self.head.next
        else:
            for i in range(index+1):
                if i==index:
                    if i==index:
                        if cell==self.head:
                            self.head = cell.next
                            cell.next.previous=cell.previous
                            cell.previous=None

                        elif cell==self.tail:
                            self.tail = cell.previous
                            cell.next=None
                            cell.previous.next =cell.next
                        else:
                            cell.next.previous=cell.previous
                            cell.previous.next =cell.next
                cell = cell.next

                

    def print_out(self):
        cell = self.head
        while cell is not self.tail:
            if cell.data is not None:
                print(cell.data, end=',')
                
            cell = cell.next
        print(self.tail.data)

     
               
            
class CycleList(DoubleLinkList):

    def append(self,data):
        cell = Cell(data)
        if self.head is None:
            self.head = cell 
            self.tail = cell
            self.head.previous = self.tail
            self.tail.next = self.head
        else:
            cell.previous = self.tail
            cell.previous.next = cell
            self.tail = cell

    def print_out(self):
        cell = self.head
        while cell != self.tail:
            if cell.data is not None:
                print(cell.data, end=',')
            cell = cell.next
        print(self.tail.data)


class GuardedList(DoubleLinkList):
    def __init__(self):
        self.head = None
        self.tail = None
        self.guard = Cell(None)
        self.guard.next = self.head
        self.guard.previous = self.tail    

    def append(self, data):
        cell = Cell(data)
        cell = Cell(data)
        if self.head is None:
            self.head = cell 
            self.tail = cell
            self.head.previous = self.tail
            self.tail.next = self.head
            self.guard.previous = self.tail  
            self.guard.next = self.head    
        else:
            cell.previous = self.tail
            cell.previous.next = cell
            self.tail = cell
            self.guard.previous = self.tail    

    def print_out(self):
        cell = self.head
        while cell != self.tail:
            if cell.data is not None:
                print(cell.data, end=',')    
            cell = cell.next
        print(self.tail.data)

    def insert(self,data,index=0):
        cell = self.head
        if index<0:
            print('Wrong index')
        elif index == 0:
            cell = Cell(data)
            cell.next = self.head
            self.head = cell
            self.guard.next = self.head
        else:
            for i in range(index):
                if i+1==index:
                    cl = Cell(data)
                    cl.next = cell.next
                    cl.previous = cell
                    cell.next = cl
                cell = cell.next
                
    def find(self, query):
        self.guard.data = query
        cell = self.head
        index = 0
        while cell is not None:
            if cell.data == self.guard.data:
                return index
            index+=1
            cell = cell.next
                    
    def remove(self, index):
        cell = self.head
        if index<0:
            print('Wrong index')
        elif index == 0:
            self.head = self.head.next
            self.guard.next = self.head
        else:
            for i in range(index+1):
                if i==index:
                    if cell==self.head:
                        self.head = cell.next
                        self.guard.next = cell.next
                        cell.next.previous=cell.previous
                        cell.previous=None

                    elif cell==self.tail:
                        self.tail = cell.previous
                        self.guard.previous = cell.previous
                        cell.next=None
                        cell.previous.next =cell.next
                    else:
                        cell.next.previous=cell.previous
                        cell.previous.next =cell.next
                cell = cell.next
ls = GuardedList()
ls.append(1)
ls.append(2)
ls.append(3)
ls.append(4)
ls.insert(5,2)
ls.find(2)
ls.print_out()
ls = DoubleLinkList()
ls.append(1)
ls.append(2)
ls.append(3)
ls.append(4)
ls.insert(5,2)
ls.remove(1)
ls.print_out()
ls = SingleLinkList()
ls.append(1)
ls.append(2)
ls.append(3)
ls.append(4)
ls.insert(5,2)
ls.remove(1)

ls.print_out()
ls = PrirityQueue(10)
ls.equeue(1)
ls.equeue(1)

ls.equeue(1)
ls.equeue(1)
ls.equeue(13)
ls.equeue(13)
ls.equeue(13)
ls.equeue(13)
ls.equeue(12)
print(ls.que)
ls.dequeue()
ls.dequeue()
print(ls.que)

ls.dequeue()
ls.dequeue()
ls.dequeue()

print(ls.que)

print(ls.find(12))
print(ls.find(13))
ls = Queue(10)
ls.equeue(1)
ls.equeue(1)

ls.equeue(1)
ls.equeue(1)
ls.equeue(13)
ls.equeue(13)
ls.equeue(13)
ls.equeue(13)
ls.equeue(12)
print(ls.que)
ls.dequeue()
ls.dequeue()
print(ls.que)

ls.dequeue()
ls.dequeue()
ls.dequeue()

print(ls.que)

print(ls.find(12))
print(ls.find(13))
ls = Stack(10)
ls.push(1)
ls.push(1)

ls.push(1)
ls.push(1)
ls.push(1)
ls.push(1)
ls.push(20)
print(ls.stack)
ls.pop()
ls.pop()

print(ls.stack)
ls.pop()
ls.pop()
ls.pop()


print(ls.stack)

print(ls.find(12))
print(ls.find(13))
