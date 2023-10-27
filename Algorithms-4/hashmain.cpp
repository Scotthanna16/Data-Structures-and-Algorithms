#include <vector> 
#include <iostream>
#include "HashLin.hpp"
#include "HashPerfect.hpp"
using namespace std;

int primenumberfinder(int size){
    bool prime=false;
    
    
    while(prime==false){
        prime =true;
        size++;
        for (int i = 2; i <= size/2; i++) {
            if (size % i == 0) {
                prime = false;
                break;
            }

        }
        
    }
    return size;
}

int main(){
    
    vector <string> words;
    string temp="";
    int count=0;
    cout<<"Please enter strings to insert (one per line; end list with '!'):\n";
    while(temp !="!"){
        cin>>temp;
        if(temp!="!"){
            count++;
            words.push_back(temp);
        }
    }

    
    
    int size= primenumberfinder(count);
    HashLin table(size);
    for(string str: words){
        table.insert(str);
    }
    table.print(0);

    cout<<"\n\n\n";
    HashPerfect table2;
    table2.insert(words);
    table2.print();
    return 0;


   


}