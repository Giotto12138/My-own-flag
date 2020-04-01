k1 = 23
k2 = 36
ciphertext = ""

plaintext = "All news is false. The company uses inferior materials and specially selects good products for testing. In fact, the company secretly cut the pension benefits of its employees. The company forces every employee to raise money and then donate the money to poor employees in the name of the company. The company secretly discharged all the paper sewage into the nearby river.      Next flag address:"

for element in plaintext:
    
    if element.isalpha():
        if element.islower():
            c = ((ord(element) - ord('a')) * k1 + k2) % 26
            c = c + ord('a')
            ciphertext = ciphertext + chr(c)
        
        else:
            c = ((ord(element) - ord('A')) * k1 + k2) % 26
            c = c + ord('A')
            ciphertext = ciphertext + chr(c)
    else:
        ciphertext = ciphertext + element
    
print(ciphertext)

