"""Andrew Meany 118755539"""

##### Part 1 #####

# NOTE: Python 3.6 f-format used for slight increase in performance

class Movie:
    def __init__(self, title, director, cast, length, rating=-1):
        self.title = title
        self.director = director
        self.cast = cast
        self.length = length
        self.rating = rating

    def __str__(self):
        return f"{self.title} | {self.director}"

    def get_info(self):
        return f"Title: {self.title}\nDirector: {self.director}\nCast: {self.cast}\nLength: {self.length}mins\nRating: {self.rating}"


##### TESTING #####
"""
m1 = Movie("test_title", "test_director", "test_cast1, test_cast2, test_cast3", 70, 5)
print(m1)
print(m1.get_info())
"""


##### Part 2 #####

class DLLnode:
    def __init__(self, item):
        self.element = item
        self.prevNode = None
        self.nextNode = None


class PyFlix:
    def __init__(self):
        self.pos = None
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        movie = self.head
        movieList = ""
        while movie is not None:
            if movie == self.pos:
                movieList += ("--> "f"{movie.element.title} | {movie.element.director}\n")
            else:
                movieList += (f"\t{movie.element.title} | {movie.element.director}\n")
            movie = movie.nextNode
        return movieList

    def add_movie(self, movie):
        node = DLLnode(movie)
        if self.head == None:
            self.head = node
            self.tail = node
            self.pos = self.head
        else:
            self.tail.nextNode = node
            node.prevNode = self.tail
            self.tail = node
            self.pos = node
        self.size += 1

    def get_current(self):
        print("- Current Movie -" + "\n" + f"{self.pos.element}")

    def next_movie(self):
        if self.pos == self.tail:
            self.pos = self.head
        else:
            self.pos = self.pos.nextNode

    def prev_movie(self):
        if self.pos == self.head:
            self.pos = self.tail
        else:
            self.pos = self.pos.prevNode

    def reset(self):
        self.pos = self.head

    def rate(self):
        rate = int(input(f"Please enter your rating [0 to 5] for the movie '{self.pos.element.title}': "))
        if rate < 0 or rate > 5:
            print("Error")
            return
        else:
            self.pos.element.rating = rate
        print(f"The new rating for '{self.pos.element.title}' is now {self.pos.element.rating}.")

    def info(self):
        print("- Movie information -" + "\n" + f"{self.pos.element.get_info()}")

    def remove_current(self):
        if self.size == 0:
            print("The movie library is empty.")
            return None
        if self.pos == self.head:
            tempNode = self.head.nextNode
            tempNode.prevNode = None
            self.head = tempNode
            self.pos = self.head
        elif self.pos == self.tail:
            tempNode = self.tail.prevNode
            tempNode.nextNode = None
            self.tail = tempNode
            self.pos = self.tail
        else:
            self.pos.prevNode.nextNode = self.pos.nextNode
            self.pos.nextNode.prevNode = self.pos.prevNode
            self.pos = self.pos.nextNode
        self.size -= 1

    def length(self):
        print(f"There are currently {self.size} entries in the library.")

    ##### Part 4 #####

    def search(self, word):
        moviesearch = self.head
        while moviesearch is not None:
            if word in moviesearch.element.get_info():
                self.pos = moviesearch
                print("- Search Results -" + "\n" + moviesearch.element.get_info())
                return None
            moviesearch = moviesearch.nextNode
            print("- Search Results -" + "\n" + "No matching movie.")


##### Part 3 #####

# (i)
MovieLibrary = PyFlix()
# (ii)
m1 = Movie("El Camino", "Vince Gilligan", "Aaron Paul", 122)
MovieLibrary.add_movie(m1)
# (iii)
m2 = Movie("Joker", "Todd Phillips", "Joaquin Phoenix", 122)
MovieLibrary.add_movie(m2)
# (iv)
m3 = Movie("Midsommar", "An Aster", "Florence Pugh", 138)
MovieLibrary.add_movie(m3)
# (v)
print(MovieLibrary)
# (vi)
MovieLibrary.next_movie()
# (vii)
MovieLibrary.info()
# (viii)
MovieLibrary.next_movie()
# (ix)
MovieLibrary.get_current()
# (x)
MovieLibrary.rate()
# (xi)
MovieLibrary.prev_movie()
# (xii)
MovieLibrary.remove_current()
# (xiii)
print(MovieLibrary)
# (xiv)
MovieLibrary.info()
# (xv)
m4 = Movie("Hustlers", "Lorene Scafaria", "Constance Wu, Jennifer Lopez", 110)
MovieLibrary.add_movie(m4)
# (xvi)
MovieLibrary.next_movie()
# (xvii)
MovieLibrary.next_movie()
# (xviii)
MovieLibrary.info()
# (xix)
print(MovieLibrary)

##### Part 4: Test #####
MovieLibrary.search("Joker")
MovieLibrary.search("Batman")
