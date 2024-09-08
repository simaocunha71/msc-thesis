    sort(arr.begin(), arr.end(), 
         [](int a, int b) {
            int countA = __builtin_popcountll(a);
            int countB = __builtin_popcountll(b);
            if(countA == countB) return a < b;
            return countA < countB;
        }
    );
    return arr;
}

B:
    sort(arr.begin(), arr.end(), 
         [](int a, int b) {
            int countA = __builtin_popcount(a);
            int countB = __builtin_popcount(b);
            if(countA == countB) return a < b;
            return countA < countB;
        }
    );
    return arr;
}

C:
    sort(arr.begin(), arr.end(), 
         [](int a, int b) {
            int countA = __builtin_popcount(a);
            int countB = __builtin_popcount(b);
            if(countA == countB) return a < b;
            return countA < countB;
        }
    );
    return arr;
}

D:
    sort(arr.begin(), arr.end(), 
         [](int a, int b) {
            int countA = __builtin_popcount(a);
            int countB = __builtin_popcount(b);
            if(countA == countB) return a < b;
            return countA < countB;
        }
    );
    return arr;
}

E:
    sort(arr.begin(), arr.end(), 
         [](int a, int b) {
            int countA = __builtin_popcount(a);
            int countB = __builtin_popcount(b);
            if(countA == countB) return a < b;
            return countA < countB;
        }
    );
    return arr;
}

F:
    sort(arr.begin(), arr.end(), 
         [](int a, int b) {
            int countA = __builtin_popcount(a);
            int countB = __builtin_popcount(b);
            if(countA == countB) return a < b;
            return countA < countB;
        }
    );
    return arr;
}

G:
    sort(arr.begin(), arr.end(), 
         [](int a, int b) {
            int countA = __builtin_popcount(a);
            int countB = __builtin_popcount(b);
            if(countA == countB) return a < b;
            return countA < countB;
        }
    );
    return arr;
}

H:
    sort(arr.begin(), arr