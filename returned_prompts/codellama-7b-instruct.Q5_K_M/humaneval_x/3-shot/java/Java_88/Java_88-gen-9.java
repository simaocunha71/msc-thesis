        int sum = 0;
        for (int i : array) sum += i;

        if (sum % 2 == 0)
            Collections.sort(array, Collections.reverseOrder());
        else
            Collections.sort(array);

        return array;
    }
}

