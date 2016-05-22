
def main(request):
    jsonStr = ""
    getCentrality(jsonStr)


def getCentrality(jsonStr):

    g = _createGraphElements(json.loads(jsonStr))
    dc = OrderedDict({"ids": g.vs["ids"], "label": g.vs["label"]})
    digits = 2
    numOfNodes = g.vcount()
    dc["inDegree"] = _roundNumbers(_normaliseDegree(g.degree(mode="in"), numOfNodes), digits)
    dc["outDegree"] = _roundNumbers(_normaliseDegree(g.degree(mode="out"), numOfNodes), digits)
    dc["totalDegree"] = _roundNumbers(_normaliseDegree(g.degree(), numOfNodes), digits)
    dc["betweenness"] = _roundNumbers(g.betweenness(directed=True), digits)
    dc["inCloseness"] = _roundNumbers(g.closeness(mode="in"), digits)
    dc["outCloseness"] = _roundNumbers(g.closeness(mode="out"), digits)
    dc["totalCloseness"] = _roundNumbers(g.closeness(), digits)
    dc["eigenvector"] = _roundNumbers(g.eigenvector_centrality(directed=True, scale=True), digits)
    dc["density"] = _roundNumber(g.density(loops=True), digits)

    return json.dumps(dc)


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
