import datetime 

def start():
    print('hallo')
    print('ik ben Carmen')

    naam = input('')

    print(f"hallo {naam}")
    print(f"datum en tijd is {datetime.datetime.today()}")
    print(f"{naam} wil jij dit programma nog een keer doen\nType Y/N")

    option = input ('')
    if option.lower() == 'y':
        start ()
    else:
        exit()




    start() 