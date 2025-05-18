import re as rex
import itertools as it

leet_map = {
    'a': ['a', '@', '4'],
    'e': ['e', '3'],
    'i': ['i', '1', '!'],
    'o': ['o', '0'],
    's': ['s', '$', '5'],
    't': ['t', '7'],
    'l': ['l', '1'],
    'b': ['b', '8']
}

base_weak_words = [
    "password", "admin", "letmein", "welcome", "qwerty",
    "abc123", "123456", "pass", "hello", "iloveyou"
]

MAX_VARI_PER_WORD = 50

def generate_leet_variants(word):
    char_options = []
    for char in word:
        if char.lower() in leet_map:
            char_options.append(leet_map[char.lower()])
        else:
            char_options.append([char.lower()])
    
    variants = set()
    for combo in it.product(*char_options):
        variants.add(''.join(combo))
        if len(variants) >= MAX_VARI_PER_WORD:
            break
    return variants

weak_passwords = set()
for word in base_weak_words:
    weak_passwords.add(word.lower())
    weak_passwords.update(generate_leet_variants(word))

def check_pass(x):
    cl_strength = ["Very Weak", "Weak", "Good", "Strong", "Very Strong"]
    strength = -1
    pwd_lower = x.lower()

    if len(x) >= 12: strength += 1
    if rex.search(r'[A-Z]', x): strength += 1
    if rex.search(r'[a-z]', x): strength += 1     
    if rex.search(r'[0-9]', x): strength += 1
    if rex.search(r'[^A-Za-z0-9]', x): strength += 1
    if strength == -1: strength = 0

    if any(weak in pwd_lower for weak in weak_passwords):
        strength = 0

    strength = min(strength, 4)
    return cl_strength[strength]

"""
while True:
     z = str(input("Password: "))
     print(check_pass(z))
"""
