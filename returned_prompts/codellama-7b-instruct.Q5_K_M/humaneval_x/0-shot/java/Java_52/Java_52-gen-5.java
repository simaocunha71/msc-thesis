        for(int n : l) {
            if(n > t) {
                return false;
            }
        }
        return true;
    }

    /**
    Return the sum of all the numbers in the list l.
    >>> sumList(Arrays.asList(1, 2, 3, 4, 5))
    15
     */
    public int sumList(List<Integer> l) {
        int sum = 0;
        for(int n : l) {
            sum += n;
        }
        return sum;
    }
}

