import datetime

def get_lmp_from_patient():
    print("When was the patient's last normal menstrual cycle? ")

    date_str= input('Format: [dd/mm/yyyy]')
    parts = date_str.split('/')          #month,day,year=date_str.split('/')

    if len(parts) !=3:
        print("Bad date found", date_str)
        return get_lmp_from_patient()
    year = int(parts[2])
    month = int(parts[1])
    day = int(parts[0])

    lmp=datetime.date(year, month, day)
    return lmp

def lmp_information(lmp_day):
    gest_length=datetime.timedelta(days=281)
    gest_std= datetime.timedelta(days=13)


    exp_due_date=lmp_day+ gest_length
    min_due_date=exp_due_date-gest_std
    max_due_date=exp_due_date+gest_std

    print("You expected due date is", exp_due_date.strftime('%a %b %d %Y'))
    print("But it may be as early as", min_due_date.strftime('%m/%d/%Y'))
    print("Or as late as", max_due_date.strftime('%m/%d/%Y'))


def main():
    lmp_day = get_lmp_from_patient()
    lmp_information(lmp_day)

main()