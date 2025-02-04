import streamlit as st
from decimal import Decimal
from debt_optimizer import DebtOptimizer
from forecast import predict_future
from calendar_service import generate_payment_calendar
from net_worth import calculate_net_worth
from plaid_auth import create_plaid_client, create_link_token
from firebase.firestore import save_simulation, load_simulations
from achievements import check_achievements
import datetime

# Initialize session state
if 'debts' not in st.session_state:
    st.session_state.debts = []
if 'simulations' not in st.session_state:
    st.session_state.simulations = []

# Main UI
st.title("💰 Ultimate Debt Destroyer Pro")

# Sidebar controls
with st.sidebar:
    st.header("⚙️ Configuration")
    strategy = st.selectbox(
        "Payment Strategy",
        ['Snowball', 'Avalanche', 'Hybrid'],
        index=1
    )
    extra_payment = st.number_input("Extra Monthly Payment", min_value=0, value=500)

# Debt input section
with st.expander("➕ Add Debts", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        name = st.text_input("Debt Name")
    with col2:
        balance = st.number_input("Balance", min_value=0.0)
    with col3:
        rate = st.number_input("Interest Rate (%)", min_value=0.0)
    
    if st.button("Add Debt"):
        st.session_state.debts.append({
            'name': name,
            'balance': balance,
            'rate': rate / 100,
            'min_payment': balance * 0.02  # Auto-calculate min payment
        })

# Main simulation
if st.button("🚀 Run Full Analysis"):
    optimizer = DebtOptimizer(
        debts=st.session_state.debts,
        strategy=strategy,
        extra_payment=extra_payment
    )
    
    with st.spinner("Crunching numbers..."):
        simulation = optimizer.calculate()
        st.session_state.simulations.append(simulation)
        
        # Show results
        st.subheader("📊 Results")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Interest Paid", f"€{sum(p['interest'] for p in simulation):,.2f}")
        with col2:
            st.metric("Time to Freedom", f"{len(simulation)} months")
        
        # Show forecast
        st.plotly_chart(predict_future(simulation))
        
        # Download options
        st.download_button(
            "📅 Download Payment Calendar",
            generate_payment_calendar(simulation),
            file_name="payment_schedule.ics"
        )

# Achievement system
achievements = check_achievements(st.session_state.simulations)
if achievements:
    st.write("## 🏆 Achievements")
    cols = st.columns(4)
    for idx, ach in enumerate(achievements):
        cols[idx % 4].success(ach)

# Net worth calculator
with st.expander("📈 Net Worth Tracker"):
    assets = {
        'savings': st.number_input("Savings", value=0.0),
        'investments': st.number_input("Investments", value=0.0)
    }
    st.metric("Current Net Worth", 
             f"€{calculate_net_worth(assets, st.session_state.debts):,.2f}")