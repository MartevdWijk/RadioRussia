from code.algorithms import randomize
from code.classes import graph, transmitters
from code.visualisation import visualise as vis

if __name__ == '__main__':
    # Create a graph from our data
    test_graph = graph.Graph('data/US/states.csv', 'data/US/neighbours.csv')

    # Create the transmitter cost schemes
    transmitters = transmitters.CostScheme('data/transmitters.csv')

    randomize.random_reassignment(test_graph, transmitters.get_scheme(1))

    violating_nodes = test_graph.get_violations()
    print(len(violating_nodes))

    print(test_graph.get_violations())

    vis.visualise(test_graph, "data/US/gz_2010_us_040_00_500k.json")
