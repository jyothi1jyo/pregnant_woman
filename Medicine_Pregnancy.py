"""
File: Medicine_Pregnancy.py

This program suggests the interpretation and details of medicines that are prescribed to pregnant women and
how much weight should a women gain at the end of pregnancy

medicines/drugs
Reference: https://wikem.org/wiki/Drug_pregnancy_categories

weight gain
https://www.cdc.gov/reproductivehealth/maternalinfanthealth/pregnancy-weight-gain.htm
"""
from termcolor import colored
from colorama import init
init(autoreset=True)

TITLE_COLOR = 'magenta'
CAN_COLOR = 'green'
CANNOT_COLOR = 'red'
LIST={'category_A.txt','category_B.txt','category_C.txt','category_D.txt','category_X.txt'}

def main():
    print("\n\t1. Query on a medicine to be taken by Pregnant women")
    print("\t2. Weight gain during Pregnancy")
    print("\t3. Exit")
    choice = input("\tEnter your choice: ")
    if choice == '':
        handle_space()
        main()

    if choice =='1':
        medicine()
    if choice == '2':
        weight()
    if choice =='3':
        exit(0)

def weight():
    print(colored("\n\tWeight gain",TITLE_COLOR))
    wt = (input("\tEnter the weight of patient before pregnancy (in pounds): "))
    if wt.isalpha():
        num_error()

    if wt == '' :  # handle if user did not enter anything
        start_again()

    ht = input("\tEnter the height of patient (in feet): ")
    if ht.isalpha():
        num_error()
    if ht == '':  # handle if user did not enter anything
        start_again()
    #convert into inches
    ht = float(ht)
    wt = float(wt)
    ht = ht*12
    bmi = (wt*703)/(ht*ht)
    print("\tBMI of the patient is "+str(round(bmi,2)))
    twin_check(bmi)
    start_again()

def twin_check(bmi):
    twin = input("\tAre you expecting twins?(Y/N) ").upper()
    if twin == 'Y':
        twin_gain(bmi)
    elif twin == 'N':
        gain(bmi)
    else:
        print("\tSorry could not quite get you.")
        get_twin(bmi)


def twin_gain(bmi):
    if bmi<18.5:
        print(colored("\n\tUnderweight", CANNOT_COLOR))
        print("\n\tYou should gain 50-62 pounds.")
    elif bmi>=18.5 and bmi<25:
        print(colored("\n\tHealthy", CAN_COLOR))
        print("\n\tYou should gain 37-54 pounds.")
    elif bmi>=25 and bmi<=30:
        print(colored("\n\tOverweight", CANNOT_COLOR))
        print("\n\tYou should gain 31-50 pounds.")
    else:
        print(colored("\n\tObese", CANNOT_COLOR))
        print("\n\tYou should gain 25-42 pounds.")

def gain(bmi):
    if bmi<18.5:
        print(colored("\n\tUnderweight", CANNOT_COLOR))
        print("\n\tYou should gain 28-40 pounds.")
    elif bmi>=18.5 and bmi<25:
        print(colored("\n\tHealthy", CAN_COLOR))
        print("\n\tYou should gain 25-35 pounds.")
    elif bmi>=25 and bmi<=30:
        print(colored("\n\tOverweight", CANNOT_COLOR))
        print("\n\tYou should gain 15-25 pounds.")
    else:
        print(colored("\n\tObese", CANNOT_COLOR))
        print("\n\tYou should gain 11-20 pounds.")


def medicine():
    print(colored("\n\tMedicine query", TITLE_COLOR))
    while True:
        is_not_medicine = False
        medicine = ((input("\n\tEnter the medicine you want to query about: ").strip()).lower())
        if medicine=='':                                            #handle if user did not enter anything
            start_again()
        for file in LIST:
            for line in open(file):
                line = line.strip()
                if medicine==line:
                    detail(medicine,file)
                    is_not_medicine = True

        if is_not_medicine !=True:
            print_error()
        end_query()

def print_error():
    print(colored("\n\tThe medicine you have entered is not in our database."
                   "\n\tIt would be best if you consult a doctor.", CANNOT_COLOR))

