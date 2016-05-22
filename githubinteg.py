
def main(request):
    _roundNumber(4.12345, 2)


def getNeighbours(jsonStr):
    data = json.loads(jsonStr)
    nodes = data["nodes"]
    edges = data["edges"]
    allNeighbours = {"nodes": []}
    
    for node in nodes:
        neighbours = {"id": node["id"], "neighbours": []}
        for edge in edges:
            #insert directly connected node's ID
            if edge["from"] == node["id"]:
                neighbours["neighbours"].append(edge["to"])
            elif edge["to"] == node["id"]:
                neighbours["neighbours"].append(edge["from"])
        # remove duplicated id from the array before adding it to allNeighbours object
        neighbours["neighbours"] = list(set(neighbours["neighbours"]))
        allNeighbours["nodes"].append(neighbours)

    allNeighbours = json.dumps(allNeighbours)
    return allNeighbours


def _createGraphElements(jdata):
    ids = []
    labels = []
    for node in jdata["nodes"]:
        ids.append(node["id"])
        labels.append(node["label"])

    connections = []
    for edge in jdata["edges"]:
        #create a tuple and set it in the array
        for val in range(0, int(edge["value"])):
            # create the same edges 'edge["value"]' times
            # edge index starts at 0, so -1 needed
            connections.append( (int(edge["from"]) - 1, int(edge["to"]) - 1) )

    g = igraph.Graph(directed=True)
    g.add_vertices(len(ids))
    g.vs["ids"] = ids
    g.vs["label"] = labels
    g.add_edges(connections)
    return g


def _normaliseDegree(targetArray, numOfNodes):
    if numOfNodes == 0:
        return 0

    index = 0
    #To normalize the degree, degree is divided by n-1, where n is the number of vertices in the graph.
    for num in targetArray:
        targetArray[index] = float(num) / (numOfNodes - 1)
        index = index + 1

    return targetArray

def _roundNumbers(targetArray, digits):
    index = 0
    for num in targetArray:
        targetArray[index] = _roundNumber(num, digits)
        index = index + 1

    return targetArray

def _roundNumber(target, digits):
    return round(target, digits)

