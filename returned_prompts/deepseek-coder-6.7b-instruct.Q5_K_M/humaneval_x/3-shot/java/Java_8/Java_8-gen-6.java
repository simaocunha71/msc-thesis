        int sum = 0;
        int product = 1;
        for(Integer number : numbers) {
            sum += number;
            product *= number;
        }
        return Arrays.asList(sum, product);
     }
}

