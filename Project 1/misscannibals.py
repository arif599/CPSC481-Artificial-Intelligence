from search import *

class MissCannibals(Problem):
    def __init__(self, M=3, C=3, goal=(0, 0, False)):
        initial = (M, C, True)
        self.M = M
        self.C = C
        super().__init__(initial, goal)

    # YOUR CODE GOES HERE
	
if __name__ == '__main__':
    mc = MissCannibals(3,3)
    #print(mc.actions((3, 2, True))) # Test your code as you develop! This should return  ['CC', 'C', 'M']
	
    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)
