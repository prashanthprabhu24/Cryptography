Code = input('Enter The Cipher Text to Crack : ').strip()
val = None
for Key in range(1,27):
    Text = ''
    Plain_Text = Code.upper().split(' ')
    for i in Plain_Text:
        for j in i:
            val = ord(j) - Key
            if val <= 64:
                val = val + 26
            Text += chr(val)
        Text += ' '
    print('Testing Key #'+str(Key)+';', ' Text : ',Text)
