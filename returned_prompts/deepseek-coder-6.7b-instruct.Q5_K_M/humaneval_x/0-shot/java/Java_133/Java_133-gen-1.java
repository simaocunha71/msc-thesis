        int sum = 0;
        for (Double num : lst) {
            sum += Math.pow(Math.ceil(num), 2);
        }
        return sum;
    }

}

The solution is to iterate over each number in the list, round it up to the nearest integer using the ceil method from the Math class, then square that number using the pow method from the Math class. The result is then added to the sum which is returned at the end.
*/

/*
