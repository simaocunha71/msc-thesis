        return a.contains(b) ||
                a.contains(new StringBuilder(b).reverse().toString()) ||
                a.contains(new StringBuilder(b).reverse().toString().substring(1)) ||
                a.contains(new StringBuilder(b).reverse().toString().substring(2)) ||
                a.contains(new StringBuilder(b).reverse().toString().substring(3)) ||
                a.contains(new StringBuilder(b).reverse().toString().substring(4)) ||
                a.contains(new StringBuilder(b).reverse().toString().substring(5)) ||
                a.contains(new StringBuilder(b).reverse().toString().substring(6)) ||
                a.contains(new StringBuilder(b).reverse().toString().substring(7)) ||
                a.contains(new StringBuilder(b).reverse().toString().substring(8)) ||
                a.contains(new StringBuilder(b).reverse().toString().substring(9)) ||
                a.contains(new StringBuilder(b).reverse().toString().substring(10));
    }
}

























