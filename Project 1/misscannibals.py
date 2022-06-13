from search import *

class MissCannibals(Problem):
    def __init__(self, M=3, C=3, goal=(0, 0, False)):
        initial = (M, C, True) # state is represented as (m, c, onLeft)
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
        onLeft = state[2]

        for action in possible_actions[:]:
            # going from L to R delete the count and check if missionaries are greater than cannibals
            # going from R to L add to the count and check if missionaries are greater than cannibals
            if action.count('M') > mCount or action.count('C') > cCount: 
                possible_actions.remove(action)
                continue
            
            if onLeft == False:
                leftMCount = self.M - mCount + action.count('M')
                leftCCount = self.C - cCount + action.count('C')
                rightMCount = mCount - action.count('M')
                rightCCount = cCount - action.count('C')
            else:
                leftMCount = mCount - action.count('M')
                leftCCount = cCount - action.count('C')
                rightMCount = self.M - mCount + action.count('M')
                rightCCount =self.M - mCount + action.count('C')

            if leftMCount > self.M or rightMCount > self.M or leftCCount > self.C or rightCCount > self.C:
                possible_actions.remove(action)
                continue
            if leftMCount < leftCCount and leftMCount != 0 or rightMCount < rightCCount and rightMCount != 0:
                possible_actions.remove(action)
                continue

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        new_state = list(state)
        mCount = state[0]
        cCount = state[1]

        if new_state[2] == True:
            new_state[0] = new_state[0] - action.count('M')
            new_state[1] = new_state[1] - action.count('C')
            new_state[2] = not new_state[2]
        else:
            new_state[0] = new_state[0] + action.count('M')
            new_state[1] = new_state[1] + action.count('C')
            new_state[2] = not new_state[2]

        return tuple(new_state)


    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal

    def check_solvability(self, state):
        """ Checks if the given state is solvable """
        return True


if __name__ == '__main__':
    mc = MissCannibals(3,3)
    # print(mc.actions((3, 2, True))) # Test your code as you develop! This should return  ['CC', 'C', 'M']
    print(mc.actions((3,2,True)))
    print(mc.actions((1,1,False)))

    print(mc.result((1,1,False), 'MC'))
    print(mc.result((1,1,False), 'MM'))

    # path = depth_first_graph_search(mc).solution()
    # print(path)
    # path = breadth_first_graph_search(mc).solution()
    # print(path)

    # print(mc.result((3,3, True), 'MM'))



