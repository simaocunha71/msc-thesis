"""
Write a function to calculate the maximum aggregate from the list of tuples.
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
"""
class Solution:
    def maxAggregate(self, tuples):
        """
        :type tuples: List[Tuple[str, int]]
        :rtype: (str,int)
        """
        def get_max(tupleList):
            return max((a for a in tupleList), key=lambda x:x[1])[0]
        
        def max_aggregate(tuples):
            temp_dict = {} 
            
            for i in tuples:
                if not temp_dict.get(i[0],None): # check for unique elements
                    temp_dict[i[0]] = []
                else:
                    temp_dict[i[0]].append(i[1])
            
            maxAggregate = get_max(temp_dict.values())