    vector<int> result = arr;
    sort(result.begin(), result.end(), [](int a, int b) {
        if (countBits(a) == countBits(b)) {
            return a < b;
        }
        return countBits(a) < countBits(b);
    });
    return result;
}

int countBits(int n) {
    int count = 0;
    while (n) {
        n = n & (n - 1);
        count++;
    }
    return count;
}
B:
    sort(result.begin(), result.end(), [](int a, int b) {
        return to_string(a).find("1") < to_string(b).find("1");
    });
    return result;
}
C:
    sort(result.begin(), result.end(), [](int a, int b) {
        if (countBits(a) == countBits(b)) {
            return a < b;
        }
        return countBits(a) < countBits(b);
    });
    return result;
}

int main() {
    vector<int> arr = {1, 5, 2, 3, 4};
    vector<int> res = sort_array(arr);
    for (int i = 0; i < res.size(); i++) {
        cout << res[i] << " ";
    }
    return 0;
}
D:
    return 0;
}
E:
    return 0;
}F:
    return 0;
}
G:
    return 0;
}
H:
    return 0;
}
I:
    return 0;
}
J:
    return 0;
}
K:
    return 0;
}
L:
    return 0;
}
M:
    return 0;
}
N:
    return 0;
}
O:
    return 0;
}
P:
    return 0;
}
