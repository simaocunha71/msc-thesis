// First we need to define our array
var a []int

// We need to fill our array
for i := 1; i <= n; i++ {
    a = append(a, i*i-i+1)
}

// We need to find the number of triples
count := 0
for i := 0; i < len(a)-2; i++ {
    for j := i+1; j < len(a)-1; j++ {
        for k := j+1; k < len(a); k++ {
            if (a[i] + a[j] + a[k]) % 3 == 0 {
                count++
            }
        }
    }
}

return count
}

func main() {
n := 5
count := GetMaxTriples(n)
fmt.Println(count) // Output: 1
}

C:

#include <stdio.h>

int GetMaxTriples(int n) {
    int a[n];
    int count = 0;
    for (int i = 1; i <= n; i++) {
        a[i-1] = i*i - i + 1;
    }
    for (int i = 0; i < n-2; i++) {
        for (int j = i+1; j < n-1; j++) {
            for (int k = j+1; k < n; k++) {
                if ((a[i] + a[j] + a[k]) % 3 == 0) {
                    count++;
                }
            }
        }
    }
    return count;
}

int main() {
    int n = 5;
    int count = GetMaxTriples(n);
    printf("%d\n", count); // Output: 1
    return 0;
}

D:

def GetMaxTriples(n):
    a = [i*i - i + 1 for i in range(1, n+1)]
    count = 0
    for i in range(len(a)-2):
        for j in range(i+1, len(a)-1):
            for k in range(j+1, len(a)):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

if __name__ == "__main__":
    n = 5
    count = GetMaxTriples(n)
    print(count) # Output: 1

B:

public class Main