#include <stdio.h>
#include <string.h>

int main() {
    char password[8];

    printf("Enter password: ");

    if (fgets(password, sizeof(password), stdin) != NULL) {

        password[strcspn(password, "\n")] = '\0';

        printf("You entered: %s\n", password);
    }

    return 0;
}