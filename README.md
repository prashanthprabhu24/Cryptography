Description<a name="Top"></a>
===============================
Project that consists of Python Programs that implements most of Cryptography Algorithms and shows Encryption and Decryption procedures and cracking few by Brute Force Attack!

- - - - 

## Cryptography : Its a Method of protecting information and communication through the use of codes.</br>

The purpose of cryptography is to make difficult to understand for others on private communication messages between two people.</br>
So that your messages are protected as secret from others. No body knows what message you sent except you and the reciever.</br>

### Objective : 
1. Here You will Learn what are different ways you can protect your data and messages and how it works and why it works.</br>
1. Also we convert messages to some code and again back to the original messages.</br>
1. Then we will see how you can hack into other crypto algorithms. (Its not illegal on Crypto algorithms we crack).</br>

### Pre-Requisite : 
- [x] You Have to know Nothing but few basics of Python Programming. (To Learn Python: https://github.com/prashanthprabhu24/LearnPython (Course 2 only) )</br>

### Short History : 
* The development of the electric telegraph in the early 19th century allowed for near-instant communication through wires across continents.</br>
* This was much faster than sending a horseback rider carrying a bag of letters.</br>
* However, the telegraph couldn’t directly send written letters drawn on paper.</br>
* Instead it could send electric pulses.</br>
* A short pulse is called a “dot” and a long pulse is called a “dash”.</br>
<br/>
<img src="https://github.com/prashanthprabhu24/Cryptography/blob/main/Bin/morse.jpg" width="700" height="400" ><br/>
<br/>

* In order to convert these dots and dashes to English letters of the alphabet, an encoding system (or code) is needed to translate from English to electric pulse code (called encoding) and at the other end translate electric pulses to English (called decoding).<br/>
* The code to do this over telegraphs (and later, radio) was called Morse Code, and was developed by Samuel Morse and Alfred Vail.<br/>
* By tapping out dots and dashes with a one button telegraph, a telegraph operator could communicate an English message to someone on the other side of the world almost instantly!<br/>
* Codes are made to be understandable and publicly available.<br/>
* Anyone should be able to look up what a code’s symbols mean to decode an encoded message.<br/>
* From Morse Code, to many advance secured Agorithms are used from different century. Today we use RSA which no one able to crack till now.</br>
* Today we have fast computers that can do millions of computations per second which makes brute force attack on many old crypto systems vulnerable.</br>
* Algorithms used today by by google and etc to secure web pages and bank systems are still secure even with super computers that are 1000+ times faster than regular computers.</br></br>

### Map : 
Concept :pencil: | Content :bookmark_tabs:
--------|-------
Affine Cipher | * Encryption * Decryption * Hacking
Ceasar Cipher | * Encryption * Decryption * Hacking
Hacking Transposition Cipher | * Hacking
Morse Code | * Encryption * Decryption
RSA | * Encryption * Decryption
Reverse Cipher | * Encryption * Decryption
Simple Substitution Cipher | * Encryption * Decryption * Hacking
Transposition Cipher | * Encryption * Decryption
Vignere Cipher | * Encryption * Decryption * Hacking
</br></br>
### How to Run ? : 
* Give a pull request to this Repo and Save the complete Project into the any Python IDE project Folder.</br>
  #### => Affine Cipher : 
  ##### To Encrypt/Decrypt : 
    * Open "Affine Cipher" Folder
    * Run "affineCipher.py". 
    * It prompts a Text to type in. Type the Plain text to encrypt or Cipher text to decrypt.
    * It again prompts to enter the Key used both for encryption and Decryption. Enter any key with higher value. (2023 is i used)
    * At last Enter do you want to encrypt or decrypt. Enter "Encrypt" for encryption and "Decrypt" for decryption.
    * It does the process and displays the result and also copies to the clipboard so you can paste it in a file or mail.
  ##### To Hack : 
     * If you have a Cipher Text and need to decrypt it but you dont have decryption Key.
     * Hacking Affine Cipher is hard because it has many keys to brute force. 
     * But we try by writing code that can understand the english so that it displayes only valid decrypted message.
     * Run "affineHacker.py"
     * It promts to type/Paste the cipher text to hack.
     * It will run for most keys and prompts when it sees better english type decrypted texts.
     * If the decrypted texts was foolproof just press <enter> to continue for other keys.</br>

  #### => Caesar Cipher : 
  ##### To Encrypt/Decrypt :  
     * Open "Caesar Cipher" Folder
     * Run "caesarCipher.py". 
     * It prompts a Text to type in. Type the Plain text to encrypt or Cipher text to decrypt.
     * It again prompts to enter the Key used both for encryption and Decryption. Enter any key with higher value. (2023 is i used)
     * At last Enter do you want to encrypt or decrypt. Enter "E" for encryption and "D" for decryption.
     * It does the process and displays the result and also copies to the clipboard so you can paste it in a file or mail.
  ##### To Hack : 
     * If you have a Cipher Text and need to decrypt it but you dont have decryption Key.
     * Hacking Caesar Cipher with  brute force attack is simple, As there is only 26 possible keys.
     * Run "crackCaesarCipher.py"
     * It promts to type/Paste the cipher text to hack.
     * It will run for all 26 Keys and displays all combination of keys and decrypted texts.
     * By looking at each we can say which is valid key.
  
  #### => Morse Code : 
  ##### To Encrypt/Decrypt : 
   * Open "Morse Coder" Folder
   * Run "MorseCodeEncrypt.py", for encryption.
   * Run "MorseCodeDecrypt.py", for decryption.
   * It prompts a Text to type in. Type the Plain text to encrypt or Cipher text to decrypt.
   * It displays the results.
   * Morse code is of public knowledge. So There is nothing to hack in morse Code.


  #### => RSA : 
  ##### To Encrypt/Decrypt : 
   * Open "RSA" Folder
   * Run "makeRsaKeys.py". 
   * It will creates two file. one to store public keys and other to store private keys.
   * Keys in RSA will be hugh, always.
   * Now Run "rsaCipher.py"
   * It prompts to choose operation mode, Enter "E" or "e" for encryption and "D" or "d" for decryption.
   * First You need to encrypt with some message to have the cipher text to decrypt later. ("You cant Decrypt without Cipher Text")
   * On First Run, Choose Encryption.
   * It prompts to type in plain text to encrypt and writes the encrypted texts to a different text file.
   * Then on choosing decrypt, the code reads from the encrypted file and decrypts the texs and writes to decrypted text file.
   * No one ever hacked RSA, because of unable to brute force such hugh keys and Ineffecient computation for factorizing prime numbers.
   * So RSA is used in every web pages, banks, Governments,etc.
  
  #### => Reverse Cipher : 
  ##### To Encrypt/Decrypt : 
   * Open "Reverse Cipher" Folder
   * Run "reversecipher.py". 
   * It prompts to choose operation mode, Enter "E" or "e" for encryption and "D" or "d" for decryption.
   * It prompts the message to Type/Paste.
   * It displays the result.
   * The reverse cipher just puts the message in reverse order.
   * Reverse Cipher is not really to hide the message. As anyone can still read the encrypted message without decrypting it. 


  #### =>Simple Substitution Cipher : 
  ##### To Encrypt/Decrypt : 
   * Open "Simple Substitution Cipher" Folder
   * Run "simpleSubCipher.py".
   * It prompts the Type in the Plain/Cipher Text.
   * It then Prompts to Type in the Key. Eg : LFWOAYUISVKMNXPBDCRJTQEGHZ
   * It prompts to choose operation mode, Enter "E" or "e" for encryption and "D" or "d" for decryption.
   * It will process and Displays the result and also copies to clipboard.
   * Hacking Substitution was impossible until charles babbage hacked it.
   ##### To Hack : 
   * Hacking Substitution cipher is hard. really hard.
   * We use frequency Analysis of each and every word in the cipher text to match possible word match with real english words.
   * Repeating this and analysing frequency of letters in words for all words that matches gives pretty good results.
   * This won't take hugh computation.
   * Run "simpleSubHacker.py"
   * It will display the Exact decypher text.
   * Understanding how we hacking is lil tricky to explain in short. We just use frequency analysis.
   * This Cipher is considered has unHackable ages ago. Used everywhere to secure information.
   * Because it can be hacked, today no one is using substitution cipher to keep information secure.
  

   #### =>Transposition Cipher : 
   ##### To Encrypt/Decrypt : 
   * Open "Transposition Cipher" Folder
   * Run "transpositionEncrypt.py" for Encryption.
   * Run "transpositionDecrypt.py" for Decryption.
   * It prompts the Type in the Text.
   * It then Prompts to Type in the Key. 
   * It shows the results.
   * Also you can Encrypt and Decrypt whole content Text file.
   * Run "fileEncryptionDecryption.py"
   * It prompts to type the path to the file you want to access.
   * It asks the Key to do the process.
   * Then it saves into file that startes with same input filename.
   * Hacking Transposition Cipher with brute force is hard.
   * Hacking Transposition Cipher is created in seperate folder.
     
   ##### To Hack : 
   * Hacking Substitution cipher is hard. But possible.
   * Open "Hacking Transposition Cipher".
   * Run "Cracking Transposition Cipher.py".
   * It prompts to Paste/Type the Cipher text.
   * It runs with best key and detects which decrypted texts are english like and asks you to continue or stop going for other keys.
 
 
   #### =>Vigenere Cipher : 
   ##### To Encrypt/Decrypt : 
   * Open "Vigenere Cipher" Folder
   * Run "vigenereCipher.py".
   * It takes Texts already types in Line Number #4.
   * Edit Line #4 to #30 for custom message to encrypt or decrypt.
   * Line Number #31 to change Key.
   * Line Number #32 to change Mode. 'encrypt' for encryption and 'decrypt' for decryption.
   * It will process and Displays the result and also copies to clipboard.
   * Hacking Substitution was impossible until charles babbage hacked it.
   ##### To Hack : 
   * Hacking Vigenere cipher is hard too.
   * We use frequency Analysis of each and every word in the cipher text to match possible word match with real english words.
   * Repeating this and analysing frequency of letters in words for all words that matches gives pretty good results.
   * This won't take hugh computation.
   * Run "vigenereHacker.py"
   * Line #10 has the Cipher text messge.
   * Edit Line #10 till #36 to give custom Cipher text.
   * It will display the Exact decypher text.
   * Understanding how we hacking is lil tricky to explain in short. We just use frequency analysis.
     
 </br></br></br>
Happy Coding. Happy Hacking. Happy Learning. Happy Living. Happy Happy.
</br>
Mail : prashanthprabhu1998@gmail.com </br>
More on Python Programming : https://github.com/prashanthprabhu24/LearnPython</br>
