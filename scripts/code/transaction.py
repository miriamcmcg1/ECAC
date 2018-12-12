class TransactionRaw:
    def __init__(self, trans_id, account_id, date, transaction_type, operation, amount, balance, k_symbol, bank, account):
        self.trans_id = trans_id
        self.account_id = account_id
        self.date = date
        self.transaction_type = transaction_type
        self.operation = operation
        self.amount = amount
        self.balance = balance
        self.k_symbol = k_symbol
        self.bank = bank
        self.account = account
