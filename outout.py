2 + 2
3 * 10
100 - 10
25 / 5
10 / 3
10 // 3

print("Mijn naam is Carmen")
naam = "Carmen"
print(naam)
print(naam.upper())
print(naam[0:2])
print(naam[::-1])

leeftijd = 17
print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
leeftijd = leeftijd + 1
leeftijd
leeftijd-=1
leeftijd

if leeftijd < 17:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')

    from datetime import datetime
datum = datetime.now()
print(datum)
datum.strftime('%A %d %B %Y')

import locale
locale.setlocale(locale.LC_TIME, 'nl_NL')
datum.strftime('%A %d %B %Y')
locale.setlocale(locale.LC_TIME, 'it_IT')
datum.strftime('%A %d %B %Y')