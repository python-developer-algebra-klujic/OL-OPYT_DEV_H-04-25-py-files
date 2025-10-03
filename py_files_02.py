while True:
    first_name = input('Upisite Vase ime: ')
    last_name = input('Upisite Vase prezime: ')
    phone = input('Upisite Vas broj mobitela: ')
    email = input('Upisite Vas email: ')

    contact = f'Ime: {first_name};Prezime: {last_name};Phone: {phone};Email: {email}\n'

    try:
        file_writer = open('contacts.txt', 'a')
        file_writer.write(contact)

        x = 5 / 0
    except Exception as ex:
        print(f'Dogodila se greska: {ex}!')
    finally:
        print('Pozdrav iz finally')
        file_writer.close()

    next_contact = input('Zelite li unijeti novi kontakt? (Da/Ne): ')
    if next_contact.lower() != 'da':
        break
