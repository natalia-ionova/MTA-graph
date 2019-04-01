
class Vertex:
    def __init__(self, key):
        self.id = key
        self.adjacent_to = []


class Graph:

    def __init__(self):
        self.vertices = {}

        input = open('stops.txt', 'r')
        for line in input:
            d = line.split(',')
            stop_id = d[0]
            location_type = d[8]
            if location_type == '1':
                pass
            else:
                vertex = Vertex(stop_id)
                self.vertices[vertex.id] = vertex

        input.close()


        input = open('stop_times.txt', 'r')
        prev_stop_id = None


        for line in input:
            d = line.split(',')
            stop_id = d[3]
            stop_seq = d[4]

            if stop_seq != "1":
                self.add_edge(prev_stop_id, stop_id)

            prev_stop_id = stop_id
        input.close()


        #for key in self.vertices:
        #    print(self.vertices[key].id, self.vertices[key].adjacent_to )


    def add_edge(self, v1, v2):
            '''v1 and v2 are transfer id's. This is an undirected graph, adds an
               edge from v1 to v2 and an edge from v2 to v1.'''
            if v1 != None and v2 != None:
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

    def find_all_paths(self, s, e, path=[]):
        '''Finds all paths given a start and end station'''
        path = path + [s]
        if s == e:
            return [path]

        paths = []
        for vertex in self.vertices[s].adjacent_to:
            if vertex not in path:
                new_paths = self.find_all_paths(vertex, e, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths


