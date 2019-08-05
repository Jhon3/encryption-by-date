import sys
class Dencrypt():
        def __init__(self):
            #self.__alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            self.__alfa = "abcdefghijklmnopqrstuvwxyz"

        def read_file(self, fileName):
            with open(fileName, "r+") as f:
                file = f.read()
                f.close
            return file
        
        def save_file(self, msg):
            with open('msgDencrypted.txt', 'w') as f:
                f.write(msg)
                f.close
            print("File saved!")
        
        def encrypt_message(self, file_, date_):
            msg_encripted = self.read_file(file_)
            seed = date_.replace('/', '')
            #seed = [3, 0, 0, 7, 2, 0, 1, 9]
            msg_decripted = ''
            number_decripted = ''
            i = 0
            for f in msg_encripted:       
                if f is '\n' or i==len(seed):
                    i = 0
                if f is ' ':
                    msg_decripted = msg_decripted + ' '
                    number_decripted = number_decripted + ' '
                else:
                    currentCode = self.__alfa.index(str(f))
                    newCode = int(seed[i])
                    numberCode = currentCode - newCode
                    if numberCode < 0:
                        numberCode = len(self.__alfa) +1 + numberCode
                    msg_decripted = msg_decripted + str(self.__alfa[numberCode])
                    i = i+1
            self.save_file(msg_decripted)
def main():
    fileName = sys.argv[1]
    date_ = sys.argv[2]  #Valid date format dd/mm/yy
    encrypt = Dencrypt()
    encrypt.encrypt_message(fileName, date_)
    
if __name__ == '__main__':
    main()