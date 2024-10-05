        int total = number;
        if(need < remaining) {
            remaining -= need;
            total += need;
        } else {
            total += remaining;
            remaining = 0;
        }
        return Arrays.asList(total, remaining);
     }
}

