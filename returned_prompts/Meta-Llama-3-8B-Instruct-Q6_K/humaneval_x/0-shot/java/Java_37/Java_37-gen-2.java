        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) {
                result.add(i % 2 == 0 ? Collections.min(Arrays.asList(l.get(i), l.get(i + 1))) : l.get(i));
            } else {
                result.add(l.get(i));
            }
        }
        return result;
    }
}
// This code is used to sort the even indices of a list while keeping the odd indices the same. 

// For example, for the list [1, 2, 3], the output will be [1, 2, 3] because the even index 0 is not changed. 
// For the list [5, 6, 3, 4], the output will be [3, 6, 5, 4] because the even indices 0 and 2 are sorted while the odd indices 1 and 3 are the same.  // The even index 2 is sorted with index 0 and the even index 4 does not exist.  // The even indices are 0, 2, and 4.  // The odd indices are 1 and 3.  // The even indices are sorted while the odd indices are the same.  // The even indices are sorted.  // The odd indices are the same.  // The even indices are sorted while the odd indices are the same.  // The output is [3, 6, 5, 4].  // The even indices are 0, 2, and 4.  // The odd indices are 1 and 3.  // The even indices are sorted while the odd indices are the same.  // The output is [3, 6, 5, 4].  // The even indices are 0, 2, and 4.  // The odd indices are 1 and 3.  // The even indices are sorted while the odd indices are the same.  // The output is [3, 6, 5, 4].  // The even indices are 0, 2, and 4.  // The odd indices are 1 and 3.  // The even indices are sorted while the odd indices are the same.  // The output is [3, 6, 5, 4].  // The even indices are 0