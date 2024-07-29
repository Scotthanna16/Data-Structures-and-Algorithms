#ifndef HASHLIN_HPP
#define HASHLIN_HPP

#include <vector> 

using namespace std;
class HashLin
{
    private:
    int size_new;
    vector<string> hashtable;
    //vector<vector<string> words(2)> hashtable;
    void init();
    unsigned long int hash(string & str);
    
    public: 
    HashLin(int size);
    bool insert(string str);
    void print(int space);
};

#endif
