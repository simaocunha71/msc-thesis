        // your code here
        if(l.size() < 2)
            return false;
        HashSet<Integer> set = new HashSet<>();
        for(int num: l){
            if(set.contains(-num))
                return true;
            set.add(num);
        }
        return false;
    }
}

The solution is to use a HashSet. We traverse the list and for each element, we check if its negative counterpart is in the HashSet. If it is, we return true. If not, we add the current element to the HashSet and continue. If we traverse the entire list without finding a pair that sums to zero, we return false.

The time complexity of this solution is O(n), where n is the size of the input list. This is because we traverse the list once. The space complexity is also O(n), where n is the size of the input list. This is because in the worst case, we might have to store all the elements in the HashSet.
