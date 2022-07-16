# You find a strange mirror that always shows a hand that is moving. The hand appears to be alive, and after a lot of questions of "yes" and "no" answer, you know that the hand is trying to teach you a program that is written in HPL (Hand Programming Language).

# This language works with a memory of an indefinite size of bytes, with all values initialized to 0. This language haves 7 instructions:

# 👉 : moves the memory pointer to the next cell

# 👈 : moves the memory pointer to the previous cell

# 👆 : increment the memory cell at the current position

# 👇 : decreases the memory cell at the current position.

# 🤜 : if the memory cell at the current position is 0, jump just after the corresponding 🤛

# 🤛 : if the memory cell at the current position is not 0, jump just after the corresponding 🤜

# 👊 : Display the current character represented by the ASCII code defined by the current position.

# As memory cells are bytes, from 0 to 255 value, if you decrease 0 you'll get 255, if you increment 255 you'll get 0.
# Loops of 🤜 and 🤛 can be nested.

# This program display "Hello"
# 👇🤜👇👇👇👇👇👇👇👉👆👈🤛👉👇👊👇🤜👇👉👆👆👆👆👆👈🤛👉👆👆👊👆👆👆👆👆👆👆👊👊👆👆👆👊

# This program (with nested loops) display "Hello World!"
# 👉👆👆👆👆👆👆👆👆🤜👇👈👆👆👆👆👆👆👆👆👆👉🤛👈👊👉👉👆👉👇🤜👆🤛👆👆👉👆👆👉👆👆👆🤜👉🤜👇👉👆👆👆👈👈👆👆👆👉🤛👈👈🤛👉👇👇👇👇👇👊👉👇👉👆👆👆👊👊👆👆👆👊👉👇👊👈👈👆🤜👉🤜👆👉👆🤛👉👉🤛👈👇👇👇👇👇👇👇👇👇👇👇👇👇👇👊👉👉👊👆👆👆👊👇👇👇👇👇👇👊👇👇👇👇👇👇👇👇👊👉👆👊👉👆👊


import emoji

string = '👉👆👆👆👆👆👆👆👆🤜👇👈👆👆👆👆👆👆👆👆👆👉🤛👈👊👉👉👆👉👇🤜👆🤛👆👆👉👆👆👉👆👆👆🤜👉🤜👇👉👆👆👆👈👈👆👆👆👉🤛👈👈🤛👉👇👇👇👇👇👊👉👇👉👆👆👆👊👊👆👆👆👊👉👇👊👈👈👆🤜👉🤜👆👉👆🤛👉👉🤛👈👇👇👇👇👇👇👇👇👇👇👇👇👇👇👊👉👉👊👆👆👆👊👇👇👇👇👇👇👊👇👇👇👇👇👇👇👇👊👉👆👊👉👆👊'
                

def MirrorFuntion(string):
    position=0
    instruction_list=[0]
    resolve=[]
    n=0     
            
    
    while True:
        
        if string[n] == '👉':
            if position==len(instruction_list)-1:
                instruction_list.append(0)
            position+=1
            n+=1
        
        elif string[n]=='👈':
            position-=1
            n+=1

        elif string[n]=='👆':
            if instruction_list[position]==255:
                instruction_list[position]=0
            else:
                instruction_list[position]=instruction_list[position]+1 
            n+=1

        elif string[n]=='👇':
            if instruction_list[position]==0:
                instruction_list[position]=255
            else:
                instruction_list[position]=instruction_list[position]-1
            n+=1

        elif string[n]=='🤜':
            if instruction_list[position]==0:
                izquierda=0
                derecha=0
                while True:

                    if string[n]=='🤜':
                        izquierda+=1
                    elif string[n]=='🤛':
                        derecha+=1
                    n+=1
                    
                    if izquierda==derecha:
                        break
            else:
                n+=1
                                      
        elif string[n]=='🤛':
            if instruction_list[position]!=0:
                izquierda=0
                derecha=0
                while True:
                    if string[n]=='🤜':
                        izquierda+=1
                    elif string[n]=='🤛':
                        derecha+=1
                    n-=1
                                        
                    if izquierda==derecha:
                        n+=2
                        break
            
            else:
                n+=1

        
        elif string[n] == '👊':
            value=chr(instruction_list[position])
            resolve.append(value)
            n+=1
            
        
        if n==len(string):
            break
        
    
    
    resolve=''.join(resolve)    
    return(resolve)
print(MirrorFuntion(string))




