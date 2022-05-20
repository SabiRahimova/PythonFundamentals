def sumOfNumbers(a,b):
    # a və b-nin ədəd olduğunu dəqiqləşdirin.a və ya b ədəd deyilsə "Düzgün dəyər daxil edilməyib" return edilsin
    # a və b arasında olan ədədlərin cəmini return edin
    pass



def sumNumber():
    while True:        
        my_list=[]
        
        try:
                
            a = int(input("A ədədini daxil edin : "))
            b = int(input("B ədədini daxil edin : ")) 
                    
            for i in range(a,b):
                my_list.append(i)
                    
                cem=0
                x=0
                while x<len(my_list):
                    cem=cem+my_list[x]
                    x+=1
            print(cem)
        except ValueError:
            print("Düzgün dəyər daxil edilməyib!")      
    
        cut=input('davam edilsinmi? No/Yes : ')
        if cut.lower()=="Yes":
          continue
        else:
           break      
sumNumber()