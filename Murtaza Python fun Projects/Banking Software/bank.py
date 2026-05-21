import random, streamlit as st
bank_all_accounts = []
bank_all_closed_accounts = []

if "bank_all_accounts" not in st.session_state:
    st.session_state.bank_all_accounts = []


def open_account(cnic, title, initial_deposit=0):
    account={'cnic':cnic,'balance':initial_deposit}
    account['account_title']= title
    account['pin'] = random.randint(1000,9999)
    account['account_number'] = random.randint(1000000,9999999)
    st.session_state.bank_all_accounts.append(account)
    return account

def check_balance(account_number,pin):
    for acc in st.session_state.bank_all_accounts:
        if acc['account_number']==account_number:
            if acc['pin']==pin:
                return {acc['balance']}
            else:
                return "Invalid Pin"
    else:
        return  'Invalid Account'

def cash_withdrawl(account_number, pin, amount):
    for acc in st.session_state.bank_all_accounts:
        if acc['account_number']==account_number:
            if acc['pin']==pin:
                if acc['balance']>=amount:
                    acc['balance']-=amount
                    return amount
                else:
                    return 'Insufficient Balance!'                
            else:
                return "Invalid Pin"    
    else:
        return 'Invalid Account'

def cash_deposit(account_number, amount):
    for acc in st.session_state.bank_all_accounts:
        if acc['account_number']==account_number:
            acc['balance']+=amount
            return amount
    else:
        return 'nvalid Account'

def transfer(account_number, pin, amount, beneficiary_acc):
    for acc in st.session_state.bank_all_accounts:
        if acc['account_number']==account_number:
            if acc['pin']==pin:
                if acc['balance']>=amount:
                    for bacc in st.session_state.bank_all_accounts:
                        if bacc['account_number']==beneficiary_acc:
                            acc['balance']-=amount
                            bacc['balance']+=amount
                            return amount
                    else:
                        return 'Invalid Beneficiary Account'
                else:
                    return 'Insufficient Balance!'                
            else:
                return "Invalid Pin"    
    else:
        return 'Invalid Account'
def close_account(account_number, pin):
    for index, acc in enumerate(st.session_state.bank_all_accounts):
        if acc['account_number']==account_number:
            if acc['pin']==pin:                
                st.session_state.bank_all_closed_accounts.append(st.session_state.bank_all_accounts.pop(index))
                return acc['balance']        
            else:
                return "Invalid Pin"
    else:
        return "Account Not Found"

def change_pin(account_number, pin, new_pin):
    for acc in st.session_state.bank_all_accounts:
        if acc['account_number']==account_number:
            if acc['pin']==pin:
                acc['pin'] = new_pin
                return "Your pin changed Successfully!"
            
            else:
                return "Invalid Pin"
    else:
        return "Account Not Found"

def show_all_accounts():
    return st.session_state.bank_all_accounts


# ---------------------------------------------
# Streamlit UI
# ---------------------------------------------

st.title("🏦 Simple Banking System - Streamlit Interface")

menu = st.sidebar.selectbox(
    "Select Action",
    ["Open Account", "Check Balance", "Deposit", "Withdraw", "Transfer", "changePin", "Close Account", "Show All Accounts"]
)

# ---------------------------------------------
# Open Account
# ---------------------------------------------
if menu == "Open Account":
    st.header("➕ Open a New Account")

    cnic = st.text_input("Enter CNIC")
    title = st.text_input("Account Title")
    deposit = st.number_input("Initial Deposit", min_value=0)

    if st.button("Create Account"):
        acc = open_account(cnic, title, deposit)
        st.success("🎉 Account Created Successfully!")
        st.write(f"**Account Number:** {acc['account_number']}")
        st.write(f"**PIN:** {acc['pin']} (Save this!)")

# ---------------------------------------------
# Check Balance
# ---------------------------------------------
elif menu == "Check Balance":
    st.header("💰 Check Balance")

    acc_no = st.number_input("Account Number", min_value=1000000, max_value=9999999)
    pin = st.number_input("PIN", min_value=1000, max_value=9999)

    if st.button("Show Balance"):
        bal= check_balance(acc_no, pin)        
        st.success(f"Your Current Balance is: **Rs {bal}**")

# ---------------------------------------------
# Deposit
# ---------------------------------------------
elif menu == "Deposit":
    st.header("📥 Deposit Amount")

    acc_no = st.number_input("Account Number", min_value=1000000, max_value=9999999)
    amt = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        bal= cash_deposit(acc_no, amt)
        st.success(f"Amount Deposited! New Balance: **Rs {bal}**")

# ---------------------------------------------
# Withdraw
# ---------------------------------------------
elif menu == "Withdraw":
    st.header("📤 Withdraw Amount")

    acc_no = st.number_input("Account Number", min_value=1000000, max_value=9999999)
    pin = st.number_input("PIN", min_value=1000, max_value=9999)
    amt = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        bal= cash_withdrawl(acc_no, pin, amt)
        st.success(f"Withdrawal Successful! New Balance: **Rs {bal}**")

# ---------------------------------------------
# Transfer
# ---------------------------------------------
elif menu == "Transfer":
    st.header("💸 Transfer Amount")

    acc_no = st.number_input("Your Account Number", min_value=1000000, max_value=9999999)
    pin = st.number_input("Your PIN", min_value=1000, max_value=9999)
    amt = st.number_input("Amount", min_value=1)
    ben = st.number_input("Beneficiary Account Number", min_value=1000000, max_value=9999999)

    if st.button("Transfer"):
        bal= transfer(acc_no, pin, amt, ben)
        st.success(f"Transfer Successful! Remaining Balance: **Rs {bal}**")

# ---------------------------------------------
# Show All Accounts (debug screen)
# ---------------------------------------------
elif menu == "Show All Accounts":
    st.header("📋 All Accounts (Debug View)")
    st.write(st.session_state.bank_all_accounts)

