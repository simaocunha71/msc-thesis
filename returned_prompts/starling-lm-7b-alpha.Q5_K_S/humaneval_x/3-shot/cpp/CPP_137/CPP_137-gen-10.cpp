    if (typeid(a)==typeid(b)){
        if (a==b) return "None";
        if (typeid(a)==typeid(int) && typeid(b)==typeid(float)){
            if (a==(int)b) return "None";
            if (a<(int)b) return a;
            return b;
        }
        if (typeid(a)==typeid(float) && typeid(b)==typeid(int)){
            if ((int)a==b) return "None";
            if ((int)a<b) return (int)a;
            return b;
        }
        if (typeid(a)==typeid(float) && typeid(b)==typeid(float)){
            if (a==b) return "None";
            if (a<b) return a;
            return b;
        }
        if (typeid(a)==typeid(string) && typeid(b)==typeid(string)){
            if (a==b) return "None";
            if (a<b) return a;
            return b;
        }
        if (typeid(a)==typeid(string) && typeid(b)==typeid(int)){
            if (a==string(1,b+'0')) return "None";
            if (a<string(1,b+'0')) return a;
            return string(1,b+'0');
        }
        if (typeid(a)==typeid(int) && typeid(b)==typeid(string)){
            if (a==(int)b[0]) return "None";
            if (a<(int)b[0]) return a;
            return (int)b[0];
        }
    }
    return "None";
}



