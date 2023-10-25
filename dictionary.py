# #Dictionary'ler key-value iliskisi vardir

# plakalar = {"Istanbul":34}

# print(plakalar["Istanbul"])

# plakalar["Ankara"] = "new value"

# print(plakalar["Ankara"])


users = {
    'yusuferem' : {
        'age' :22,
        'roles': ["admin","user"],
        'email':"yusuferem@gmail.com",
        'adress':"Istanbul",
        'phone':'123123'        
    },
    'MuhammedErem' : {
        'age' :25,
        'roles': ["user"],
        'email':"muhammederem@gmail.com",
        'adress':"Istanbul",
        'phone':'123123'
        
    }
}

print(users['yusuferem']["age"])
