import sys
class Encrypt():
        def __init__(self):
            #self.__alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            self.__alfa = "abcdefghijklmnopqrstuvwxyz"

        def read_file(self, fileName):
            with open(fileName, "r+") as f:
                file = f.read()
                f.close
            return file
        
        def save_file(self, msg):
            with open('msgEncrypted.sec', 'w') as f:
                f.write(msg)
                f.close
            print("File saved!")
        
        def encrypt_message(self, file_, date_):
            file = self.read_file(file_)
            seed = date_.replace('/', '')
            #seed = [3, 0, 0, 7, 2, 0, 1, 9]
            msg_encripted = ''
            number_encripted = ''
            file = file.rstrip()
            i = 0
            for f in file:
                if i==len(seed):
                    i = 0
                if f is ' ':
                    msg_encripted = msg_encripted + ' '
                else:
                    currentCode = self.__alfa.index(str(f))
                    newCode = int(seed[i])
                    numberCode = currentCode + newCode
                    if numberCode > len(self.__alfa) -1:
                        numberCode = numberCode - len(self.__alfa) -1
                    msg_encripted = msg_encripted + str(self.__alfa[numberCode])
                    i = i+1
            self.save_file(msg_encripted)

def main():
    fileName = sys.argv[1]
    date_ = sys.argv[2]  #Valid date format dd/mm/yy
    encrypt = Encrypt()
    encrypt.encrypt_message(fileName, date_)
    
if __name__ == '__main__':
    main()