        int count = 0;
        for (int i = 0; i < arr.size(); i++) {
            int sum = 0;
            for (int j = i; j < arr.size(); j++) {
                sum += arr.get(j);
                if (sum > 0) count++;
            }
        }
        return count;
    }
}

