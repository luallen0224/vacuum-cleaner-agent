'''
VacWorld.py

This is code to get you started.
You need to write code for 3 functions:

    def getAction(state):
        given the current state, return either:
          'SUCK', 'MOVELEFT' or 'MOVERIGHT'
     - in R with dirt -> SUCK
     - in L with dirt -> SUCK
     - in R no dirt   -> MOVELEFT
     - in L no dirt   -> MOVERIGHT

    def updateState(state, action)
        return the next state given current state and action
            action:SUCK vacRoom:R -> ['R', [.., 0]]
            action:SUCK vacRoom:L -> ['L', [0, ..]]
            action:MOVELEFT  vacRoom:R -> ['L', .. ]
            action:MOVERIGHT vacRoom:L -> ['R', .. ]
            other state action pairs: -> no change to state
            note: in above, ... means no change

    def bool_all_rooms_clean(state):
        #returns True or False  if all room are clean or not

'''

# add your name and ID here    --------------
Name = 'Luigi Allen'
ID = '47853472'


def getAction(state):
    '''state: current state
       return  the action based on state
    '''
    # add code so that the appropriate choice is returned
    vacuum_position, room_states = state

    if vacuum_position == 'R' and room_states[1] == 1:
        return 'SUCK'
    elif vacuum_position == 'R' and room_states[1] == 0:
        return 'MOVELEFT'
    elif vacuum_position == 'L' and room_states[0] == 1:
        return 'SUCK'
    elif vacuum_position == 'L' and room_states[0] == 0:
        return 'MOVERIGHT'
    else:
        print("Failed.")


def updateState(state, action):
    ''' state : current state
        action : current action
        return : next state
    '''
    # code to return next state given current state and action
    next_state = state

    if action == 'SUCK':
        this_room = 0
        if state[0] == 'R':
            this_room = 1
        next_state[1][this_room] = 0
    elif action == 'MOVELEFT':
        next_state[0] = 'L'
    else:
        next_state[0] = 'R'

    return next_state


def bool_all_rooms_clean(state):
    '''returns True or False if all room are clean or not'''

    room_states = state[1]
    return room_states[0] == 0 and room_states[1] == 0


def run_vacuum(start_state):
    state = start_state
    loop_count = 0  # counter to stop program when it goes wrong

    # run the simulation until all rooms clean
    while not bool_all_rooms_clean(state):

        action = getAction(state)
        state = updateState(state, action)

        # show state and stop if too many loops
        print(f"cycle:{loop_count}\taction={action}\t\tstate={state}")
        loop_count += 1

        if loop_count > 20:
            print(
                "Uh oh ! Code stuck in a state ... program terminated")
            return

    print("All rooms clean!")
    return


def main():
    # when you run this code without implementing above functions
    # the program will stop after 20 cycles
    # Part 1: Start in room R
    start_state = ['R', [1, 1]]
    print(f"\nPart1. Start in room R\nStart State: {start_state}")
    run_vacuum(start_state)

    # Part 2: Start in room L
    start_state = ['L', [1, 1]]
    print(f"\nPart2. Start in room L\nStart State: {start_state}")
    run_vacuum(start_state)


if __name__ == '__main__':
    main()
