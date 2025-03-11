class Sorting:
    def __init__(self):
        pass

    def linear_search(self,arry,item):
        flag=0
        for i in range (len(arry)):
            if arry[i]==item:
                flag=1
                return i
        if flag==0:
            return 'item not in array'
    
    def binary_search(self,sorted_array,item):
        low_index=0
        high_index=len(sorted_array)-1
        middle_index=(low_index+high_index)//2
        flag=0
        for i in range (len(sorted_array)):
            if sorted_array[middle_index]==item:
                flag=1
                return middle_index
            if sorted_array[middle_index]>item:
                low_index=low_index
                high_index=middle_index-1
            if sorted_array[middle_index]<item:
                low_index=middle_index+1
                high_index=high_index
            middle_index=(low_index+high_index)//2
        if flag==0:
            return 'item not in array'
    
    def is_sorted(self,array):
        flag=True
        for i in range (len(array)-1):
            if array[i]>array[i+1]:
                flag=False
                break
        return flag
    
    def bubble_sort(self,array):
        for i in range (len(array)-1):
            flag=0
            for j in range (len(array)-1-i):
                if array[j]>array[j+1]:
                    flag=1
                    array[j],array[j+1] = array[j+1],array[j]
            if flag==0:
                break
        return array

    
    def selection_sort(self,array):
        for i in range (len(array)-1):
            min=i
            for j in range ((1+i),len(array)):
                if array[min]>array[j]:
                    min=j
            array[i],array[min]=array[min],array[i]
        return array

    
    def merge_sorted(self,array1,array2):
        i=j=0
        merged_array=[]
        while i<len(array1) and j<len(array2):
            if array1[i]<array2[j]:
                merged_array.append(array1[i])
                i+=1
            else:
                merged_array.append(array2[j])
                j+=1
        while i<len(array1):
            merged_array.append(array1[i])
            i+=1
        while j<len(array2):
            merged_array.append(array2[j])
            j+=1
        return merged_array

    def merge_sort(self,array):
        if len(array)==1:
            return array
        mid=len(array)//2
        right_array=array[:mid]
        left_array=array[mid:]
        right_array=self.merge_sort(right_array)
        left_array=self.merge_sort(left_array)
        return self.merge_sorted(right_array,left_array)
    

s1=Sorting()
array=[56,24,21,100,256,49,1005]
#m=s1.linear_search(array,25)

sorte_arr=[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21]
#print(s1.binary_search(sorte_arr,601))
print(s1.merge_sort(array))
        