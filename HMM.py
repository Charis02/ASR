


def forward(state_distr,transitions,outputs,desired,memo):
    """
    Forward algorithm for HMMs.

    Given state distribution, transition matrix,
    output matrix and the desired sequence,
    return probability of the desired sequence
    occuring.

    We memoize the results of the forward algorithm
    to use again if we end up in the same state distribution
    """

    if desired == []:   # base case
        return 1

    identifier = tuple(state_distr)+(len(desired),)

    if identifier in memo: # if we have already calculated the probability of this state distribution
        return memo[identifier]
    
    # Initialize result
    result = 0

    for cur_state in range(len(state_distr)):
        # Assume each state to be the initial state,
        # and calculate the probability of the desired sequence
        # starting from this state
        # Sum over all possible initial states

        # Get next state's probability distribution
        next_distr = transitions[cur_state]

        #print("here! current state distribution: ", state_distr,"current state: ", cur_state,"next state distribution: ", next_distr)

        # Get the probability of the desired sequence
        # starting from this state
        piece = state_distr[cur_state]*outputs[cur_state][desired[0]]*forward(next_distr,transitions,outputs,desired[1:],memo)
        result += piece

    memo[identifier] = result
    return result

if __name__ == '__main__':
    state_distr = [1,0,0]
    transitions = [[0.6,0.4,0.0],[0.0,0.3,0.7],[0.0,0.0,1.0]]
    outputs = [
        [0.80,0.15,0.05],
        [0.65,0.10,0.25],
        [0.20,0.30,0.50]
    ]

    mapper = {"red":0,"green":1,"blue":2}
    result_sequence = ["red","red","blue","green","red","blue"]
    desired_sequence = [mapper[x] for x in result_sequence]
    memo = {}

    prob = forward(state_distr,transitions,outputs,desired_sequence,memo)

    print("Probability of the desired sequence occuring:",prob)
