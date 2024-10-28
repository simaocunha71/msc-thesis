        int count = 0;

        for(int num : nums)  {
            if(num > 10 && 
               Math.abs(num) % 10 % 2 == 1 && 
               num / 10 % 2 == 1) 
            count++;
        }

        return count;
     }
}

