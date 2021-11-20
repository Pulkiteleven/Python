nums = {0:" ",1:" one",2:" three",3:" three",4:" four",5:" five",6:" six",7:" seven",8:" eight",9:" nine",10:" ten",11:" eleven",
12:" twelve",13:" thirteen",14:" fourteen",15:" fifteen",16:" sixteen",17:" seventeen",18:" eighteen",19:" nineteen"}
tens = {0:" ",2:" twennty",3:" thirty",4:" forty",5:" fifty",6:" sixty",7:" seventy",8:" eighty",9:" ninty"}
notations = {0:" ",3:" hundred",4:" thousand",6:" lacks",8:" crores"}

def printer(num):
    a = ""
    l = len(str(num))
    if num < 20:
        a += str(nums.get(num))
        
    elif num < 100:
        if str(num)[-1] == "0":
            a += tens.get(int(str(num)[0]))
        else:
            a += tens.get(int(str(num)[0]))
            a += printer(int(str(num)[-1]))
    else:
        if l%2 == 0 or l == 3:
            a += printer(int(str(num)[0]))
            a += notations.get(l)
            a += printer(int(str(num)[1:]))
        elif l%2 != 0 and l != 3:
            a +=  printer(int(str(num)[0:2]))
            a += notations.get(l-1)  
            a += printer(int(str(num)[2:]))
        





    return a 

numss = int(input())
if len(str(numss)) <= 9:
    print(printer(numss))
else:
    print("currenly our program support numbers upto croes only")    


            

