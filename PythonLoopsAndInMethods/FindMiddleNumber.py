def findMiddleNumber(a,b):
    # a və b-nin ədəd olduğunu dəqiqləşdirin.a və ya b ədəd deyilsə "Düzgün dəyər daxil edilməyib" return edilsin
    # a və b ədədlərinin ədədi ortasından böyük olan ədədləri çap edin
    pass

def Foo():
    while True : 
       my_list=[]
       try:
            
            a = int(input("A ədədini daxil edin : "))
            b = int(input("B ədədini daxil edin : ")) 
         
            for i in range(a,b):
                my_list.append(i)
                
                average=0
                x=0
                while x<len(my_list):
                    average=average+my_list[x]/len(my_list)
                    x+=1
            print(average)   
       except ValueError:
            print("Düzgün dəyər daxil edilməyib!") 
            
       k=input('davam edilsinmi? No/Yes : ')
       if k.lower=='no':
            break
       

Foo()