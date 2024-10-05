        int maxCount = 0;
        int maxVal = -1;

        for (int num : lst) {
            int count = Collections.frequency(lst, num);
            if (count >= num && num > maxVal) {
                maxCount = count;
                maxVal = num;
            }
        }
        return maxVal;
    }
}

