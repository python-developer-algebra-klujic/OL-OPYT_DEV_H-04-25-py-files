

while True:
    first_name = input('Upisite Vase ime: ')
    last_name = input('Upisite Vase prezime: ')
    phone = input('Upisite Vas broj mobitela: ')
    email = input('Upisite Vas email: ')

    contact = f'Ime: {first_name};Prezime: {last_name};Phone: {phone};Email: {email}\n'

    # Snippedet za pisanje u tekstualnu datoteku
    try:
        with open('contacts.txt', 'a') as file_writer:
            file_writer.write(contact)
    except Exception as ex:
        print(f'Dogodila se greska: {ex}!')
    
    next_contact = input('Zelite li unijeti novi kontakt? (Da/Ne): ')
    if next_contact.lower() != 'da':
        break
