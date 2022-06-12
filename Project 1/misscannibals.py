from search import *

class MissCannibals(Problem):
    def __init__(self, M=3, C=3, goal=(0, 0, False)):
        initial = (M, C, True)
        self.M = M
        self.C = C
        super().__init__(initial, goal)

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only five possible actions ('MM', 'MC', 'CC', 'M', 'C')
        in any given state of the environment """

        possible_actions = ['MM', 'MC', 'CC', 'M', 'C']
        mCount = state[0]
        cCount = state[1]

        for action in possible_actions[:]:
            if action.count('M') > mCount or action.count('C') > cCount: 
                possible_actions.remove(action)

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        new_state = list(state)
        mCount = state[0]
        cCount = state[1]
        new_state[0] = new_state[0] - action.count('M')
        new_state[1] = new_state[1] - action.count('C')
        new_state[2] = not new_state[2]

        return tuple(new_state)


    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal



if __name__ == '__main__':
    mc = MissCannibals(3,3)
    #print(mc.actions((3, 2, True))) # Test your code as you develop! This should return  ['CC', 'C', 'M']
	
    # path = depth_first_graph_search(mc).solution()
    # print(path)
    # path = breadth_first_graph_search(mc).solution()
    # print(path)

    print(mc.result((3,3, True), 'MM'))



