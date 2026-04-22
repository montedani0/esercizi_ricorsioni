def count_leaf_nodes(input_list):
    if len(input_list)==0:
        return 0
    else:
        counter = 0
        for elem in input_list:
            #se è una lista rifai la funzione su quella lista
            if type(elem)==list:
                counter += count_leaf_nodes(elem)
            else:
                counter += 1
        return counter

if __name__ == '__main__':
    names =['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
    print(count_leaf_nodes(names)) # ci aspettiamo 10