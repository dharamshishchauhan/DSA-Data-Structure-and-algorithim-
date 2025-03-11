class Node:
    def __init__(self,value):
        self.data=value
        self.address=None
        
class Stack:
    def __init__(self):
        self.head_add=None
        self.n=0
    
    def isempty(self):
        return self.head_add==None
        '''if self.n==0:#this is another way 
            return True
        else:
            return False'''
    
    def push(self,item):
        new_node=Node(item)
        new_node.address=self.head_add
        self.head_add=new_node
        self.n=self.n+1
    
    def traverser(self):
        start_add=self.head_add
        em=''
        while start_add!=None:
            print(start_add.data)
            start_add=start_add.address

    def peek(self):
        if self.isempty():
            return 'empty stack'
        else:
            return self.head_add.data
    
    def pop(self):
        if self.isempty():
            return 'empty stack'
        else:
            data1=self.head_add.data
            self.head_add=self.head_add.address
            return  data1
        

s=Stack()
s.push(21)
s.push(22)
s.push(58)
s.push(101)

def reverse_string(string):
    s1=Stack()
    for i in string:
        s1.push(i)
    emp=''
    head_add=s1.head_add
    while head_add!=None:
        emp=emp+str(head_add.data)
        head_add=head_add.address
    return emp
#print(reverse_string('hello'))

def tex_editor(string:str,undo_reo:str):
    s2=Stack()
    s4=Stack()
    for i in string:
        s2.push(i)
    for i in undo_reo:
        if i=='u' and s2.isempty()==False:
            data2=s2.pop()
            #this is another way of writing code 
            '''data2=s2.head_add.data
            s2.head_add=s2.head_add.address'''
            s4.push(data2)
        if i=='r' :
            data2=s4.pop()
            #this is another way of writing code 
            '''data2=s4.head_add.data
            s4.head_add=s4.head_add.address'''
            s2.push(data2)
    
    head_=s2.head_add
    st=''
    while head_!=None:
        st=str(head_.data)+st
        head_=head_.address
    return st

#print(tex_editor(string='Kolkata',undo_reo='u'))



    
