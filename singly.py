class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linked:
    def __init__(self):
        self.head=None
    def add_begin(self,data):
        newnode = node(data)
        if self.head is None:
            self.head=newnode
        else:


            newnode.ref=self.head
            self.head=newnode
    def add_end(self,data):
        if self.head is None:
            newnode=node(data)
            self.head=newnode
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            newnode=node(data)
            n.ref=newnode

    def traversal(self):
        if self.head is None:
            print("empty linked list")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.ref
    def add_before(self,data,x):
        if self.head is None:
            print("empty ll")
            return
        if self.head.data==x:
            newnode=node(data)
            newnode.ref=self.head
            self.head=newnode
            return

        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            else:
                n=n.ref
        if n.ref is None:
            print("node not found")
        else:
            newnode=node(data)
            newnode.ref=n.ref
            n.ref=newnode
    def add_after(self,data,x):
        if self.head is None:
            print("empty linked list")
            return
        n=self.head
        while n is not None:
            if n.data==x:
                break
            else:
                n=n.ref
        if n is None:
            print("node not found")
        else:
            newnode=node(data)
            newnode.ref=n.ref
            n.ref=newnode
    def delete_f(self):
        if self.head is None:
            print("empty ll")
            return
        else:
            self.head=self.head.ref
    def delete_l(self):
        if self.head is None:
            print("empty")
            return
        if self.head.ref is None:
            self.head=None
            return
        n=self.head
        while n.ref.ref is not None:
            n=n.ref
        n.ref=None
    def delete_b(self,data,x):
        if self.head is None:
            print("empty")
            return
        if self.head.data==x:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            else:
                n=n.ref
        if n.ref is None:
            print("not not found")
        else:
            n.ref=n.ref.ref


n1=linked()



n1.add_begin(30)
n1.add_begin(10)
n1.add_begin(20)
n1.add_before(60,10)
n1.add_before(70,60)
n1.add_after(80,70)
n1.traversal()
print("\n")
n1.delete_f()

n1.delete_l()


n1.traversal()