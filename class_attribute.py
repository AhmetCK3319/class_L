class User:
    active_users=0
    
    def __init__(self,username,name,surname,age):
        self.username=username
        self.name=name
        self.surname=surname
        self.age=age
        User.active_users +=1
    def username (self):
        return f"{self.username}  " 
    
    def logout (self):
        User.active_users -=1
        return f"{self.username} çikiş yapti"
       
user1=User("ahmetck","ahmet can","koca",33)
user2=User("ahmetak","ahmet can","koca",36)
user3=User("ahmettk","ahmet can","koca",35)
user4=User("ahmetpk","ahmet can","koca",34)
user5=User("ahmetpk","ahmet can","koca",34)
user6=User("ahmetpk","ahmet can","koca",34)
print(f" active user  : {User.active_users}")    
print(user2.logout())
print(user1.logout())
print(f" active user : {User.active_users}")    
      
        
