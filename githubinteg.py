
def main(request):
    jsonStr = getTestData()
    getCentrality(jsonStr)

def getTestData():
	ret = {
	    "nodes":[
	        {"node":0,"name":"node0"},
	        {"node":1,"name":"node1"},
	        {"node":2,"name":"node2"},
	        {"node":3,"name":"node3"},
	        {"node":4,"name":"node4"},
	        {"node":5,"name":"node5"},
	        {"node":6,"name":"node6"},
	        {"node":7,"name":"node7"},
	        {"node":8,"name":"node8"},
	        {"node":9,"name":"node9"},
	        {"node":10,"name":"node10"},
	        {"node":11,"name":"node11"},
	        {"node":12,"name":"node12"}
	    ],
	    "links":[
	        {"source":0,"target":1,"value":4},
	        {"source":1,"target":2,"value":5},
	        {"source":2,"target":3,"value":10},
	        {"source":3,"target":4,"value":12},
	        {"source":4,"target":5,"value":14},
	        {"source":5,"target":6,"value":18},
	        {"source":6,"target":7,"value":20},
	        {"source":7,"target":8,"value":53},
	        {"source":8,"target":9,"value":45},
	        {"source":9,"target":10,"value":44},
	        {"source":10,"target":11,"value":60},
	        {"source":11,"target":12,"value":88}
	    ]
	}
	return ret

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
