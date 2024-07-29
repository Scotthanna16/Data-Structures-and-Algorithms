#include <vector> 
#include <iostream>
#include "HashLin.hpp"

using namespace std;


void HashLin::init(){
    for(int i=0;i<size_new;i++){
        hashtable.push_back("");
        
    }
    
}

HashLin::HashLin(int size){
    size_new =size;
    init();
}

bool HashLin::insert(string str){

    string & tempstr=str;
    int index=hash(tempstr);
    bool succ=false;
    while(succ==false){
        if(hashtable [index]==""){
            hashtable [index]=str;
            succ=true;
        }
        else{
            if(index!=size_new-1){
            index++;
            
            }
            else{
            index=0;
            }

        }
    }

   

    return true;

}

void HashLin::print(int space){
    for(int i=0;i<size_new;i++){
        cout<<string(space,' ')<<i<<": "<< hashtable.at(i)<<"\n";
    }
}


unsigned long int HashLin::hash(string & str){
    unsigned long int hash=0;

    
    for(char c:str){
        hash= 37 * hash + c;
    }
    hash = hash % size_new;
    
    

    return hash;
    // & stores memory adress, * gets valie address at memory
}


