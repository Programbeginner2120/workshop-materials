#include <stdio.h>
#include <time.h>

int normalRecursiveFibonacci(int fibNum){
  if (fibNum <= 1)
    return 1;

  return normalRecursiveFibonacci(fibNum - 2) + normalRecursiveFibonacci(fibNum - 1);
}

// long dynamicRecursiveFibonnaci(int fibNum){
//   long fibArr [fibNum];
//
//   for (int i = 0; i < fibNum; i++)
//     fibArr[i] = 0;
//
//   if (fibNum <= 1)
//     return 1;
//
//   if (fibArr[fibNum] == 0){
//     if (fibArr[fibNum - 2] == 0)
//       fibArr[fibNum - 2] = dynamicRecursiveFibonnaci(fibNum - 2);
//     if (fibArr[fibNum - 1] == 0)
//       fibArr[fibNum - 1] = dynamicRecursiveFibonnaci(fibNum - 1);
//     fibArr[fibNum] = fibArr[fibNum - 2] + fibArr[fibNum - 1];
//   }
//
//   return fibArr[fibNum];
// }

int dynamicIterativeFibonnaci(int fibNum){
  long fibArr [fibNum + 1];
  fibArr [0] = 1;
  fibArr [1] = 1;

  for (int i = 2; i <= fibNum; i++)
    fibArr[i] = fibArr[i-2] + fibArr[i-1];

  return fibArr[fibNum];
}

int main (int argc, char * argv []){

  int fibNum = 100;

  // 1, 1, 2, 3, 5, 8, 13,...

  clock_t start, end;
  //
  // start = clock();
  // long temp = normalRecursiveFibonacci(45);
  // end = clock();
  // double cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;  // converts to seconds
  // printf("Fibonacci Number: %ld\nTime taken in seconds: %lf\n", temp, cpu_time_used);


  // long iterativeRes = dynamicIterativeFibonnaci(4);
  // printf("%ld\n", iterativeRes);

  start = clock();
  // int res = normalRecursiveFibonacci(fibNum);
  int res = dynamicIterativeFibonnaci(fibNum);
  end = clock();
  double cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;  // converts to seconds
  printf("Fibonacci Number: %d\nTime taken in seconds: %f\n", res, cpu_time_used);


  return 0;

}
