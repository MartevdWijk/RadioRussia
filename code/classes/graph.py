import csv

from .node import Node


class Graph():
    def __init__(self, nodes_file, neighbours_file, geo_json=None):
        self.nodes = self.load_nodes(nodes_file)
        self.load_neighbours(neighbours_file)

    def load_nodes(self, node_file):
        """
        Load all the nodes into the graph.
        """
        nodes = {}
        with open(node_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                nodes[row['id']] = Node(row['name'], row['id'])

        return nodes

    def load_neighbours(self, neighbour_file):
        """
        Load all the neighbours into the loaded nodes.
        """
        with open(neighbour_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                # List comprehension that does the same as the code below
                # neighbours = [neighbour.strip('[] ') for neighbour in row['neighbours'].split(',') if neighbour.strip('[] ') != ""]

                neighbours = []
                for neighbour in row['neighbours'].split(','):
                    # Only add if the result is not an empty string
                    if neighbour.strip('[] ') != '':
                        neighbours.append(neighbour.strip('[] '))

                node_id = row['state']

                # Add the neighbours to the correct node
                for neighbour in neighbours:
                    neighbour = self.nodes[neighbour]
                    self.nodes[node_id].add_neighbour(neighbour)

    def get_violations(self):
        """
        Returns the ids of all nodes that have a neighbour with the same value.
        """
        violations = []

        for node in self.nodes.values():
            if not node.is_valid():
                violations.append(node)

        return violations

    def is_solution(self):
        """
        Returns True if each node in the graph is assigned a value. False otherwise.
        """
        for node in self.nodes.values():
            if not node.has_value():
                return False

        return True

    def calculate_value(self):
        """
        Returns the sum of the values of all nodes.
        """
        value = 0
        for node in self.nodes.values():
            value += node.get_value().value

        return value

    def get_empty_node(self):
        """
        Returns the first empty node.
        """
        for node in self.nodes.values():
            if not node.has_value():
                return node

        return None
