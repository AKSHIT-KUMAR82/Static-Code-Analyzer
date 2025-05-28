#include <stdio.h>
#include <string.h>

void vulnerable() {
    char buffer[10];
    gets(buffer);  // unsafe: buffer overflow
    printf("%s\n", buffer);
}
