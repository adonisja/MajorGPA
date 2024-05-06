import sys
import pytesseract

if __name__ == '__main__':
    print(f'Welcome to The Major GPA Calculator: ')
    with open('test.txt', 'r') as f:
        for line in f:
            print(line, end='')