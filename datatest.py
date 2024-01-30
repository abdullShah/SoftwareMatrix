def test_printm(matrix):
    combinations = [
        {"num_test": 1, "width": 0, "height": 0, "border": '', "verge": '', "horz": False},
        {"num_test": 2, "width": 0, "height": 0, "border": '', "verge": '', "horz": True},
        {"num_test": 3, "width": 0, "height": 0, "border": '', "verge": '~', "horz": False},
        {"num_test": 4, "width": 0, "height": 0, "border": '', "verge": '~', "horz": True},
        {"num_test": 5, "width": 0, "height": 0, "border": '|', "verge": '', "horz": False},
        {"num_test": 6, "width": 0, "height": 0, "border": '|', "verge": '', "horz": True},
        {"num_test": 7, "width": 0, "height": 0, "border": '|', "verge": '~', "horz": False},
        {"num_test": 8, "width": 0, "height": 0, "border": '|', "verge": '~', "horz": True},
        {"num_test": 9, "width": 0, "height": 1, "border": '', "verge": '', "horz": False},
        {"num_test": 10, "width": 0, "height": 1, "border": '', "verge": '', "horz": True},
        {"num_test": 11, "width": 0, "height": 1, "border": '', "verge": '~', "horz": False},
        {"num_test": 12, "width": 0, "height": 1, "border": '', "verge": '~', "horz": True},
        {"num_test": 13, "width": 0, "height": 1, "border": '|', "verge": '', "horz": False},
        {"num_test": 14, "width": 0, "height": 1, "border": '|', "verge": '', "horz": True},
        {"num_test": 15, "width": 0, "height": 1, "border": '|', "verge": '~', "horz": False},
        {"num_test": 16, "width": 0, "height": 1, "border": '|', "verge": '~', "horz": True},
        {"num_test": 17, "width": 1, "height": 0, "border": '', "verge": '', "horz": False},
        {"num_test": 18, "width": 1, "height": 0, "border": '', "verge": '', "horz": True},
        {"num_test": 19, "width": 1, "height": 0, "border": '', "verge": '~', "horz": False},
        {"num_test": 20, "width": 1, "height": 0, "border": '', "verge": '~', "horz": True},
        {"num_test": 21, "width": 1, "height": 0, "border": '|', "verge": '', "horz": False},
        {"num_test": 22, "width": 1, "height": 0, "border": '|', "verge": '', "horz": True},
        {"num_test": 23, "width": 1, "height": 0, "border": '|', "verge": '~', "horz": False},
        {"num_test": 24, "width": 1, "height": 0, "border": '|', "verge": '~', "horz": True},
        {"num_test": 25, "width": 1, "height": 1, "border": '', "verge": '', "horz": False},
        {"num_test": 26, "width": 1, "height": 1, "border": '', "verge": '', "horz": True},
        {"num_test": 27, "width": 1, "height": 1, "border": '', "verge": '~', "horz": False},
        {"num_test": 28, "width": 1, "height": 1, "border": '', "verge": '~', "horz": True},
        {"num_test": 29, "width": 1, "height": 1, "border": '|', "verge": '', "horz": False},
        {"num_test": 30, "width": 1, "height": 1, "border": '|', "verge": '', "horz": True},
        {"num_test": 31, "width": 1, "height": 1, "border": '|', "verge": '~', "horz": False},
        {"num_test": 32, "width": 1, "height": 1, "border": '|', "verge": '~', "horz": True}
    ]

    for test in combinations:
        print(f'-------------{test["num_test"]}-------------')
        matrix.printm(width=test["width"],
                      height=test["height"],
                      border=test["border"],
                      verge=test["verge"],
                      horz=test["horz"])
        print(f'----------------------------')
        print()
