#include <stdio.h>
#include <stdarg.h>




int *arrDS(int size, ...){
    int *first_element;
    va_list valist;
    va_start(valist, size);
    for (int i=0; i<size; i++){
        *(first_element + i) = va_arg(valist, int);
    }
    va_end(valist);
    return first_element;
}



int main(){
    int *my_arr = arrDS(4, 1, 3, 4, 6);
    printf("%i", my_arr[1]);
    return 0;
}