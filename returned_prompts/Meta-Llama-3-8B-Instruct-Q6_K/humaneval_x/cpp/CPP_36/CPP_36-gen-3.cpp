    int count = 0;
    for(int i = 1; i < n; i++) {
        if(i % 11 == 0 || i % 13 == 0) {
            while(i > 0) {
                if(i % 10 == 7) {
                    count++;
                    i /= 10;
                } else {
                    i /= 10;
                }
            }
        }
    }
    return count;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", fizz_buzz(n));
    return 0;
}

B:
def fizz_buzz(n):
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            while i > 0:
                if i % 10 == 7:
                    count += 1
                    i //= 10
                else:
                    i //= 10
    return count

print(fizz_buzz(50))
print(fizz_buzz(78))
print(fizz_buzz(79))
C:
#include <iostream>
using namespace std;
int fizz_buzz(int n) {
    int count = 0;
    for(int i = 1; i < n; i++) {
        if(i % 11 == 0 || i % 13 == 0) {
            while(i > 0) {
                if(i % 10 == 7) {
                    count++;
                    i /= 10;
                } else {
                    i /= 10;
                }
            }
        }
    }
    return count;
}

int main() {
    int n;
    cin >> n;
    cout << fizz_buzz(n) << endl;
    return 0;
}
D:
let fizz_buzz n =
  let count = ref 0 in
  for i = 1 to (n - 1) do
    if i mod 11 = 0 || i mod 13 = 0 then
      let rec helper i =
        if i = 0 then ()
        else (
          if i mod 10 = 7 then
            (count := !count + 1; helper (i / 10))
          else
            helper (i / 10)
        )
      in
      helper i
  done;
  !count

let () =
  printf "%d\n" (fizz_buzz 50