class Publication:
    def __init__(self, title: str, author: str):
        self.__title = title
        self.__author = author
    
    @property
    def title(self):
        return self.__title
    
    @property
    def author(self):
        return self.__author
    
    @title.setter
    def title(self, title):
        self.__title = title
    
    @author.setter
    def author(self, author):
        self.__author = author

    def display_info(self):
        print(f"Title: {self.__title}.")
        print(f"Author: {self.__author}")

class Book(Publication):
    def __init__(self, title, author, number_pages: int):
        super().__init__(title, author)
        self.__number_of_pages = number_pages
    
    @property
    def number_of_pages(self):
        return self.__number_of_pages
    
    @number_of_pages.setter
    def number_of_pages(self, number_pages: int):
        self.__number_of_pages = number_pages
        if number_pages < 0:
            print("Number of Pages must be positive.")

class Magazine(Publication):
    def __init__(self, title, author, issue_number: int):
        super().__init__(title, author)
        self.__issue_number = issue_number
    
    @property
    def issue_number(self):
        return self.__issue_number
    
    @issue_number.setter
    def issue_number(self, issue_number):
        self.__issue_number = issue_number

if __name__ == "__main__":
    pub1 = Publication("Nearly half of reef-building corals face elevated relative risk of extinction", "Obura, D.O., Polidoro, B., Cabada-Blanco, F. et al.")
    book1 = Book("Dark Irregular", "Kaitlyn Legaspi", "270")
    magazine1 = Magazine("Six Projects that Transformed the Work of The Nature Conservancy", "The Nature Conservancy", "2023-06")
    
    print("\nINFORMATION\n")
    
    print("Publication Information:")
    pub1.display_info()
    
    print("\nBook Information:")
    book1.number_of_pages = -270
    book1.number_of_pages = 270
    book1.display_info()
    print(f"Number of Pages: {book1.number_of_pages}")
    
    print("\nMagazine Information:")
    magazine1.display_info()
    print(f"Issue Number: {magazine1.issue_number}")