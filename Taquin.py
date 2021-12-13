import numpy as np

class Taquin:



    def __init__(self, initial_state):
        self.state = np.array(initial_state)
        self.nb_rows , self.nb_columns =self.state.shape 


    def get_state(self):
        return self.state.tolist()


    def display_state(self):
        print("---------------------------")
        s = [[str(e) for e in row] for row in self.state]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print ('\n'.join(table))
        print("---------------------------")



    def move(self,direction):

        voidLocation=np.where(self.state==" ")
        voidRow=voidLocation[0][0]
        voidColumn=voidLocation[1][0]


        if(direction=="down"):
            if(voidRow>0):
                print("down")
                self.state[voidRow][voidColumn],self.state[voidRow-1][voidColumn]=self.state[voidRow-1][voidColumn],self.state[voidRow][voidColumn]
        elif(direction=="up"):
            if(voidRow<self.nb_rows-1):
                print("up")
                self.state[voidRow][voidColumn],self.state[voidRow+1][voidColumn]=self.state[voidRow+1][voidColumn],self.state[voidRow][voidColumn]
        elif(direction=="left"):
            if(voidColumn<self.nb_columns-1):
                print("left")
                self.state[voidRow][voidColumn],self.state[voidRow][voidColumn+1]=self.state[voidRow][voidColumn+1],self.state[voidRow][voidColumn]
        elif(direction=="right"):
            if(voidColumn>0):
                print("right")
                self.state[voidRow][voidColumn],self.state[voidRow][voidColumn-1]=self.state[voidRow][voidColumn-1],self.state[voidRow][voidColumn]
        
        else:
            print("wrong direction")



    def check_done(self):
        return self.get_state()==self.get_goal_state().tolist()

        
    def get_goal_state(self):
        goal=np.ndarray(shape=(self.nb_rows,self.nb_columns),dtype='<U21')
        order=1;
        for r in range(self.nb_rows):
            
            for c in range(self.nb_columns):
                onLastElement= r==self.nb_rows-1 and c==self.nb_columns-1
                if( onLastElement ):
                    goal[r,c]=" "
                else:
                    goal[r,c]=order
                order+=1

        return goal
    
    def generate_id(self):
        id=''
        for r in range(self.nb_rows):
            
            for c in range(self.nb_columns):
                
                id+=self.state[r][c]+'|'
        
        return id


