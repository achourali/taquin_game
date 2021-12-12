import numpy as np


class A_star_node:

    def __init__(self, taquin):
        self.taquin = taquin
        self.parent = None
        self.g_cost = 0

    def set_parent(self, parent):
        self.parent = parent

    def set_g_cost(self, g_cost):
        self.g_cost = g_cost

    def calculate_h1(self):
        result = 0
        goal_state = self.taquin.get_goal_state()
        for r in range(self.taquin.nb_rows):

            for c in range(self.taquin.nb_columns):

                if self.taquin.state[r, c] != goal_state[r, c]:
                    result += 1
        return result

    def calculate_h2(self):
        result = 0
        goal_state = self.taquin.get_goal_state()
        for r in range(self.taquin.nb_rows):

            for c in range(self.taquin.nb_columns):
                element = self.taquin.state[r, c]
                (goal_position_r, goal_position_c) = np.where(goal_state == element)[
                    0][0], np.where(goal_state == element)[1][0]
                distance = np.linalg.norm(
                    [goal_position_r-r, goal_position_c-c])
                result += distance
        return result

    def calculate_f(self):
        return round(self.calculate_h2()+self.g_cost,3)

    def generate_id(self):
        if self.parent:
            return self.taquin.generate_id()+self.parent.taquin.generate_id()
        else:
            return self.taquin.generate_id()
    def generate_html_table(self):
      
        html='<<TABLE BORDER="0" CELLBORDER="3" CELLSPACING="0">'
        html+='<TR><TD colspan="'+str(self.taquin.nb_columns)+'">f='+str(self.calculate_f())+'</TD></TR>'
        for r in range(self.taquin.nb_rows):
            html+='<TR>'
            for c in range(self.taquin.nb_columns):
                html+='<TD BORDER="1">'+self.taquin.state[r][c]+'</TD>'
            html+='</TR>'
        html+='</TABLE>>'
        return html





