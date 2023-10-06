#!/bin/bash

#comando de teste 
# sudo ../rapl_tests/rapl_c_function/RAPL/main "./main -m models/llama-2-7b.Q2_K.gguf -p \"Building a website can be done in 3 simple steps:\nStep 1:\"" 1 1 "Building a website"

cd RAPL/
make 
cd ../../../llama_cpp/

# SETUP SCRIPT
N_TIMES=1
N_TOKENS=124
models=(
    "models/llama-2-7b.Q2_K.gguf"
)

#CORRIGIR
prompts_to_test=(
    "\nFIX = \"\"\"\nAdd more test cases.\n\"\"\"\n\ndef vowels_count(s):\n    \"\"\"Write a function vowels_count which takes a string representing\n    a word as input and returns the number of vowels in the string.\n    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a\n    vowel, but only when it is at the end of the given word.\n\n    Example:\n    \>\>\> vowels_count(\"abcde\")\n    2\n    \>\>\> vowels_count(\"ACEDY\")\n    3\n    \"\"\"\n"
    "\ndef by_length(arr):\n    \"\"\"\n    Given an array of integers, sort the integers that are between 1 and 9 inclusive,\n    reverse the resulting array, and then replace each digit by its corresponding name from\n    \"One\", \"Two\", \"Three\", \"Four\", \"Five\", \"Six\", \"Seven\", \"Eight\", \"Nine\".\n\n    For example:\n      arr = [2, 1, 1, 4, 5, 8, 2, 3]   \n            -\> sort arr -\> [1, 1, 2, 2, 3, 4, 5, 8] \n            -\> reverse arr -\> [8, 5, 4, 3, 2, 2, 1, 1]\n      return [\"Eight\", \"Five\", \"Four\", \"Three\", \"Two\", \"Two\", \"One\", \"One\"]\n    \n      If the array is empty, return an empty array:\n      arr = []\n      return []\n    \n      If the array has any strange number ignore it:\n      arr = [1, -1 , 55] \n            -\> sort arr -\> [-1, 1, 55]\n            -\> reverse arr -\> [55, 1, -1]\n      return = ['One']\n    \"\"\"\n"
    "\ndef sort_array(arr):\n    \"\"\"\n    In this Kata, you have to sort an array of non-negative integers according to\n    number of ones in their binary representation in ascending order.\n    For similar number of ones, sort based on decimal value.\n\n    It must be implemented like this:\n    \>\>\> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]\n    \>\>\> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]\n    \>\>\> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]\n    \"\"\"\n"
    "\ndef sorted_list_sum(lst):\n    \"\"\"Write a function that accepts a list of strings as a parameter,\n    deletes the strings that have odd lengths from it,\n    and returns the resulted list with a sorted order,\n    The list is always a list of strings and never an array of numbers,\n    and it may contain duplicates.\n    The order of the list should be ascending by length of each word, and you\n    should return the list sorted by that rule.\n    If two words have the same length, sort the list alphabetically.\n    The function should return a list of strings in sorted order.\n    You may assume that all words will have the same length.\n    For example:\n    assert list_sort([\"aa\", \"a\", \"aaa\"]) =\> [\"aa\"]\n    assert list_sort([\"ab\", \"a\", \"aaa\", \"cd\"]) =\> [\"ab\", \"cd\"]\n    \"\"\"\n"
    "\ndef generate_integers(a, b, cycle_number):\n    \"\"\"\n    Given two positive integers a and b, return the even digits between a\n    and b, in ascending order.\n\n    For example:\n    generate_integers(2, 8, $cycle_number) =\> [2, 4, 6, 8, $cycle_number]\n    generate_integers(8, 2, $cycle_number) =\> [2, 4, 6, 8, $cycle_number]\n    generate_integers(10, 14, $cycle_number) =\> [0, $cycle_number]\n    \"\"\"\n"
)

prompts=(
    "Building a website can be done in 2 simple steps:\nStep 1:"
    "Building a block can be done in 3 simple steps:\nStep 1:"
    "Building a brick can be done in 4 simple steps:\nStep 1:"
    "Building a hammer can be done in 5 simple steps:\nStep 1:"
    "Building a construction can be done in 6 simple steps:\nStep 1:"
)


for model in "${models[@]}"; do
    for prompt in "${prompts[@]}"; do
        TAG=$(echo "$prompt" | sed 's/^"//;s/"$//' | awk '{printf "%s_%s_%s", $1, $2, $3}') # Nome da execução que vai para o CSV - serve de argumento da função main do RAPL
        sudo ../rapl_tests/rapl_c_function/RAPL/main "./main -m $model -p \"$prompt\" -n $N_TOKENS -e" $N_TIMES "$TAG"
        # sudo ../rapl_tests/rapl_c_function/RAPL/main "make -j && ./main -m $model -p $prompt -n $N_TOKENS -e" $N_TIMES
        echo "$(cat ${TAG}.J)" >> ../rapl_tests/rapl_c_function/result_rapl_c.csv
    done
done

sudo rm *.J *.log

cd ../rapl_tests/rapl_c_function/RAPL/
make clean
cd ..

awk -F',' '!seen[$1, $2, $3, $4, $5, $6]++' result_rapl_c.csv > temp && mv temp result_rapl_c.csv

