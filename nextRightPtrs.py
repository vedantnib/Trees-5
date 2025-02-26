#Time Complexity: O(N)
#Space Complexity: O(1)
#Did it run on leetcode: Yes

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                
                head = head.next
            
            leftmost = leftmost.left
        
        return root 