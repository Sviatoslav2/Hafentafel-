################################################
################################################
################################################
import string
class Field:
    def __init__(self):
        self.player1 = Player1()
        self.player2 = Player2()
        self.list_of_figures = self.player1.lst_blake+self.player2.lst_withe
        self.last = None
    def __str__(self):
        str = "   0 1 2 3 4 5 6 7 8 9 10"+"\n"
        lst = [["*" for i in range(11)] for i in range(11)]
        lst[0][0] = "#"
        lst[0][10] = "#"
        lst[10][0] = "#"
        lst[10][10] = "#"
        for i in self.list_of_figures:
            if i.figure_name == "Blake":
                lst[i.get_position()[0]][i.get_position()[1]] = "B"
            elif i.figure_name == "Withe":
                lst[i.get_position()[0]][i.get_position()[1]] = "W"
            elif i.figure_name == "Hnefi":
                lst[i.get_position()[0]][i.get_position()[1]] = "H"
            elif i.figure_name == " ":
                lst[i.get_position()[0]][i.get_position()[1]] = "*"
        for i in range(len(lst)):
            str += string.ascii_uppercase[i] + "  "
            for j in lst[i]:
                str += j + " "
            str += "\n"
        return str
    def make_muve_in_game(self,col,row,col2,row2,count):
        lst = [(col, i) for i in range(11)]+[(j, row) for j in range(11)]
        for i in self.list_of_figures:
            if i.get_position() == (col,row) and i.figure_name != "Hnefi" and (col2,row2) not in[(0,0),(10,0),(10,10),(0,10)] :
                for i in self.list_of_figures:
                    if i.get_position() in lst:
                        if i.get_position()[0] == col:
                            if i.get_position()[1] < row:
                                lst1 = [(col, j) for j in range(11) if i.get_position()[1] > j]
                            elif i.get_position()[1] > row:
                                lst1 = [(col, j) for j in range(11) if i.get_position()[1] < j]
                        elif i.get_position()[1] == row:
                            if i.get_position()[0] < col:
                                lst1 = [(j, row) for j in range(11) if i.get_position()[0] > j]
                            elif i.get_position()[0] > col:
                                lst1 = [(j, row) for j in range(11) if i.get_position()[0] < j]
                            for j in lst1:
                                if j in lst:
                                    lst.remove(j)
                        lst.remove(i.get_position())
                if (col2,row2) in lst:
                    if count%2 == 0:
                        self.player2.make_muve(col,row,col2,row2)
                        self.last = self.player2.last
                    elif count%2 == 1:
                        self.player1.make_muve(col, row, col2, row2)
                        self.last = self.player1.last
            elif i.get_position() == (col,row) and i.figure_name == "Hnefi" :
                for i in self.list_of_figures:
                    if i.get_position() in lst:
                        if i.get_position()[0] == col:
                            if i.get_position()[1] < row:
                                lst1 = [(col, j) for j in range(11) if i.get_position()[1] > j]
                            elif i.get_position()[1] > row:
                                lst1 = [(col, j) for j in range(11) if i.get_position()[1] < j]
                        elif i.get_position()[1] == row:
                            if i.get_position()[0] < col:
                                lst1 = [(j, row) for j in range(11) if i.get_position()[0] > j]
                            elif i.get_position()[0] > col:
                                lst1 = [(j, row) for j in range(11) if i.get_position()[0] < j]
                            for j in lst1:
                                if j in lst:
                                    lst.remove(j)
                        lst.remove(i.get_position())
                if (col2, row2) in lst:
                    if count % 2 == 0:
                        self.player2.make_muve(col, row, col2, row2)
                        self.last = self.player2.last
                    elif count % 2 == 1:
                        self.player1.make_muve(col, row, col2, row2)
                        self.last = self.player1.last
    #############################################
    #############################################
    #############################################
    def is_figure(self,col,row,name):
        for i in self.list_of_figures:
            if i.get_position() == (col, row) and i.figure_name == name:
                return True
        return False
    #############################################
    #############################################
    #############################################
    def is_dead(self):
        for i in self.list_of_figures:
            col = i.get_position()[1]
            row = i.get_position()[0]
            if self.is_figure(row, col-1,"Blake") and self.is_figure(row,col+1,"Blake")and i.figure_name =="Withe":
                self.list_of_figures.remove(i)
            elif self.is_figure(row-1,col,"Blake") and self.is_figure(row+1,col,"Blake") and i.figure_name =="Withe":
                self.list_of_figures.remove(i)
            elif self.is_figure(row,col-1,"Withe") and self.is_figure(row,col+1,"Withe")and i.figure_name =="Blake":
                self.list_of_figures.remove(i)
            elif self.is_figure(row-1,col,"Withe") and self.is_figure(row+1,col,"Withe") and i.figure_name =="Blake":
                self.list_of_figures.remove(i)
            elif self.is_figure(row,col-1,"Blake") and self.is_figure(row,col+1,"Blake")and self.is_figure(row-1,col,"Blake") \
                    and self.is_figure(row+1,col,"Blake") and i.figure_name == "Hnefi":
                self.list_of_figures.remove(i)


    def is_blacke_win(self):
        for i in self.player2.lst_withe:
            if self.is_that_figure_can_be_moved(i):
                return False
            else:
                return True
    def is_withe_win(self):
        return self.player2.is_withe_win()

    def is_that_figure_can_be_moved(self, figure):
        col = figure.cell._col
        row = figure.cell._row
        lst = [(col, i) for i in range(11)] + [(j, row) for j in range(11)]
        for i in self.list_of_figures:
            if i.get_position() in lst:
                if i.get_position()[0] == col:
                    if i.get_position()[1] < row:
                        lst1 = [(col, j) for j in range(11) if i.get_position()[1] > j]
                    elif i.get_position()[1] > row:
                        lst1 = [(col, j) for j in range(11) if i.get_position()[1] < j]
                elif i.get_position()[1] == row:
                    if i.get_position()[0] < col:
                        lst1 = [(j, row) for j in range(11) if i.get_position()[0] > j]
                    elif i.get_position()[0] > col:
                        lst1 = [(j, row) for j in range(11) if i.get_position()[0] < j]
                    for j in lst1:
                        if j in lst:
                            lst.remove(j)
                lst.remove(i.get_position())
        return lst != []

