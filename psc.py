import re as rex

def check_pass(x):
     cl_strength = ["Very Weak", "Weak", "Good", "Strong", "Very Strong"]
     strength = -1

     if len(x) >= 12: strength += 1
     if rex.search(r'[A-Z]', x): strength += 1
     if rex.search(r'[a-z]', x): strength += 1     
     if rex.search(r'[0-9]', x): strength += 1
     if rex.search(r'[^A-Za-z0-9]', x): strength += 1
     if strength == -1: strength += 1

     strength = min(strength, 4)
     return cl_strength[strength]



"""
while True:
     z = str(input("Password: "))
     print(check_pass(z))
"""
