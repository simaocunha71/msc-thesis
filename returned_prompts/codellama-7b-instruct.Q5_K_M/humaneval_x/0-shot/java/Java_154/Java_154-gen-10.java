        if(a == null || b == null)
            return false;
        if(a.length() < b.length())
            return false;
        if(a.equals(b))
            return true;
        int i = 0;
        while(i < b.length())
        {
            if(a.contains(b.substring(i)))
                return true;
            i++;
        }
        return false;
    }
}
