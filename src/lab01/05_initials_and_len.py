FIO = input("ФИО: ")
countt = 0
while "  " in FIO:
    FIO = FIO.replace("  ", " ")
words = FIO.split()
FIO_w_2spases = FIO.rstrip().lstrip()
first_letters = []
str_first_letters = ""
for word in words:
    first_letters.append(word[0])
for letter in first_letters:
    str_first_letters += letter
print(f"Инициалы: {str_first_letters}")
print(f"Длина (символов): {len(FIO_w_2spases)}")
