#include<stdio.h>

int  main(){
    int N=0;
    scanf("%d",&N);
    int A[N];
    for(int i=0;i<N;i++){
        scanf("%d",&A[i]);
    }
    int Sum=0;
    for(int i=0;i<N;i++){
        Sum += A[i];
    }
    printf("%d",Sum);
    return 0;
}
