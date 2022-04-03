public class Factorial{

    /**
     * Imperative calculation of n!, where the programmer explicitly 
     * tells the computer what to do via iteration
     * @param n
     * @return result of factorial calculation result
     */
    public int imperativeFactorial(int n){
        int result = 1;
        for (int i = 2; i <= n; i++){
            result *= i;
        }
        return result;
    }

    public static void main(String [] args){

    }
}