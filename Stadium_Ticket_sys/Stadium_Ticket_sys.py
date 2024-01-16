import sys
maindict={}

def saving_func(inpt):#save messages into text file
        with open('output.txt', "a",encoding="utf-8") as f:
            f.write(inpt)
            f.close()

def sell(buyername,tick_statu,category,*arg):
    try:
        global maindict 
        arg=[*arg][0]
        for element in tuple(arg):
            if element.__contains__("\n"):
                element=element.strip("\n")    
            letter=element[0]
            element=element[1:]
            if element.__contains__("-"):
                firstnum,lastnum=int(element.split("-")[0]),int(element.split("-")[1])
                numberrange=[*range(firstnum,lastnum+1)]
            else:
                firstnum=element
                numberrange=[firstnum]
            harfseldeger=[]      
            for numb in numberrange:
                harfseldeger.append(f"{letter.upper() +str(numb)}")
        
            if all(item in maindict[f"{category}"] for item in harfseldeger):
                flag=True
                for item in harfseldeger:
                    if maindict[f"{category}"][f"{item}"]!=f"X":
                        if len(harfseldeger)>1:
                            inpt=f"Error: The seats {letter+element} cannot be sold to {buyername} due some of them have already been sold!\n"
                            print(f"Error: The seats {letter+element} cannot be sold to {buyername} due some of them have already been sold!")
                            saving_func(inpt)
                            flag=False
                            break
                        else:
                            inpt=f"Warning: The seat {letter+element} cannot be sold to {buyername} since it was already sold!\n"
                            saving_func(inpt)   
                            print(f"Warning: The seat {letter+element} cannot be sold to {buyername} since it was already sold!")
                            flag=False
                if flag:
                    for i in harfseldeger:
                        if tick_statu=="student":
                            tick_statu="S"
                        elif  tick_statu=="full":
                            tick_statu="F" 
                        elif tick_statu=="season":
                            tick_statu="T"    

                        maindict[f"{category}"][f"{i}"]=f"{tick_statu}"
                    inpt=f"Success: {buyername} has bought {letter+element} at {category}\n"
                    saving_func(inpt)
                    print(f"Success: {buyername} has bought {letter+element} at {category}")
                
            else:
                lastkey=list(maindict[f"{category}"])[-1]
                harf=lastkey[0]
                row=int(ord(harf))-65+1
                col=int(lastkey[1:])+1
                baris=element.split("-")
                if len(baris)>1:
                    bariselement=baris[-1]
                    
                else:
                    bariselement=baris[0]   
                if ord(letter)-65>row and int(bariselement)>int(col):#Error: The category ’category-1F’ has less row and column than the specified index X54!
                    inpt=f"Error: The category {category} has less row and column than the specified index {letter+element}!\n"
                    saving_func(inpt)
                    print(f"Error: The category {category} has less row and column than the specified index {letter+element}!")

                elif ord(letter)-65>int(row):

                    inpt=f"Error: The category {category} has less row than the specified index {letter+element}!\n"
                    saving_func(inpt)
                    print(f"Error: The category {category} has less row than the specified index {letter+element}!")
                else:
                    inpt=f"Error: The category {category} has less column than the specified index {letter+element}!\n"
                    saving_func(inpt)
                    print(f"Error: The category {category} has less column than the specified index {letter+element}!")       
    except:
        pass                
def cancel(category,*arg):
    try:
        global maindict 
        arg=[*arg][0]
        for element in tuple(arg):
            if element.__contains__("\n"):
                element=element.strip("\n")
            if element in maindict[f"{category}"]:
                if maindict[f"{category}"][f"{element}"]!="X":
                    maindict[f"{category}"][f"{element}"]="X"
                    inpt=(f"Success: The seat {element} at '{category}' has been canceled and now ready to sell again\n")
                    saving_func(inpt)
                    print((f"Success: The seat {element} at '{category}' has been canceled and now ready to sell again"))
                else:
                    inpt=(f"Error: The seat {element} at '{category}' has already been free! Nothing to cancel!\n")   
                    saving_func(inpt) 
                    print((f"Error: The seat {element} at '{category}' has already been free! Nothing to cancel!"))
            else:
                lastkey=list(maindict[f"{category}"])[-1]
                harf=lastkey[0]
                row=int(ord(harf))-65+1
                col=int(lastkey[1:])+1
                if  ord(element[0])-65>row and int(element[1:])>col-1:  # some error msg
                    inpt=f"Error: The category {category} has less row and column than the specified index {element}!\n"
                    saving_func(inpt)
                    print(f"Error: The category {category} has less row and column than the specified index {element}!")

                elif ord(element[0])-65>row:
                    inpt=f"Error: The category {category} has less row than the specified index {element}!\n"
                    saving_func(inpt)
                    print(f"Error: The category {category} has less row than the specified index {element}!")
                else:
                    inpt=f"Error: The category {category} has less column than the specified index {element}!\n"
                    saving_func(inpt)
                    print(f"Error: The category {category} has less column than the specified index {element}!")
    except:
        pass                
