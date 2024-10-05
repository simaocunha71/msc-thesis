        if(interval1.size()!=2 || interval2.size()!=2)
            return "NO";
        if(interval1.get(1)<interval2.get(0) || interval1.get(0)>interval2.get(1))
            return "NO";
        if(interval1.get(0)<=interval2.get(0) && interval1.get(1)>=interval2.get(1))
            return "YES";
        if(interval1.get(0)>interval2.get(0) && interval1.get(1)<interval2.get(1))
            return "NO";
        if(interval1.get(0)>=interval2.get(0) && interval1.get(1)<=interval2.get(1))
            return "YES";
        if(interval1.get(0)<interval2.get(0) && interval1.get(1)>interval2.get(1))
            return "NO";
        return "YES";
    }
}

