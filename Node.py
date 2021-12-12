
class Node:
    def __init__(self,taquin):
        self.taquin=taquin
        self.parent=None
    
    def set_parent(self, parent):
        self.parent = parent

    def generate_id(self):
        if self.parent:
            return self.taquin.generate_id()+self.parent.taquin.generate_id()
        else:
            return self.taquin.generate_id()

    def generate_html_table(self):
          
        html='<<TABLE BORDER="0" CELLBORDER="3" CELLSPACING="0">'
        for r in range(self.taquin.nb_rows):
            html+='<TR>'
            for c in range(self.taquin.nb_columns):
                html+='<TD BORDER="1">'+self.taquin.state[r][c]+'</TD>'
            html+='</TR>'
        html+='</TABLE>>'
        return html

