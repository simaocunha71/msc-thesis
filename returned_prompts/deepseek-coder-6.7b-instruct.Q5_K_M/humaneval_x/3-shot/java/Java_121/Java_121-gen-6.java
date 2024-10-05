        int sum = 0;
        for  (int  i  in  range(0, lst.size(), 2)) {
            if  (lst.get(i) % 2 != 0) sum += lst.get(i);
        }
        return sum;
    }
}

