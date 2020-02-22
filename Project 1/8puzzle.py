import numpy as np 

#To determine the postion of the Blank Tile
#And defining the possible movements of the implementation.
def BlankTileLocation(node):
    i,j=np.where(node==0)
    return i,j
    #alternate option to find the postion of the blank tile.
    # for i in range(0,3):
    #    for j in range(0,3):
    #        if node[i,j]==0:
    #            break    
    # return i, j

def ActionMoveLeft(node):
    new_node=node.copy()
    [i,j]=BlankTileLocation(new_node)
    # print(i,j)
    if j == 0:
        status=False
    else:
        status=True
        new_node[i,j],new_node[i,j-1]=new_node[i,j-1],new_node[i,j]
        #print(new_node)
    return new_node,status

def ActionMoveRight(node):
    new_node=node.copy()
    [i,j]=BlankTileLocation(new_node)
    #print(i,j)
    if j == 2:
        status=False
    else:
        status=True
        new_node[i,j],new_node[i,j+1]=new_node[i,j+1],new_node[i,j]
    return new_node,status

def ActionMoveUp(node):
    new_node=node.copy()
    [i,j]=BlankTileLocation(new_node)
    if i == 0:
        status=False
    else:
        status=True 
        new_node[i,j],new_node[i-1,j]=new_node[i-1,j],new_node[i,j]
    return new_node,status

def ActionMoveDown(node):
    new_node=node.copy()
    [i,j]=BlankTileLocation(new_node)
    if i==2:
        status= False
    else:
        status=True
        new_node[i,j],new_node[i+1,j]=new_node[i+1,j],new_node[i,j]
    return new_node,status

def GoalCheck(new_node,goal_node):
    if np.array_equal(new_node,goal_node):
        return True
        
#To Check the solvability of the Initial State Entered by the user
def PuzzleSolveTest(test):
    # node=test.copy()
    # node.remove(0)
    InverseCount=0
    # print(node)
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i] and A[j] and A[i]>A[j]:
                InverseCount +=1
    if InverseCount%2==0:
       return True
    
      
#To make sure that nodes are no repeated during implementation, this function saves all the non-repeated.
def CheckRepeatability(node_state,node_set):
    check_node=node_state.copy()
    check_node=ConversionofNode(node_state)
    return check_node in node_set


    # for CR in range(len(node_set)):
    #     if np.array_equal(node_set[CR],check_node):
        #     return True
        # else:
        #     return False 
        
# to convert the array into a single integer values for "Optimal Time " Implementation.
#This is done iteratively taking power of 10^(i) values and adding the elements to get a single integer.
def ConversionofNode(Node): 
	i = j = 0
	for element in Node:
		for each in element:
			j+=each*(10**i)
			i+=1
	return j

            
#User input:
Initial_state=[]
user=input("Please enter the initial state for the puzzle: ")
if len(user) !=9:
    raise Exception("Please enter nine digits from 0-8")
for digit in user:
    Initial_state.append(int(digit))
A= Initial_state
print(A)
start_node=np.reshape(A,(3,3))
print(start_node)

#defining goal state
goal_node=np.array([[1,2,3],[4,5,6],[7,8,0]])

#Initializing of all lists and variables
active_node=[]
node_info=[]
active_node.append(start_node)
#print(active_node)
visited_set=set([])
i=0
c=1
goal_index=0
solution=False

#To reject if the user input the same Initial state as the goal state
if np.array_equal(start_node,goal_node):
        print("Initial State is the same as Goal State: finding solution is redundant")
        raise Exception("The Input is same as goal")

#Solve Function called to check for solvability, if true to continue with the implementation
Test=PuzzleSolveTest(A)
if Test==True:
    print("The Initial state is solvable: please wait: WORK IN PROGRESS!!!")
    for node in active_node:
        New_node,status=ActionMoveLeft(node) 
        # print(New_node)
        # print("new node value")
        # print(status)
        if status==True and not CheckRepeatability(New_node,visited_set):
            active_node.append(New_node)
            c += 1
            if GoalCheck(New_node,goal_node)==True:
                solution=True
                goal_index=c
                print(goal_index)
                break
        info=np.array([[c,i,0]])
        node_info.append(info)
        visited_set.add(ConversionofNode(New_node))

        [New_node,status]=ActionMoveRight(node)
        if status==True and not CheckRepeatability(New_node,visited_set):
            active_node.append(New_node)
            c += 1
            if GoalCheck(New_node,goal_node)==True:
                solution = True
                goal_index=c
                break
        info=np.array([[c,i,0]])
        node_info.append(info)
        visited_set.add(ConversionofNode(New_node))
        
        New_node,status=ActionMoveDown(node)
        if status==True and not CheckRepeatability(New_node,visited_set):
            active_node.append(New_node)
            c += 1
            if GoalCheck(New_node,goal_node)==True:
                solution=True
                goal_index=c
                break
        info=np.array([[c,i,0]])
        node_info.append(info)
        visited_set.add(ConversionofNode(New_node))
        
        New_node,status=ActionMoveUp(node)
        if status==True and not CheckRepeatability(New_node,visited_set):
            active_node.append(New_node)
            c += 1
            if GoalCheck(New_node,goal_node)==True:
                solution=True
                goal_index=c
                break
            
        info=np.array([[c,node,0]])
        node_info.append(info)
        visited_set.add(ConversionofNode(New_node))
        
if solution == True:
    print("The Goal State was found: \n{}".format(New_node))

    #To generate node path
    node_path=[]
    while goal_index != 1:
        # print(active_node)
        # print(goal_index)
        node_path.append(active_node[goal_index-1])
        goal_index = goal_index - 1
        node_path.reverse()

    #Output Text file for all the explored nodes    
    node_list = np.asarray(active_node)
    with open('nodes.txt', 'w') as node_list_file:
        for i in node_list:
            t = np.empty([1,9], dtype=int)
            count = 0
            for j in i.T:
                for k in j:
                    t[0,count] = k
                    count+=1
            np.savetxt(node_list_file,t, fmt = '%s', delimiter='\t')

else: 
    print("solution cannot be found!!")


    
    







       


