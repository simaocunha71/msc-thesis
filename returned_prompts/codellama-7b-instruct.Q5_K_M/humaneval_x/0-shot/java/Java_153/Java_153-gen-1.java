        int strongest = 0;
        String strongest_extension = "";
        String class_name_lower = class_name.toLowerCase();
        for(String extension : extensions)
        {
            int count_upper = 0;
            int count_lower = 0;
            for(int i = 0; i < extension.length(); i++)
            {
                if(Character.isUpperCase(extension.charAt(i)))
                {
                    count_upper++;
                }
                else if(Character.isLowerCase(extension.charAt(i)))
                {
                    count_lower++;
                }
            }
            int strength = count_upper - count_lower;
            if(strength > strongest)
            {
                strongest = strength;
                strongest_extension = extension;
            }
            else if(strength == strongest && class_name_lower.contains(extension.toLowerCase()))
            {
                strongest_extension = extension;
            }
        }
        return class_name + "." + strongest_extension;
    }
}



