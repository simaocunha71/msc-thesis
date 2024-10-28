        int sum = 0;
        for(Double num : lst){
            sum += Math.ceil(num)*Math.ceil(num);
        }
        return sum;
    }
}



A: The problem statement is asking to round each element in the list to the upper integer first,