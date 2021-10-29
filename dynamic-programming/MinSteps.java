import java.util.Arrays;

public class MinSteps {

    public static void main(String [] args){
        int n = 1000000;
        int [] memo = new int [n+1];
//        int res = MinSteps.getMinStepsMemo(n, memo);
        int res = MinSteps.getMinStepsTab(n);
        System.out.println(res);
    }

    static int getMinSteps(int n){  //naive recursive approach
        if (n == 1)
            return 0;

        int res = getMinSteps(n - 1);
        if (n % 2 == 0)
            res = Math.min(getMinSteps(n / 2), res);
        if (n % 3 == 0)
            res = Math.min(getMinSteps(n / 3), res);

        return res + 1;
    }

    static int getMinStepsMemo(int n, int [] memo){  //dp solution using Memoization
        if (n == 1)
            return 0;

        if (memo[n] != 0)
            return memo[n];

        int res = getMinStepsMemo(n - 1, memo);
        if (n % 3 == 0)
            res = Math.min(getMinStepsMemo(n / 3, memo), res);
        if (n % 2 == 0)
            res = Math.min(getMinStepsMemo(n / 2, memo), res);

        memo[n] = res + 1;
        return memo[n];
    }

    static int getMinStepsTab(int n){ //dp solution using Tabulation
        int [] table = new int[n+1];
        Arrays.fill(table, n);

        table[1] = 0;

        for(int i = 1; i < n; i++){
            table[i+1] = Math.min(table[i] + 1, table[i+1]);
            if (i*2 <= n)
                table[i*2] = Math.min(table[i] + 1, table[i*2]);
            if (i*3 <= n)
                table[i*3] = Math.min(table[i] + 1, table[i*3]);
        }

        return table[n];
    }

}
