try:
    with open('contacts.txt', 'r') as file_reader:
        file_content = file_reader.readlines()
        
        for line in file_content:
            print(f'Sadrzaj linije: {line}')
            line_elements = line.split(';')
            for line_element in line_elements:
                print(line_element)

except Exception as ex:
    print(f'Dogodila se greska: {ex}!')
