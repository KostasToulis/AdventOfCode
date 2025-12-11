import numpy as np

class Junction:
    def __init__(self, i, x, y, z):
        self.id = i
        self.x = x
        self.y = y
        self.z = z
        self.connections = set()
        self.circuit = None

    def add_connection(self, other):
        self.connections.add(other)

class Circuit:
    def __init__(self, junction):
        self.junctions = {junction}

    def add_junction(self, junction):
        self.junctions.add(junction)
        junction.circuit = self

def merge_circuits(circuit_1, circuit_2):
    for junction in circuit_2.junctions:
        circuit_1.add_junction(junction)

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_data = file.readlines()

    input_data = [line.rstrip('\n').split(',') for line in input_data]

    input_data = [[int(item) for item in line] for line in input_data]

    junctions = []

    for  i, line in enumerate(input_data):
        junc_id = i
        x, y, z = map(int, line[0:3])
        junction = Junction(junc_id, x, y, z)
        junctions.append(junction)



    dist_matrix = np.zeros((len(junctions), len(junctions)))
    for i in range(len(junctions)):
        for j in range(len(junctions)):
            if i != j:
                dist = ((junctions[i].x - junctions[j].x) ** 2 +
                        (junctions[i].y - junctions[j].y) ** 2 +
                        (junctions[i].z - junctions[j].z) ** 2) ** 0.5
                dist_matrix[i,j] = dist
            else:
                dist_matrix[i,j] = float('inf')

    connected = 1
    circuits = []
    for j in junctions:
        circuit = Circuit(j)
        j.circuit = circuit
        circuits.append(circuit)

    while len(circuits) > 1:
        min_dist = float('inf')
        min_i, min_j = -1, -1
        same_circuit = False
        for i in range(len(junctions)):
            for j in range(len(junctions)):
                if i != j and dist_matrix[i,j] < min_dist:
                    junction_1 = junctions[i]
                    junction_2 = junctions[j]
                    if junction_1.circuit != junction_2.circuit:
                        min_dist = dist_matrix[i, j]
                        min_i, min_j = i, j

        if min_i != -1 and min_j != -1:

            junction_1 = junctions[min_i]
            junction_2 = junctions[min_j]
            circuits.remove(junction_2.circuit)
            merge_circuits(junction_1.circuit, junction_2.circuit)

            dist_matrix[min_i,min_j] = float('inf')
            dist_matrix[min_j,min_i] = float('inf')
            connected += 1
            last_connected = (junction_1, junction_2)
            print(connected)

    print(last_connected[0].x * last_connected[1].x)