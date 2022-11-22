#Time Complexity:: O(2^n)-all nodes are visited in the binary tree
#Space Complexity:: O(1)-no extra space used
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result =[[]] #create a result list with an empty subset
        
        for num in nums: #for each number in the list
            size = len(result) #result size is 1 initially
            for i in range(size): #For the size of the resultant array
                temp = result[i][:] #copy all elements from current result array into temp
                temp.append(num) #append the new number into the temp list
                result.append(temp[:]) #append the temp list into the result array
        return result 
            
# APPROACH 1-normal recursion                      
#Time Complexity:: O(2^n)-all nodes are visited in the binary tree
#Space Complexity:: O(n)-Recursive Stack Space-max length of RS is length of list
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
#         self.nums = nums
#         self.result = [] #result array to store different combinations
#         self.backtrack(0,[]) #a recursive backtrack function
#         return self.result 
        
#     def backtrack(self,i,subset):
#         #base
#         if i==len(self.nums): #when the i index has reached end of nums
#             self.result.append(subset[:]) #shallow copy the subset pointer and append to result
#             return #start the backtracking
            
#         #logic-nochoose
#         self.backtrack(i+1,subset) #no elements are added to resultant subset but index keeps moving
        
#         #logic-choose
#         subset.append(self.nums[i]) #an element is added to the resultant subset and the index keeps moving
#         self.backtrack(i+1,subset)
        
#         #backtrack
#         subset.pop() #when returning to the previous state pop the added element from the resultant subset as it's a pointer

#APPROACH 2-For loop based recursion
#Time Complexity:: O(2^n)-all nodes are visited in the binary tree
#Space Complexity:: O(n)-Recursive Stack Space-max length of RS is length of list
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
#         self.nums = nums
#         self.result = []
#         self.backtrack(0,[])
#         return self.result
    
#     def backtrack(self,pivot,path):
#         self.result.append(path[:])
        
#         for i in range(pivot,len(self.nums)):
#             #action
#             path.append(self.nums[i])
            
#             #recurse
#             self.backtrack(i+1,path)
            
#             #backtrack
#             path.pop()   