def coords(square_str):
    file_letter = square_str[0].lower()
    rank_number = square_str[1]
    y = int(rank_number)
    letter_map = {
        'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8
    }
    x = letter_map[file_letter]
    return (x, y)

if __name__ == "__main__":
    test_1 = "e2"
    print(f"Result: {coords(test_1)}")
