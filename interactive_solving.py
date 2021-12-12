from Taquin import Taquin
import sys
from _Getch import _Getch

def main():
    getch = _Getch()
    t=Taquin([[1,2,3], [4,5,6] ,[7," ",8]])

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

if __name__ == "__main__":
    main()
