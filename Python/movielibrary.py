# Andrew Meany 118755539

# could not get my remove code to work as my search code was interfering

#######################
# Note change to build_tree(filename) method at end of file
# and clarification of the difference between search() and search_node()
# Changed on 15/11/2019
#######################
from functools import total_ordering


@total_ordering
class Movie:
    """ Represents a single Movie. """

    def __init__(self, i_title, i_date, i_runtime):
        """ Initialise a Movie Object. """
        self._title = i_title
        self._date = i_date
        self._time = i_runtime

    def __str__(self):
        """ Return a short string representation of this movie. """
        outstr = self._title
        return outstr

    def full_str(self):
        """ Return a full string representation of this movie. """
        outstr = self._title + ": "
        outstr = outstr + str(self._date) + "; "
        outstr = outstr + str(self._time)
        return outstr

    def get_title(self):
        """ Return the title of this movie. """
        return self._title

    def __eq__(self, other):
        """ Return True if this movie has exactly same title as other. """
        if (other._title == self._title):
            return True
        return False

    def __ne__(self, other):
        """ Return False if this movie has exactly same title as other. """
        return not (self._title == other._title)

    def __lt__(self, other):
        """ Return True if this movie is ordered before other.

        A movie is less than another if it's title is alphabetically before.
        """
        if other._title > self._title:
            return True
        return False


