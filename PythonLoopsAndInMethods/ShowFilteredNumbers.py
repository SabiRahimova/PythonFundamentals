def showFilteredNumbers(a,b):
    # a və b-nin ədəd olduğunu dəqiqləşdirin.a və ya b ədəd deyilsə "Düzgün dəyər daxil edilməyib" return edilsin
    # a b-dən kiçikdirsə ekrana "Daxil edilən dəyərlər tələblərə uyğun deyil" çap edin
    # a b-dən böyükdürsə a və b ədədləri arasında 5-ə bölünən amma 7-yə bölünməyən ədədləri ekrana çap edin
    pass
    



def inputEded():
    
    
   while True : 
       my_list=[]
       try:
            
            a = int(input("A ədədini daxil edin : "))
            b = int(input("B ədədini daxil edin : ")) 
            
            cut=input('davam edilsinmi? No/Yes : ')
            if cut.lower=="No":
                break
            if a>b:
                print('Daxil edilən dəyərlər tələblərə uyğun deyil')
                
            if a<b:        
                for i in range(a,b):
                    if i%5==0 and i%7!=0:
                        my_list.append(i)

                print(my_list) 
                                         
       except ValueError:
            print("Düzgün dəyər daxil edilməyib!") 
       cut=input('davam edilsinmi? No/Yes : ')
       if cut.lower=="Yes":
          continue
       else:
           break                   
           
inputEded()