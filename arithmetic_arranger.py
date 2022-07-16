#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter
#instructions to this code

def arithmetic_arranger(problems, solv=False):
  lista=[]
  
  if len(problems)>5:
    return "Error: Too many problems."
  
  for arg in problems:
    items=arg.split(" ")
    n1=items[0]
    ope=items[1]
    n2=items[2]
    if len(n1)>4 or len(n2)>4:
      return "Error: Numbers cannot be more than four digits."
    try:
      n1=int(n1)
      n2=int(n2)
    except:
      return "Error: Numbers must only contain digits."
    
    if ope=="+":
      resultado=n1+n2
    elif ope=="-":
      resultado=n1-n2
    else:
      return "Error: Operator must be '+' or '-'."
         
    aux_dict = {
      'n1': str(n1),
      'n2': str(n2),
      'ope': ope,
      'result': str(resultado),
    }
    lista.append(aux_dict)
  
  fort1=''
  fort2=''
  fort3=''
  fort4=''
  aux=0

  for keys in lista:
    aux=aux+1
    
    if len(keys['n1']) >= len(keys['n2']):
      columna=max(len(keys['n1']),(len(keys['n2'])))+2
      spc= columna-(len(keys['n2'])+1)
      
      
      if len(problems)==aux:
        fort3+=(max(len(keys['n1']),(len(keys['n2'])))+2)*'-'
        fort1+=2*' '+keys['n1']
        fort2+=keys['ope']+spc*' '+keys['n2']
      else:
        fort3+=(max(len(keys['n1']),(len(keys['n2'])))+2)*'-'+4*' '
        fort1+=2*' '+keys['n1'] + 4*' '
        fort2+=keys['ope']+spc*' '+keys['n2']+ 4*' '
        
        
    elif len(keys['n2'])>len(keys['n1']):
      columna=max(len(keys['n2']),len(keys['n1'])) +2  
      spc=columna-(len(keys['n1']))
      
      
      if len(problems)==aux:
        fort3+=(max(len(keys['n1']),(len(keys['n2'])))+2)*'-'
        fort1+=spc*' '+keys['n1']
        fort2+=keys['ope']+' '+keys['n2']
      else:
        fort3+=(max(len(keys['n1']),(len(keys['n2'])))+2)*'-'+4*' '
        fort1+=spc*' '+keys['n1']+4*' '
        fort2+=keys['ope']+' '+keys['n2']+4*' ' 
    if solv==True:
      spc=columna-len(keys['result'])
      if len(problems)==aux:
        fort4+=spc*' '+ keys['result']       
      else:
        fort4+=spc*' '+ keys['result'] + 4*' '
  if solv:
    arranged_problems=fort1+'\n'+fort2+'\n'+fort3+'\n'+fort4
  else:
    arranged_problems=fort1+'\n'+fort2+'\n'+fort3

  return arranged_problems