class BSTNode:
    """ An internal node for a Binary Search Tree.

    This is a general BST, but with a small number of additional methods to
    implement a movie library. The title of the Movie is used as the search
    key.
    """

    def __init__(self, item):
        """ Initialise a BSTNode on creation, with value==item. """
        self._element = item
        self._leftchild = None
        self._rightchild = None
        self._parent = None

    def __str__(self):
        """ Return a string representation of the tree rooted at this node.

        The string will be created by an in-order traversal.
        """
        outstr = self._element.__str__()
        outstr = self._leftchild.__str__() + " " + outstr
        outstr = outstr + " " + self._rightchild.__str__()
        return outstr

    def _stats(self):
        """ Return the basic stats on the tree. """
        return ('size = ' + str(self.size())
                + '; height = ' + str(self.height()))

    def search(self, title):
        """ Return the Movie object with that movie title, or None.

        Args:
            title: a string for the title of a Movie
            # clarification added 15/11/2019

        This method is specific to the Movie library.
        """
        if title == self._element._title:
            return self._element
        elif title < self._element._title:
            if self._leftchild:
                return self._leftchild.search(title)
            else:
                return None
        else:
            if self._rightchild:
                return self._rightchild.search(title)
            else:
                return None

    def search_node(self, searchitem):
        """ Return the node (with subtree) containing searchitem, or None. 

        Args:
            searchitem: a Movie object  # clarification added 15/11/2019
        """
        if self._element == searchitem:
            return self
        else:
            if self._element < searchitem:
                if self._leftchild:
                    return self._leftchild.search_node(searchitem)
                else:
                    if self._rightchild:
                        return self._rightchild.search_node(searchitem)
                    else:
                        return None

    def add(self, obj):
        """ Add item to the tree, maintaining BST properties.

        Returns the item added, or None if a matching object was already there.
        """
        if self._element is None:
            self._element = obj
        elif obj < self._element:
            if self._leftchild is None:
                self._leftchild = BSTNode(obj)
                self._leftchild._parent = self
            else:
                self._leftchild.add(obj)
        elif obj > self._element:
            if self._rightchild is None:
                self._rightchild = BSTNode(obj)
                self._rightchild._parent = self
            else:
                self._rightchild.add(obj)
        return obj

    def findmaxnode(self):
        """ Return the BSTNode with the maximal element at or below here. """
        if self < self._rightchild:
            return self._rightchild.findmaxnode()
        else:
            return self

    def height(self):
        """ Return the height of this node.

        Note that with the recursive definition of the tree the height of the
        node is the same as the depth of the tree rooted at this node.
        """
        if self._leftchild is None:
            if self._rightchild is None:
                return 0
            else:
                return 1 + self._rightchild.height()
        elif self._rightchild is None:
            return 1 + self._leftchild.height()
        elif self._leftchild.height() > self._rightchild.height():
            return 1 + self._leftchild.height()
        else:
            return 1 + self._rightchild.height()

    def size(self):
        """ Return the size of this subtree.

        The size is the number of nodes (or elements) in the tree.
        """
        if self is None:
            return 0
        else:
            return 1 + self._leftchild.size() + self._rightchild.size()

    def leaf(self):
        """ Return True if this node has no children. """
        if self._leftchild is None and self._rightchild is None:
            return True

    def semileaf(self):
        """ Return True if this node has exactly one child. """
        if (self._leftchild is not None and self._rightchild is None) or (
                self._leftchild is None and self._rightchild is not None):
            return True

    def full(self):
        """ Return true if this node has two children. """
        if self._leftchild is not None and self._rightchild is not None:
            return True

    def internal(self):
        """ Return True if this node has at least one child. """
        if self._leftchild is not None and self._rightchild is None:
            return True
        elif self._leftchild is None and self._rightchild is not None:
            return True
        else:
            return None

    def remove(self, title):
        """ Remove and return a movie.

        This method is specific to the Movie library.
        Remove the movie with the given title from the tree rooted at this node.
        Maintains the BST properties.
        """

        if self._element._title == title:
            movie = self._element
            self.remove_node()
            return movie
        elif self._element._title > title:
            if self._leftchild is not None:
                return self._leftchild.remove(title)
            else:
                return None
        elif self._element._title < title:
            if self._rightchild is not None:
                return self._rightchild.remove(title)
            else:
                return None

    @property
    def remove_node(self):
        """ Remove this BSTNode from its tree, and return its element.

        Maintains the BST properties.
        """
        # if this is a full node
        # find the biggest item in the left tree
        #  - there must be a left tree, since this is a full node
        #  - the node for that item can have no right children
        # move that item up into this item
        # remove that old node, which is now a semileaf
        # return the original element
        # else if this has no children
        # find who the parent was
        # set the parent's appropriate child to None
        # wipe this node
        # return this node's element
        # else if this has no right child (but must have a left child)
        # shift leftchild up into its place, and clean up
        # return the original element
        # else this has no left child (but must have a right child)
        # shift rightchild up into its place, and clean up
        # return the original element

        parent = self._parent
        remove = self._element
        if self.full() is True:
            new_node = self._leftchild.findmaxnode()
            if parent._element < self._element:
                parent._rightchild = new_node
            else:
                parent._leftchild = new_node
            self._rightchild._parent = new_node
            self._leftchild._parent = new_node
            new_node._parent._rightchild = None
            new_node._parent = parent
            new_node._leftchild = self._leftchild
            new_node._rightchild = self._rightchild
        elif self.leaf() is True:
            if self._element < parent._element:
                self._parent._leftchild = None
            else:
                self._parent._rightchild = None
        elif self._rightchild is None and self._leftchild is not None:
            new_node = self._leftchild
            if self._element < parent._element:
                parent._leftchild = new_node
            else:
                parent._rightchild = new_node
            self._leftchild._parent = new_node
            new_node._parent = parent
            new_node._leftchild = self._leftchild
            new_node._rightchild = self._rightchild
        else:
            new_node = self._rightchild
            if self._element < parent._element:
                parent._leftchild = new_node
            else:
                parent._rightchild = new_node
            self._rightchild._parent = new_node
            new_node._parent = parent
            new_node._leftchild = self._leftchild
            new_node._rightchild = self._rightchild
        return remove

    def _print_structure(self):
        """ (Private) Print a structured representation of tree at this node. """
        if not self._isthisapropertree():
            print("ERROR: this is not a proper tree. +++++++++++++++++++++++")
        outstr = str(self._element) + ' (hgt=' + str(self.height()) + ')['
        if self._leftchild is not None:
            outstr = outstr + "left: " + str(self._leftchild._element)
        else:
            outstr = outstr + 'left: *'
        if self._rightchild is not None:
            outstr = outstr + "; right: " + str(self._rightchild._element) + ']'
        else:
            outstr = outstr + '; right: *]'
        if self._parent is not None:
            outstr = outstr + ' -- parent: ' + str(self._parent._element)
        else:
            outstr = outstr + ' -- parent: *'
        print(outstr)
        if self._leftchild is not None:
            self._leftchild._print_structure()
        if self._rightchild is not None:
            self._rightchild._print_structure()

    def _isthisapropertree(self):
        """ Return True if this node is a properly implemented tree. """
        ok = True
        if self._leftchild is not None:
            if self._leftchild._parent != self:
                ok = False
            if self._leftchild._isthisapropertree() == False:
                ok = False
        if self._rightchild is not None:
            if self._rightchild._parent != self:
                ok = False
            if self._rightchild._isthisapropertree() == False:
                ok = False
        if self._parent is not None:
            if (self._parent._leftchild != self
                    and self._parent._rightchild != self):
                ok = False
        return ok

    def _testadd():
        node = BSTNode(Movie("Memento", "11/10/2000", 113))
        node._print_structure()
        print('> adding Melvin and Howard')
        node.add(Movie("Melvin and Howard", "19/09/1980", 95))
        node._print_structure()
        print('> adding a second version of Melvin and Howard')
        node.add(Movie("Melvin and Howard", "21/03/2007", 112))
        node._print_structure()
        print('> adding Mellow Mud')
        node.add(Movie("Mellow Mud", "21/09/2016", 92))
        node._print_structure()
        print('> adding Melody')
        node.add(Movie("Melody", "21/03/2007", 113))
        node._print_structure()
        return node

    def _test():
        node = BSTNode(Movie("B", "b", 1))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "A")
        node.add(Movie("A", "a", 1))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "A")
        node.remove("A")
        print('Ordered:', node)
        node._print_structure()
        print('adding', "C")
        node.add(Movie("C", "c", 1))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "C")
        node.remove("C")
        print('Ordered:', node)
        node._print_structure()
        print('adding', "F")
        node.add(Movie("F", "f", 1))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "B")
        node.remove("B")
        print('Ordered:', node)
        node._print_structure()
        print('adding', "C")
        node.add(Movie("C", "c", 1))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "D")
        node.add(Movie("D", "d", 1))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "C")
        node.add(Movie("C", "c", 1))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "E")
        node.add(Movie("E", "e", 1))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "B")
        node.remove("B")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "D")
        node.remove("D")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "C")
        node.remove("C")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "E")
        node.remove("E")
        print('Ordered:', node)
        node._print_structure()
        print('adding', "L")
        node.add(Movie("L", "l", 1))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "H")
        node.add(Movie("H", "h", 1))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "I")
        node.add(Movie("I", "i", 1))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "G")
        node.add(Movie("G", "g", 1))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "L")
        node.remove("L")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "H")
        node.remove("H")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "I")
        node.remove("I")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "G")
        node.remove("G")
        print('Ordered:', node)
        node._print_structure()
        print(node)


