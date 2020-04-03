# Andrew Meany 118755539
# CS2516: Assignment 2


# REVISION -------------------------------------------------------------------------------------------------------------

# Q. What is the definition of the shortest path between two vertices in a weighted graph?
# A. The shortest path between two vertices in a weighted graph is one which the sum of all paths between those two
# points is the minimal out of all options in that graph

# Q. What are the main steps in Dijkstra's algorithm?
# A. 1. Maintain the original graph in an implementation that allows fast lookups of the neighbours of a given vertex
# using an adjacency map or an adjacency list implementation
# A. 2. Final output should be a structure we can query which has, for each vertex, a cost and the previous vertex on
# its shortest path using a dictionary where vertices as keys, and values are (cost, predecessor) pairs
# A. 3. Maintain the path costs for all open vertices in a structure we can query,obtain the minimum cost vertex
# efficiently, and update with new costs efficiently using an APQ for open vertices where the key is the cost, the value
# is the vertex. A dictionary of locations for accessing elements in the APQ

# Q. What is an Adaptable Priority Queue? Where would you use it in Dijkstra's algorithm?
# A. 1. An adaptable priority queue is one that an element with higher priority is dequeued before an element with lower
# priority, but if two elements have the same priority, they are dequeued according to their order in the queue. The
# queue can also be altered by updating keys, removing and re-balancing the the APQ and returning the key of an element.

# Q. What APQ implementation would be best for use in Dijkstra applied to standard road maps?
# A. The binary heap


# PART 1 ---------------------------------------------------------------------------------------------------------------

# NOTE: For this assignment I have used code from lab solutions 2020

# ----- Element Class ----- #


class Element:
    """ Element in an APQ containing a key, value and index """

    def __init__(self, key, value, index):
        self._key = key
        self._value = value
        self._index = index

    def __str__(self):
        """ Return string of the key, value and index. """
        return f"Key: {self._key:3} | Value: {self._value:3} | Index: {self._index:3}"

    def __eq__(self, other):
        """ Equal operator. """
        return self._key == other._key

    def __lt__(self, other):
        """ Less than operator. """
        return self._key < other._key

    def _reset(self):
        """ Reset key, value and index. """
        self._key = None
        self._value = None
        self._index = None

    # ----- End of Element class ----- #


# ----- Adaptable Priority Queue (APQ) Class ----- #


class APQ:
    def __init__(self):
        """ Set heap as an empty list. """
        self._heap = []

    def __str__(self):
        """ Return string of the key, value and index. """
        output = ""
        for i in self._heap:
            element = f"Key: {i._key:3} | Value: {i._value:3} | Index: {i._index:3}"
            output += element
            output += " --> \n"
        return output

    def add(self, key, item):
        """ Add a new item into the priority queue with priority key, and return its Element in the APQ. """
        if len(self._heap) == 0:
            i = 0
        else:
            i = len(self._heap)
        element = Element(key, item, i)
        self._heap.append(element)
        if len(self._heap) > 1:
            self.bubble_up_sort(element)
        return element

    def min(self):
        """ Return the item with the minimum value. """
        return self._heap[0]._value

    def remove_min(self):
        """ Remove and return the value with the minimum key. """
        element = self._heap[0]
        if len(self._heap) == 1:
            self._heap.pop(0)
        else:
            self._heap[0] = self._heap[-1]
            self._heap[0]._index = 0
            self._heap.pop(-1)
            self.bubble_down_sort(self._heap[0])
        return element

    def is_empty(self):
        """ Return True if no items in the priority queue. """
        return self._heap == []

    def length(self):
        """ Return the number of items in the priority queue. """
        return len(self._heap)

    def update_key(self, element, new_key):
        """ Update key of the current element to a new key, and balance the APQ. """
        element._key = new_key
        self.balance(element)

    def get_key(self, element):
        """ Return key for the current element. """
        return self._heap[element._index]._key

    def remove(self, element):
        """ Remove the current element from the APQ, and balance APQ. """
        j = element._index
        last = len(self._heap) - 1
        (self._heap[-1], self._heap[j]) = (self._heap[j], self._heap[-1])
        self._heap[j]._index = j
        self._heap.pop(-1)
        self.balance(self._heap[-1])

    def swap(self, element, other):
        """ Swap the indexes of two elements. """
        i = element._index
        other_i = other._index
        self._heap[i] = other
        self._heap[other_i] = element
        element._index = other_i
        other._index = i

    def balance(self, elt):
        """ Balance the heap. """
        j = elt._index
        parent = (j - 1) // 2
        left = 2 * j + 1
        if j <= len(self._heap) - 1:
            if parent >= 0:
                if self._heap[j]._key < self._heap[parent]._key:
                    self.bubble_up_sort(self._heap[j])
            elif left < len(self._heap):
                self.bubble_down_sort(self._heap[j])
        else:
            return self._heap

    def bubble_down_sort(self, element):
        """ Bubble an element down through the heap. """
        i = element._index
        left = 2 * i + 1
        right = 2 * i + 2
        if right < self.length():
            if self._heap[left] and self._heap[right]:
                if self._heap[left] < self._heap[right]:
                    if element > self._heap[left]:
                        self.swap(element, self._heap[left])
                        self.bubble_down_sort(self._heap[left])
                elif self._heap[right] < self._heap[left]:
                    if element > self._heap[right]:
                        self.swap(element, self._heap[right])
                        self.bubble_down_sort(self._heap[right])
        elif left < self.length():
            if element > self._heap[left]:
                self.swap(element, self._heap[left])
                self.bubble_down_sort(self._heap[left])
        return self._heap

    def bubble_up_sort(self, element):
        """ Bubble an element up through the heap. """
        parent_i = (element._index - 1) // 2
        if parent_i >= 0 and parent_i < len(self._heap) - 1:
            p = self._heap[parent_i]
            if element._key < p._key:
                self.swap(element, p)
                self.bubble_up_sort(element)
        return self._heap

    # ----- End of APQ class ----- #


