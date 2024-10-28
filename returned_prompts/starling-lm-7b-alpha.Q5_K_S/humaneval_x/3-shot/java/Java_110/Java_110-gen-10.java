        int odd_count = 0;
        for (int x : lst1) {
            if (x % 2 != 0) odd_count += 1;
        }
        if (odd_count == 0) return "YES";
        for (int x : lst2) {
            if (x % 2 != 0) {
                lst1.set(odd_count - 1, x);
                odd_count -= 1;
                if (odd_count == 0) return "YES";
            }
        }
        return "NO";
    }
}


```