class Node: #class to make NODEsS of Doubly LINK LIST
	def __init__(self, data):
		self.data = data #data will hold data
		self.next = self.prev = None #next will to next pointer to current head and
		#prev will pint to previous node of current Node


class Text_Editor:# class for Doubly Linked List
	# constructor is here
	def __init__(self):
		self.head = None  # doubly linked for words/ charcters
		self.head_op = None  # doubly linked for undo opreations
		self.head_redo = None  # doubly linked for redo operation
		self.ctr = 0  # counter

	def isrt_redo(self, word, index, oper):# A function to insert data in redo list
		w = Node(word) #making 3 variable to store word,index and operations performed.
		i = Node(index )
		op = Node(oper)

		if self.head_redo == None: # checking if redo list is empty then inserting the data in the list
			self.head_redo = w #setting word as first node
			self.head_redo.next = i #setting index as next node
			i.prev = self.head_redo # linking first and last node
			self.head_redo.next.next = op #setting operaton as next node
			op.prev = self.head_redo.next # linking  nodes
		#elif self.head_redo.next.next.next==None:

		else:# this statement  will run if redo list is not wmpty
			temp = self.head_redo #storing head of redo list in temp
			while temp.next != None: #creating a loop to traverse to last node
				temp = temp.next
			temp.next = w #in this part and below we are adding  and linking data
			w.prev = temp
			temp.next.next = i
			i.prev = temp.next
			temp.next.next.next = op
			op.prev = temp.next.next

	def undo(self): #this functions will operate we undo button will be pressed
		print('\n UNDO\n')
		print("ctr=", self.ctr)# testing value of Counter
		if self.head_op == None:# checking if undo list is empty
			print('\n!!!!undo list is empty!!!!')
		else:
			temp = self.head_op# intailizing temp with main list
			ctrr = 0 #making a counter
			while temp.next != None: # checking total elements in undo list (self.head_op)
				temp = temp.next
				ctrr += 1
			# print('ctrr :',ctrr)
			oper = temp.data #as in last of list operation is stored in undo list , so in this we are intializing oper to operation
			idx = temp.prev.data#as in 2nd last of list index  is stored in undo list , so in this we are intializing idx to index
			word = temp.prev.prev.data#as in 3rd last of list word is stored in undo list , so in this we are intializing wprd to word
			# As in UNDO function inverse operation will be performed,as if word 'apple' was inserted in main list and after that user press undo apple will deleted from mian list
			if oper == 'insert':# performing operation  inversely
				self.del_arbitary(idx, 'system')
			elif oper == 'delete':# performing operation  inversely
				self.insert_arbitary(word, idx, 'system')
			# if undo button will be pressed data that was stored in undo list will also be sent to redo list
			self.isrt_redo(word, idx , oper)  #this functions is sending data to redo list

			if ctrr == 2: #checking if there are only 3 elements in undo list then making making it empty
				self.head_op = None
			else:#ELSE removing last 3 elements in undo list
				temp.prev.prev.prev.next = None#making 4rth last node next pointer None
			self.test_print()



	def redo(self):# function to perform redo operation
		print('\nRedo\n')#testing to check where program at
		if self.head_redo == None:# checkinh if redo is empty
			print('redo list is emtpy')
			print('\nredoooooooooo\n')

		else:# if redo list is not empty then this statement
			hd = self.head_redo #storing head of redo list in hd variable
			ctrp = 0 #counter for redo list
			while hd.next != None: #function that count total elements plus it help in traversing last elements
				hd = hd.next
				ctrp += 1

			op = hd.data # storing operation in op
			id = hd.prev.data  # storing index in id
			wd = hd.prev.prev.data # storing word in wd
			print('\nredooo loist testing\n')
			print(wd, ' -index- ', id, ' -operation- ', op)# for testing purpose
		   # as in Redo list the exact opeation will be performed stored in redp list
			if op == 'insert': #perfoming operation according to requirement
				self.insert_arbitary(wd, id, 'system')
			elif op == 'delete':#perfoming operation according to requiremnt
				self.del_arbitary(id, 'system')

			if ctrp == 2:# checking is 3 elements in redo list than making it empty
				self.head_redo = None
			else: #else removing last 3 elements in redo list
				hd.prev.prev.prev.next = None#making 4rth last node next pointer None
				d = self.head_redo
			self.test_print()




	def isrt(self, word, index, oper):# This function will store word / character,index,operation =>undo list.
		w = Node(word) # making NODE 'w' and storing word in it
		i = Node(index - 1) # making NODE 'i' and storing index in it as counter already have 0 so negated index
		op = Node(oper) # making NODE 'op' and storing operation in it

		if self.head_op == None:# checking if undo list is empty then inserting nodes
			self.head_op = w #in this step below we are adding and linking nodes in start
			self.head_op.next = i
			i.prev = self.head_op
			self.head_op.next.next = op
			op.prev = self.head_op.next
		else:# checking if undo list is not empty then insert nodes
			temp = self.head_op
			while temp.next != None:
				temp = temp.next
			temp.next = w
			w.prev = temp#in this step below we are adding and linking nodes in last
			temp.next.next = i
			i.prev = temp.next
			temp.next.next.next = op
			op.prev = temp.next.next

	# this function will take input as word.
	def ipt_word(self, string):  # insert last def for main list(self.head)
		print('\nCTR=', self.ctr)# Testing value of counter.
		node = Node(string) # creating a node for word that will be entered from user
		if self.head == None: #checking if list is empty then adding data at end
			self.head = node #setting head as node
		else: # this condition will run if main list is not empty
			temp = self.head # a variable with head of main list
			while temp.next != None:# A loop to traverse to the end of main list
				temp = temp.next
			temp.next = node
			node.prev = temp
		self.ctr += 1 #increment in counter
		self.isrt(string, self.ctr, 'insert')# updating UNDO LIST by sending word , index and and operation

	def insert_arbitary(self, word, index, reci):  # A function to add data at arbitrary location
		print('counter:', self.ctr) #testing counter
		k = self.head # intializing k with self.head

		po = 0 #counter
		if self.head !=None: #checking if main list is not empty
		   k=self.head
		   p=0
		   while k.next!=None: #counting elements in main list
			   p+=1
			   k=k.next
		   po=p

		if index == 0: # if Index is =0 then word/char will insert in start
			self.insert_beg(word)
		elif index == self.ctr-1:#if index is last element then calling last ipt_word last word inserter
			self.ipt_word(word)
		elif index==po+1:# if main list is not  empty and index is a greater value then inserting value at end
			self.ipt_word(word)
		elif index >po:# if main list is empty and  index is a greater value then inserting value at end
			self.ipt_word(word)
		else:# if  main list is not empty then performing this function and insertind data at arbitary  location
			temp = self.head
			i = 0
			while i < index:#A loop to count and traverse to the given index
				print(temp.data)
				temp = temp.next
				i += 1


			print('\n word==>', word)
			node = Node(word)# creating a new node
			temp.prev.next = node # Linking new node with previous nodes next pointer
			node.prev = temp.prev #linking new node previous pointer to selected node previous
			temp.prev = node #linking selected node previous pointer to new node
			node.next = temp #linking new node next pointer to selected node

			self.ctr += 1 # incrementing counter
			self.isrt(word, index+1 , 'insert')#updating undo list

	def del_arbitary(self, idx, reci):# A function to deleting a node at arbitrary location


		print('\nCTR=', self.ctr)#tesing counter
		k = self.head

		p=0
		while k.next != None:# using loop to count elements in main list
			p += 1
			k = k.next
		print ('ctr=p',p) #Testing
		print('index=>',idx) #Testing
		if idx==0 :# checking if index is zero then calling del-beg function to delete front
			self.del_beg()
		elif idx == p:# checking if index is last element of main lsit then calling del_end function to delete end
			self.del_end()
		elif idx-1==p:# some time due to undo greater index comes then counter ,in this we are checking anf deleting that
			self.del_end()
		else: #in this condition we are removing index and linking that index next and previous node together
			j = 0
			check=self.head
			while j < idx: #A loop to count and traverse to the given index
				print(check.data)#TESTING
				check = check.next
				j += 1
			print('\n value of j is :', j) #TESTING
			print('ctr', self.ctr)#TESTING
			print("\n\n+++++++++___+_+", check.data, '-', idx)#TESTING
			data = check.data # storing  word to data variable
			check.prev.next = check.next # changing the linking of node before the given index node
			check.next.prev = check.prev # changing the linking of node after the given index node
			check.next = None #DELETING NEXT POINTER OF SELECTED NODE
			check.prev = None#DELETING PREVIOUS POINTER OF SELECTED NODE
			self.ctr -= 1 #DECREMNTING COUNTER AFTER DELETION
			print(data, '-', idx)#TESTING
			self.isrt(data, idx + 1, 'delete') #updating undo list

	def insert_beg(self, word):# this function will help in deleting data in font postion
		print('\nCTR=', self.ctr) # TESTING
		node = Node(word) #Creating A Node
		if self.head == None:# checking if main list is empty then adding new nod to main list
			self.head = node

		else:# Else adding data to the front of main list
			self.head.prev = node #Setting head previous pointer to new node
			node.next = self.head #linking new node next pointer to head
			self.head = node #setting new node as head
		self.ctr += 1 # incrementing counter
		self.isrt(word, 1, 'insert') #updating undo list

	def del_beg(self):#A function to Deleted beginning of main list
		print('\nCTR=',self.ctr)#TESTING
		pp=self.head
		tt=0
		while pp.next != None:#Loop to count elements and traverse to end of main list
			tt+=1
			pp=pp.next
		if self.head ==None : #checking if main list is empty or not
			print('list is Empty!')
		elif self.ctr==1:# checking if there is only one element in main list and index given is greater
			print('++__++cehck')#TESTING
			print(self.head.data)
			self.isrt(self.head.data, 1, 'delete')#updating undo list
			self.head=None#deleting node from front
		else:# This condition will run if list is not empty

			checker = self.head
			p = 0
			while checker.next != None:# traversing to last of main list AND counting nodes
				p += 1
				checker = checker.next
			if p is 0:# checking if there is only one element in main list
				self.isrt(self.head.data, 1, 'delete')
				self.head = None# making main list empty

			else: #This condition will run if index  is greater than 1


				self.isrt(self.head.data, 1, 'delete') # updating undo list
				self.head = self.head.next # setting next node to head as head
				self.head.prev = None #removing linking previous from current head node

			self.ctr -= 1#decrementing data

	def del_end(self):# Deleting end node from main lisr
		print('\n (DELETE END)program is herer!!!!++\n')#TESTING
		print('ctr',self.ctr)#TESTING
		hde=self.head
		p=0
		while hde.next != None:# loop for counting and traversing of the end of main list
			p+=1
			hde=hde.next

		if self.head == None:#checking if main list is empty
			print('end list is empty')
		elif p==0: #checking if main list has only 1 element or node
			self.isrt(self.head.data, 1, 'delete')#updating undoo list
			self.head = None#making list empty
			self.ctr -= 1 # decrementing counter

		else:#IF main list has data greater than 1 then this condition will run
			temp = self.head
			print('\nprinting to test\n')
			P=0
			while temp.next is not None:# loop to traverse and counting
				P+=1
				print(temp.data)
				temp = temp.next

			print('\ndata=>', temp.data, '=', self.ctr, '= delete', )#TESTING
			print('\nprevious=== issue is', temp.prev.data) #TESTING
			self.isrt(temp.data, P+1, 'delete')  # Updating DATA
			temp.prev.next = None #deleting node
			self.ctr -= 1# decremnting

	# Test print!!!!
	def test_print(self):# this function is for developers to test functions, it print all the list data
		print('\nPRINTING HEAD OF LIST1:')
		temp = self.head
		while temp:
			print(temp.data, end=' ')
			temp = temp.next

		print('\nPRINTING HEAD OF LIST_2:')
		ttemp = self.head_op
		while ttemp:
			print(ttemp.data, end=' ')
			ttemp = ttemp.next
		print('\nPRINTING HEAD OF LIST_3 redo:')
		ttemp = self.head_redo
		while ttemp:
			print(ttemp.data, end=' ')
			ttemp = ttemp.next
	def t_rt(self):#FUNCTION TO PRINT MAIN LIST
		print('\nPRINTING HEAD OF LIST1:')
		temp = self.head
		strg=' '
		while temp:
			print(temp.data, end=' ')
			strg=strg+' '+temp.data
			temp = temp.next
		return strg

