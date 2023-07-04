# task 1
if __name__ == "__main__":
    try:
        numOne = int(input("Введіть число 1"))
        numTwo = int(input("Введіть число 2"))
        numThree = int(input("Введіть число 3"))
        print(numOne+numTwo+numThree, numOne*numTwo*numThree)
    except ValueError:
        print("Вводити можна лише цифри, спробуйте ще раз ")

    # task 2
    try:
        salary = int(input("Вкажіть свою зарплатню "))
        bankCredit = int(input("Введіть суму, яку ви сплачуєте щомісяця через кредит у банку"))
        utilities = int(input("Введіть суму, яку ви мусите сплатити за користування комунальних послуг"))
        restMoney = salary-bankCredit-utilities

        if restMoney > 0:
            print("У вас залишається", restMoney)
        elif restMoney < 0:
            print("У вас не залишається грошей, до тогож ви будете у боргу на", restMoney)
        else:
            print("У вас нічого не залишається, але ви все спроможні сплатити")

    except ValueError:
        print("Кількість грошей можна вводити лише у цифрах ")


# task 3

    try:

        stDiagonal = float(input("Введіть довжину першої діагоналі"))
        ndDiagonal = float(input("Введіть довжину другої діагоналі"))
        print(0.5*stDiagonal*ndDiagonal)

    except ValueError:
        print("Довжини діагоналей можна записувати лише в цифрах")
