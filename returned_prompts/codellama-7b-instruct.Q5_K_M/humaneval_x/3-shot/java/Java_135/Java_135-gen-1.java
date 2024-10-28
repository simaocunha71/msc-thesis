        int largest = -1;
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) <= arr.get(i - 1)) largest = i;
        }

        return largest;
    }
}

