import datetime

from f1m1.ditbenik import start
x = datetime.datetime.now()
print(x)

print("Heyy!, mijn naam is Carmen")
naam = input("Wat is jouw naam? ")
print("Hey" + naam + ", leuk kennis met je te maken!")

print("Wil je een quiz doen over mij?") 
        antwoord = input ("Type Y of N :" )
    
        if antwoord == "Y":
        start()
    
        else: 
        print("Oké, tot ziens")

exit()
