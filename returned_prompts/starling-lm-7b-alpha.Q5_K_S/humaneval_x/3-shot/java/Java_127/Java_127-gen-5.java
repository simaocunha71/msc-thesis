        int start = Math.max(interval1.get(0), interval2.get(0));
        int end = Math.min(interval1.get(1), interval2.get(1));
        return (end - start + 1) == 2 || (end - start + 1) == 3 ? "NO" : "YES";
    }
}

