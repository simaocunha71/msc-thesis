  for (int i = 0; i < numbers.size() - 1; i++)
    for(int j = i + 1; j < numbers.size(); j++)
      if(abs(numbers[i] - numbers[j]) < threshold)
        return true;
  return false;
}

