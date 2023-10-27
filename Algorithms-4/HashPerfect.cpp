#include <array>
#include <iostream>
#include <vector>
#include "HashPerfect.hpp"

using namespace std;

void HashPerfect:: init(){
    for(int i=0; i<10; i++){
        table[i]=NULL;
    }
}
HashPerfect::HashPerfect(){
    init();
}

unsigned long int HashPerfect::hash(string & str){
    unsigned long int hash=0;

    
    for(char c:str){
        hash= 37 * hash + c;
    }
    hash = hash % 10;
    
    

    return hash;
    // & stores memory adress, * gets valie address at memory
}

void HashPerfect::print(){
    for(int i=0; i<10;i++){
        cout<<i<<": -->\n" ;
        table[i]->print(7);

    }
}

bool HashPerfect::insert(vector<string>list){
    int sizes[10];
    for(int i=0;i<10;i++){
        sizes[i]=0;
    }

    for(string str:list){
        string & temp=str;
        int hashindex=hash(temp);
        sizes[hashindex]+=1;
    }
    for(int i=0;i<10;i++){
        HashLin * hashtable=new HashLin(sizes[i]*sizes[i]);
        table[i]=hashtable;
    }
    for(string temp:list){
        int hashindex=hash(temp);
        table[hashindex]->insert(temp);
    }
    return true;
}


