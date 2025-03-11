class Node:
    def __init__(self,key,value):
        self.key=key
        self.data=value
        self.address=None

import time
class LinkedList:
    size=0
    def __init__(self):
        self.head_address=None
        self.n=0

    def __len__(self):
        return self.n
    
    
    def trasverse(self):
        head_address=self.head_address
        while True:
            if head_address!=None:
                print(head_address.key,'-->',head_address.data)
                head_address=head_address.address
            else:
                break
            
    def __str__(self):
        print_data=''
        d11=d1.buckets
        for item in d11:
            head_ad1=item.head_address
            while True:
                if head_ad1==None:
                    break
                print_data=print_data+str(head_ad1.key)+':'+str(head_ad1.data)+'->'
                head_ad1=head_ad1.address
                
        return '{'+print_data[:-2]+'}'
    
    def append(self,key,item):
        new_node=Node(key,item)
        if self.head_address==None:
            self.head_address=new_node
            self.n=self.n+1
            LinkedList.size=LinkedList.size+1
            return
        head_add=self.head_address
        update=0
        while True:
            if head_add.key==key:
                head_add.data=item
                update=1
            if head_add.address!=None:
                head_add=head_add.address
            else:
                break
        if update==0:
            head_add.address=new_node
            self.n=self.n+1
            LinkedList.size=LinkedList.size+1
        if (LinkedList.size/d1.capacity)>=2:
            pass


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
    
        
    def del_by_key(self,key):
        head_add=self.head_address
        cahge_add=None
        loop=0
        while head_add.address!=None:
            if head_add.key==key:
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
    
    def search_by_key(self,key):
        head_add=self.head_address
        index=0
        #in return it will index of data
        while head_add.address!=None:
            if head_add.key==key:
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
    
    

class Dictinory:
    def __init__(self,capacity):
        self.capacity=capacity
        self.n=0
        self.buckets=self.create_ll()
        self.ap=None
        self.old_buckets=None

    def create_ll(self):
        buckets=[]
        for i in range (self.capacity):
            buckets.append(LinkedList())
        return buckets
    
    def hasing(self,key):
        return sum(ord(c) for c in str(key)) % self.capacity
    
    def number_of_nodes_in_linkedlist(self,add):
        num=0
        for i in (self.old_buckets):
            if i==add:
                add1=i.head_address
                while add1!=None:
                    add1=add1.address
                    num=num+1
        return num
         
    
    def __str__(self):
        print_data=''
        d11=self.buckets
        for item in d11:
            head_ad1=item.head_address
            while True:
                if head_ad1==None:
                    break
                print_data=print_data+str(head_ad1.key)+':'+str(head_ad1.data)+'->'
                head_ad1=head_ad1.address
                
        return '{'+print_data[:-2]+'}'
    
    def append(self,key,item):
        new_node=Node(key,item)
        bucket_index=self.hasing(key)
        head_ad=self.buckets[bucket_index]
        if head_ad.head_address==None:
            head_ad.head_address=new_node
            self.n=self.n+1
            return
        head_add=head_ad.head_address
        update=0
        while True:
            if head_add.key==key:
                head_add.data=item
                update=1
            if head_add.address!=None:
                head_add=head_add.address
            else:
                break
        if update==0:
            head_add.address=new_node
            self.n=self.n+1
        load_factor=self.n/self.capacity
        print('load factor ', load_factor)
        if load_factor>=2:
            self.capacity=self.capacity*2
            old_list=self.buckets
            self.old_buckets=old_list
            self.buckets=self.create_ll()
            for item in old_list:
                if item.head_address==None:
                    continue
                else:
                    ad1=item.head_address
                    no_nodes=self.number_of_nodes_in_linkedlist(item)
                    for i in range (no_nodes):
                        key1=ad1.key
                        value1=ad1.data
                        self.append(key1,value1)
                        ad1=ad1.address
                    
    def delete(self,key):
        add_list=self.buckets
        for item in add_list:
            add=item.head_address
            while add!=None:
                if add.key==key:
                    item.del_by_key(key)
                    self.n=self.n-1
                    return
                add=add.address
    
    def get(self,key):
        add_list=self.buckets
        da=0
        for item in add_list:
            add=item.head_address
            while add!=None:
                if add.key==key:
                    da=1
                    return add.data
                add=add.address
        if da==0:
            return 'invalid key'

        
    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self,key,value):
        return self.append(key,value)

    
d1=Dictinory(2)
d1.append('python',51)
d1.append('c',1011)
d1.append('java',48)
d1.append('c++',1251)
#d1.delete('c++')
d1['lavies']=562363

print(d1['c'])
print(d1)





