from random import randint
from typing import Callable, Tuple, Union


class SoftwareMatrix:
    """
    The class for representing a matrix and performing various operations with it.

    Attributes:
    n: int, a number of rows in the matrix;
    m: int, a number of columns in the matrix;
    size: tuple, a pair of values for the number of rows and columns;
    matrix: list, a two-dimensional list representing the elements of the matrix;
    is_square: bool, a belonging to the square matrix;
    minm: int, the smallest value in the matrix;
    maxm: int, the largest value in the matrix;
    summa: int, the sum of the elements in the matrix;

    Class method:
    validate(matrix): check whether the matrix meets the class standards;
    ------------------------------
    create(n, m, mode='d'): initialize a matrix with the size of n rows by m columns with a definite mode;

    Methods:
    unpack(): return the unpacked matrix;
    ------------------------------
    get_diagonal(side=False): Return the diagonal of the matrix;
    ------------------------------
    get_triangle(downward=False, lower=False, strict=False): return the upper/lower triangular of the nearest
    square matrix;
    ------------------------------
    transpose(): transposes the nearest square matrix;
    ------------------------------
    change(func, start=(0, 0)): changes the elements of the matrix according to a certain condition;
    ------------------------------
    printm(width=0, height=0, border='', verge='', cross='+', horz=False): outputs the matrix according to
    certain rules;
    ------------------------------
    fill(iterator, downward=False, start=(0, 0)): replaces the elements of the matrix according to the entered
    set of values;
    ------------------------------
    rotate(clockwise=True, turns=1): rotates the nearest square matrix by 90 degrees;
    ------------------------------
    move_contour(clockwise=True, depth=0, turns=1): rotates the contour of the nearest square matrix to shift;
    ------------------------------
    get_sector(section=1, strict=False): return the sector elements;
    ------------------------------
    reflect_side_sector(): reflects the left and right sectors (not including diagonals) relative to the vertical
    line drawn through the center;
    """

    def __init__(self, matrix=None) -> None:
        # Validation
        if matrix is None:
            matrix = []
        if not self.validate(matrix):
            raise TypeError("matrix does not meet the standards")

        # Initialization
        temp_n = len(matrix)
        temp_m = len(matrix[0])

        # Main
        self.__n = temp_n
        self.__m = temp_m
        self.__size = (temp_n, temp_m)
        self.__is_square = (temp_n == temp_m)
        self.__matrix = matrix
        self.__minm = self.__maxm = self.__summa = matrix[0][0]

    def __getitem__(self, key: int) -> list:
        return self.matrix[key]

    def __setitem__(self, index: Tuple[int, int], value: int) -> None:
        row, col = index
        self.matrix[row][col] = value

    def __str__(self) -> str:
        max_len = len(str(self.maxm))
        delta = 2
        lines = ''
        for i in range(self.n):
            for j in range(self.m):
                lines += f'{self.matrix[i][j]:^{max_len + delta}}'
            if i != self.n - 1:
                lines += '\n'
        return lines

    @classmethod
    def validate(cls, matrix: list) -> bool:
        """
        Check whether the matrix meets the class standards.

        :param matrix: the matrix being checked;
        :return: the value of the correctness of the matrix;
        """
        if isinstance(matrix, list) and all(isinstance(row, list) for row in matrix):
            if len(matrix) != 0:
                num_cols = len(matrix[0])
                return all(isinstance(val, int) for row in matrix for val in row) and all(
                    len(row) == num_cols for row in matrix[1:])
        return False

    @classmethod
    def create(cls, n: int, m: int, mode: str = 'd') -> 'SoftwareMatrix':
        """
        Initialize a matrix with the size of n rows by m columns with a definite mode.

        :param n: a number of rows in the matrix;
        :param m: a number of columns in the matrix;
        :param mode: initial filling of the matrix, by default mode='d':
        d (default) - a series positive integer (natural) numbers;
        z (zero) - all elements are zeros;
        r (random) - random integer are generated in the range from -100 to 100;
        """
        # Validation
        if not (isinstance(n, int) and n > 0 and
                isinstance(m, int) and m > 0):
            raise TypeError("size must be natural number")

        # Initialization
        matrix = [[] for _ in range(n)]

        # Main
        match mode:
            case 'd':
                gen = (q for q in range(1, n * m + 1))
                for i in range(n):
                    for j in range(m):
                        matrix[i].append(next(gen))
            case 'z':
                for i in range(n):
                    for j in range(m):
                        matrix[i].append(0)
            case 'r':
                for i in range(n):
                    for j in range(m):
                        matrix[i].append(randint(-100, 100))
            case _:
                raise TypeError(f"mode is not defined '{mode}'")
        return SoftwareMatrix(matrix)

    @property
    def n(self) -> int:
        """
        Return a number of rows in the matrix.

        :return: a number of rows in the matrix;
        """
        return self.__n

    @property
    def m(self) -> int:
        """
        Return a number of columns in the matrix.

        :return: a number of columns in the matrix;
        """
        return self.__m

    @property
    def size(self) -> tuple:
        """
        Return a pair of values for the number of rows and columns.

        :return: a pair of values for the number of rows and columns;
        """
        return self.__size

    @property
    def is_square(self) -> bool:
        """
        Return a belonging to the square matrix.

        :return: a belonging to the square matrix;
        """
        return self.__is_square

    @property
    def matrix(self) -> list:
        """
        Return the matrix.

        :return: the matrix;
        """
        return self.__matrix

    @property
    def minm(self) -> int:
        """
        Return the smallest element of the matrix.

        :return: the smallest element of the matrix;
        """
        for i in range(self.n):
            for j in range(self.m):
                self.__minm = min(self.__minm, self.matrix[i][j])
        return self.__minm

    @property
    def maxm(self) -> int:
        """
        Returns the largest element of the matrix.

        :return: the largest element of the matrix;
        """
        for i in range(self.n):
            for j in range(self.m):
                self.__maxm = max(self.__maxm, self.matrix[i][j])
        return self.__maxm

    @property
    def summa(self) -> int:
        """
        Return the sum of the elements in the matrix.

        :return: the sum of the elements in the matrix;
        """
        temp_summa = 0
        for i in range(self.n):
            for j in range(self.m):
                temp_summa += self.matrix[i][j]
        self.__summa = temp_summa
        return self.__summa

    def unpack(self) -> list:
        """
        Return the unpacked matrix.

        :return: the unpacked matrix;
        """
        # Main
        return [self.matrix[i][j] for i in range(self.n) for j in range(self.m)]

    def get_diagonal(self, side: bool = False) -> list:
        """
        Return the diagonal of the matrix.

        :param side: defines the diagonals for output: main (True) or side (False), by default side=False;
        :return: the diagonal of the matrix;
        """
        # Validation
        if not (isinstance(side, bool)):
            raise TypeError("side must be boolean")

        # Initialization
        s = min(self.n, self.m)
        res = []

        # Main
        match side:
            case False:
                for ind in range(s):
                    res.append(self.matrix[ind][ind])
            case True:
                for ind in range(s):
                    res.append(self.matrix[ind][self.n - ind])
        return res

    def get_triangle(self, downward: bool = False, lower: bool = False, strict: bool = False) -> list:
        """
        Return the upper/lower triangular of the nearest square matrix.

        :param downward: determines the reading direction of the elements: up (True) or down (False), by
                default downward=False;
        :param lower: defines the type of triangle: upper (True) and lower (False), by default lower=False;
        :param strict: determines the severity of the output (whether to take into account the elements on the
                diagonal): strictly or loosely, by default strict=False;
        :return: the upper/lower triangular of the nearest square matrix;
        """
        # Validation
        if not (isinstance(downward, bool)):
            raise TypeError("downward must be boolean")

        if not (isinstance(lower, bool)):
            raise TypeError("lower must be boolean")

        if not (isinstance(strict, bool)):
            raise TypeError("strict must be boolean")

        # Initialization
        s = min(self.n, self.m)
        res = []
        edge = 1 if strict else 0

        # Main
        match lower:
            case False:
                match downward:
                    case False:
                        for i in range(s):
                            for j in range(i + edge, s):
                                res.append(self.matrix[i][j])
                    case True:
                        for j in range(s):
                            for i in range(j + 1 - edge):
                                res.append(self.matrix[i][j])
            case True:
                match downward:
                    case False:
                        for i in range(s):
                            for j in range(0, i + edge):
                                res.append(self.matrix[i][j])
                    case True:
                        for j in range(s):
                            for i in range(j + 1 - edge, s):
                                res.append(self.matrix[i][j])
        return res

    def transpose(self) -> 'SoftwareMatrix':
        """
        Transposes the nearest square matrix.

        :return: an instance of the current object;
        """
        # Initialization
        s = min(self.n, self.m)

        # Main
        for i in range(s):
            for j in range(i, s):
                self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]

        return self

    def change(self, func: Callable, start: Tuple[int, int] = (0, 0)) -> 'SoftwareMatrix':
        """
        Changes the elements of the matrix according to a certain condition.

        :param func: function by which the element will be changed;
        :param start: coordinates of the point from which the function will be applied in the truncated
                square, by default start=(0, 0);
        :return: an instance of the current object;
        """
        # Validation
        if not callable(func):
            raise TypeError("function must be called")

        if not (0 <= start[0] < self.n and 0 <= start[1] < self.m):
            raise IndexError("list index out of range")

        # Main
        for i in range(start[0], self.n):
            for j in range(start[1], self.m):
                self.matrix[i][j] = func(self.matrix[i][j])

        return self

    def printm(self, width: int = 0, height: int = 0,
               border: str = '', verge: str = '', cross: str = '+',
               horz: bool = False) -> None:
        """
        Outputs the matrix according to certain rules.

        :param width: horizontal distance from the table border in spaces, by default width=0;
        :param height: vertical distance from the table border in spaces, by default height=0;
        :param border: one character that will be the border of the table, by default border='';
        :param verge: one character that will be the upper and lower bounds of the table, if the parameter is not
                specified, the value border will be taken, by default verge='';
        :param cross: one character to be inserted at the intersection of the lines, by default cross='+';
        :param horz: drawing the border horizontally, by default horz=False;
        :return: an instance of the current object;
        """
        # Validation
        if not (isinstance(width, int) and width >= 0):
            raise TypeError("width must be natural number")

        if not (isinstance(height, int) and height >= 0):
            raise TypeError("height must be natural number")

        if not (isinstance(horz, bool)):
            raise TypeError("horizontal must be boolean")

        if not (isinstance(border, str) and
                isinstance(verge, str) and
                isinstance(cross, str)):
            raise TypeError("elements of the table must be string")

        if not (len(border) < 2):
            raise TypeError("border must contain one character")

        if not (len(verge) < 2):
            raise TypeError("verge must contain one character")

        if not (len(cross) == 1):
            raise TypeError("cross must contain exactly one character")

        # Initialization
        max_len = len(str(self.maxm))
        delta = 2
        frame = True
        if len(border) == 0 and len(verge) == 0:
            cross = ''
            frame = False
        if len(border) == 0:
            border = ' '
        if len(verge) == 0 and border != '':
            verge = border

        empty = ''
        space = ' '
        if height != 0:
            for _ in range(self.m):
                empty += (max_len + delta + width) * space + f'{border}'
            else:
                empty = f'{border}' + empty

        base = f'{cross}'
        for _ in range(self.m):
            base += (max_len + delta + width) * f'{verge}' + f'{cross}'

        # Main
        if frame:
            print(base)
        for i in range(self.n):
            row = border if len(border) == 1 else ''
            for _ in range(height):
                print(empty)
            for j in range(self.m):
                row += f'{self.matrix[i][j]:^{max_len + delta + width}}' + f'{border}'
            print(row)
            for _ in range(height):
                print(empty)
            if frame:
                if horz:
                    print(base)
        if frame:
            if not horz:
                print(base)

    def fill(self, iterator: Union[list, tuple, set], downward: bool = False,
             start: Tuple[int, int] = (0, 0)) -> 'SoftwareMatrix':
        """
        Replaces the elements of the matrix according to the entered set of values.

        :param iterator: collection of elements (list / tuple / set) from which the elements will be taken;
        :param downward: , by default downward=False;
        :param start: coordinates of the point from which the elements will be replaced horizontally, by
                default start=(0, 0);
        :return: an instance of the current object;
        """
        # Validation
        if not (isinstance(iterator, list) or
                isinstance(iterator, tuple) or
                isinstance(iterator, set)):
            raise TypeError(f"collection of elements must be in the form of a list, tuple or set")

        if not (isinstance(downward, bool)):
            raise TypeError("downward must be boolean")

        if not (0 <= start[0] < self.n and 0 <= start[1] < self.m):
            raise IndexError("list index out of range")

        # Initialization
        arr = list(iterator)
        ind = 0
        first_pass = True

        # Main
        match downward:
            case False:
                i = start[0]
                while i < self.n:
                    j = start[1] if first_pass else 0
                    while j < self.m:
                        if ind != len(arr):
                            self.matrix[i][j] = arr[ind]
                            ind += 1
                        j += 1
                    first_pass = False
                    i += 1

            case True:
                j = start[1]
                while j < self.m:
                    i = start[0] if first_pass else 0
                    while i < self.n:
                        if ind != len(arr):
                            self.matrix[i][j] = arr[ind]
                            ind += 1
                        i += 1
                    first_pass = False
                    j += 1

        return self

    def rotate(self, clockwise: bool = True, turns: int = 1) -> 'SoftwareMatrix':
        """
        Rotates the nearest square matrix by 90 degrees.

        :param clockwise: setting the direction: clockwise (True) or counterclockwise (False), by default
                clockwise=True;
        :param turns: number of turns, by default turns=1;
        :return: an instance of the current object;
        """
        # Validation
        if not (isinstance(clockwise, bool)):
            raise TypeError("clockwise must be boolean")
        if not (isinstance(turns, int) and turns > 0):
            raise TypeError("turns must be natural number")

        # Initialization
        s = min(self.n, self.m)
        turns %= 4

        # Main
        match clockwise:
            case True:
                for _ in range(turns):
                    for i in range(s // 2):
                        for j in range(i, s - i - 1):
                            temp = self.matrix[i][j]
                            self.matrix[i][j] = self.matrix[s - j - 1][i]
                            self.matrix[s - j - 1][i] = self.matrix[s - i - 1][s - j - 1]
                            self.matrix[s - i - 1][s - j - 1] = self.matrix[j][s - i - 1]
                            self.matrix[j][s - i - 1] = temp
            case False:
                for _ in range(turns):
                    for i in range(s // 2):
                        for j in range(i, s - i - 1):
                            temp = self.matrix[i][j]
                            self.matrix[i][j] = self.matrix[j][s - i - 1]
                            self.matrix[j][s - i - 1] = self.matrix[s - i - 1][s - j - 1]
                            self.matrix[s - i - 1][s - j - 1] = self.matrix[s - j - 1][i]
                            self.matrix[s - j - 1][i] = temp
        return self

    def move_contour(self, clockwise: bool = True, depth: int = 0, turns: int = 1) -> 'SoftwareMatrix':
        """
        Rotates the contour of the nearest square matrix to shift.

        :param clockwise: setting the direction: clockwise (True) or counterclockwise (False), by default
                clockwise=True;
        :param depth: depth level to which the rotation will be applied, by default depth=0;
        :param turns: number of turns, by default turns=1;
        :return: an instance of the current object;
        """
        # Validation
        if not (isinstance(clockwise, bool)):
            raise TypeError("clockwise must be boolean")
        if not (isinstance(turns, int) and turns > 0):
            raise TypeError("turns must be natural number")
        if not (0 <= depth < self.n // 2):
            raise IndexError("depth out of range")

        # Initialization
        s = min(self.n, self.m)
        turns %= 4

        # Main
        match clockwise:
            case True:
                temp_up = self.matrix[depth][s - depth - 1]
                for j in range(s - depth - 1, depth, -1):
                    self.matrix[depth][j] = self.matrix[depth][j - 1]

                temp_right = self.matrix[s - depth - 1][s - depth - 1]
                for i in range(s - depth - 1, depth, -1):
                    self.matrix[i][s - depth - 1] = self.matrix[i - 1][s - depth - 1]
                self.matrix[1 + depth][s - depth - 1] = temp_up

                temp_down = self.matrix[s - depth - 1][depth]
                for j in range(depth, s - depth - 1):
                    self.matrix[s - depth - 1][j] = self.matrix[s - depth - 1][j + 1]
                self.matrix[s - depth - 1][s - depth - 1 - 1] = temp_right

                for i in range(depth, s - depth - 1):
                    self.matrix[i][depth] = self.matrix[i + 1][depth]
                self.matrix[s - depth - 1 - 1][depth] = temp_down
            case False:
                temp_up = self.matrix[depth][depth]
                for j in range(depth, s - depth - 1):
                    self.matrix[depth][j] = self.matrix[depth][j + 1]

                temp_left = self.matrix[s - depth - 1][depth]
                for i in range(s - depth - 1, depth, -1):
                    self.matrix[i][depth] = self.matrix[i - 1][depth]
                self.matrix[1 + depth][depth] = temp_up

                temp_down = self.matrix[s - depth - 1][s - depth - 1]
                for j in range(s - depth - 1, depth, -1):
                    self.matrix[s - depth - 1][j] = self.matrix[s - depth - 1][j - 1]
                self.matrix[s - depth - 1][1 + depth] = temp_left

                for i in range(depth, s - depth - 1):
                    self.matrix[i][s - depth - 1] = self.matrix[i + 1][s - depth - 1]
                self.matrix[s - depth - 1 - 1][s - depth - 1] = temp_down
        return self

    def get_sector(self, section: int = 1, strict: bool = False) -> list:
        """
        Return the sector elements.

        :param section: number of the output sector, sections are clockwise, by default section=1;
        :param strict: determines the severity of the output (whether to take into account the elements on the
                diagonal): strictly or loosely, by default strict=False;
        :return: the sector elements;
        """
        # Validation
        if not (1 <= section <= 4):
            raise IndexError("section must be from 1 to 4")

        if not (isinstance(strict, bool)):
            raise TypeError("strict must be boolean")

        # Initialization
        s = min(self.n, self.m)
        res = []
        edge = 1 if strict else 0

        # Main
        match section:
            case 1:
                for i in range(s // 2 + 1 - edge):
                    for j in range(i + edge, s - i - edge):
                        res.append(self.matrix[i][j])
            case 3:
                for i in range(s - 1, s // 2 - 1 - edge, -1):
                    for j in range((s - i) - 1 + edge, s - (s - i) + 1 - edge):
                        res.append(self.matrix[i][j])
            case 4:
                for j in range(s // 2 + 1 - edge):
                    for i in range(j + edge, s - j - edge):
                        res.append(self.matrix[i][j])
            case 2:
                for j in range(s - 1, s // 2 - 1 - edge, -1):
                    for i in range((s - j) - 1 + edge, s - (s - j) + 1 - edge):
                        res.append(self.matrix[i][j])
        return res

    def reflect_side_sector(self) -> 'SoftwareMatrix':
        """
        Reflects the left and right sectors (not including diagonals) relative
        to the vertical line drawn through the center.

        :return: an instance of the current object;
        """
        # Initialization
        s = min(self.n, self.m)

        # Main
        for i in range(1, s - 1):
            for j in range(min(i, s - i - 1)):
                self.matrix[i][j], self.matrix[i][s - j - 1] = self.matrix[i][s - j - 1], self.matrix[i][j]
        return self
