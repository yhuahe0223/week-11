#nexted loop ~ a loop within another loop (outer,inner)
#               outer loop:
#                   inner loop:
#nexted loops are useful because 


rows = int(input("Enter the # of rows: "))
colums  = int(input("Enter # of colums: "))
symbol = input('Enter a symbol to use: ')


for x in range(rows):
    for y in range(colums):
        print(symbol, end="")
    print()