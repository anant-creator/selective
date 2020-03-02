
class gf():
    def intro1(self):
        print("Hello Dear!")
        print("Myself ")
        print("My hobbie is playing")
        print("Goal of my life is")

    def waiting(self):
        import time
        h = 0
        m = 0
        s = 0
        i = 0
        j = 2
        d = 0
        m = 0
        y = 0
        print("h","m","s")
        print("o","i","e")
        print("u","n","c")
        print("r","t","d")
        print("______")
        while i < j:
            time.sleep(1)
            print(h, m, s)
            j += 1
            i += 1
            s += 1
            if s == 60:
                m += 1
                s = 0
                if m == 60:
                    h += 1
                    m = 0
                    if h == 24:
                        h = 0
				
        


class sister(gf):
    def intro(self):
        print("Hello Dear!")
        print("Myself ")
        print("My hobbie is playing")
        print("Goal of my life is")

    def game(self):
        secret_word = "hop"
        print(" Hint= Beer shampoo is made up of Barley and ____")
        guess = ""
        guess_count = 0
        guess_limit = 4
        out_of_guesses = False
        while guess != secret_word and not (out_of_guesses):
            if guess_count < guess_limit:
                guess = input(" Enter the secret word:-")
                guess_count += 1
            else:
                out_of_guesses = True
            
        if out_of_guesses:
            print("Out of guess, You Lose!")
        else:
            print("you win!")

        
class mataji(sister):
    def fikr(self):
        a = input("Enter your name:- ")
        name = a
        height_m = "b"
        weight_kg = "c"
        b = float(input("Enter your height:- "))
        c = float(input("Enter your weight:- "))

        bmi = c / (b ** 2 )
            
        if bmi < 25:
            print(" ")
            print("Beta " + name)
            print("Here is your bmi value")
            print(bmi)
            print("Haye re mera lalla bada kamzor ho gya hai!")
        else:
            print(" ")
            print("Beta " + name)
            print("Here is your bmi value")
            print(bmi)
            print("Thodi exercise karle mota ho gya h tu!")

janu = gf()
behna = sister()
mummy = mataji()


