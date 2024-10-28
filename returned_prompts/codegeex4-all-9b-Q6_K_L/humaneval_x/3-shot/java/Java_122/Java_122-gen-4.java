        int sum = 0;
        for (int i = 0; i < Math.min(k, arr.size()); i++) {
            int element = arr.get(i);
            if (element < 10) {
                sum += element;
            } else if (element < 100) {
                sum += element % 10;
            }
        }
        return sum;
    }
}

