def debt_left(credit_value: int, interest: float, installment: int,
              inflation_table: list):
    debt = [credit_value]
    for month, inflation in enumerate(inflation_table):
        payment = (1 + ((inflation + interest) / (credit_value / 10))) * debt[
            month] - installment
        debt.append(payment)

    return debt[1:]

def message(debt: list):
    for month, d in enumerate(debt):
        if d == debt[0]:
            paid_off = credit_value - d
        else:
            paid_off = debt[month - 1] - d
        print(f"Twoja pozostała kwota kredytu to {d}, to {paid_off} mniej niż w poprzednim miesiącu.")


inflation_table = [1.59282448436825,
                       -0.453509101198007,
                       2.32467171712441,
                       1.26125440724877,
                       1.78252628571251,
                       2.32938454145522,
                       1.50222984223283,
                       1.78252628571251,
                       2.32884899407637,
                       0.616921348207244,
                       2.35229588637833,
                       0.337779545187098,
                       1.57703524727525,
                       -0.292781442607648,
                       2.48619659017508,
                       0.267110317834564,
                       1.41795267229799,
                       1.05424326726375,
                       1.4805201044812,
                       1.57703524727525,
                       -0.0774206903147018,
                       1.16573339872354,
                       -0.404186717638335,
                       1.49970852083123,
                       ]
credit_value = int(input("Początkowa wartość kredytu: "))
interest = float(input("Oprocentowanie: "))
installment = int(input("Stała rata: "))

debt = debt_left(credit_value, interest, installment, inflation_table)

message(debt)