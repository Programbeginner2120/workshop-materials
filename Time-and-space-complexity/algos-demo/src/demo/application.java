package demo;

import java.util.Arrays;

public class application {

    public static void main (String [] args){
        int [] myArray = {2, 1, 4,-3};

        int [] rv = sortSearch.mergeSort(myArray);
        System.out.println(Arrays.toString(rv));

        rv = sortSearch.insertionSort(myArray);
        System.out.println(Arrays.toString(rv));

        int len = rv.length;
        int sought_element = sortSearch.binarySearch(rv, 0, len - 1, -3);
        System.out.println(sought_element);
    }
}
