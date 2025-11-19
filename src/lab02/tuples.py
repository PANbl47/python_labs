def format_record(rec: tuple[str, str, float]) -> str:
    fio_clean = rec[0].strip()
    FIO = fio_clean.split()

    gpa = round(rec[2], 2)

    if len(FIO) == 3:
        return f"{FIO[0][0].upper()}{FIO[0][1:]} {FIO[1][0].upper()}.{FIO[2][0].upper()}. , гр. {rec[1]}, GPA {gpa:.2f}"
    elif len(FIO) == 2:
        return (
            f"{FIO[0]}{FIO[0][1:]} {FIO[1][0].upper()}. , гр. {rec[1]}, GPA {gpa:.2f}"
        )
    else:
        raise ValueError


print(format_record((("  сидорова  анна   сергеевна ", "ABB-01", 3.999))))
