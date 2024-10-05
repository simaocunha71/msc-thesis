        if (dict.size() == 0) return false;
        Collection<Object> values = dict.values();
        Iterator<Object> iterator = values.iterator();
        char prev_char = ' ';
        while (iterator.hasNext()) {
            Object next = iterator.next();
            if (next instanceof String) {
                char curr_char = ((String)next).charAt(0);
                if (prev_char != ' ' && prev_char != curr_char) return false;
                prev_char = curr_char;
            } else {
                return false;
            }
        }
        return true;
    }
}


class A {
    int a;
    public A(int a) {
        this.a = a;
    }
    public int get_a() {
        return a;
    }
    public void set_a(int a) {
        this.a = a;
    }
}

class B {
    int b;
    public B(int b) {
        this.b = b;
    }
    public int get_b() {
        return b;
    }
    public void set_b(int b) {
        this.b = b;
    }
}

class C {
    int c;
    public C(int c) {
        this.c = c;
    }
    public int get_c() {
        return c;
    }
    public void set_c(int c) {
        this.c = c;
    }
}

class D {
    int d;
    public D(int d) {
        this.d = d;
    }
    public int get_d() {
        return d;
    }
    public void set_d(int d) {
        this.d = d;
    }
}

class E {
    int e;
    public E(int e) {
        this.e = e;
    }
    public int get_e() {
        return e;
    }
    public void set_e(int e) {
        this.e = e;