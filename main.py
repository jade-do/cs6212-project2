# Project 2: Hoffman coding
# Jade Do | GWID: G29249309
import sys
import heapq
import time
import random

class node:
    def __init__(self, freq, symbol, left = None, right = None):
        self.freq = freq            # frequency
        self.symbol = symbol  # character
        self.left = left            # left node
        self.right = right          # right node
        self.hoff = ''              # # tree direction (0/1)

    def __lt__(self, nxt):
        return self.freq < nxt.freq


# utility function to print hoffman codes for all symbols in the newly created Hoffman tree
def printNodes(node, val=''):
    newVal = val + str(node.hoff)           # hoffman code for current node

    # if node is not an edge node then traverse inside it
    if (node.left):
        printNodes(node.left, newVal)
    if (node.right):
        printNodes(node.right, newVal)

    # if node is edge node then display its hoffman code
    if (not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # List of all possible unicode characters
    chars = [chr(i) for i in range(sys.maxunicode)]
    # List of random frequencies for all possible unicode characters
    freq = random.sample(range(sys.maxunicode+1), k = sys.maxunicode)

    # Hard coded small list of characters for testing
    # chars = ['a', 'b', 'c', 'd', 'e', 'f']  # characters for Hoffman tree
    # freq = [5, 9, 12, 13, 16, 45]           # frequency of characters

    for i in range(1, 10001, 50):
        subChars = chars[0:i]
        subFreq = freq[0:i]

        nodes = []   # list of unused nodes

        # converting characters and frequencies into hoffman tree nodes
        for x in range(len(subChars)):
            heapq.heappush(nodes, node(subFreq[x], subChars[x]))

        start_time = time.time()
        while len(nodes) > 1:
            # sort all the nodes in ascending order based on their frequency
            left = heapq.heappop(nodes)
            right = heapq.heappop(nodes)

            # assign directional value to these nodes
            left.hoff = 0
            right.hoff = 1

            # combine the 2 smallest nodes to create new node as their parent
            newNode = node(left.freq + right.freq, left.symbol+right.symbol, left, right)
            #print(f"{newNode.freq}, {newNode.symbol}, {newNode.left.symbol}, {newNode.right.symbol}")

            heapq.heappush(nodes, newNode)
        end_time = time.time()
        print(f"input size: n = {len(subChars)} takes {end_time - start_time} seconds")
        # print((end_time - start_time) * 1000)
        # printNodes(nodes[0])

    # Print Final Hoffman Tree
    printNodes(nodes[0])
