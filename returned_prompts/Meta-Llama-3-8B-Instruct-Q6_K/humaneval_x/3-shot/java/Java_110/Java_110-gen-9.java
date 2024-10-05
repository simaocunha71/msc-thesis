        int even_count = 0;
        for (int num : lst1) {
            if (num % 2 == 0) even_count++;
        }
        if (even_count == lst1.size()) return "YES";
        return "NO";
    }
}

