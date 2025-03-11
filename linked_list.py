class Node:
    def __init__(self,value):
        self.data=value
        self.address=None

import time
class LinkedList:
    def __init__(self):
        self.head_address=None
        self.n=0

    def __len__(self):
        return self.n
    
    def insert(self,value):
        new_node=Node(value)
        new_node.address=self.head_address
        self.head_address=new_node
        self.n=self.n+1
    
    def trasverse(self):
        head_address=self.head_address
        while True:
            if head_address!=None:
                print(head_address.data)
                head_address=head_address.address
            else:
                break
            
    def __str__(self):
        head_address=self.head_address
        print_data=''
        while True:
            if head_address!=None:
                print_data=print_data+str(head_address.data)+'->'
                head_address=head_address.address
            else:
                break
        return print_data[:-2]
    
    def append(self,item):
        new_node=Node(item)
        if self.head_address==None:
            self.head_address=new_node
            self.n=self.n+1
            return
        head_add=self.head_address
        while True:
            if head_add.address!=None:
                head_add=head_add.address
            else:
                break
        head_add.address=new_node
        self.n=self.n+1

    def del_head(self):
        if self.head_address==None:
            return 'empty linked list'
        self.head_address=self.head_address.address
        self.n=self.n-1

    def pop(self):
        if self.head_address==None:
            return 'empty linked list'
        if self.head_address.address==None:
            return self.del_head()

        head_add=self.head_address
        while True:
            if head_add.address.address!=None:
                head_add=head_add.address
            else:
                break
        head_add.address=None
        self.n=self.n-1
    
    def insert(self,value,item):
        new_node=Node(item)
        head_add=self.head_address
        if head_add.data==value:
            change_1st=head_add.address
            new_node.address=change_1st
            head_add.address=new_node
            self.n=self.n+1
            return
        while True:
            head_add=head_add.address
            if head_add.data==value:
                change_1st=head_add.address
                break
        new_node.address=change_1st
        head_add.address=new_node
        self.n=self.n+1
        
    def del_by_value(self,item):
        head_add=self.head_address
        cahge_add=None
        loop=0
        while head_add.address!=None:
            if head_add.data==item:
                cahge_add=head_add.address
                head_add.address==None
                break
            loop=1
            last_add=head_add
            head_add=head_add.address
        if loop==0:
            self.head_address=cahge_add
            self.n=self.n-1
            return
        last_add.address=cahge_add
        self.n=self.n-1
    
    def search_by_value(self,item):
        head_add=self.head_address
        index=0
        #in return it will index of data
        while head_add.address!=None:
            if head_add.data==item:
                break
            index=index+1
            head_add=head_add.address
        return index
    
    def del_by_index(self,index):
        head_add=self.head_address
        init_index=0
        index_bool=True
        while head_add.address!=None:
            if index==init_index:
                index_bool=False
                value=head_add.data
                self.del_by_value(value)
            init_index=init_index+1
            head_add=head_add.address
        if index_bool==True:
             print('index out of range or put in integer typ')
    
    def reverse_linked_list(self):
        head_add=self.head_address
        pre_add=None
        while head_add!=None:
            nex_add=head_add.address
            head_add.address=pre_add
            pre_add=head_add
            head_add=nex_add
        self.head_address=pre_add

        

LL=LinkedList()
LL.append(1)
LL.append(2)
LL.append(3)
LL.append(4)
LL.append(5)
LL.reverse_linked_list()
print(LL)

