import sys
from account import AccountRaw
from client import ClientRaw
from card import CardRaw
from loan import LoanRaw
from transaction import TransactionRaw
from disposition import DispositionRaw
from district import DistrictRaw

from utils.loader import Loader
from utils.utils import convert_datetime

FILES_COMPETITION = "../ficheiros_competicao/"

def load_accounts():
    print('Start loading accounts dataset...')
    accounts = load_accounts_dataset()
    print('Finish loading accounts dataset...')
    print('Example of account: '
            + '\n\tAccountId: ' + str(accounts[0].account_id)
            + '\n\tDistrictId: ' + str(accounts[0].district_id)
            + '\n\tFrequency: ' + accounts[0].frequency
            + '\n\tDate: ' + str(accounts[0].date))
    print('\n')

    return accounts
def load_clients():
    print('Start loading clients dataset...')
    clients = load_clients_dataset()
    print('Finish loading clients dataset...')
    print('Example of client: '
            + '\n\tClientId: ' + str(clients[0].client_id) +
            '\n\tDistrictId: ' + str(clients[0].district_id) +
            '\n\tAge: ' + str(clients[0].age) +
            '\n\tGenre: ' + str(clients[0].genre))
    print('\n')

    return clients 
def load_cards(dataset_type):
    keyword = 'unknown'
    if "train" in dataset_type:
        keyword = 'train'
    if "test" in dataset_type:
        keyword = 'test'
    
    print('Start loading cards ' + keyword + ' dataset...')
    cards = load_card_dataset(dataset_type)
    print('Finish loading cards train dataset...')
    print('Example of card: '
            + '\n\tCardId: ' + str(cards[0].card_id)
            + '\n\tDispositionId: ' + str(cards[0].disp_id)
            + '\n\tType: ' + str(cards[0].card_type)
            + '\n\tIssuedDate: ' + str(cards[0].issued_date))
    print('\n')

    return cards
def load_dispositions():
    print('Start loading dispositions dataset...')
    dispositions = load_dispositions_dataset()
    print('Finish loading dispositions dataset...')
    print('Example of disposition: '
            + '\n\tDispositionId: ' + str(dispositions[0].disp_id)
            + '\n\tClientId: ' + str(dispositions[0].client_id)
            + '\n\tAccountId: ' + str(dispositions[0].account_id)
            + '\n\tType: ' + str(dispositions[0].disposition_type))
    print('\n')

    return dispositions
def load_districts():
    print('Start loading districts dataset...')
    districts = load_districts_dataset()
    print('Finish loading districts dataset...')
    print('Example of district: '
            + '\n\tDistrictId: ' + str(districts[0].district_id)
            + '\n\tDistrictName: ' + districts[0].name
            + '\n\tRegion: ' + districts[0].region
            + '\n\tNumberOfInhabitants: ' + str(districts[0].no_of_inhabitants)
            + '\n\tNumberOfMunicipalitiesWithInhabitants<499: ' + str(districts[0].no_of_municipalities_with_inhabitants_lt_499)
            + '\n\tNumberOfMunicipalitiesWithInhabitants500-1999: ' + str(districts[0].no_of_municipalities_with_inhabitants_gt_500_lt_1999)
            + '\n\tNumberOfMunicipalitiesWithInhabitants2000-9999: ' + str(districts[0].no_of_municipalities_with_inhabitants_gt2000_lt_9999)
            + '\n\tNumberOfMunicipalitiesWithInhabitants>10000: ' + str(districts[0].no_of_municipalities_with_inhabitants_gt_10000)
            + '\n\tNumberOfCities: ' + str(districts[0].no_of_cities)
            + '\n\tRatioOfUrbanInhabitants: ' + str(districts[0].ratio_of_urban_inhabitants)
            + '\n\tAverageSalary: ' + str(districts[0].average_salary)
            + '\n\tUnemploymantRate95: ' + str(districts[0].unemploymant_rate_95)
            + '\n\tUnemploymantRate96: ' + str(districts[0].unemploymant_rate_96)
            + '\n\tNumberOfEnterpreneursPer1000Inhabitants: ' + str(districts[0].no_of_enterpreneurs_per_1000_inhabitants)
            + '\n\tNumberOfCommitedCrimes1995: ' + str(districts[0].no_of_commited_crimes_1995)
            + '\n\tNumberOfCommitedCrimes1996: ' + str(districts[0].no_of_commited_crimes_1996))
    print('\n')

    return districts
