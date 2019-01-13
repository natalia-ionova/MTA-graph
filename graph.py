class Vertex:
    def __init__(self, key):
        self.id = key
        self.adjacent_to = []


class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the transfers.txt file and creates a graph using an adjacency list representation.
           Graph is not directed so each edge specified
           in the input file appears on the adjacency list of each vertex of the two vertices associated
           with the edge.'''

        self.vertices = {}
        input = open(filename, 'r')
        lines = input.readlines()
        lines = lines[1:]

        lines = [x.strip() for x in lines]

        list_transfers_all = []
        for x in lines:
            x = x.split()
            list_transfers_all.append(x)


        list_transfers_stops = []
        for x in list_transfers_all:
            str = x[0]
            a = str[0:3]
            b = str[4:7]
            list_transfers_stops.append(a)
            list_transfers_stops.append(b)


        pair_transfers = [(list_transfers_stops[i], list_transfers_stops[i+1]) for i in range(0, len(list_transfers_stops), 2)]



        for x in pair_transfers:
            for y in x:
                y = Vertex(y)
                self.vertices[y.id] = y
        for x in pair_transfers:
            self.add_edge(x[0], x[1])

        input.close()

    def add_edge(self, v1, v2):
        '''v1 and v2 are transfer id's. This is an undirected graph, adds an
           edge from v1 to v2 and an edge from v2 to v1.'''
        if v1 not in self.vertices[v2].adjacent_to:
            self.vertices[v2].adjacent_to.append(v1)
        if v2 not in self.vertices[v1].adjacent_to:
            self.vertices[v1].adjacent_to.append(v2)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None
