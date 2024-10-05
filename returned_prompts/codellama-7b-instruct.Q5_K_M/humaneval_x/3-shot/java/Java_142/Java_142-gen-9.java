        int sum = 0;
        for (int i = 0; i < lst.size(); i++) {
            int element = lst.get(i);
            if (i % 3 == 0) sum += element * element * element;
            else if (i % 4 == 0) sum += element * element;
            else sum += element;
        }
        return sum;
    }
}

