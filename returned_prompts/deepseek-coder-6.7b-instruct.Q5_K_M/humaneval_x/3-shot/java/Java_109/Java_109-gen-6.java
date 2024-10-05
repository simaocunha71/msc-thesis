        for(int i=0;i<arr.size()-1;i++)
        {
            if(arr.get(i)>arr.get(i+1))
            {
                return false;
            }
        }
        if(arr.get(arr.size()-1)>arr.get(0))
        {
            return false;
        }
        return true;
    }
}

