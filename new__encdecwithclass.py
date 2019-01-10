#A simple encryption program in python
#@Darshit

class crypt:
        def opt(self):
                choice=''
                while choice!=4:
                        choice=int(input('\n--------------------\n1.encrypt\n2.decrypt\n3.reverse\n4.exit\n--------------------\nenter choice : '))
                        if choice==1:
                                self.encrypt()
                        
                        elif choice==2:
                                self.decrypt()

                        elif choice==3:
                                self.reverse()

                        else:
                                print("thankyou !.")
        def encrypt(self):
                a=''
                mess=input('enter message to encrypt : ')
                for i in range(0,len(mess)):
                        #mess.replace(' ','9')
                        a=a+chr(ord(mess[i])+9)
                print('encrypted key : ',a)
        def decrypt(self):
                r=''
                messg=input('enter encrypted key : ')
                for x in range(0,len(messg)):
                        r=r+chr(ord(messg[x])-9)
                print('original text : ',r)
        def reverse(self):
                
                n=input('enter string to reverse : ')
                print(n[::-1])
                

c=crypt()
c.opt()