# ----- Vertex Class ----- #


class Vertex:
    """ A Vertex in a graph. """

    def __init__(self, element):
        """ Create a vertex, with a data element.

        Args:
            element - the data or label to be associated with the vertex
        """
        self._element = element

    def __str__(self):
        """ Return a string representation of the vertex. """
        return str(self._element)

    def __lt__(self, v):
        """ Return true if this element is less than v's element.

        Args:
            v - a vertex object
        """
        return self._element < v.element()

    def element(self):
        """ Return the data for the vertex. """
        return self._element

    # ----- End of Vertex class ----- #


# ----- Edge Class ----- #


class Edge:
    """ An edge in a graph.

        Implemented with an order, so can be used for directed or undirected
        graphs. Methods are provided for both. It is the job of the Graph class
        to handle them as directed or undirected.
    """

    def __init__(self, v, w, element):
        """ Create an edge between vertices v and w, with label element.

            element can be an arbitrarily complex structure.
        """
        self._vertices = (v, w)
        self._element = element

    def __str__(self):
        """ Return a string representation of this edge. """
        return f"({str(self._vertices[0])}-->{str(self._vertices[1])}:{str(self._element)})"

    def vertices(self):
        """ Return an ordered pair of the vertices of this edge. """
        return self._vertices

    def start(self):
        """ Return the first vertex in the ordered pair. """
        return self._vertices[0]

    def end(self):
        """ Return the second vertex in the ordered. pair. """
        return self._vertices[1]

    def opposite(self, v):
        """ Return the opposite vertex to v in this edge. """
        if self._vertices[0] == v:
            return self._vertices[1]
        elif self._vertices[1] == v:
            return self._vertices[0]
        else:
            return None

    def element(self):
        """ Return the data element for this edge. """
        return self._element

    # ----- End of Edge class ----- #


# ----- RouteMap Class ----- #


