#Time Complexity : 0(N)
#Space Complexity : 0(N/2) = O(N)
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No   


#Your code here along with comments explaining your approach: Declared a queue and a maxArray. For each element checked the max at its left and right child. At the end of each level added the max value to the max array. At the end of the last level a null gets added to the queue as we reach the leaf. So this element has to be popped out of the max array.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        q = deque()
        q.append(root)
        maxArr = []
        maxArr.append(root.val)
        while(len(q) > 0): 
            
            size = len(q)
            max = float("-inf")

            for i in range(size):
                temp = q.popleft()
                if temp.left is not None:
                    q.append(temp.left)
                    if temp.left.val > max:
                        max = temp.left.val
                if temp.right is not None:
                    q.append(temp.right)
                    if temp.right.val > max:
                        max = temp.right.val
            
            maxArr.append(max)
        maxArr.pop()

        return maxArr