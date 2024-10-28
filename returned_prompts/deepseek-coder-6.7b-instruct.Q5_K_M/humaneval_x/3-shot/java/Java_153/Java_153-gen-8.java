        String strongest_extension = "";
        double max_strength = - Double.MAX_VALUE;

        for  (String extension : extensions)  {
            int cap_count = 0;
            int sm_count = 0;
            for  (char c : extension.toCharArray())  {
                if  (Character.isUpperCase(c)) cap_count+=1;
                if  (Character.isLowerCase(c)) sm_count+=1;
            }
            double strength = (double)cap_count - sm_count;
            if  (strength > max_strength)  {
                max_strength = strength;
                strongest_extension = extension;
            }
        }
        return class_name + '.' + strongest_extension;
    }
}

