#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app
#Instructions to this code
class Category:
  
  
  def __init__(self, type):   
    self.ledger=list()
    self.type=type 
    self.contador=0
    self.expend=0
    
    
    
  def deposit(self,amount,description=''): 
    dic_aux={}
    dic_aux={
      'amount': amount,
      'description':description,
    }
    self.contador+=amount
    self.ledger.append(dic_aux)
    
    

  def withdraw (self, amount, description=''):
    dic_aux={}
    
    if self.check_funds(amount)==True:
      self.amount= -amount
      self.contador=self.contador-amount
      self.expend+=amount
      
      dic_aux['amount']=-amount
      dic_aux['description']=description
      self.ledger.append(dic_aux)
      
      return True
      
    else:return False

  def get_balance (self):
    return self.contador
        
  def transfer (self,amount,destination):
      if self.check_funds(amount)==True:
        self.withdraw(amount,f'Transfer to {destination.type}')
        destination.deposit(amount,f'Transfer from {self.type}')
        return True
      
      else:
        return False

  def check_funds(self, amount):
    if amount <= self.contador:
      return True

    else: return False
  
  
  
  def __str__ (self):
    
    tittle_spc=int((30-len(self.type))/2)
    extra_spc=(30-len(self.type))%2
        
    form1=(tittle_spc+extra_spc) * '*' +self.type + tittle_spc * '*'
            
    form2=''
    total=0
    for keys in self.ledger: #descricion->precio.
      if len(str(keys['amount']))>7:
        pass
      else:
        str_len=len(keys['description'][0:23])+len(str(format(float(keys['amount']),'.2f')))
        
        str_total=30- str_len
      
      form2+=keys['description'][0:23]+str_total*' '+str(format(float(keys['amount']),'.2f'))+'\n'
      total=total+float(keys['amount'])
      
    
    
    total=format(total,'.2f')
    form3='Total:'+' '+str(total)#total
    solv=form1+'\n'+form2+form3
    return solv
    
    

def create_spend_chart(categories):
  expendtotal=0
  listadestr=[]
  lista_aux=[]
  
  
  listadestr=['100|',' 90|',' 80|',' 70|',' 60|',' 50|',' 40|',' 30|',' 20|',' 10|','  0|']
  
    
  for budgets in categories: #gastos totales
    expendtotal+=budgets.expend
    
  for budgets in categories: #porcentaje por categoria redondeado
    porcentaje=int((budgets.expend/expendtotal)*100)
    porcentaje=int(porcentaje/10)
    porcentaje=str(porcentaje*10)
    lista_aux.append(porcentaje)
    
  
  palabras=''
  
  
  temp=''
  for keys in listadestr: #consiguiendo formato de grafica y separador
    temp=keys
    for porc in lista_aux:
      if porc=='100':
        temp+=' '+'o'+' '
      elif keys in listadestr[10-int(porc[0]):]:
        
        temp+=' '+'o'+' '
        
      else:temp+=3*' '
    separador=4*' '+((len(lista_aux)*3+1)*'-')    
    palabras+=temp+' '+'\n'
  
  #budgets en vertical
  lista_test=[]
  maxlen=0
  for titulos in categories:    
    lista_test.append(titulos.type)
  
  numerodepalabras=len(lista_test)
  
  for i in range (numerodepalabras):
        length = len(lista_test[i])
        if length >= maxlen:
            maxlen = length
  
  for i in range (numerodepalabras):
    if len(lista_test[i]) < maxlen:
      lista_test[i] = lista_test[i] + (" ")*(maxlen-len(lista_test[i]))
      
  newline=''
  ans = ["" for i in range(maxlen)]
  
  
  for i in range (numerodepalabras):
    j=0
    while j<len(lista_test[i]):
           
        
      ans[j] +=lista_test[i][j]+2*' '
      j+=1
  u=0    
  for i in ans:
    u+=1
    newline+=5*' '+i
    if u<len(ans):
      newline+='\n'
     
  title= 'Percentage spent by category'  
  form=title+'\n'+palabras+separador+'\n'+newline
  
  return form