def load_loans(dataset_type):
    keyword = 'unknown'
    if "train" in dataset_type:
        keyword = 'train'
    if "test" in dataset_type:
        keyword = 'test'

    print('Start loading loans ' + keyword + ' dataset...')
    loans = load_loan_dataset(dataset_type)
    print('Finish loading loans train dataset...')
    print('Example of loan: ' + '\n\tLoanId: ' + str(loans[0].loan_id)
            + '\n\tAccountId: ' + str(loans[0].account_id)
            + '\n\tDate: ' + str(loans[0].date)
            + '\n\tAmount: ' + str(loans[0].amount)
            + '\n\tDuration: ' + str(loans[0].duration)
            + '\n\tPayments: ' + str(loans[0].payments)
            + '\n\tStatus: ' + str(loans[0].status))
    print('\n')

    return loans
def load_transactions(dataset_type):
    keyword = 'unknown'
    if "train" in dataset_type:
        keyword = 'train'
    if "test" in dataset_type:
        keyword = 'test'

    print('Start loading transactions ' + keyword + ' dataset...')
    transactions = load_trans_dataset(dataset_type)
    print('Finish loading transactions train dataset...')
    print('\n')

    return transactions

#Loading loan_train dataset
def load_trans_dataset(dataset_type):
    transactions = []
    a = Loader(FILES_COMPETITION +  dataset_type)
    for entry in a.data:
        if not entry[7]:
            print("K Symbol is unknown...")
            k_symbol = None
        else:
            k_symbol = entry[7]
        if entry[4] == 'collection from another bank' and not entry[8]:
            print("Bank is unknown...")
            bank = None
        elif not entry[8]:
            bank = None
        else:
            bank = entry[8]
        try:
            if entry[4] == 'collection from another bank':
                account = int(entry[9])
            else:
                account = None
        except ValueError:
            print("Account is unknown...")
            account = None

        transactions.append(TransactionRaw(int(entry[0]), int(entry[1]), convert_datetime(entry[2]), entry[3], entry[4], float(entry[5]), float(entry[6]), k_symbol, bank, account))

    return transactions
#Loading loan_train dataset
def load_loan_dataset(dataset_type):
    loans = []
    a = Loader(FILES_COMPETITION +  dataset_type)
    for entry in a.data:
        if 'test' in dataset_type:
            status = None
        else:
            status = int(entry[6])

        loans.append(LoanRaw(int(entry[0]), int(entry[1]), convert_datetime(entry[2]), int(entry[3]), int(entry[4]), int(entry[5]), status))

    return loans
#Loading districts dataset
def load_districts_dataset():
    districts = []
    a = Loader(FILES_COMPETITION +  'district.csv')
    for entry in a.data:
        try:
            number_of_inhabitants = int(entry[3])
        except ValueError:
            print("Number of Inhabitants is unknown...")
            number_of_inhabitants = None

        try:
            no_of_municipalities_with_inhabitants_lt_499 = int(entry[4])
        except ValueError:
            print("Number of Municipalities with Inhabitants less than 499 is unknown...")
            no_of_municipalities_with_inhabitants_lt_499 = None
        
        try:
            no_of_municipalities_with_inhabitants_gt_500_lt_1999 = int(entry[5])
        except ValueError:
            print("Number of Municipalities with Inhabitants greater than 500 and less than 1999 is unknown...")
            no_of_municipalities_with_inhabitants_gt_500_lt_1999 = None

        try:
            no_of_municipalities_with_inhabitants_gt2000_lt_9999 = int(entry[6])
        except ValueError:
            print("Number of Municipalities with Inhabitants greater than 2000 and less than 9999 is unknown...")
            no_of_municipalities_with_inhabitants_gt2000_lt_9999 = None

        try:
            no_of_municipalities_with_inhabitants_gt_10000 = int(entry[7])
        except ValueError:
            print("Number of Municipalities with Inhabitants greater than 1000 is unknown...")
            no_of_municipalities_with_inhabitants_gt_10000 = None

        try:
            no_of_cities = int(entry[8])
        except ValueError:
            print("Number of cities is unknown...")
            no_of_cities = None

        try:
            ratio_of_urban_inhabitants = float(entry[9])
        except ValueError:
            print("Ratio of urban inhabitants is unknown...")
            ratio_of_urban_inhabitants = None

        try:
            average_salary = int(entry[10])
        except ValueError:
            print("Average salary is unknown...")
            average_salary = None

        try:
            unemploymant_rate_95 = float(entry[11])
        except ValueError:
            print("Unemploymant rate in 95 is unknown...")
            unemploymant_rate_95 = None

        try:
            unemploymant_rate_96 = float(entry[12])
        except ValueError:
            print("Unemploymant rate in 96 is unknown...")
            unemploymant_rate_96 = None

        try:
            no_of_enterpreneurs_per_1000_inhabitants = int(entry[13])
        except ValueError:
            print("Number of enterpreneurs per 1000 inhabitants is unknown...")
            no_of_enterpreneurs_per_1000_inhabitants = None

        try:
            no_of_commited_crimes_1995 = int(entry[14])
        except ValueError:
            print("Number of commited crimes in 1995 is unknown...")
            no_of_commited_crimes_1995 = None

        try:
            no_of_commited_crimes_1996 = int(entry[15])
        except ValueError:
            print("Number of commited crimes in 1996 is unknown...")
            no_of_commited_crimes_1996 = None

        districts.append(
            DistrictRaw(
                int(entry[0]),
                entry[1],
                entry[2],
                number_of_inhabitants,
                no_of_municipalities_with_inhabitants_lt_499,
                no_of_municipalities_with_inhabitants_gt_500_lt_1999,
                no_of_municipalities_with_inhabitants_gt2000_lt_9999,
                no_of_municipalities_with_inhabitants_gt_10000,
                no_of_cities,
                ratio_of_urban_inhabitants,
                average_salary,
                unemploymant_rate_95,
                unemploymant_rate_96,
                no_of_enterpreneurs_per_1000_inhabitants,
                no_of_commited_crimes_1995,
                no_of_commited_crimes_1996
            )
        )

    return districts
