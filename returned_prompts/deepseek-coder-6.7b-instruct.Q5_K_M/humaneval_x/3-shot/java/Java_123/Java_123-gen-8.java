        Set<Integer> oddNumbers = new TreeSet<>();
        while  (n  != 1)  {
            if  (n  % 2  !=  0)  {
                oddNumbers.add(n);
            }
            n  =  n  %  2  ==  0  ?  n  /  2  :  3  *  n  +  1;
        }
        oddNumbers.add(1);
        return new ArrayList<>(oddNumbers);
     }
}

