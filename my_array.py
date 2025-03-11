import ctypes 

class Mera_list:

    def __init__(self ):
        self.size=1
        self.n=0
        self.A=self.__create_array(self.size)
        
    def __create_array(self,capacity):
        #return (ctypes.py_object *capacity)()
        return (capacity*ctypes.py_object)()
    
    def __len__(self):
        return self.n
    
    def __resize(self,capcity):
        B=self.__create_array(capcity)
        for item in range (self.n):
            B[item]=self.A[item]
        self.A=B
        self.size=capcity

    def append(self,item):
        if self.size>self.n:
            self.A[self.n]=item
        else:
            self.__resize(self.size*2)
            self.A[self.n]=item
        self.n=self.n+1
        
    def __str__(self):
        new=''
        for item in range (self.n):
            new=new+str(self.A[item])+','
        return '['+new[:-1]+']'
    
    def index(self,item):
        item1=False
        for i in range (self.n):
            if self.A[i]==item:
                item1=True
                return i
        if item1==False:
            return 'item is not in list -value eror'
            
    def pop(self,index):
        item_removing=self.A[index]
        for i in range (index,(self.n-1)):
            self.A[i]=self.A[i+1]
        self.n=self.n-1
        return f'removed item is  {item_removing}'
    
    def clear(self):
        self.n=0
        self.size=1
    
    def insert(self,index,item):
        if self.size==self.n:
            self.__resize(self.size*2)
        for i in range (self.n,index,-1):
            self.A[i]=self.A[i-1]
        self.A[index]=item
        self.n=self.n+1

    def delete(self,index):
        for i in range (index,(self.n-1)):
            self.A[i]=self.A[i+1]
        self.n=self.n-1



ml=Mera_list()
ml.append(5)
ml.append('hell0')
ml.append(True)
ml.append(56)
ml.append('cand')
print(len(ml))

