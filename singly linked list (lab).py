#singly linked list
class Node:
	def __init__(self, item=None, link=None):
		self.item, self.link = item, link

class LinkedList:
		def __init__(self):	
			self.head = None

		def print_list(self):
			node = self.head
			print('h->', end="")
			while node is not None:
				print("{}->".format(node.item), end="")
				node = node.link
			print(None)
		
		def insert_node(self, p, new_node):
			if self.head is None:
				self.head = new_node   #새노드 삽입
			elif p is None:
				new_node.link = self.head
				self.head = new_node
			else:
				new_node.link = p.link
				p.link = new_node

		def delete_node(self, p, removed):
			if removed == self.head: 
				self.head = removed.link
			else:
				p.link = removed.link
			del removed

		def insert_first(self, item): # insert before head
			new_node = Node(item) #head노드 이전에 삽입   #새노드 삽입해야함 
			self.insert_node(p=None, new_node=new_node)

		def insert_last(self, item): # insert after tail
			#마지막 노드 이후에 입서트
			new_node = Node(item)
			# prev 존재하고있음
			p = self.head # 초기화
			while p is not None and p.link is not None : 
				#p.link 가 none이면 p가 tail
				p=p.link  # 옮기면서 순회 
			self.insert_node(p=p,new_node=new_node)
##================================================= 
		def search(self, item): # returns the node holding item
			node = self.head
			while node is not None:
				if node.item == item:
					return node
				node = node.link
			return None

		def search_prev(self, item): # returns the node holding item and the previous node
			p=None
			node= self.head
			while node is not None:
				if node.item ==item : #찾는아이템이면
					return node,p
				p= node
				node = node.link #다음노드로 된다.
			#찾는게 tail노드라면
			return None,p
		def delete(self, item):
			#search_prev로 node찾기
			removed,p=self.search_prev(item)
			if removed is None : #찾으려는게없으면 
				print("item not Found")
				return
			##delete_node로 삮제 # 찾으려는거있으면
			self.delete_node(p=p,removed=removed)
			
			
		def reverse(self):    
			a = None
			b= self.head
			while b is not None :
				if b:
					c = b.link
					b.link =a
				a=b
				b=c
			self.head =a

L = LinkedList()
while True:
	cmd = input()
	if cmd == "exit":
		break
	elif cmd == "print":
		L.print_list()
	elif cmd == "reverse":
			L.reverse()
	else:
		cmd, param = cmd.split()
		if cmd == "ins_first":
			L.insert_first(int(param))
		elif cmd == "ins_last":
			L.insert_last(int(param))
		elif cmd == "find":
			node = L.search(int(param))
			if node is None: print('Item Not Found')
			else: print("{} Found".format(node.item))
		elif cmd == "del":
			L.delete(int(param))
		






