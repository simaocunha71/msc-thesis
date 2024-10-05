        int sum = 0;
        for (Object element : lst) {
            if (element instanceof Integer) {
                int num = (Integer) element;
                if (num % 2 != 0) sum += num * num;
            }
        }
        return sum;
    }
}

