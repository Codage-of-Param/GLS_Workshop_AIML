
import streamlit as st


# Title
st.title("🏠 Home Energy Calculator")

# User Profile Input
st.header("👤 User Profile")
name = st.text_input("Enter your Name")
age = st.number_input("Enter your Age", min_value=1, step=1)
city = st.text_input("Enter your City")
area = st.text_input("Enter your Area")

# Store profile
if name and city and area:
    profile = [(name, age, city, area)]
    st.success(f"Profile Saved: {profile}")

# BHK and Appliances
st.header("🧾 Appliance Usage")

bhk = st.number_input("Number of BHK", min_value=1, step=1)
lights = st.number_input("Number of Lights", min_value=0, step=1)
fans = st.number_input("Number of Fans", min_value=0, step=1)
tv = st.number_input("Number of TVs", min_value=0, step=1)

# Optional appliances with default 0
ac = 0
fridge = 0
wm = 0

if st.checkbox("Do you have Air Conditioner?"):
    ac = st.number_input("Number of Air Conditioners", min_value=0, step=1)

if st.checkbox("Do you have Fridge?"):
    fridge = st.number_input("Number of Fridges", min_value=0, step=1)

if st.checkbox("Do you have Washing Machine?"):
    wm = st.number_input("Number of Washing Machines", min_value=0, step=1)

# Energy Calculation
st.header("⚡ Energy Consumption")

cal_energy = (
    lights * 0.2 +
    fans * 0.2 +
    tv * 0.3 +
    ac * 3.0 +
    fridge * 3.1 +
    wm * 2.8
)

rate_per_unit = 8  # ₹ per kWh
total_cost = round(cal_energy * rate_per_unit, 2)

# Display Results
st.subheader(f"🔋 Total Energy Used: {cal_energy:.2f} kWh")
st.subheader(f"💰 Estimated Bill: ₹{total_cost}")

# Optional: Energy breakdown table
st.header("📊 Energy Breakdown")
breakdown_data = {
    "Appliance": ["Lights", "Fans", "TV", "Air Conditioner", "Fridge", "Washing Machine"],
    "Quantity": [lights, fans, tv, ac, fridge, wm],
    "Energy Consumption (kWh)": [
        lights * 0.2,
        fans * 0.2,
        tv * 0.3,
        ac * 3.0,
        fridge * 3.1,
        wm * 2.8
    ]
}

st.table(breakdown_data)
