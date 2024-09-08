int i = 0;
int j = 0;
int k = 0;
int m = 0;
int n = 0;
for (i = 1; i < n; i++) {
  for (j = 2; j <= i / 2; j++) {
    if (i % j == 0) {
      break;
    }
  }
  if (j > i / 2) {
    k = i;
    m = k;
  }
}
printf("%d", m);
