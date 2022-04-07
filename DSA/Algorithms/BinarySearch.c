#include <stdio.h>
#include <stdlib.h>




int binarySearch(int arr[], int arrLEN, int target){
    int start = 0, end = arrLEN-1, mid;
    while (start <= end){
        mid = (start + end) / 2;
        if (target == arr[mid]){
            return 1;
        }
        else if (target < arr[mid]){
            end = mid-1;
        }
        else{
            start = mid+1;
        }
    }
    return 0;
}


int main(){
    int arr[] = {1, 2, 3, 4, 5};
    int len = (int) sizeof(arr)/sizeof(arr[0]);
    printf("%i", binarySearch(arr, len, 10));
    return 0;
}
