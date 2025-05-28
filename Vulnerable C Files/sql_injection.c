#include <stdio.h>
#include <string.h>

void sql_injection(char *userInput) {
    char query[100] = "SELECT * FROM users WHERE username='";
    strcat(query, userInput);  // unsafe concat
    strcat(query, "';");
    printf("Query: %s\n", query);
}
