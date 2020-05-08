class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    tdict = {}
    route = [None] * length

    for i in tickets:
        tdict[i.source] = i.destination

    cdest = tdict["NONE"]

    j = 0
    while cdest != "NONE":
        route[j] = cdest
        cdest = tdict[cdest]
        j += 1
    route[j] = "NONE"
    
    return route