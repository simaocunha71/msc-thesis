def largest_subset(lst):
   n = len(lst)
   if n < 2: return n
   lst.sort()
   cnt = [1]*n
   res = 1
   for i in range(1, n):
      for j in range(i):
         if lst[i] % lst[j] == 0:
            cnt[i] = max(cnt[i], cnt[j] + 1)
      res = max(res, cnt[i])
   return res