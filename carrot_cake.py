try:
 try:





  box_num=int(input('how many boxes do you have?: '))

  carrot_num=int(input('how many carrots do you have?: '))
  if box_num>=0 and carrot_num>=0:
      

   if carrot_num%box_num==7:
      print('Cake time')
   else:
      print(f'You need to buy {7-(carrot_num%box_num)} carrots more')
  else:
     print('invalid value')    
 except ZeroDivisionError:
      print('zero division error')
    
except ValueError:
      print('invalid value')
      