public class fibTest{

public static int normalRecFib(int fibNum){  // Normal old recursive fibonnaci
  if (fibNum <= 1)
    return 1;
  return normalRecFib(fibNum - 2) + normalRecFib(fibNum - 1);
}

public static int normalIterFib(int fibNum){  //Normal iterative fibonnaci

  if (fibNum <= 1)
    return 1;

  int prev = 1;
  int curr = 1;
  int result = prev + curr;
  for (int i = 0; i < fibNum - 2; i++){
    int temp = curr;
    curr = result;
    prev = temp;
    result = prev + curr;
  }

  return result;
}

public static int recFib(int fibNum){  // Recursive fibonnaci utilizing memoization i.e. dynamic programming approach
    int [] fibArr = new int [fibNum + 1];

    // 1,1,2,3,4,5,8

    if (fibNum <= 1)
        return 1;

    if (fibArr[fibNum] == 0){
        if (fibArr[fibNum - 2] == 0)
            fibArr[fibNum - 2] = recFib(fibNum - 2);
        if (fibArr[fibNum - 1] == 0)
            fibArr[fibNum - 1] = recFib(fibNum - 1);
        fibArr[fibNum] = fibArr[fibNum - 2] + fibArr[fibNum - 1];
    }

    return fibArr[fibNum];
}

public static int iterFib(int fibNum){  // Iterative fibonnaci utilizing memoization i.e. dynamic programming approach
    int [] fibArr = new int[fibNum + 1];
    fibArr[0] = 1;
    fibArr[1] = 1;  //1,1,2,3,5,8.....

    for (int i = 2; i <= fibNum; i++)
        fibArr[i] = fibArr[i-2] + fibArr[i-1];

    return fibArr[fibNum];
}

public static void main(String[] args) {
  int fibNum = 10000000;

  long start = System.currentTimeMillis();
  // int res = fibTest.iterFib(fibNum);
//  int res = fibTest.normalRecFib(fibNum);
//  System.out.println(fibTest.recFib(fibNum));
    int res = fibTest.iterFib(fibNum);
   System.out.println(fibTest.iterFib(fibNum));
  long finish = System.currentTimeMillis();

  long timeElapsed = finish - start;

  System.out.println("Fibonacci Number: " + res);
  System.out.println("Time Elapsed in milliseconds: " + timeElapsed);

  }

}
