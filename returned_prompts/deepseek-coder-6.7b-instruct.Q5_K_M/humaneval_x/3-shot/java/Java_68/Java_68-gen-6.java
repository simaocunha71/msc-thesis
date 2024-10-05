        if (arr.isEmpty())  return new ArrayList<>();

        int min_even = Integer.MAX_VALUE;
        int min_even_index = -1;

        for (int i = 0; i < arr.size(); i++)  {
            if (arr.get(i) < min_even && arr.get(i) % 2 == 0)  {
                min_even = arr.get(i);
                min_even_index = i;
            }
        }

        if (min_even_index == -1)  return new ArrayList<>();

        return Arrays.asList(min_even, min_even_index);
    }
}

