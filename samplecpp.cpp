#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool isValidFilename(const string& filename) {

    for (char c : filename) {

        if (!(isalnum(c) || c == '.' || c == '_')) {
            return false;
        }
    }

    return true;
}

int main() {

    string filename;

    cout << "Enter filename: ";
    cin >> filename;

    if (!isValidFilename(filename)) {
        cout << "Invalid filename.\n";
        return 1;
    }

    ifstream file(filename);

    if (!file.is_open()) {
        cout << "Cannot open file.\n";
        return 1;
    }

    string line;

    while (getline(file, line)) {
        cout << line << endl;
    }

    return 0;
}