        class Strength{
            String name;
            int cap;
            int sm;
            int strength;
            public Strength(String name, int cap, int sm, int strength){
                this.name = name;
                this.cap = cap;
                this.sm = sm;
                this.strength = strength;
            }
            public String toString(){
                return "Name: "+this.name+"\nCap: "+this.cap+"\nSm: "+this.sm+"\nStrength: "+this.strength+"\n";
            }
        }
        List<Strength> strengths = new ArrayList<Strength>();
        for(String extension : extensions)
        {
            int cap = 0, sm = 0;
            for(int i = 0; i < extension.length(); i++)
            {
                if(extension.charAt(i) >= 'A' && extension.charAt(i) <= 'Z')
                    cap++;
                else
                    sm++;
            }
            int strength = cap - sm;
            Strength s = new Strength(extension, cap, sm, strength);
            strengths.add(s);
        }
        Collections.sort(strengths, new Comparator<Strength>(){
            public int compare(Strength s1, Strength s2){
                if(s1.strength == s2.strength)
                    return s1.name.compareTo(s2.name);
                else
                    return s2.strength - s1.strength;
            }
        });
        return class_name + "." + strengths.get(0).name;
    }

}