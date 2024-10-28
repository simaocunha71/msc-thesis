        int odd_count = 0;
        for (Integer num : lst1) {
            if (num % 2 != 0) odd_count++;
        }
        if (odd_count > lst2.size()) return "NO";
        return "YES";
    }
}

