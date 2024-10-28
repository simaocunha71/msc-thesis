        int total_eaten = number;
        if(need < remaining){
            remaining -= need;
            total_eaten += need;
        } else {
            total_eaten += remaining;
            remaining = 0;
        }
        return Arrays.asList(total_eaten, remaining);
     }
}

