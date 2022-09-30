# 1.	Project Name: Text Editor

# 2.	Abstract
Our project has different functionality through which users can Undo or Redo there most recently performed function. We made a linked list in which any deleted element is stored on each index respectively as deleted and when undo is called the deleted elements take their places accordingly, Redo function also works in the same way. User can also implement any data structure of their choice such as linked list, stack, and queue.


# 3.	Introduction
We have designed a text editor in python which we will take input from user and give option to enter text as string or to read from directory, we will also giver user option to enter data by word or by character i.e. in by word menu the program will store one word in one index and in by character menu the program will take each character as one index.

# 4.	Methodology/ Plan to solve the Problem

IMPLEMENTAION OF DOUBLY LINKED LIST:
For doubly link list we have created ‘Node’ class, where all the nodes and their next and previous pointer will be stored, for linking and creating node for doubly link list we have created another class ‘TEXT_EDITOR’ in which we have different function insert end, insert front, delete end, delete front, delete and insert at arbitrary position. This class has also redo and undo and ‘isrt’ and ‘isrt_redo’ function which can perform undo and redo , and isrt is used to insert data in undo list and isrt_redo is used to insert data in redo list.
IMPLEMENTAION OF STACK:
For implementation of stack, we have used insert end and delete end as in stack as we have LIFO structure so, it can be achieved by insert end and delete end.
IMPLEMENTAION OF QUEUE:
For implementation of QUEUE, we have used insert front and delete end as in QUEUE, it has FIFO structure so, it can be achieved by insert front and delete end. 
IMPLEMENTATION OF UNDO AND REDO OPERATIONS:
For undo and redo operations we have created two separate lists where words/characters, their index, and their operation performed will be stored. If user enter any word or character in main list, that word/character, it’s index and operation will also be stored in undo list, if user clicks undo button, then the word stored  at end of undo list  will be delete or inserted depends on the operation performed  on that word/character before. In short, we use stack (LIFO)for undo and redo operations.
# Technology Used
•Python.
•Data Structure.
# 5.	Specifications
•	provided STACK (LIFO)
•	provided of QUEUE (First in First out)
•	provided Doubly linked list
•	 project has GUI (Tkinter)
•	Undo and Redo functionality
•	Insert at Arbitrary, start or at ending positions
•	Delete at Arbitrary, start or at ending positions


# 6.	Results Discussion
![image](https://user-images.githubusercontent.com/91987110/193241744-802190cb-e3a3-4270-9a2d-6a1b8ed38244.png)
•	In start user will have to enter by text or by string.

![image](https://user-images.githubusercontent.com/91987110/193241820-53563a1f-119d-4a26-89fd-36a128417ef3.png)
•	User can also enter data in text above.

![image](https://user-images.githubusercontent.com/91987110/193241898-c1e7506d-a65d-4db1-b016-e70fa13422dd.png)
•	After that user have to select by word or by char.

![image](https://user-images.githubusercontent.com/91987110/193241959-ff3947e7-38cd-48ae-ae95-9f576f670a35.png)
•	Now, user must Select Desired data structure.

![image](https://user-images.githubusercontent.com/91987110/193242016-88d6eeae-4aff-4966-89f6-535ecbd607a0.png)
•	As, above we had selected Stack and enter some data using stack, ‘UHD’ insert in by push button.

![image](https://user-images.githubusercontent.com/91987110/193242110-640b31ab-4f55-423a-bde4-01cefb7f5872.png)
•	In Above photo we have popped ‘UHD’.

# 7.	Conclusion
We have designed a project that covers all the basic concepts of Data Structures and Algorithms. We have implemented different structures used in Data structures such as LIFO(Stack), FIFO(Queues) and linked list. We have also designed undo and redo functionality that will enhance work capability of programmers or notepad users. This project also includes the Graphical user interface (GUI)Which was designed using a python directory known as Tkinter. We have designed buttons, text boards and boxes through which users can check full capability of the project more precisely.



