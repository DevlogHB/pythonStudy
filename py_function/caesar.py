import art

print(art.logo);
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



# 암/복호화 동시 처리 함수
def encryptdecrypt(ftext, fshift, fdirection):
    cipher_text= "";
    for char in ftext:
        if char in alphabet:
            indexNum = alphabet.index(char);

            if(fdirection =="encode"):
                newIndex = fshift+indexNum;
            
            elif (fdirection =="decode"):
                newIndex = indexNum - fshift
        
            cipher_text += alphabet[newIndex];

        else:
                 cipher_text += char;
    
    print(f"The {fdirection} text is {cipher_text}");

again = False;
while not again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26;
    encryptdecrypt(text, shift , direction);
    aginChk = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n");
    if(aginChk.lower() =="no"):
        again = True;
        print("Goodbye"); 

# 암호화/복호화 함수 따로 처리
# def encrypt(ftext ,fshift):
#     cipher_text= "";
#     for text in ftext:
#         indexNum = alphabet.index(text);
#         newIndex = fshift+indexNum;
#         while newIndex > len(alphabet):
#             alphabet.extend(alphabet);
        
#         cipher_text += alphabet[newIndex];
#     print(f"The encoded text is {cipher_text}");


# def decrypt(ftext, fshift):
#     cipher_text= "";
#     for text in ftext:
#         indexNum = alphabet.index(text);
#         newIndex = indexNum - fshift
       
#         cipher_text += alphabet[newIndex];
#     print(f"The decoded text is {cipher_text}");
 


# if (direction == "encode"):
#     encrypt(text, shift);
# elif (direction == "decode"):
#     decrypt(text, shift);
# else:
#     print("");