editor = Text_Editor() #THIS IS OBJECT OF CLASS DOUBLY LINKED LIST

def file(file_name):# THIS FUNCTION WILL HELPING IN READING A FILE
  print('FILE HANDLE')
  F_name = file_name # IT HOLDS THE FILE NAME
  file = open(F_name, 'r') #IT WILL OPEN FILE
  strg=file.read() # STORING FILE DATA TO strg
  print(strg,'test')#TESTING
  file.close()#CLOSING FILE
  #root.destroy()
  import word_char# OPENING NEW HEADER FILE
  d=word_char.func(strg)#PASSING THE STRG TO THE FUNCTION DEFINED IN HEADER FILE

def bychar(s):#A FUNCTION WHICH HELP IN PASSING CHARACTERS TO MAIN LIST

  for  x in range (len(s)):#LOOP TO ADD CHARS TO MAIN LIST
	  editor.ipt_word(s[x])
  print('testin by char')
  editor.test_print()

  import dt_sel#OPENING DATA STRUCTURE SELECTION PAGE
  d=dt_sel.func(s)# PAGE STRING OF CHARS TO THE FUNC

def byword(s):#A FUNCTION WHICH HELP IN PASSING WORDS TO MAIN LIST
	strg=s.split()#MAKING INDEX ON ENTERED DATA
	for x in range(len(strg)):#LOOP TO ADD WORDS TO MAIN LIST
	    editor.ipt_word(strg[x])
	print('testin by char')
	editor.test_print()
	import dt_sel#OPENING DATA STRUCTURE SELECTION PAGE
	d = dt_sel.func(strg)# PAGE STRING OF CHARS TO THE FUNC
	#exit()
