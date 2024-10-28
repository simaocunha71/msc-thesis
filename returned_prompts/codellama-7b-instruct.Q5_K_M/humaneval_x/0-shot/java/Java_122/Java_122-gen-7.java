        int count = 0;
        int sum = 0;
        int digit = 0;

        // check if k is valid
        if (k > arr.size())
            return sum;

        // loop through the array, up to k elements
        for (int i = 0; i < k; i++) {
            int num = arr.get(i);

            // check if the number is less than 10
            if (num < 10)
                count++;
            else
                digit++;

            sum += num;
        }

        // check if there are more than 1 digit
        if (digit > 1)
            return sum;

        // check if there are less than 2 digits
        if (count < 2)
            return sum;

        // check if there are 2 digits
        if (count == 2)
            return sum - arr.get(k-1);

        return sum;
    }

    public static void main(String[] args) {
        List<Integer> arr = new ArrayList<Integer>();
        arr.add(111);
        arr.add(21);
        arr.add(3);
        arr.add(4000);
        arr.add(5);
        arr.add(6);
        arr.add(7);
        arr.add(8);
        arr.add(9);

        Solution s = new Solution();
        System.out.println(s.addElements(arr, 4));
    }
}
