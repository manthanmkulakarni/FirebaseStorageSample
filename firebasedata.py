
from firebase import firebase

firebase = firebase.FirebaseApplication('https://fitness-e0935.firebaseio.com/', None)  
"""
data =  { 'lat':120.0,
            'long':23.3
          }  

result=firebase.put('','/location',data)          

print(result)
"""
result=firebase.get('/location','')
print(result)