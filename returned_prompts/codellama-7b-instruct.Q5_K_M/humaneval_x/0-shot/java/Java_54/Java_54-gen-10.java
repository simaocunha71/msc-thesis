        for(int i=0;i<s0.length();i++)
        {
            for(int j=0;j<s1.length();j++)
            {
                if(s0.charAt(i)==s1.charAt(j))
                {
                    continue A;
                }
            }
            return false;
        }
        return true;
    }
}

