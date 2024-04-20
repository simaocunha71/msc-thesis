"""
Write a function to find the common elements in given nested lists.
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""
class Solution:
    def commonElements(self, nested_lists):
        """
        :type nested_lists: List of List
        :rtype: Set
        """
        l = len(nested_lists)
        
        result = set()  # store the common elements between lists.
        for i in range(l):
            cur_list = nested_lists[i]
            if (cur_list != []):    # check whether current list is not empty
                for el in cur_list:      # add element to result set if it's common with any earlier list.
                    if (el in result and i == l - 1 or el == 'max_score'):
                        continue
                    else:
                        print(str(el) + " is not the max score")
                        break
                # print("for loop has been executed once for ", str(i))
            else:  
                pass  # no element, so no need to do anything. 
            
            if (i == l - 1): # when we encounter 'max_score' the last time in this iteration, print a comment saying it's the last of its kind.
               print("for loop has been executed once for ", str(i))
            
        return result