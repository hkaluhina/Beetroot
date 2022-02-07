
height = float(input())
weight = float(input())

if height < 0 or height > 2.5 or weight < 0 or weight > 250:
    print("Ошибочные входные данные")
else:
    bmi = weight / height ** 2
    bmi = round(bmi, 2)

    if bmi < 18.5:
        description = "недостаточная масса тела"
    elif bmi < 25:
        description = "нормальная масса тела"
    elif bmi < 30:
        description = "избыточная масса тела"
    else:
        description = "ожирение"

    print("bmi=", bmi, "У вас", description)
