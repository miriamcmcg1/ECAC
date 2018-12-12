class LoanRaw:
    def __init__(self, loan_id, account_id, date, amount, duration, payments, status):
        self.loan_id = loan_id
        self.account_id = account_id
        self.date = date
        self.amount = amount
        self.duration = duration
        self.payments = payments
        self.status = status