if __name__ == "__main__":
    dollar = 37.8
    euro = 40.16
    # a - dollar - 2 euro 3- hrywnia
    while True:
        value = input("Це переводчик валют, для того щоб перевести долари у гривні та євро - напишіть 1, для того щоб перевести євро у долари та гривні - напишіть 2, для того, щоб перевести гривін у долари та євро - напишіть 3")
        if value == "1":
            try:
                amount = float(input("Скільки ви маєте доларів?"))
                print(amount, "доларів у гривнях буде:", amount*dollar, "а у євро буде ", amount*0.91)

            except ValueError:
                print("кількість грошей можна вводити лише в цифрах")


        elif value == "2":
            try:
                amount = float(input("Скільки ви маєте євро?"))
                print(amount, "євро у гривнях буде:", amount * euro, "а у доларах буде ", amount / 0.91)

            except ValueError:
                print("кількість грошей можна вводити лише в цифрах")



        elif value == "3":
            try:
                amount = float(input("Скільки ви маєте гривень?"))
                print(amount, "гривень у доларах буде:", amount / dollar, "а у євро буде ", amount / euro)

            except ValueError:
                print("кількість грошей можна вводити лише в цифрах")

        else:
            print("Вводити можна лише відповідні цифри, спробуйте ще раз")
