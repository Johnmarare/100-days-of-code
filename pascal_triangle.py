#!/usr/bin/python3
# pascal_triangle.py
""""pascal triangle is a common inteview question"""


def pascal_triangle(n):
    """implementation of the python triangle
    Args:
        n (int):  
    """
    # Returns an empty list if n <= 0.
    if n <= 0:
        return []
    # initialize my pascal triangle as a list of list
    triangle = [[1]]
    # look through the rows
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))