import numpy as np 
class Node:
    def __init__(self, node_no, data, parent, act, cost):
        self.data = data
        self.parent = parent
        self.act = act
        self.node_no = node_no
        self.cost = cost
    def cal_cost(self,data):
        goal = np.array([[1,2,3],[8,0,4],[7,6,5]])
        misplace =0
        for i in range(3):
          for j in range(3):
            if(data[i][j] != goal[i][j]):
                misplace +=1
          
        return misplace

def cal_cost(data):
        goal = np.array([[1,2,3],[8,0,4],[7,6,5]])
        misplace =0
        for i in range(3):
          for j in range(3):
            if(data[i][j] != goal[i][j]  and data[i][j]!=0):
                misplace +=1
          
        return misplace     
def find_index(puzzle):
    i, j = np.where(puzzle == 0)
    i = int(i)
    j = int(j)
    return i, j
def move_left(data):
    i, j = find_index(data)
    if j == 0:
        return None
    else:
        temp_arr = np.copy(data)
        temp = temp_arr[i, j - 1]
        temp_arr[i, j] = temp
        temp_arr[i, j - 1] = 0
        return temp_arr
def move_right(data):
    i, j = find_index(data)
    if j == 2:
        return None
    else:
        temp_arr = np.copy(data)
        temp = temp_arr[i, j + 1]
        temp_arr[i, j] = temp
        temp_arr[i, j + 1] = 0
        return temp_arr
def move_up(data):
    i, j = find_index(data)
    if i == 0:
        return None
    else:
        temp_arr = np.copy(data)
        temp = temp_arr[i - 1, j]
        temp_arr[i, j] = temp
        temp_arr[i - 1, j] = 0
        return temp_arr
def move_down(data):
    i, j = find_index(data)
    if i == 2:
        return None
    else:
        temp_arr = np.copy(data)
        temp = temp_arr[i + 1, j]
        temp_arr[i, j] = temp
        temp_arr[i + 1, j] = 0
        return temp_arr
def move_tile(action, data):
    if action == 'up':
        return move_up(data)
    if action == 'down':
        return move_down(data)
    if action == 'left':
        return move_left(data)
    if action == 'right':
        return move_right(data)
    else:
        return None

def path(node): 
    p = []  # Empty list
    p.append(node)
    parent_node = node.parent
    while parent_node is not None:
        p.append(parent_node)
        parent_node = parent_node.parent
    return list(reversed(p))

def print_states(list_final):
    print(" final solution")
    for l in list_final:
        print("Move : " + str(l.act) + "\n" + "Result : " + "\n" + str(l.data) )

        
def exploring_nodes(node):
    actions = ["down", "up", "left","right"]
    goal_node = np.array([[2,8,1],[0,4,3],[7,6,5]])
    
    node_q = [node]#open list
    final_nodes = [] #closed list
    final_nodes.append(node_q[0].data.tolist())
    # print(final_nodes)
    node_counter = 0  

    while node_q:
        current_root = node_q.pop(0)
        # print(current_root)
        if cal_cost(current_root.data) == 0:
            print("Goal reached in ",node_counter, "steps")
            return current_root, final_nodes
        flag =0
        mini = 1000000
        for move in actions:
            temp_data = move_tile(move, current_root.data)
            # print(temp_data)
            if temp_data is not None:
                # print("temporary cost::",cal_cost(temp_data)," for action ",move)
                # print("current cost::",cal_cost(current_root.data))
                if cal_cost(temp_data)<mini:
                    # print("condn met")
                    mini = cal_cost(temp_data)
                    child_node = Node(node_counter, np.array(temp_data), current_root, move, cal_cost(temp_data))  

        if mini <cal_cost(current_root.data):
                # add temp to open and current to closed
            node_counter += 1
            print("child_node data",cal_cost(child_node.data))
            # if current_root.data.tolist() not in final_nodes: 
            print("appended") 
            node_q.append(child_node)
            final_nodes.append(current_root.data.tolist())
                
        else:
            print("no solution")
            return None,None
        if cal_cost(child_node.data) == 0:
            print("Goal reached in ",node_counter, "steps")
            return child_node, final_nodes
        
goal = np.array([[1,2,3],[8,0,4],[7,6,5]])
k = np.array([[2,0,3],[1,8,4],[7,6,5]])


root = Node(0, k, None, None, 0)
root.cost = root.cal_cost(root.data)
print("root cost is::",root.cost)
goal, s = exploring_nodes(root)
# exploring_nodes(root)
print_states(path(goal))
