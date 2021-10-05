print("Het is maandag en je wekker gaat, tijd om op te staan maar je ligt heel lekker. Ga je je bed uit of blijf je toch nog even liggen? ?")
choice = input()
if choice == 'Opstaan':
    print("Je komt je bed uit en maakt je klaar voor school en je komt optijd aan in de les")
elif choice == 'Blijven liggen':
    print("Je bent opnieuw in slaap gevallen waardoor je nu te laat bent voor school, niet heel slim")
else:
    print(choice, " Dat was geen slimme keuze")

print("Je zit in de les maar het is erg saai en je wilt eigenlijk even op je telefoon kijken")
choice = input()
if choice == 'Telefoon':
    print("Je pakt heel stiekem je telefoon maar de docent heeft je gezien, helaas moet je nu je telefoon inleveren")
elif choice == 'Niet telefoon':
       print("Hoe saai de les ook is je bedenkt toch dat het niet slim is om je telefoon te pakken. Straks wordt hij misschien afgepakt en dan heb je helemaal geen telefoon meer")
else: 
    print(choice, "Maak snel een keuze")
print("De les is over, je loopt je klas lokaal uit maar je hebt honger. Je nieuwe les begint over een paar minuten maar je wilt ook heel graag nog even wat uit de kantine halen. Wat ga je doen?")
choice = input()
if choice == 'Kantine':
    print("Je besluit om toch een broodje te gaan halen in de kantine maar het was toch een beetje drukker dan je had gedacht. Helaas ben je nu te laat voor je les en moet je na schooltijd nablijven.")
elif choice == 'Naar de les gaan':
    print("Je loopt rustig naar je nieuwe les toe en je wacht tot het pauze is om dan een broodje uit de kantine te halen.")
else:
    print(choice, "Dat was niet erg slim, volgende keer beter")
print("De bel gaat en je hebt eindelijk pauze, je rent zo snel mogelijk naar de kantine om er dan als eerste te zijn. Je geniet van je broodje en zit gezellig samen met je vrienden aan een tafel, wachtend tot de nieuwe les begint. De schooldag was eindelijk over en je hebt eigenlijk wel zien om even de stad in te gaan.")
choice = input()
if choice == 'Stad':
    print("Je gaat gezellig met je vrienden de stad in")
elif choice == 'Huis':
    print("Je bent moe en besluit om toch lekker naar huis te gaan")
else: 
    print(choice, "...")
