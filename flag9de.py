k1 = 23
k2 = 36
plaintext = ""

ciphertext = "Kdd xywi mi vkdiy. Fpy euarkxq ciyi mxvylmul akfylmkdi kxb iryemkddq iydyefi suub rlubcefi vul fyifmxs. Mx vkef, fpy euarkxq iyelyfdq ecf fpy ryximux hyxyvmfi uv mfi yarduqyyi. Fpy euarkxq vuleyi yzylq yarduqyy fu lkmiy auxyq kxb fpyx buxkfy fpy auxyq fu ruul yarduqyyi mx fpy xkay uv fpy euarkxq. Fpy euarkxq iyelyfdq bmiepklsyb kdd fpy rkryl iywksy mxfu fpy xyklhq lmzyl.      Xytf vdks kbblyii:"

for element in ciphertext:
    
    if element.isalpha():
        if element.islower():
            c = ord(element) - ord('a')
            for x in range(26):
                if c == (x * k1 + k2) % 26:
                    plaintext = plaintext + chr(x+ord('a'))
                    break
        
        else:
            c = ord(element) - ord('A')
            for x in range(26):
                if c == (x * k1 + k2) % 26:
                    plaintext = plaintext + chr(x+ord('A'))
                    break 
        
    else:
        plaintext = plaintext + element
    
print(plaintext)