        int min_even_value = Integer.MAX_VALUE;
        int min_even_index = -1;

        for  (int i = 0; i < arr.size(); i++)  {
            int value = arr.get(i);
            if  (value % 2 == 0  &&  value < min_even_value)  {
                min_even_value = value;
                min_even_index = i;
            }
        }

        if  (min_even_index == -1)  {
            return new ArrayList<>();
        }  else  {
            return Arrays.asList(min_even_value, min_even_index);
        }
     }
}

