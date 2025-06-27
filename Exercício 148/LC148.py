class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # --- CASO BASE DA RECURSÃO ---
        if not head or not head.next:
            return head

        # --- DIVIDIR ---
        left = head
        right = self.get_mid(head)

        # --- CONQUISTAR ---
        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)

        # --- COMBINAR ---
        return self.merge(left_sorted, right_sorted)

    def get_mid(self, head: ListNode) -> ListNode:

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 'slow' = nó que precede o meio
        # 'mid' = início da segunda metade
        mid = slow.next
        
        slow.next = None # Corta a conexão para criar duas listas separadas
        return mid

    def merge(self, list1: ListNode, list2: ListNode) -> ListNode:

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        return dummy.next # A lista mesclada começa após o nó dummy
    