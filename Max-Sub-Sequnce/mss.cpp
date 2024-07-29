#include <iostream>
#include <iomanip>
#include <time.h>

/*
First subSum alg, O(n^3) complexity
*/
double maxSubSum1 ( int num[], int length ) {
    clock_t time=clock();
    //still need to do time control
    int maxSum=0;

    for(int i=0; i< length;++i){
        for(int j=i; j< length; ++j){
            int thisSum=0;
            for (int k=i; k<=j;++k)
                thisSum +=num[k];
            if (thisSum>maxSum){
                maxSum=thisSum;
            }
        }
    }
    time=clock()-time;
    std::cout<<"Algorithm 1: "<<maxSum<<"\n\n";
    
    return time;

}
/*
Second subSum alg, O(n^2) complexity
*/
double maxSubSum2 (int num[], int length){
    //still need to do time control
    clock_t time=clock();
    int maxSum=0;
    for (int i=0; i<length; ++i){
        int thisSum =0;
        for(int j=i; j<length; ++j){
            thisSum+=num[j];
            if (thisSum>maxSum){
                maxSum=thisSum;
            }

        }
    }
    std::cout<<"Algorithm 2: "<<maxSum<<"\n\n";
    time=clock()-time;
    return time;
}
/*
calculate max of three integers
*/
int max3(int first, int second, int third){
    int max=first;
    if(second>max){
        max=second;
    }
    if(third>max){
        max=third;
    }
    return max; 
}
/*
Third subSum alg, O(nlogn) complexity
*/
int maxSubSum3rec(int num[], int left, int right){
    // Base Case
    if(left==right){
        if(num[left]>0){
            return num[left];
        }
        
        else{
            return 0; }
    }
    int center=(left+right)/2;
    int maxLeftSum=maxSubSum3rec(num, left, center);
    int maxRightSum=maxSubSum3rec(num, center+1, right);
    int maxleftbordersum=0, leftbordersum=0; 
    for (int i=center; i>=left; --i){
        leftbordersum+=num[i];
        if(leftbordersum>maxleftbordersum){
            maxleftbordersum=leftbordersum;
        }
    }

    int maxrightbordersum=0, rightbordersum=0; 
    for (int j=center+1; j<=right; ++j){
        rightbordersum+=num[j];
        if(rightbordersum>maxrightbordersum){
            maxrightbordersum=rightbordersum;
        }
    }
   
    
    return max3(maxLeftSum,maxRightSum, maxrightbordersum+maxleftbordersum);

}
/*
Controller for recursive method
*/
double maxSubSum3(int num[], int length){
    //still need to do time control
    clock_t time=clock();
    int maxSum=maxSubSum3rec(num,0, length-1);
    std::cout<<"Algorithm 3: "<<maxSum<<"\n\n";
    time=clock()-time;
    return time;

}

double maxSubSum4(int num[], int length){
    clock_t time= clock();
    int maxSum=0, thisSum=0;
    for(int i=0; i<length;++i){
        thisSum+=num[i];
        if(thisSum>maxSum){
            maxSum=thisSum;
        }
        else if(thisSum<0){
            thisSum=0;
        }
    }
    std::cout<<"Algorithm 4: "<<maxSum<<"\n\n";
    time=clock()-time;
    return time;
}
// may want to use int main (int argc, char *argv[])
int main(){
    using namespace std;
    cout<<"Please Enter Sequence of Integers:\n";  
    int count=0;    // Variable to keep count of each number
    int numarr[2500];
    while(cin>>numarr[count]){
        count++;
    }
    double time1=maxSubSum1(numarr, count);
    double time2=maxSubSum2(numarr,count);
    double time3=maxSubSum3(numarr,count);
    double time4=maxSubSum4(numarr,count);
    cout<<"Final Results\n";
    cout<<"  Algorithm 1 O(n^3)   :"<<setprecision(0) <<fixed<<(float)time1*1000000/CLOCKS_PER_SEC<<"ms\n";
    cout<<"  Algorithm 2 O(n^2)   :"<<setprecision(0) <<fixed<<(float)time2*1000000/CLOCKS_PER_SEC<<"ms\n";
    cout<<"  Algorithm 3 O(nlogn) :"<<setprecision(0) <<fixed<<(float)time3*1000000/CLOCKS_PER_SEC<<"ms\n";
    cout<<"  Algorithm 4 O(n)     :"<<setprecision(0) <<fixed<<(float)time4*1000000/CLOCKS_PER_SEC<<"ms\n";
    return 0;

}


