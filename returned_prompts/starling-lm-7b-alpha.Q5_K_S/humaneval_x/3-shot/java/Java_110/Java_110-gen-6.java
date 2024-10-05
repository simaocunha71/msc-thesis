        int count_odd_one = 0;
        int count_odd_two = 0;
        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 == 1) count_odd_one += 1;
        }
        for (int i = 0; i < lst2.size(); i++) {
            if (lst2.get(i) % 2 == 1) count_odd_two += 1;
        }
        return count_odd_one <= count_odd_two ? "YES" : "NO";
    }
}


