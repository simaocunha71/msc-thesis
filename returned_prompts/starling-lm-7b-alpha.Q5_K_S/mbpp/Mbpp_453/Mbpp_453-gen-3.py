"""
def sumofFactors(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            if i % 2 == 0:
                sum += i
    return sum
"""

def sumofFactors(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            if i % 2 == 0:
                sum += i
    return sum

def test_sumofFactors():
    assert sumofFactors(18) == 26

test_sumofFactors()

# Made By Mostafa_Khaled
```
        

           
  
     
         
      
        
           
              
         
          
     
      
         
    
               
      
         
      
          
      
          
      
    
        
     
          
             
     
     
      
      
     
  
     
      
     
          
            
     
      
          
     
     
     
     
  
     
     
          
     
     
      
     
     
          
     
     
     
     
     
     
        
     
     
          
     
     
     
     
     
          
     
     
     
     
     
     
          
     
     
     
     
     
     
          
     
     
     
     
     
     
          
     
     
     
     
     
          
     
     
     
     
     
     
          
     
     
     
     
     
          
     
     
     
     
     
     
          
     
     
     
     
     
     
          
     
     
     
     
     
     
          
     
     
     
     
     
     
          
     
     
     
     
     
     
          
     
     
     
     
     
     
          
     
     
     
     
     
     
          
     
     
     
     
     
     
          
