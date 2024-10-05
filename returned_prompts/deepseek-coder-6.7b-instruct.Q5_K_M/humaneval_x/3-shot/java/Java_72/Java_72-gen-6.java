        int sum = 0;
        for(int i : q) sum += i;
        if(sum > w) return false;

        int l = 0, r = q.size() - 1;
        while(l <= r) {
            if(q.get(l) != q.get(r)) return false;
            l++;
            r--;
        }

        return true;
     }
}

