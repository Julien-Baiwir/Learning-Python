sales = open('sales.txt', 'r')
for line in sales:
    index    = line.index(',')
    product  = line[:index]
    quantity = int(line[index+1:])
    print( product.rjust(20) + ': ' + '#' * quantity)
    

    
