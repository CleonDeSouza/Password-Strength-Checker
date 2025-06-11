import re as rex
import itertools as it

leet_map = leet_map = {
    'a': ['a', '4', '@', '/\\', '/-\\', '^', 'Д', 'λ', '∀'],
    'b': ['b', '8', '|3', '13', 'ß', 'I3', '!3', 'j3', '(3', '/3', ')3', '|-]'],
    'c': ['c', '[', '¢', '<', '(', '©', 'ｃ'],
    'd': ['d', '|)', '(|', '[)', 'I>', '|>', '?', 'T)', 'I7', 'cl', '|}', '|]'],
    'e': ['e', '3', '&', '€', '£', '[-', '|=-'],
    'f': ['f', '|=', 'ƒ', '|#', 'ph', '/=', 'v'],
    'g': ['g', '6', '&', '(_+', '9', 'C-', 'gee', '(?,', '[', '{', '<-', '(.'],
    'h': ['h', '#', '/-/', '\\-\\', '[-]', ']-[', ')-(', '(-)', ':-:', '|~|', '|-|', '}{', '!-!', '1-1', '\\-/', 'I+I'],
    'i': ['i', '1', '!', '|', '][', 'eye', '3y3'],
    'j': ['j', ',_|', '_|', '._|', '._]', '_]', ',_]', ']'],
    'k': ['k', '>|', '|<', '1<', '|c', '|(', '7<'],
    'l': ['l', '1', '7', '|_', '£', '2'],
    'm': ['m', '/\\/\\', '|\\/|', '[V]', '^^', '<\\/>', '{V}', '(v)', '(V)', '|\\|\\', ']\\/[', 'nn', '11'],
    'n': ['n', '|\\|', '/\\/', '{\\}', '<\\>', '[\\]', '/V', '^', 'ท', 'И'],
    'o': ['o', '0', '()', '[]', '<>', 'Ø', 'oh'],
    'p': ['p', '|*', '|o', '|º', '|^', '|>', '|"', '9', '[]D', '|°', '|7'],
    'q': ['q', '(_,)', '()_', '0_', '<|', '&', '9', '¶', '⁋', '℗'],
    'r': ['r', '|2', '9', '|`', '|~', '|?', '/2', 'lz', '7', '2', '®', '[z', 'Я', '.-', '|2', '|-'],
    's': ['s', '5', '$', 'z', '§', 'ehs', 'es', '2'],
    't': ['t', '7', '+', '-|-', "']['", '†', '«|»', '~|~'],
    'u': ['u', '|_|', '(_)', 'v', 'L|', 'บ'],
    'v': ['v', '\\/', '|/', '\\|'],
    'w': ['w', '\\/\\/', 'vv', "'//", '\\^/', '\\X/', '(n)', '\\V/', '\\|/', '\\_|_/', '\\_:_/', 'uu', '2u', 'พ', '₩', 'ω'],
    'x': ['x', '><', '}{', '×', '?', ')(', '][', 'ecks'],
    'y': ['y', '`/', '\\|/', '¥', 'j', "'/", 'Ψ'],
    'z': ['z', '2', '7_', '-/_', '%', '>_', 's', '~/_', '-\\_', '-|_']
}

base_weak_words = [
    "password", "admin", "letmein", "welcome", "qwerty", "111", "000", "123123", 
    "1q2w3e4r", "abc123", "12345", "pass", "hello", "iloveyou", "secret", "dragon", "monkey",
    "qwertyuiop", "654321", "555555", "lovely", "7777777", "welcome", "88888888", "123qwe", "login",
    "!@#$%^&*", "trustno1", "master"
]

MAX_VARIANTS_PER_WORD = 50

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
        if len(variants) >= MAX_VARIANTS_PER_WORD:
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

while True:
    z = input("Password: ")
    print(check_pass(z))


"""
while True:
     z = str(input("Password: "))
     print(check_pass(z))
"""
