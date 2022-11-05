from bill import Flatmate, Bill
from pdfbill import PDFreport

def main():

    try:
        flatmate1 = Flatmate("Victoria Kruger", 20)
        flatmate2 = Flatmate("Paul Kruger", 28)
        flatmate3 = Flatmate("Maria Tall", 10)

        bill = Bill("November 2022", 15500)
        bill.get_total_days(flatmate1, flatmate2, flatmate3)

        print(f"{flatmate1.name}, you should pay {flatmate1.how_many_pay(bill)}")
        print(f"{flatmate2.name}, you should pay {flatmate2.how_many_pay(bill)}")
        print(f"{flatmate3.name}, you should pay {flatmate3.how_many_pay(bill)}")

        report = PDFreport(filename=f"files/{bill.period}.pdf")
        report.create_file(bill, flatmate1, flatmate2, flatmate3)

    except ValueError as e:
        print(str(e))
    except TypeError as e:
        print(str(e))

if __name__ == "__main__":
    main()