class Graph:
    """ Represent a simple graph.

        This version maintains only undirected graphs, and assumes no
        self loops.
    """

    # Implement as a Python dictionary
    #  - the keys are the vertices
    #  - the values are the edges for the corresponding vertex
    #    Each edge set is also maintained as a dictionary,
    #    with opposite vertex as the key and the edge object as the value

    def __init__(self):
        """ Create an initial empty graph. """
        self._structure = dict()

    def __str__(self):
        """ Return a string representation of the graph. """
        hstr = f"|V| = {str(self.num_vertices())} & |E| = {str(self.num_edges())}"
        vstr = "\nVertices: "
        for v in self._structure:
            vstr += f"{str(v)}-->"
        edges = self.edges()
        estr = '\nEdges: '
        for e in edges:
            estr += f"{str(e)} "
        return hstr + vstr + estr

    # -------------------------------------------------- #
    # ADT methods to query the graph

    def num_vertices(self):
        """ Return the number of vertices in the graph. """
        return len(self._structure)

    def num_edges(self):
        """ Return the number of edges in the graph. """
        num = 0
        for v in self._structure:
            num += len(self._structure[v])  # the dict of edges for v
        return num // 2  # divide by 2, since each edege appears in the
        # vertex list for both of its vertices

    def vertices(self):
        """ Return a list of all vertices in the graph. """
        return [key for key in self._structure]

    def get_vertex_by_label(self, element):
        """ get the first vertex that matches element. """
        for v in self._structure:
            if v.element() == element:
                return v
        return None

    def edges(self):
        """ Return a list of all edges in the graph. """
        edgelist = []
        for v in self._structure:
            for w in self._structure[v]:
                # to avoid duplicates, only return if v is the first vertex
                if self._structure[v][w].start() == v:
                    edgelist.append(self._structure[v][w])
        return edgelist

    def get_edges(self, v):
        """ Return a list of all edges incident on v. """
        if v in self._structure:
            edgelist = []
            for w in self._structure[v]:
                edgelist.append(self._structure[v][w])
            return edgelist
        return None

    def get_edge(self, v, w):
        """ Return the edge between v and w, or None. """
        if (self._structure is not None
                and v in self._structure
                and w in self._structure[v]):
            return self._structure[v][w]
        return None

    def degree(self, v):
        """ Return the degree of vertex v. """
        return len(self._structure[v])

    # -------------------------------------------------- #
    # ADT methods to modify the graph

    def add_vertex(self, element):
        """ Add a new vertex with data element.

            If there is already a vertex with the same data element,
            this will create another vertex instance.
        """
        v = Vertex(element)
        self._structure[v] = dict()
        return v

    def add_vertex_if_new(self, element):
        """ Add and return a vertex with element, if not already in graph.

            Checks for equality between the elements. If there is special
            meaning to parts of the element (e.g. element is a tuple, with an
            'id' in cell 0), then this method may create multiple vertices with
            the same 'id' if any other parts of element are different.

            To ensure vertices are unique for individual parts of element,
            separate methods need to be written.
        """
        for v in self._structure:
            if v.element() == element:
                # print('Already there')
                return v
        return self.add_vertex(element)

    def add_edge(self, v, w, element):
        """ Add and return an edge between two vertices v and w, with  element.

            If either v or w are not vertices in the graph, does not add, and
            returns None.

            If an edge already exists between v and w, this will
            replace the previous edge.
        """
        if not v in self._structure or not w in self._structure:
            return None
        e = Edge(v, w, element)
        self._structure[v][w] = e
        self._structure[w][v] = e
        return e

    def add_edge_pairs(self, elist):
        """ add all vertex pairs in elist as edges with empty elements. """
        for (v, w) in elist:
            self.add_edge(v, w, None)

    # -------------------------------------------------- #
    # Additional methods to explore the graph

    def highestdegreevertex(self):
        """ Return the vertex with highest degree. """
        hd = -1
        hdv = None
        for v in self._structure:
            if self.degree(v) > hd:
                hd = self.degree(v)
                hdv = v
        return hdv

    # -------------------------------------------------- #
    # Depth First Search Algorithm

    def depthfirstsearch(self, v):
        """ Return a DFS tree from v. """
        marked = {v: None}
        self._depthfirstsearch(v, marked)
        return marked

    def _depthfirstsearch(self, v, marked):
        """ Do a recursive DFS from v, storing nodes in marked. """
        for e in self.get_edges(v):
            w = e.opposite(v)
            if w not in marked:
                marked[w] = e
                self._depthfirstsearch(w, marked)

    # -------------------------------------------------- #
    # Breadth First Search Algorithm

    def breadthfirstsearch(self, v):
        """ Return a BFS tree from v. """
        levelnum = 1
        marked = {v: (None, 0)}
        level = [v]
        while len(level) > 0:
            nextlevel = []
            for w in level:
                for e in self.get_edges(w):
                    x = e.opposite(w)
                    if x not in marked:
                        marked[x] = (w, levelnum)
                        nextlevel.append(x)
            level = nextlevel
            levelnum += 1
        return marked

    # ----- Dijkstra's Algorithm ----- #

    def dijkstra(self, s):
        """ Dijkstra's algorithm for finding the shortest path. """
        open = APQ()
        locs = {}
        closed = {}
        preds = {s: None}
        element = open.add(0, s)
        locs[s] = element
        while not open.is_empty():
            apq_elementt = open.remove_min()
            vertex = apq_elementt._value
            cost = apq_elementt._key
            locs.pop(vertex)
            predecessor = preds.pop(vertex)
            closed[vertex] = (cost, predecessor)
            for edge in self.get_edges(vertex):
                w = edge.opposite(vertex)
                if w not in closed:
                    new_cost = cost + edge._element
                    if w not in locs:
                        preds[w] = vertex
                        elt = open.add(new_cost, w)
                        locs[w] = elt
                    elif new_cost < open.get_key(locs[w]):
                        preds[w] = vertex
                        open.update_key(locs[w], new_cost)
        return closed

    # ----- End of RouteMap class ----- #


# ----- Graph Reader ----- #


def graphreader(filename):
    """ Read and return the route map in filename. """
    graph = Graph()
    file = open(filename, 'r')
    entry = file.readline()  # either 'Node' or 'Edge'
    num = 0
    while entry == 'Node\n':
        num += 1
        nodeid = int(file.readline().split()[1])
        vertex = graph.add_vertex(nodeid)
        entry = file.readline()  # either 'Node' or 'Edge'
    print("")
    print('Read in', num, 'vertices and added into the graph')
    num = 0
    while entry == 'Edge\n':
        num += 1
        source = int(file.readline().split()[1])
        sv = graph.get_vertex_by_label(source)
        target = int(file.readline().split()[1])
        tv = graph.get_vertex_by_label(target)
        length = float(file.readline().split()[1])
        edge = graph.add_edge(sv, tv, length)
        file.readline()  # read the one-way data
        entry = file.readline()  # either 'Node' or 'Edge'
    print('Read in', num, 'edges and added into the graph')
    print("")
    return graph


# ----- Testing ----- #


def test():
    print("*** Running test on Simple Graph 1 ***")
    graph1 = graphreader('simplegraph1.txt')
    print(graph1)

    print("\n==========================================================================================\n")

    print("*** Running test on Simple Graph 2 ***")
    graph2 = graphreader('simplegraph2.txt')
    print(graph2)


test()
