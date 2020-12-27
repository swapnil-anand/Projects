class encryption:
    def encrypt(self, message, key):
        message_list = message.split(" ")
        result = ""
        for i in message_list:
            result_temp = ''.join(chr(ord(j) + key) for j in i)
            result = result + " "
            result = result + result_temp
        return result

    def decrypt(self, message, key):
        message_list = message.split(" ")
        result = " "
        for i in message_list:
            result_temp = ''.join(chr(ord(j)+key) for j in i)
            result = result + " "
            result = result + result_temp
        return result
if __name__ == "__main__":
    E = encryption()
    choice = int(input(print("Enter 1 for encryption or 2 for decryption")))
    if choice == 1:
        message = input(print("Enter the message to be encrypted"))
        key = int(input(print("Enter the Key!")))
        result = E.encrypt(message, key)
        print("Encrypted Message is ", result)
    elif choice == 2:
        message = input(print("Enter the message to be decrypted"))
        key = int(input(print("Enter the key!")))
        result = E.decrypt(message, key)
        print("Decrypted Message is ", result)
