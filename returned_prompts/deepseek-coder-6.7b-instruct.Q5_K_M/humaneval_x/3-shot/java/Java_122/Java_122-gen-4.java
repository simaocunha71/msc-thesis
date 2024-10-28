        int sum = 0;
        for  (int i = 0; i < k; i++)  {
            if  (String.valueOf(arr.get(i)).length() <= 2)  {
                sum += arr.get(i);
            }
        }
        return sum;
     }
}

