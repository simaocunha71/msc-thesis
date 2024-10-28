        int odd_count1 = 0, odd_count2 = 0;
        for (int i : lst1) if (i % 2 != 0) odd_count1++;
        for (int i : lst2) if (i % 2 != 0) odd_count2++;

        if (odd_count1 > 0 && odd_count2 > 0) return "NO";
        if (odd_count1 == 0) return "YES";
        else return "NO";
    }
}

