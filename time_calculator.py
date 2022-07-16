# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator
# instructions to this code

def add_time(start, duration, day=False):
  dic_aux={
    '1':'monday',
    '2':'tuesday',
    '3':'wednesday',
    '4':'thursday',
    '5':'friday',
    '6':'saturday',
    '7':'sunday',
      
  }
  formt=''
  aux=''
  aux2=''
  reference=0
  ndays=''
  try:
    day=day.lower()
  except:pass

 
  ################################################## codigo para conseguir la hora y am/pm
  (hora1,min1,ampm)=start.replace(' ',':').split(':') #Extrayendo datos
  (hora2,min2)=duration.split(':')
  if ampm=='PM':                               #convirtiendo a formato 24hrs
    hora1=int(hora1)+12
    
  horaf=int(hora1)+int(hora2)
  minf=int(min1)+int(min2)
  
  while True: 
    if minf>=60:
      minf=minf-60
      horaf=horaf+1
    elif minf<60:
      break

  if minf<10:
    aux+='0'
  
  while horaf>=24:
    horaf=horaf-24
    reference=reference+1
  
  if horaf<12:
    ampm='AM' 
  elif horaf>=12 and horaf<24:
    horaf=horaf-12
    if ampm=='AM':
      ampm='PM'
          
  if horaf==0:
    horaf=12
     
  
  ############################################################# codigo para conseguir el dia
  if day!=False:
    for keys,values in dic_aux.items(): 
      if day == values:
        aux2=keys
        aux2=int(aux2)
    aux2=aux2+reference
    
    while aux2>7:
       aux2=aux2-7
    aux2=str(aux2)
    for keys,values in dic_aux.items():
      if str(aux2)==keys:
        aux2=(dic_aux[keys])
    
  #################################################### codigo para saber cuantos dias pasaron
  if reference==1:
    ndays="next day"
  elif reference!=0:
    reference=str(reference)
    ndays=reference+' '+'days later'
  if ndays!='':
    ndays=' '+'('+ndays+')'
    
  
  if day==False:  
    formt+=formt+str(horaf)+':'+aux+str(minf)+' '+ampm+ ndays
  if day!=False:
    formt+=formt+str(horaf)+':'+aux+str(minf)+' '+ampm+','+' '+aux2.capitalize()+ndays
  
  new_time=formt
  



  return new_time