#ifndef HASHPERFECT_HPP
#define HASHPERFECT_HPP

#include <array>
#include <vector>
#include "HashLin.hpp"
using namespace std;
class HashPerfect{

    private:
    HashLin * table[10];
    void init();
    unsigned long int hash(string & str);

    public:
    HashPerfect();
    bool insert(vector<string>list);
    void print();

};
#endif