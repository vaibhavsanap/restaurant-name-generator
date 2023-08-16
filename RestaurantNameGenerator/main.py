import streamlit as st
import langchain_helper


if __name__ == '__main__':
    st.title("Restaurant Name Generator")

    cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American"))

    if cuisine:
        response = langchain_helper.generate_restaurant_name_and_items(cuisine)
        st.header(response['restaurant_name'].strip())
        menu_items = response['menu_items'].strip().split(",")
        print(menu_items)
        st.write("**Menu Items**")
        for item in menu_items:
            st.write("-", item)

