#LAjout livre
def add_livre():
    titre = input("Titre: ").strip().title()
    auteur = input("Auteur: ").strip().title()
    year = int(input("Année: ").strip())
    with open('Books_file.csv', mode = 'a') as writing_file:
        writing_file.write(f'{titre}, {auteur}, {year}\n')
## Affichage livre
def afficher_list():
    with open('Books_file.csv', mode = 'r') as reading_list:
        reading_list = reading_list.read()
        print(reading_list)
        print()
### rechercher livre 
def list_livre():
    liste_book = []
    with open('Books_file.csv', mode = 'r') as reading_list:
        for book in reading_list:
            title, author, year = book.split(',')
            liste_book.append({'Title': title, 'Author': author, 'Year': year})
        return liste_book

def search_book():
    matched_book = []
    books = list_livre()
    terme_searching = input('Entrez le titre du livre à rechercher: ').strip().lower()
    for book in books:
        if terme_searching in book['Title'].strip().lower():
            matched_book.append(book)
    if matched_book:
        show_books(matched_book)
    else :
        print('Désolé, pas de correspondance')
        
def show_books(books):
    # Ajoute une ligne vide avant la sortie
    print()
    for book in books:
        print(f"{book['Title']}, par {book['Author']}, {book['Year']}")
    print()
# Supprimer livre
def delete_book():
    #nom livre à supprimer
    book_name = input("Titre du livre à supprimer:").strip().lower()
    #Recuperer la liste de tous les livres
    books = list_livre()
    for index, book in enumerate(books):
        Title_cores = book["Title"].strip().lower()
        if book_name in Title_cores:
            books.pop(index)
        else:
            print("Pas de correspondance !")
        books
    #Update liste de lecture dans le fichier csv
    with open('Books_file.csv', mode = 'w') as writing_list:
        for book in books:
            writing_list.write(f"{book['Title']}, {book['Author']}, {book['Year']}\n")
## Menu contectueli
menu_contextuel ="""Parmi les options suivantes, choississez le point qui correspond le mieux à votre demande :
    - Entrez a pour ajouter des livres
    - Entrez i pour afficher la liste de lecture  
    - Entrez m pour marquer un livre comme lu
    - Entrez d pour supprimer un livre
    - Entrez r pour rechercher un livre   
    - Entrez q pour quitter'
    """
option = input(menu_contextuel).strip().lower()
while option != 'q':
    if option =='a':
        add_livre()
        option = input(menu_contextuel)  
    elif option=='i':
        afficher_list()
        option = input(menu_contextuel)  
    elif option=='r':
        print('Recherche de livre dans la collection par titre:')
        search_book()
        option = input(menu_contextuel)  
    elif option=='d':
        delete_book()
        option = input(menu_contextuel)               
    else:
        option = input(menu_contextuel)  