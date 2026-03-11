import streamlit as st

# Page settings
st.set_page_config(page_title="SBI Bank App", page_icon="🏦", layout="wide")

class BankApplication:
    bank_name = "SBI"

    def __init__(self, name, account_number, age, mobile_number, balance):
        self.name = name
        self.account_number = account_number
        self.age = age
        self.mobile_number = mobile_number
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"✅ Transaction Successful! Collected ₹{amount}"
        else:
            return "❌ Insufficient Balance"

    def deposit(self, amount):
        self.balance += amount
        return f"✅ Deposit Successful! Total Balance: ₹{self.balance}"

    def update_mobile(self, new_number):
        self.mobile_number = new_number
        return f"📱 Mobile number updated: {self.mobile_number}"

    def check_balance(self):
        return f"💰 Total Account Balance: ₹{self.balance}"


# Title
st.title("🏦 SBI Digital Banking")

st.markdown("---")

# Session state
if "account" not in st.session_state:
    st.session_state.account = None

# Sidebar Menu
menu = st.sidebar.selectbox(
    "📌 Select Option",
    ["Create Account", "Deposit Money", "Withdraw Money", "Check Balance", "Update Mobile"]
)

# ---------------- CREATE ACCOUNT ----------------
if menu == "Create Account":

    st.subheader("📝 Open New Bank Account")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=1)

    with col2:
        acc_no = st.text_input("Account Number")
        mobile = st.text_input("Mobile Number")

    balance = st.number_input("Initial Balance", min_value=0)

    if st.button("🏦 Create Account"):
        st.session_state.account = BankApplication(name, acc_no, age, mobile, balance)
        st.success("🎉 Account Created Successfully!")

# ---------------- DEPOSIT ----------------
elif menu == "Deposit Money":

    st.subheader("💰 Deposit Money")

    if st.session_state.account:
        amount = st.number_input("Enter Amount", min_value=1)

        if st.button("Deposit"):
            result = st.session_state.account.deposit(amount)
            st.success(result)
    else:
        st.warning("⚠ Please create an account first.")

# ---------------- WITHDRAW ----------------
elif menu == "Withdraw Money":

    st.subheader("💸 Withdraw Money")

    if st.session_state.account:
        amount = st.number_input("Enter Amount", min_value=1)

        if st.button("Withdraw"):
            result = st.session_state.account.withdraw(amount)
            st.success(result)
    else:
        st.warning("⚠ Please create an account first.")

# ---------------- CHECK BALANCE ----------------
elif menu == "Check Balance":

    st.subheader("📊 Account Balance")

    if st.session_state.account:
        st.info(st.session_state.account.check_balance())
    else:
        st.warning("⚠ Please create an account first.")

# ---------------- UPDATE MOBILE ----------------
elif menu == "Update Mobile":

    st.subheader("📱 Update Mobile Number")

    if st.session_state.account:
        new_mobile = st.text_input("Enter New Mobile Number")

        if st.button("Update"):
            result = st.session_state.account.update_mobile(new_mobile)
            st.success(result)
    else:
        st.warning("⚠ Please create an account first.")

# Footer
st.markdown("---")
st.caption("🏦 SBI Digital Banking App | Built with Streamlit")