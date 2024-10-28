        int start = Math.max(interval1.get(0), interval2.get(0));
        int end = Math.min(interval1.get(1), interval2.get(1));
        int intersectionLength = end - start;

        if (intersectionLength < 2) 
            return "NO";

        for (int i = 2; i * i <= intersectionLength; i++) 
            if (intersectionLength % i == 0) 
                return "NO";

        return "YES";
    }
}

