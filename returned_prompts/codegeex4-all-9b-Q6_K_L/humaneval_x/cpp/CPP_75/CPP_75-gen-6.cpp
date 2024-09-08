bool is_multiply_prime(int a)
{
  int count = 0;
  for (int i = 2; i <= a; i++)
  {
    if (a % i == 0)
    {
      count++;
      a = a / i;
      i = 1;
    }
  }
  if (count == 3)
    return true;
  else
    return false;
}

B:
bool is_multiply_prime(int a)
{
  if (a < 2)
    return false;
  int count = 0;
  for (int i = 2; i <= a; i++)
  {
    while (a % i == 0)
    {
      a = a / i;
      count++;
      if (a == 1)
        break;
    }
  }
  if (count == 3)
    return true;
  else
    return false;
}

C:
bool is_multiply_prime(int a)
{
  if (a < 2)
    return false;
  int count = 0;
  for (int i = 2; i <= a; i++)
  {
    if (a % i == 0)
    {
      count++;
      a = a / i;
      if (a == 1)
        break;
    }
  }
  if (count == 3)
    return true;
  else
    return false;
}

D:
bool is_multiply_prime(int a)
{
  if (a < 2)
    return false;
  int count = 0;
  for (int i = 2; i <= a; i++)
  {
    if (a % i == 0)
    {
      count++;
      a = a / i;
      if (a == 1)
        break;
    }
  }
  if (count == 3)
    return true;
  else
    return false;
}

E:
bool is_multiply_prime(int a)
{
  if (a < 2)
    return false;
  int count = 0;
  for (int i = 2; i <= a; i++)
  {
    if (a % i == 0)
    {
      count++;
      a = a / i;
      if (a == 1)
        break;
    }
  }
  if (count == 3)
    return true;
  else
    return false;
}

F:
bool is_multiply_prime(int a)
{
  if (a < 