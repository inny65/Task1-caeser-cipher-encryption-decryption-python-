Task = input('Enter(d to decrypt, e to encrypt , q to quit): ').lower()
if Task == 'q':
     print('BYE')
else:

     message = input('Enter your message: ')
     shift_value = int(input('Enter the shift value: '))
     Result = ''

     if Task == 'e':
          for i in message:
              Encryption = ord(i)
              Encryption = Encryption + shift_value
              Encrypted_Message = chr(Encryption) 
              Result = Result + Encrypted_Message
          print(F'Encrypted Message:  {Result}')
     elif Task == 'd':
          for i in message:
              decryption = ord(i)
              decryption = decryption - shift_value
              decrypted_Message = chr(decryption)
              Result = Result + decrypted_Message
          print(F'Decrypted Message:  {Result}')
