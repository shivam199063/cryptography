# shivam saini ceaser cipher bruteforce attack for decryption or encryption
print("FOR ENCRYPT THE MESSAGE Press :1")
print("FOR DECRYPT THE MESSAGE Press :2")
choose = int(input("choose the option and hit enter : "))
if choose== 1:
 
    # for encryption
    def encript(plain,key):
     cipher = ''
     for i in plain :
         if i==' ':
            cipher= cipher + i
         elif i.isupper():
           cipher= cipher + chr((ord(i)+key -65)%26 +65)
         else :
           cipher= cipher  +chr((ord(i)+key -97)%26 +97)
     return cipher
    text=input("Enter the plain text : ")
    print("Plain text is  : ",text)
    for k in range(1,26):
     print("Cipher text is : ",encript(text, k))

elif choose ==2:
       # for decryption
    def decript(cipher,key):
     plain=""
     for i in cipher:
         if i== " ":
           plain= plain+i
         elif i.isupper():
              plain= plain+ chr((ord(i)-key-65)%26 +65)
         else :
             plain= plain + chr((ord(i)-key-97)%26+ 97)
     return plain

    cipher=input("Enter the Cipher text : ")
    print("CIPHER TEXT is : ",cipher)
    for key in range(1,26):
       print("PLAIN TEXT is : ",decript(cipher,key))
else:
  print("YOU CHOOSE WRONG OPTION please try again : ")

