from search import *

class MissCannibals(Problem):
    def __init__(self, M=3, C=3, goal=(0, 0, False)):
        initial = (M, C, True) # state is represented as (m, c, onLeft)
        self.M = M
        self.C = C
        super().__init__(initial, goal)

    def valid_state(self, count):
        mLeftCount = count[0]
        cLeftCount = count[1]
        mRightCount = count[2]
        cRightCount = count[3]
        onLeft = count[4]

        if (mLeftCount != 0 and cLeftCount > mLeftCount) \
                or (mRightCount != 0 and cRightCount > mRightCount) \
                or mLeftCount < 0 or cLeftCount < 0 or mRightCount < 0 \
                or cRightCount < 0:
            return False
        else:
            return True

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only five possible actions ('MM', 'MC', 'CC', 'M', 'C')
        in any given state of the environment """

        possible_actions = ['MM', 'MC', 'CC', 'M', 'C']
        onLeft = state[2]
        result = []

        if onLeft:
            mLeftCount = state[0]
            cLeftCount = state[1]
            mRightCount = self.M - mLeftCount
            cRightCount = self.C - cLeftCount

            for action in possible_actions:
                actionMCount = action.count('M')
                actionCCount = action.count('C')
                new_counts = (mLeftCount-actionMCount, cLeftCount-actionCCount, mRightCount+actionMCount, cRightCount+actionCCount, not onLeft)
                if self.valid_state(new_counts):
                    result.append(action)
        else:
            mLeftCount = state[0]
            cLeftCount = state[1]
            mRightCount = self.M - mLeftCount
            cRightCount = self.C - cLeftCount

            for action in possible_actions:
                actionMCount = action.count('M')
                actionCCount = action.count('C')
                new_counts = (mLeftCount+actionMCount, cLeftCount+actionCCount, mRightCount-actionMCount, cRightCount-actionCCount, not onLeft)
                if self.valid_state(new_counts):
                    result.append(action)
        return result

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

    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)

    print(mc.result((3,3, True), 'MM'))



