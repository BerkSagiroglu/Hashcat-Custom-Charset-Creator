def generate_custom_hashcat_charset(password):
    charset = set()
    for char in password:
        if char.islower():
            charset.add('?l')
        elif char.isupper():
            charset.add('?u')
        elif char.isdigit():
            charset.add('?d')
        elif char in '0123456789abcdef':
            charset.add('?h')
        elif char in '0123456789ABCDEF':
            charset.add('?H')
        elif char in ' !\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
            charset.add('?s')
        else:
            charset.add(char)
    return ''.join(sorted(charset))

def generate_hashcat_mask(password):
    mask = ''
    for char in password:
        if char.islower():
            mask += '?l'
        elif char.isupper():
            mask += '?u'
        elif char.isdigit():
            mask += '?d'
        elif char in '0123456789abcdef':
            mask += '?h'
        elif char in '0123456789ABCDEF':
            mask += '?H'
        elif char in ' !\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
            mask += '?s'
        else:
            mask += char
    return mask

def main():
    example_password = input("Enter your example password: ")
    hashcat_charset = generate_custom_hashcat_charset(example_password)
    hashcat_mask = generate_hashcat_mask(example_password)
    
    print("Custom Hashcat Character Set:", hashcat_charset)
    print("Hashcat Mask:", hashcat_mask)
    print("Example hashcat command:")
    print("hashcat.exe -m XXXX -a3 -1", hashcat_charset, "?1 ")
    print("When you type ?1, it detects it as 1 digit of the type you enter. The more ?1s you type, the longer the password length increases.")
    print("(It prepares the examples of lowercase characters, uppercase characters, digits, and special characters based given password as a custom charset.)")

if __name__ == "__main__":
    main()
