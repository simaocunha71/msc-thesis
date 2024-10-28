        int sum = 0;
        for (Object element : lst) {
            if (element instanceof Integer && (int)element % 2 == 1 && (int)element > 0) {
                sum += Math.pow((int)element, 2);
            }
        }
        return sum;
    }
}

