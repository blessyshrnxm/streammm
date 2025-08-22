import streamlit as st
import pandas as pd
import plotly.express as px
st.title("Supermarket Daily sales tracker")
if "sales" not in st.session_state:
    st.session_state.sales=pd.DataFrame(columns=["Product","Quantity","Price"
,"Revenue"])
with st.form("sales_form"):
    product=st.text_input("Enter the product name")
    quantity=st.number_input("Enter the quantity",min_value=1,step=1)
    price=st.number_input("Enter the price  per unit",min_value=0.0,step=0.5)
    submit=st.form_submit_button("Add Sale")
if submit and product:
    revenue=quantity*price
    new_row={"Product":product,"Quantity":quantity,"Price":price,"Revenue":revenue}
    st.session_state.sales=pd.concat([st.session_state.sales,pd.DataFrame([new_row])],ignore_index=True)
    st.success(f"Added the product {product},Revenue made: revenue")
    st.subheader("Sales Record")
    st.dataframe(st.session_state.sales,use_container_width=True)
total_revenue=st.session_state.sales["Revenue"].sum()
st.metric("Total revenue Today",f"${total_revenue}")
if not st.session_state.sales.empty:
    fig = px.bar(
        st.session_state.sales,
        x="Product",
        y="Revenue",
        color="Product",
        title="Revenue by Product",
        text="Revenue"
    )
    st.plotly_chart(fig, use_container_width=True)