def balance(category):
    try:
        global maindict
        sler,tler,fler=0,0,0
        for value in maindict[f"{category}"].values():
            if value=="S":
                sler+=1
            elif value=="T":
                tler+=1
            elif value=="F":
                fler+=1            
            else:
                pass

        inpt=f"""Category report of '{category}'
--------------------------------
Sum of students = {sler}, Sum of full pay = {fler}, Sum of season ticket={tler}, and Revenues = {tler*250+sler*10+fler*20} Dollars\n"""
        saving_func(inpt)
        print(f"""Category report of '{category}'
--------------------------------
Sum of students = {sler}, Sum of full pay = {fler}, Sum of season ticket={tler}, and Revenues = {tler*250+sler*10+fler*20} Dollars"""
    )

    except:
        pass

def table(category):
    try:
        inpt=""
        
        lastkey=list(maindict[f"{category}"])[-1] 
        harf=lastkey[0]
        row,col=int(ord(harf))-65+1,int(lastkey[1:])+1
        inpt+=f"Printing category layout of {category}\n\n"
        print(f"Printing category layout of {category}\n")
    
        degerler=list(maindict[f"{category}"].values())
        degerler.reverse()
        result = []
        
        for i in range(0,row*col,col): 
            a=degerler[i:i+col]
            a.reverse()
            result+=a 

        harfler=[chr(i) for i in range(65,65+row)]
        harfler.reverse()
        del degerler
        for ind in range(len(result)): 
            if ind%col==0:
                print(harfler[int(ind/col)],end="  ")
                inpt+=f"{harfler[int(ind/col)]}  "
                print(result[ind],end="  ")
                inpt+=f"{result[ind]}  "
            if ind%col==col-1:
                inpt+=f"{result[ind]}\n"
                print(result[ind],end="\n")
            elif ind%col!=0:
                print(result[ind],end="  ")    
                inpt+=f"{result[ind]}  "
              
        print(" ",end="")
        inpt+=f" "    
             
        for i in range(col):
            print(f"{i:3}",end="")
            inpt+=f"{i:3}" 
        print() 
        inpt+="\n"
        saving_func(inpt)            
    except:
        pass


def create(catename,row,col):
    global maindict
    if catename in maindict: 
        inpt=(f"Warning: Cannot create the category for the second time. The stadium has already {catename}!\n")
        saving_func(inpt)
        print((f"Warning: Cannot create the category for the second time. The stadium has already {catename}!"))
    else:    
        collist,rowlist=[chr(65+i) for i in range(row)],range(col)  
        maindict[catename]={f"{collist[i]+str(rowlist[a])}":"X" for i in range(len(collist)) for a in range(len(rowlist))}
        inpt=f"The category '{catename}' having {row*col} seats has been created\n"
        saving_func(inpt)
        print(f"The category '{catename}' having {row*col} seats has been created")
    



file_to_delete = open("output.txt",'w',encoding="utf-8")
file_to_delete.close()  
with open(f'{sys.argv[1]}',encoding="utf-8") as f:  
    try: 
        for line in f.readlines(): 
            currentlinelist=list(line.split(" "))
            if currentlinelist[0]=='CREATECATEGORY':    
                row,col=currentlinelist[2].strip("\n").split("x")
                create(currentlinelist[1],int(row),int(col))
            elif currentlinelist[0]=='SELLTICKET': 
               sell(currentlinelist[1],currentlinelist[2],currentlinelist[3],currentlinelist[4:])

            elif currentlinelist[0]=='CANCELTICKET':
                cancel(currentlinelist[1],currentlinelist[2:])
            elif currentlinelist[0]=='BALANCE':
                if currentlinelist[-1].__contains__("\n"):
                    currentlinelist[-1]=currentlinelist[-1].strip("\n")
                balance(currentlinelist[1])

            elif currentlinelist[0]=='SHOWCATEGORY':
                if currentlinelist[-1].__contains__("\n"):
                    currentlinelist[-1]=currentlinelist[-1].strip("\n")
                table(currentlinelist[1])     
    except:
        pass        