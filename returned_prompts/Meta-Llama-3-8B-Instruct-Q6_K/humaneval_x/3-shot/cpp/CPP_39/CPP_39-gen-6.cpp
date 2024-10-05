    int a = 0, b = 1;
    for (int i = 1; i < n; i++) {
        int temp = a;
        a = b;
        b = temp + b;
        if (is_prime(b)) {
            return b;
        }
    }
    return -1;  // not found
}

bool is_prime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}
}  // namespace std; // using namespace std;
}  // namespace std; // using namespace std; // namespace std; // using namespace std; // using namespace std;
// namespace std;
// using namespace std; // namespace std;
// using namespace std; // using namespace std; // namespace std; // using namespace std; // using namespace std;
// namespace std;
// using namespace std; // namespace std;
// using namespace std; // using namespace std; // namespace std; // using namespace std; // using namespace std;
// namespace std; // namespace std;
// using namespace std; // namespace std;
// using namespace std; // using namespace std; // namespace std; // using namespace std; // using namespace std;
// namespace std;
// using namespace std; // namespace std;
// using namespace std; // using namespace std; // namespace std; // using namespace std; // using namespace std; // namespace std;
// namespace std; // namespace std;
// using namespace std; // namespace std;
// using namespace std; // using namespace std; // namespace std; // using namespace std; // using namespace std; // namespace std;
// namespace std;
// using namespace std; // namespace std;
// using namespace std; // using namespace std; // namespace std; // using namespace std; // using namespace std; // namespace std;
// namespace std; // namespace std;
// using namespace std; // namespace std;
// using namespace std; // using namespace std; // namespace std; // using namespace std; // using namespace std; // namespace std;
// namespace std; // namespace std;
// using namespace std; // namespace std;
// using namespace std; // using namespace std; // namespace std; // using namespace std; // using namespace std; // namespace std;
// namespace std; // namespace std;
// using namespace std; // namespace