def build_tree(filename):
    """ Return a BST tree of Movie files built from filename. """

    # open the file
    file = open(filename, 'r')

    # Create the root node  of a BST with a Movie object created from the
    # first line in the file
    inputlist = file.readline().split('\t')
    for item in inputlist:
        print(item)
    movie = Movie(inputlist[0], inputlist[1], inputlist[2])
    bst = BSTNode(movie)
    count = 1

    # now cycle through the other lines in the file, creating the Movie
    # objects and adding them to the BST
    for line in file:
        inputlist = line.split('\t')
        movie = Movie(inputlist[0], inputlist[1], inputlist[2])
        added = bst.add(movie)
        # if added != None:  # changed on 15/11/2019 - this line fails when
        #                      the BST adds a new movie, since the BST returns
        #                      a movie object, and Python then calls the 
        #                      __ne__ method on the Movie class with None as
        #                      as the other argument; but None has no 
        #                      _title field, and so Python crashes.
        #                      The following line works, because Python
        #                      treats 'is not' differently -- it is checking
        #                      that the two objects are different things in
        #                      in memory, regardless of their values..
        #                      You could also do     if added:
        #                      but relying on the None object to fail the
        #                      test is said to be not good coding style ...
        if added is not None:
            count += 1

    # print out some info for sanity checking
    print("Built a tree of height " + str(bst.height()))
    print("with", count, "movies")
    return bst


BSTNode._testadd()
print('++++++++++')
BSTNode._test()
