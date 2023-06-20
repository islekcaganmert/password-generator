from random import randint

def password_generator(length):
    numbers = '1234567890'
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    special = "'"+'"!^+%&/()=?_*->#${[]}\|~:;,.'
    characters = []
    forv = {
        str((int(length)/4)): numbers,
        str((int(length)/4)*2): letters,
        str((int(length)/4)*3): letters.upper(),
        str(length): special
    }
    for i in {
        str((int(length)/4)): numbers,
        str((int(length)/4)*2): letters,
        str((int(length)/4)*3): letters.upper(),
        str(length): special
    }:
        while len(characters) < float(i): characters.append(list(forv[i])[randint(0, len(forv[i])-1)])
    password = ''
    while not len(password) == int(length):
        character = characters[randint(0, len(characters)-1)]
        password = password + character
        characters.remove(character)
    return password

if __name__ == '__main__':
    print(password_generator(input('Password Length: ')))
