        int smallestEvenValue = Integer.MAX_VALUE;
        int smallestEvenIndex = -1;

        for  (int i = 0; i < arr.size(); i++) {
            int value = arr.get(i);
            if  (value % 2 == 0  &&  value <= smallestEvenValue)  {
                smallestEvenValue = value;
                smallestEvenIndex = i;
            }
        }

        if  (smallestEvenIndex == -1)  {
            return new ArrayList<>();
        }  else  {
            return Arrays.asList(smallestEvenValue, smallestEvenIndex);
        }
    }
}