#Loading dispositions dataset
def load_dispositions_dataset():
    dispositions = []
    a = Loader(FILES_COMPETITION +  'disp.csv')
    for entry in a.data:
        dispositions.append(DispositionRaw(int(entry[0]), int(entry[1]), int(entry[2]), entry[3]))

    return dispositions
#Loading card_train dataset
def load_card_dataset(dataset_type):
    cards = []
    a = Loader(FILES_COMPETITION +  dataset_type)
    for entry in a.data:
        cards.append(CardRaw(int(entry[0]), int(entry[1]), entry[2], convert_datetime(entry[3])))

    return cards
#Loading clients dataset
def load_clients_dataset():
    clients = []
    a = Loader(FILES_COMPETITION +  'client_final.csv')
    for entry in a.data:
        clients.append(ClientRaw(int(entry[0]), int(entry[1]), entry[2],int(entry[3])))

    return clients
#Loading accounts dataset
def load_accounts_dataset():
    accounts = []
    a = Loader(FILES_COMPETITION +  'account.csv')
    for entry in a.data:
        accounts.append(AccountRaw(int(entry[0]), int(entry[1]), entry[2], convert_datetime(entry[3])))

    return accounts

def get_negative_balance_clients(clients, dispositions, accounts, transactions):
    negative_balance_clients = []

    for client in clients:
        for disposition in dispositions:
            if client.client_id == disposition.disp_id:
                for account in accounts:
                    if account.account_id == disposition.account_id:
                        for transaction in transactions:
                            if transaction.account_id == account.account_id and transaction.balance < 0:
                                negative_balance_clients.append(client.client_id)
    return negative_balance_clients

def get_loans_with_negative_balance(loans, transactions):
    loans_dict = {}

    for loan in loans:
        is_balance_negative = False
        for transaction in transactions:
            if loan.account_id == transaction.account_id and transaction.balance < 0:
                is_balance_negative = True
                break
        loans_dict[loan.loan_id] = { 'negative_balance': is_balance_negative }

    return loans_dict

def average_salary_per_district(accounts, districts, loans, dictionary):
    #vai buscar o average salary, average unemploymant_rate e entrepreneurs_ratio
    account_average_salary_per_district = {}

    for account in accounts:
        for district in districts:
            if account.district_id == district.district_id:
                account_average_salary_per_district[account.account_id] ={'average_salary': district.average_salary}
                unemploymant_rate = (district.unemploymant_rate_95 + district.unemploymant_rate_96*2)/3
                account_average_salary_per_district[account.account_id]['unemploymant_rate'] = unemploymant_rate
                account_average_salary_per_district[account.account_id]['entrepreneurs_ratio'] = district.no_of_enterpreneurs_per_1000_inhabitants

    for loan in loans:
       if loan.account_id in account_average_salary_per_district:
            dictionary[loan.loan_id]['average_salary'] = account_average_salary_per_district[loan.account_id]['average_salary']
            dictionary[loan.loan_id]['unemploymant_rate'] = account_average_salary_per_district[loan.account_id]['unemploymant_rate']
            dictionary[loan.loan_id]['entrepreneurs_ratio'] = account_average_salary_per_district[loan.account_id]['entrepreneurs_ratio']

    return dictionary

