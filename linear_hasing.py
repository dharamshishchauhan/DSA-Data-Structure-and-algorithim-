class Dictonary:
    def __init__(self,size):
        self.size=size
        self.key=[None]*self.size
        self.value=[None]*self.size
        
    def hasing(self,key):
        return sum(ord(c) for c in str(key)) % self.size
    
    def put (self,key,value):
        index_key1=self.hasing(key)    
        for i in range (self.size):
            index_key=(index_key1+i)%self.size
            if self.key[index_key]==None:
                self.key[index_key]=key
                self.value[index_key]=value
                return
            if self.key[index_key]==key:
                self.key[index_key]=key
                self.value[index_key]=value
                return
    
    def __setitem__(self,key,value):
        return self.put(key,value)
    
    def __getitem__(self,key):
        return self.get(key)
    
    def get(self,key):
        index_key1=self.hasing(key)
        not_found=0
        for i in range (self.size):
            index_key=(index_key1+i)%self.size
            if self.key[index_key]==key:
                not_found=1
                break
        if not_found==0:
            return 'item not in list'
        if not_found==1:
            return self.value[index_key]
    
    def __str__(self):
        string=''
        for item in range (self.size):
            d1=self.key[item]
            d2=self.value[item]
            string=str(d1)+':'+str(d2)+','+string
        
        return '{'+string[:-1]+'}'
    

d1=Dictonary(3)

d1.put('python',1000)
d1.put('java',45)
d1.put('php',100)
#d1.put('c',2)
d1['python']=8

print(d1.key)
print(d1.value)  
print(d1['python'])
print(d1)
        
    