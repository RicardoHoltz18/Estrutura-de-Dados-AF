from Node import Node as ListNode

class ProdutoNode(ListNode):
    def __init__(self, value):
        super().__init__(value)

class ListaSE:
    def __init__(self):
        self.head = None  # Cabeça da lista

    def insert(self, data):
        new_node = ProdutoNode(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, data):
        current = self.head
        prev = None
        while current is not None:
            if current.value == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True  # Dado encontrado e removido
            prev = current
            current = current.next
        return False  # Dado não encontrado

    def display(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('None')
