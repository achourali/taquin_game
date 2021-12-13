from Taquin import Taquin
import sys
from _Getch import _Getch

def interactive_solving(initial_state):
    getch = _Getch()
    t=Taquin(initial_state)

    while(True):
        
        t.display_state()
        if(t.check_done()):
                print("DONE :) ")
                exit()
        k=getch()

        if k=='5':
                t.move ("up")
        elif k=='2':
                t.move("down")
        elif k=='3':
                t.move("right")
        elif k=='1':
                t.move("left")

        if(ord(k)==3):
            exit()
