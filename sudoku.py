import sys, traceback
from tkinter import *
class box:

	def __init__(self):
		self.persList = [1,2,3,4,5,6,7,8,9]
		self.fixList = [1,2,3,4,5,6,7,8,9]
		self.value=0
		self.fixed=False


def solve():
	
	for i in range(1,10):
		for j in range(1,10):
			#Entry(master,width=3).grid(row=i, column=j)
			
			if(sudoku[i-1][j-1].value.get()):
				if(int(sudoku[i-1][j-1].value.get()) > 0 and int(sudoku[i-1][j-1].value.get()) < 10):
					sudoku[i-1][j-1].fixed = True
					sudoku[i-1][j-1].value = int(sudoku[i-1][j-1].value.get())
				else:
					sudoku[i-1][j-1].value =0;
	

	for i in range(0,9):
		for j in range(0,9):
			for k in range(1,10):
				if(sudoku[i][j].fixed == True):
					sudoku[i][j].fixList=[sudoku[i][j].value]
				elif(isPresentRow(i,k,j)==True or isPresentCol(j,k,i)==True or isPresentBox(i,j,k)):
					sudoku[i][j].fixList.remove(k)
				
			
			sudoku[i][j].persList= list(sudoku[i][j].fixList);



	i=0
	j=0
	k=0
	while(i<9):
		j=0;
		while(j<9):
			while(sudoku[i][j].fixed == False and len(sudoku[i][j].persList)>0 and ((isPresentRow(i,sudoku[i][j].persList[0],j)==True or isPresentCol(j,sudoku[i][j].persList[0],i)==True or isPresentBox(i,j,sudoku[i][j].persList[0])==True ))):	
				sudoku[i][j].persList.remove(sudoku[i][j].persList[0])
				sudoku[i][j].value = 0

			if(len(sudoku[i][j].persList)>0 ):
				sudoku[i][j].value = sudoku[i][j].persList[0]

			if(sudoku[i][j].value==0):
				sudoku[i][j].persList = list(sudoku[i][j].fixList)	
				flag =0;
				

				if(j>0 and i>0):
					while(flag==0):
						while(len(sudoku[i][j-1].persList)<2 and sudoku[i][j-1].fixed == False):
							sudoku[i][j-1].persList = list(sudoku[i][j-1].fixList)
							sudoku[i][j-1].value= 0
							j=j-1
							if(j==0):
								if(i!=0):
									i=i-1
									j=9	
								else:
									sys.exit(0)

						if(j==0):
							if(i!=0):
								i=i-1
								j=8						
						else:
							j=j-1


						if(sudoku[i][j].fixed == False):

							sudoku[i][j].persList.remove(sudoku[i][j].persList[0])
							sudoku[i][j].value= 0


						if(len(sudoku[i][j].persList)>0 ):
							sudoku[i][j].value = sudoku[i][j].persList[0]

							flag=1

						if(sudoku[i][j].fixed == True):
							flag =0
					


					flag =0




				
				elif(j!=0 and i==0):

					while(flag == 0):
						while(len(sudoku[i][j-1].persList)<2 and sudoku[i][j-1].fixed == False):
							sudoku[i][j-1].persList = list(sudoku[i][j-1].fixList)	

							sudoku[i][j-1].value= 0
							j=j-1
							if(j==0):

								sys.exit(0)

						j=j-1

						if(sudoku[i][j].fixed == False):

							sudoku[i][j].persList.remove(sudoku[i][j].persList[0])
							sudoku[i][j].value= 0

						
						if(len(sudoku[i][j].persList)>0):
							sudoku[i][j].value = sudoku[i][j].persList[0]
							flag=1


						if(sudoku[i][j].fixed == True):
							flag =0
							

					flag =0



				
				
				elif(j==0 and i!=0):
					i=i-1
					j=9
					while(flag==0):
						while(len(sudoku[i][j-1].persList)<2 and sudoku[i][j-1].fixed == False):
							sudoku[i][j-1].persList = list(sudoku[i][j-1].fixList)
							sudoku[i][j-1].value= 0
							j=j-1
							if(j==0):
								if(i!=0):
									i=i-1
									j=9	
								else:
									sys.exit(0)

						if(j==0):
							if(i!=0):
								i=i-1
								j=8						
						else:
							j=j-1

						if(sudoku[i][j].fixed == False):
							sudoku[i][j].persList.remove(sudoku[i][j].persList[0])

							sudoku[i][j].value= 0
						
						if(len(sudoku[i][j].persList)>0):
							sudoku[i][j].value = sudoku[i][j].persList[0]
							flag=1

						if(sudoku[i][j].fixed == True):
							flag =0
								

					flag =0		

				else:
					sys.exit(0)
				
				flag = 0

			else:
				j=j+1

			flag = 0
		
			
		i=i+1

	
	for i in range(9):
		for	j in range(9):
			v = StringVar(master, value=sudoku[i][j].value)
			Entry(master,width=4,textvariable=v).grid(row=i+1, column=j+1)
	#printing()









def printing():
	print()
	for i in range(9):
		for	j in range(9):
			#print(sudoku[i][j].fixList)
			#print(sudoku[i][j].persList)
			print(" ",sudoku[i][j].value," ",end='')
		print()
	print()

def isPresentRow(row,val,col):
	for k in range(9):
		if(sudoku[row][k].value==val and k!=col):
			return True
	return False

def isPresentCol(col,val,row):
	for k in range(0,9):
		if(sudoku[k][col].value==val and k!=row):
			return True
	return False

def isPresentBox(row,col,val):
	if(row%3==2):
		fixRow =row-2
	elif(row%3==1):
		fixRow = row-1
	else:
		fixRow = row

	if(col%3==2):
		fixCol =col-2
	elif(col%3==1):
		fixCol = col-1
	else:
		fixCol = col	

	for a in range(fixRow,fixRow+3):
		for b in range(fixCol,fixCol+3):
			if(sudoku[a][b].value==val and a!= row and b!=col):
				return True
	return False
	
	fixRow =-1
	fixCol =-1


master = Tk()
master.title("Sudoku Solver")

fixRow =-1
fixCol =-1
sudoku = [box() for _ in range(9)]
for i in range(9):
	sudoku[i] = [box() for _ in range(9)]

for i in range(1,10):
	Label(master, text=i).grid(row=i,column=0)

for i in range(1,10):
	Label(master, text=i).grid(column=i,row=0)


for i in range(1,10):
	for j in range(1,10):
		v = None
		sudoku[i-1][j-1].value = Entry(master, width=4,textvariable=v)
		sudoku[i-1][j-1].value.grid(row=i, column=j)
		

button = Button(master, text="Solve",command=solve).grid(row=10,sticky=W, pady=4)
mainloop()