###############################################
###############################################
###############################################
class Figure():
    def __init__(self,figure_name,cell=None):
        self.figure_name = figure_name
        self.cell = cell
    def get_position(self):
        if self.cell == None:return None
        if type(self.cell)==Cell:return self.cell.get_position()
#############################################
#############################################
#############################################
class Cell:
    def __init__(self,col,row,mark=False):
        self._col = col
        self._row = row
        self.mark = mark
    def get_position(self):
        return (self._col,self._row)
    def is_thise_cell_victory(self):
        return self.mark
    def get_col(self):
        return self.get_position()[0]
    def get_row(self):
        return self.get_position()[1]
##########################################
##########################################
##########################################
class Player1:
    def __init__(self):
        self.lst_blake = [Figure("Blake",Cell(0,i))for i in range(3,8)]+[Figure("Blake",Cell(10,i))for i in range(3,8)]+[Figure("Blake",Cell(i,0))for i in range(3,8)]+[Figure("Blake",Cell(i,10))for i in range(3,8)]+[Figure("Blake",Cell(1,5)),Figure("Blake",Cell(5,9)),Figure("Blake",Cell(5,1)),Figure("Blake",Cell(9,5))]
        self.last = None

    def make_muve(self,col,row,col2,row2):
        for i in self.lst_blake:
            if i.get_position() == (col,row):
                i.cell._col = col2
                i.cell._row = row2
                self.last = i
class Player2:
    def __init__(self):
        self.lst_withe = [Figure("Withe",Cell(i,5)) for i in range(3,8) if i!=5] + [Figure("Withe",Cell(5,i))for i in range(3,8) if i!=5]+[Figure("Hnefi",Cell(5,5))]+[Figure("Withe",Cell(6,6)),Figure("Withe",Cell(4,4)),Figure("Withe",Cell(4,6)),Figure("Withe",Cell(6,4))]
        self.last = None
    def make_muve(self,col,row,col2,row2):
        for i in self.lst_withe:
            if i.get_position() == (col, row):
                i.cell._col = col2
                i.cell._row = row2
                self.last = i
    def is_withe_win(self):
        for i in self.lst_withe:
            if i.figure_name == "Hnefi" and i.get_position() == (0,0) and i.get_position() == (10,10) and i.get_position() == (0,10) and i.get_position() == (10,0):return True
            else:return False
