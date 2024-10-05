        if(remaining >= need) {
            return Arrays.asList(number + need, 0);
        } else {
            return Arrays.asList(number + remaining, remaining - need);
        }

     }
 }

