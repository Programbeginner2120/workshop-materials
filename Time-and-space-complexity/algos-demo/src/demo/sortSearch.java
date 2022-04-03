package demo;

import java.util.Arrays;

public class sortSearch {

    // Time complexity: O(n^2)
    // Space complexity: O(1)
    public static int [] insertionSort(int [] arr){  // size n recurrence
        for (int i = 1; i < arr.length; i++){
            int curr = arr[i];
            int j = i;
            while (j != 0 && arr[j - 1] > curr){
                arr[j] = arr[j - 1];
                j--;
            }
            arr[j] = curr;
        }
        return arr;
    }

    public static int [] merge(int [] left, int [] right){
        int i = 0;
        int j = 0;
        int idx = 0;
        int [] returnArray = new int [(left.length + right.length)];
        while (i < left.length && j < right.length){
            if (left[i] <= right[j]){
                returnArray[idx] = left[i];
                i++;
            }
            else{
                returnArray[idx] = right[j];
                j++;
            }
            idx++;
        }

        int [] arrayRemains = j < i ? right : left;
        int remainderIndex = j < i ? j : i;
        for (int k = remainderIndex; k < arrayRemains.length; k++){
            returnArray[idx] = arrayRemains[k];
            idx++;
        }

        return returnArray;
    }

    // Time complexity: O(nlogn)
    // Space complexity: O(n)
    public static int [] mergeSort(int [] arr){
        if (arr.length <= 1)
            return  arr;

        int midpoint = arr.length / 2;
        int [] left = mergeSort(Arrays.copyOf(arr, midpoint));
        int [] right = mergeSort(Arrays.copyOfRange(arr, midpoint, arr.length));

        return merge(left, right);
    }

    // Time complexity: O(logn)
    // Space complexity: O(1)
    public static int binarySearch(int arr[], int l, int r, int x)
    {
        if (r >= l) {
            int mid = l + (r - l) / 2;

            // If the element is present at the
            // middle itself
            if (arr[mid] == x)
                return mid;

            // If element is smaller than mid, then
            // it can only be present in left subarray
            if (arr[mid] > x)
                return binarySearch(arr, l, mid - 1, x);

            // Else the element can only be present
            // in right subarray
            return binarySearch(arr, mid + 1, r, x);
        }

        // We reach here when element is not present
        // in array
        return -1;
    }

}
