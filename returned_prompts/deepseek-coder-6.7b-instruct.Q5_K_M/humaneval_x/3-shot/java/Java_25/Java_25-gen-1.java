        List<Integer> factors = new ArrayList<>();
        for  (int i = 2; i <= n; i++) {
            while  (n % i == 0)  {
                factors.add(i);
                n /= i;
             }
         }
        return factors;
     }
}

