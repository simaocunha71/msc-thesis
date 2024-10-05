        List<Integer> result = new ArrayList<>();

        for  (int i = 1; i <= n; i++) {
            if  (i % 2 == 0)  {
                result.add(factorial(i));
            } else  {
                result.add(sumOfNumbers(i));
            }
        }

        return result;
    }

    private int factorial(int num)  {
        int fact = 1;
        for  (int i = 1; i <= num; i++) {
            fact *= i;
        }
        return fact;
    }

    private int sumOfNumbers(int num)  {
        return num * (num + 1) / 2;
    }
}

