#include <stdio.h>
#include <string.h>

int main() {
    char password[8];

    printf("Enter password: ");
    gets(password);   // DANGEROUS

    printf("You entered: %s\n", password);

    return 0;
}