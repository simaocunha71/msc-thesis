        List<Integer> result = new ArrayList<>();
        for  (int i = 1; i <= n; i++) {
            if  (i % 2 == 0)  {
                result.add(factorial(i));
            }  else  {
                result.add(summation(i));
            }
        }
        return result;
    }

    private int factorial(int n)  {
        int result = 1;
        for  (int i = 1; i <= n; i++)  {
            result *= i;
        }
        return result;
    }

    private int summation(int n)  {
        int result = 0;
        for  (int i = 1; i <= n; i++)  {
            result += i;
        }
        return result;
    }
}

