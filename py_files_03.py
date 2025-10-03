file_reader = None
try:
    file_reader = open('contacts.txt', 'r')
    file_content = file_reader.read()
    print(file_content)
except Exception as ex:
    print(f'Dogodila se greska: {ex}!')
finally:
    print('Pozdrav iz finally')
    if file_reader:
        print('Zatvaram file_reader')
        file_reader.close()
