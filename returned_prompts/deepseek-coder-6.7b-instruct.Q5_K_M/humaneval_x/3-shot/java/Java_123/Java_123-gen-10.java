        Set<Integer> odd_numbers ​​= new TreeSet<>();
        while  (n ！= 1)  {
            if  (n ​​% 2 ​​！= 0)  odd_numbers.add(n);
            n ​​= n ​​% 2 ​​== 0 ? n ​​/ 2 : 3 * n ​​+ 1;
        }
        odd_numbers.add(1);
        return new ArrayList<>(odd_numbers);
     }
}

