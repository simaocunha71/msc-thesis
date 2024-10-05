        int evenCount = 0;
        for (int num : lst1) {
            if (num % 2 == 0) evenCount++;
        }

        if (evenCount == lst1.size()) return "YES";
        else {
            for (int num : lst2) {
                if (num % 2 == 0) {
                    lst1.add(num);
                    lst2.remove(num);
                    return exchange(lst1, lst2);
                }
            }
        }
        return "NO";
    }
}

