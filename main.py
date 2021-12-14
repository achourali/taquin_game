from dfs import dfs
from a_star import a_star
from bfs import bfs
from interactive_solving import interactive_solving


def main():
    initial_states=[
        [[1,2, " "], [4, 5,3], [7,8,6]],
        [[1," ", 3], [4, 2,6], [7,5,8]],
        [[1,3,5],[4,2,6],[7,8," "]],
        [[1,2,7,3], [5,6,11,4], [ 9," ",10,8]],
        [[" ",2,7,3], [1,11,4,8], [ 5,9,6,10]],
        [[1,2,7,3], [" ",11,4,8], [ 5,9,6,10]]

    ]


    a_star(initial_states[5])

if __name__=="__main__":
    main()
