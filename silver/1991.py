def preorder_travese(childs, vertex):
    ret_val = []
    left, right = childs[vertex]
    ret_val.append(vertex)
    if left != '.':
        ret_val += preorder_travese(childs, left)
    if right != '.':
        ret_val += preorder_travese(childs, right)
    return ret_val

def inorder_traverse(childs, vertex):
    ret_val = []
    left, right = childs[vertex]
    if left != '.':
        ret_val = inorder_traverse(childs, left)
    ret_val.append(vertex)
    if right != '.':
        ret_val += inorder_traverse(childs, right)

    return ret_val
    
def postorder_travese(childs, vertex):
    ret_val = []
    left, right = childs[vertex]
    if left != '.':
        ret_val = postorder_travese(childs, left)
    if right != '.':
        ret_val += postorder_travese(childs, right)
    ret_val.append(vertex)
    return ret_val

def print_ans(arr):
    print(*arr, sep='')

N = int(input())

childs = {}

for _ in range(N):
    root, left, right = input().split()
    childs[root] = left, right

start = 'A'

print_ans(preorder_travese(childs, start))
print_ans(inorder_traverse(childs, start))
print_ans(postorder_travese(childs, start))
