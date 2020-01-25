from decimal import Decimal
from dateutil.parser import parse


from bricklane_platform.models.bank import BankAccount
from bricklane_platform.config import PAYMENT_FEE_RATE


class BankPayment(object):

    customer_id = None
    date = None
    amount = None
    fee = None
    account_id = None


    def __init__(self, data=None):

        if not data:
            return

        self.customer_id = int(data["customer_id"])
        self.date = parse(data["date"])

        total_amount = Decimal(data["amount"])
        self.fee = total_amount * PAYMENT_FEE_RATE
        self.amount = total_amount - self.fee

        bank = BankAccount()
        bank.account_id = int(data["bank_account_id"])
        self.bank = bank

    def is_successful(self):
        return True