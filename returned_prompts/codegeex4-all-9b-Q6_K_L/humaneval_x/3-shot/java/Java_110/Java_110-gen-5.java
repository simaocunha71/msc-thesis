        int oddCount = 0;
        for (int i : lst1) {
            if (i % 2 != 0) oddCount++;
        }
        for (int i : lst2) {
            if (i % 2 == 0) oddCount--;
        }
        return oddCount > 0 ? "NO" : "YES";
    }
}

