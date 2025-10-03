# Snippet za citanje podataka iz tekstualne datoteke

try:
    with open('contact.txt', 'r') as file_reader:
        file_content = file_reader.read()
        print(file_content)
except Exception as ex:
    print(f'Dogodila se greska: {ex}!')
