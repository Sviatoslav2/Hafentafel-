import classes
import string
field = classes.Field()

lst_of_uper = list(string.ascii_uppercase[:11])
#print("Figura ==",field.is_figure(4,4,"Withe"))
def Letters_corector():
    lst_of_lowercase = list(string.ascii_lowercase[:11])
    x = input("Enter the row :", )
    for i in x:
        if i in string.punctuation or i !=" ":
            if i in lst_of_uper:
                return lst_of_uper.index(i)
            elif i in lst_of_lowercase:
                return lst_of_lowercase.index(i)
def corector_of_muving(count):
    if count%2 == 0:
        print("Whites are moving")
    elif count%2 == 1:
        print("Blacks are moving ")
    print("From position...")
    row = Letters_corector()
    col = eval(input("Enter the col :", ))
    print("To position...")
    row2 = Letters_corector()
    col2 = eval(input("Enter the col :", ))
    i = str(field)
    field.make_muve_in_game(row, col, row2, col2, count)

    if i == str(field):
        return corector_of_muving(count)
    else:
        #field.make_muve_in_game(col2, row2, col, row, count)
        return (row, col, row2, col2)
def main():
    #field = classes.Field()
    print (str(field))
    count = 0

    while not(field.is_withe_win()or field.is_blacke_win()):
        #figure row and col
        tupl = corector_of_muving(count)
        row = tupl[1]
        col = tupl[0]
        #move position
        row2 = tupl[3]
        col2 = tupl[2]
        field.make_muve_in_game(col, row, col2, row2, count)
        field.is_dead()
        count += 1
        print(str(field))

    if field.is_withe_win():
        print("Withe_win")
    elif field.is_blacke_win():
        print("Blacke win")

main()
