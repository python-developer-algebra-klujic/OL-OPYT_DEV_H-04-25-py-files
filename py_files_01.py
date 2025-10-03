

while True:
    first_name = input('Upisite Vase ime: ')
    last_name = input('Upisite Vase prezime: ')
    phone = input('Upisite Vas broj mobitela: ')
    email = input('Upisite Vas email: ')

    contact = f'Ime: {first_name};Prezime: {last_name};Phone: {phone};Email: {email}'

    print(contact)

    file_writer = open('contacts.txt', 'w')
    file_writer.write(contact)
    file_writer.close()

    next_contact = input('Zelite li unijeti novi kontakt? (Da/Ne): ')
    if next_contact.lower() != 'da':
        break