def loan_information(loans, dictionary):
    #vai buscar o loan duration e o monthly payment
    for loan in loans:
        dictionary[loan.loan_id]['loan_duration'] = loan.duration
        dictionary[loan.loan_id]['monthly_payment'] = loan.payments
        dictionary[loan.loan_id]['status'] = loan.status

    return dictionary

def get_balances(transactions, loans, dictionary):
    account_transactions = {}

    for transaction in transactions:
        if transaction.account_id in account_transactions:
            account_transactions[transaction.account_id].append(transaction.balance)
        else:
            account_transactions[transaction.account_id] = [transaction.balance]

    for loan in loans:
       if loan.account_id in account_transactions:
            dictionary[loan.loan_id]['max_balance'] = max(account_transactions[loan.account_id])
            dictionary[loan.loan_id]['min_balance'] = min(account_transactions[loan.account_id])
            dictionary[loan.loan_id]['avg_balance'] = sum(account_transactions[loan.account_id])/float(len(account_transactions[loan.account_id]))

    return dictionary 

def get_clients_information(clients, dispositions, loans, dictionary):
    clients_info = {}

    for client in clients:
        for disposition in dispositions:
            if client.client_id == disposition.client_id:
                clients_info[disposition.account_id] = {'age': client.age, 'genre': client.genre}
    for loan in loans:
        if loan.account_id in clients_info:
            dictionary[loan.loan_id]['age'] = clients_info[loan.account_id]['age']
            dictionary[loan.loan_id]['genre'] = clients_info[loan.account_id]['genre']

    return dictionary

def write_features_to_file(loans_features_train, loans_features_test):
    
    with open('features_train.csv', 'w') as file:
        file.write('loan_id;negative_balance;average_salary;unemploymant_rate;entrepreneurs_ratio;loan_duration;monthly_payment;max_balance;min_balance;avg_balance;age;genre;status\n')
        for key, value in loans_features_train.items():
            file.write(str(key) +';'+str(value['negative_balance'])+';'+str(value['average_salary'])+';'+str(value['unemploymant_rate'])+';'+str(value['entrepreneurs_ratio'])+ ';'+ str(value['loan_duration']) + ';' + str(value['monthly_payment'])+';'+str(value['max_balance'])+';'+str(value['min_balance'])+';'+ str(value['avg_balance'])+ ';' + str(value['age']) +';'+str(value['genre'])+';'+str(value['status']) + '\n')

    with open('features_test.csv', 'w') as file:
        file.write('loan_id;negative_balance;average_salary;unemploymant_rate;entrepreneurs_ratio;loan_duration;monthly_payment;max_balance;min_balance;avg_balance;age;genre;status\n')
        for key, value in loans_features_test.items():
            file.write(str(key) +';'+str(value['negative_balance'])+';'+str(value['average_salary'])+';'+str(value['unemploymant_rate'])+';'+str(value['entrepreneurs_ratio'])+ ';'+ str(value['loan_duration']) + ';' + str(value['monthly_payment'])+';'+ str(value['max_balance'])+';'+str(value['min_balance'])+';'+str(value['avg_balance'])+ ';' + str(value['age'])+ ';' + str(value['genre']) + '; \n')

def main():
    accounts = load_accounts()
    clients = load_clients()
    cards_train = load_cards('card_train.csv')
    dispositions = load_dispositions()
    districts = load_districts()
    loans_train = load_loans('loan_train.csv')
    transactions_train = load_transactions('trans_train.csv')

    loans_test = load_loans('loan_test.csv')
    transactions_test = load_transactions('trans_test.csv')
    
    train_data = get_loans_with_negative_balance(loans_train, transactions_train)
    train_test = get_loans_with_negative_balance(loans_test, transactions_test)

    loan_salary_per_district_train = average_salary_per_district(accounts,districts, loans_train, train_data )
    loan_salary_per_district_test = average_salary_per_district(accounts,districts, loans_test, train_test)

    loan_info_train = loan_information(loans_train, loan_salary_per_district_train)
    loan_info_test = loan_information(loans_test, loan_salary_per_district_test)

    balances_test = get_balances(transactions_test, loans_test, loan_info_test)
    balances_train = get_balances(transactions_train, loans_train, loan_info_train)

    clients_information_test = get_clients_information(clients, dispositions, loans_test, balances_test)
    clients_information_train = get_clients_information(clients, dispositions, loans_train, balances_train)
 
    write_features_to_file(clients_information_train, clients_information_test)

if __name__ == "__main__":
    main()