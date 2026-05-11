#include <stdio.h>
#include <string.h>

int main() {
    char password[8];

    printf("Enter password: ");
    gets(password);   // Unsafe function

    if (strcmp(password, "admin") == 0) {
        printf("Access granted\n");
    } else {
        printf("Access denied\n");
    }

    return 0;
}