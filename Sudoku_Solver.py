# Introduction
#   Sudoku puzzle solver code by Chandra Tupelly
#   Date: 10/29/2014
#   Lot of references from internet to know the rules and laying down the principles in Python
#   couple of references I found useful
#   Sudoku rules book: http://www.sudoku.ws/rules.htm
#   Sudoku implementing in python!!
#       https://jakevdp.github.io/blog/2013/04/15/code-golf-in-python-sudoku/
#   future work: 
#       1)refining the code making it more elegant for solving pairs level complicated

# Ok, The Actual code rather fun part starts here. :)

# defining the functions for rules
import string
import csv
import time

# the below section is to read the csv file into a matrix format
# assumption of the file structure is a CSV file
count=0
sudoku_fname='input_1.csv'
a=[]
index=[0,1,2,3,4,5,6,7,8]
sudoku_set=['1','2','3','4','5','6','7','8','9']
block_index=[0,1,2]

#actual reading of the file in csv format and breaking down into nested list form
with open(sudoku_fname,'rb') as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        a.append(row)
    print a

# identifying the peers to down select the options to fill the empty cell

# row peers
def row_peers(row1,col1):
    row_set=solve_a[row1]
    for m in sudoku_set:
        if m not in row_set:
            opt_sol_val.append(m)
    if (len(opt_sol_val))==1:
        solve_a[row1][col1]=opt_sol_val[0]

# column peers       
def col_peers(row1,col1):
    if len(opt_sol_val) > 1:
        col_set=t_solve_a[col1]
        # one of the trickier solution when using counter within modified list(mutable sequence)
        for m in opt_sol_val[:]:
            if m in col_set:
                opt_sol_val.remove(m)
    if (len(opt_sol_val))==1:
        solve_a[row1][col1]=opt_sol_val[0]

# block peers
def block_peers(row1,col1):
    if len(opt_sol_val) > 1:
        block_set=[]
        opt_sol_val_temp=opt_sol_val
        for i in block_index:
            for j in block_index:
                row2=3*(row1//3)+i
                col2=3*(col1//3)+j
                block_set.append(solve_a[row2][col2])
        # one of the trickier solution when using counter within modified list(mutable sequence)
        for m in opt_sol_val[:]:
            if m in block_set:
                opt_sol_val.remove(m)
#        print opt_sol_val
    if (len(opt_sol_val))==1:
        solve_a[row1][col1]=opt_sol_val[0]

# checking for the row level pairs and unique set comparing other rows
# def find_pairs(row1,col1):
    # if len(opt_sol_val) > 1:
  
# keep tracking of zeros
def findZ():
    z=[]
    for i in index:
        for j in index:
            if solve_a[i][j] == '0':
                z.append([i,j])
    return (z)

# main section looping through     
# creating a copy to solve
solve_a=a
# transpose to call the columns easily
t_solve_a=zip(*a)
opt_solve_a=[]
count=0

# determining the possibilities for each location of zeros and searching
# finish line
def search(solve_a):
    z=findZ()

for x in xrange(100):
    zeros=findZ()
    opt_sol_c_val=[]
    if len(zeros)==0:
        print "all done"
        print solve_a
        break
    else:
        for coord in zeros:
            count=count+1
            opt_sol_val=[]
            row_peers(coord[0],coord[1])
            col_peers(coord[0],coord[1])
            block_peers(coord[0],coord[1])
            opt_sol_c_val.append([coord,opt_sol_val,len(opt_sol_val)])
    if x == 99:
        print "more iterations and need native pairs sol."
        print solve_a
        print opt_sol_c_val

# writing the solution in csv file        
with open("sudoku_output.csv","wb") as csv_file:
    csv_writer=csv.writer(csv_file, delimiter=',')
    for row in solve_a:
        csv_writer.writerow(row)
          
