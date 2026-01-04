"""
Chapter01: Python Basics

NOTE:
This file is a log of experiments originally executed
in Python interactive mode as recommended by the book.
To preserve the learning order and history,
all examples are kept as commented code.
"""

# items = ["book", "note"]
# print("book" in items)
# print("book" not in items)

# count = {"book":1, "note":2}
# print("book" in count)
# print("1" in count)

# chars = "word"
# for count, char in enumerate(chars):
#     print(f"{count}番目の文字は{char}")

# nums = [2, 4, 6, 8]
# for n in nums:
#     if n % 2 == 1:
#         break
# else:
#     print("奇数の値を含めてください")

# def has_book(items):
#     for item in items:
#         if "book" in item:
#             print("found")
#             break
#     else:
#         print("Not found")

# has_book(["note"])
# has_book(["notebook"])

# #while文で書くと
# def has_book(items):
#     #pop()はリストの内容を変更するのでコピーを取る
#     copied = items.copy()
#     #要素が空になるまでループを続ける
#     while copied:
#         item = copied.pop()
#         if "book" in item:
#             print("found")
#             break
#     else:
#         print("Not found")

# has_book(["notebook"])

# def list_book(items):
#     for item in items:
#         if "book" not in item:
#             continue
#         print(item)

# list_book(["note", "notebook", "sketchbook"])

# def get_book(index):
#     items = ["note", "notebook", "sketchbook"]
#     try:
#         return items[index]
#     except IndexError:
#         return "範囲外です"

# print(get_book(10))

# def get_book(index):
#     items = ["note", "notebook", "sketchbook"]
#     try:
#         return items[index]
#     except (IndexError, TypeError) as e:
#         print(f"例外が発生しました: {e}")
#         return "範囲外です"

# print(get_book(3))
# print(get_book("3"))

# from io import UnsupportedOperation

# f = open("some.txt", "w")
# try:
#     f.read()
# except UnsupportedOperation as e:
#     print(f"例外が発生しました: {e}")
# finally:
#     print("ファイルをクローズします")
#     f.close()

# raise ValueError("不正な引数です")

# with open("some.txt", "w") as f:
#     f.write("some text")