def end_query():
    print("\n\t ------------------------------------------------------------------------------------------------ \n")


def detail(medicine,file):
    if 'A' in file:
        print_details_A()
    elif 'B' in file:
        print_details_B()
    elif 'C' in file:
        if medicine=='nasal steroids':
            month = get_month()
            if month < 1:
                print_details_D()
            else:
                print_details_C()
        else:
            print_details_C()

    elif 'D' in file:
        if medicine=='aspirin':
            month = get_month()
            if month<=3:
                print_details_D()
            else:
                donot()

        elif medicine=='bismuth subsalicylate':
            month = get_month()
            if month==3:
                print_details_D()
            else:
                donot()

        elif medicine == 'ibuprofen':
            month = get_month()
            if month == 3:
                print_details_D()
            else:
                print_details_C()

        elif medicine == 'meloxicam':
            month = get_month()
            if month>6.9:
                print_details_D()
            else:
                print_details_C()
        else:
            print_details_D()

    elif 'X' in file:
        print_details_X()
    else:
        print_error()



def print_details_A():
        print(colored("\n\tThis is a Category A drug", CAN_COLOR))
        print(colored("\tInterpretation: Human studies show no risk", CAN_COLOR))
        print(colored("\tDetails: Adequate, well-controlled studies in pregnant women have not shown an increased\n"
                      "\trisk of fetal abnormalities to the fetus in any trimester of pregnancy", CAN_COLOR))
def print_details_B():
    print(colored("\n\tThis is a Category B drug", CAN_COLOR))
    print(colored("\tInterpretation: No evidence of risk in studies", CAN_COLOR))
    print(colored("\tDetails: Animal studies have revealed no evidence of harm to the fetus, however, there are no\n"
                  "\tadequate and well-controlled studies in pregnant women.\n"
                  "\tOR Animal studies have shown an adverse effect, but adequate & well-controlled studies in \n"
                  "\tpregnant women have failed to demonstrate a risk to the fetus in any trimester.", CAN_COLOR))

def print_details_C():
    print(colored("\n\tThis is a Category C drug",CANNOT_COLOR))
    print(colored("\tInterpretation: Risk cannot be ruled out",CANNOT_COLOR))
    print(colored("\tDetails: Animal studies have shown an adverse effect and there are no adequate and well-\n"
                  "\tcontrolled studies in pregnant women.\n"
                  "\tOR No animal studies have been conducted and there are no adequate and well-controlled studies\n"
                  "\tin pregnant women.",CANNOT_COLOR))

def print_details_D():
    print(colored("\n\tThis is a Category D drug",CANNOT_COLOR))
    print(colored("\tInterpretation: Positive evidence of risk",CANNOT_COLOR))
    print(colored("\tDetails: Adequate well-controlled or observational studies in pregnant women have demonstrated\n"
                  "\ta risk to the fetus. However, the benefits of therapy may outweigh the potential risk.\n"
                  "\tFor example, the drug may be acceptable if needed in a life-threatening situation or serious\n"
                  "\tdisease for which safer drugs cannot be used or are ineffective.",CANNOT_COLOR))

def print_details_X():
    print(colored("\n\tThis is a Category X drug",CANNOT_COLOR))
    print(colored("\tInterpretation: Contraindicated in pregnancy",CANNOT_COLOR))
    print(colored("\tDetails: Adequate well-controlled or observational studies in animals or pregnant women have\n"
                  "\tdemonstrated positive evidence of fetal abnormalities or risks. The use of the product is \n"
                  "\tcontraindicated in women who are or may become pregnant.",CANNOT_COLOR))

def get_month():
    month = (input("\tHow many months is the patient pregnant?(0-9) "))
    try:
        month = float(month)
    except ValueError:
        print("\t Please enter correct month number")
        get_month()

    if month >= 0 and month <=9:
        return month

def num_error():
    print("\tPlease enter number")
    weight()

def donot():
    print(colored("\tDetails: Not to be consumed at this stage",CANNOT_COLOR))

def start_again():
    main()

if __name__ == "__main__":
    main()
