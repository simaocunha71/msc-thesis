        int total = number;
        if  (remaining >= need)  {
            total += need;
            remaining -= need;
        }
        else  {
            total += remaining;
            remaining = 0;
        }
        return Arrays.asList(total, remaining);
     }
}

