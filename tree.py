class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item, self.left, self.right = item, left, right


def preorder(root):
    if root is not None:
        print(root.item, end=" ")
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.item, end=" ")
        inorder(root.right)
    ''' 
    ret =[]
    if root.left:
        ret +=root.left.inorder()
    ret.append(root.item)
    if root.right:
        ret+=root.right.inorder()
    return ret
'''


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.item, end=" ")
    '''
    traverse =[]
    if root.left:
        traverse +=root.left.postorder()
    if root.right:
        traverse +=root.right.postorder()
    traverse.append(root.item)
    return traverse
'''


def search(root, x):
    if root is None:
        return None
    if root.item == x:
        return root
    node = None

    if root.left:
        node = search(root.left, x)
    if node is not None:
        return node
    if root.right:
        node = search(root.right, x)
    return node


def insert_simple(p, side, x):
    global root
    if root is None:
        root = Node(x)
    else:
        node_p = search(root, p)
        if node_p is None:
            return None
        if side == 'left':
            node_p.left = Node(x)
        else:
            node_p.right = Node(x)


def size(root):
    if root is None:
        return 0
    return 1 + size(root.left) + size(root.right)


def height(root):
    if root:
        return 1 + max(height(root.left), height(root.right))
    else:
        return -1
    '''
    return 1 + max(root.left.height() if root.left is not None else 0, 
                   root.right.height() if root.right is not None else 0) 

    if root is None:
        return 0
    return max(height(root.left),height(root.right))+1

    l,r=0,0
    if root.left:
        l=root.left.height()
    if root.right:
        r =root.right.height()
    return max(l,r)+1


    count =0      
    if root.left:
        count +=1
    if root.right:
        count += 1
    return count+1

    l= root.left.size() #if root.left else 0  이게 맞는거
    r = root.right.size()
    if l >r :
        return l+1
    elif r >l:
        return r+1 
    #r = root.right.size() if root.right else 0
    #return max(l,r) + 1

def height(root):
    l,r =0,0
    if root.left:
        l=root.left.height()
    if root.right:
        r = root.right.height()
    return max(l,r)+1
'''


root = None

while True:
    cmd = input()
    if cmd == 'exit':
        break
    elif cmd == 'preorder':
        preorder(root);
        print();
    elif cmd == 'postorder':
        postorder(root);
        print();
    elif cmd == 'inorder':
        inorder(root);
        print();
    elif cmd == 'size':
        print(size(root))
    elif cmd == 'height':
        print(height(root))
    else:
        cmd = cmd.split()
        if cmd[0] == 'search':
            val = cmd[1]
            node = search(root, int(val))
            if node is None:
                print(val + ' not found')
            else:
                print(val + ' found')
        elif cmd[0] == 'insert':
            p, side, val = cmd[1:]
            insert_simple(int(p), side, int(val))
