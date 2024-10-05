        int total_eaten  ;
        if(need <= remaining) {
            total_eaten  = number + need;
            remaining -= need;
        } else {
            total_eaten  = number + remaining;
            remaining = 0;
        }
        return Arrays.asList(total_eaten , remaining);

     }
}

