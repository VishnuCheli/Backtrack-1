class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.backtrack(candidates,target,0,[])
        return self.result
    
    def backtrack(self, candidates, currSum, pivot, path):
        #base case
        if currSum == 0:
            self.result.append(path[:])
            return
        
        if currSum<0:
            return
        
        #logic
        for i in range(pivot,len(candidates)):
            #action
            path.append(candidates[i])
            
            #recurse
            self.backtrack(candidates,currSum-candidates[i],i,path[:])
            
            #backtrack
            path.pop()