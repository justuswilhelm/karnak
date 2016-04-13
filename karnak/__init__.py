"""Compile stuff."""
PROLOGUE = """.section .data

"""
MAIN = """.section .text
.globl  main
main:
    movl $1, %eax
    movl $0, %ebx
    int $0x80

"""
EPILOGUE = """.size   main, .-main
"""

def compile(raw):
    return PROLOGUE + MAIN + EPILOGUE
