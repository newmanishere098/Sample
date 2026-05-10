#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

int main() {

    string input;

    cout << "Enter filename: ";
    cin >> input;

    string command = "cat " + input;

    system(command.c_str());   // DANGEROUS

    return 0;
}

