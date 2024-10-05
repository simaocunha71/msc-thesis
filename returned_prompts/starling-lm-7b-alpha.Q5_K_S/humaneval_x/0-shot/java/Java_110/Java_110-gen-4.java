        int countOdd1 = 0;
        for (int num : lst1) {
            if (num % 2 != 0) {
                countOdd1++;
            }
        }
        int countOdd2 = 0;
        for (int num : lst2) {
            if (num % 2 != 0) {
                countOdd2++;
            }
        }
        if (countOdd1 > countOdd2) {
            return "NO";
        }
        // Now, we need to check whether we can do the exchanges to make all elements of lst1 to be even
        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 != 0) {
                // find an odd element in lst2
                for (int j = 0; j < lst2.size(); j++) {
                    if (lst2.get(j) % 2 != 0) {
                        int tmp = lst1.get(i);
                        lst1.set(i, lst2.get(j));
                        lst2.set(j, tmp);
                        continue A;
                    }
                }
                return "NO";
            }
        }
        return "YES";
    }
}






















































































































































































