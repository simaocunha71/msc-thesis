        int sum = 0;
        for (int i = 0; i < k; i++) {
            int element = arr.get(i);
            while (element > 9) {
                element /= 10;
            }
            sum += element;
        }
        return sum;
    }
}

