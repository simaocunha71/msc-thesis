        ArrayList<Integer> evenNum = new ArrayList<>();
        if(a > b){
            int temp = a;
            a = b;
            b = temp;
        }
        for(int i = a; i <= b; i++){
            if(i % 2 == 0){
                evenNum.add(i);
            }
        }
        return evenNum;
    }
}

This program will return the even digits between a and b in ascending order. If the user inputs the numbers in reverse order, the program will still work and return the even numbers in the right order.
If there are no even numbers between a and b, it will return an empty list.

