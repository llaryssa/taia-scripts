## TAIA LISTA 2

import random

def addNode():
    global counter; global graph
    counter += 1
    graph.append([])

def weightedChoice(prob):
   total = sum(p for p in prob)
   r = random.uniform(0, total)
   upto = 0
   cnt = 0
   for p in prob:
      if upto + p >= r:
         return cnt
      upto += p
      cnt += 1

def findConnection():
    global counter; global graph
    probs = [len(l) for l in graph]
    node1 = node2 = weightedChoice(probs)
    while node2 == node1:
        node2 = weightedChoice(probs)

    addConnection(counter, node1)
    addConnection(counter, node2)

def addConnection(a, b):
    global graph
    graph[a].append(b)
    graph[b].append(a)

counter = -1
graph = []

addNode()
addNode()
addConnection(0,1);

while counter < 100:
    addNode()
    findConnection()

print counter+1, graph
