        if (q.size() % 2 == 0) {
            int sum = 0;
            for (Integer i : q) {
                sum += i;
            }
            return sum <= w;
        }
        return false;
    }
}

