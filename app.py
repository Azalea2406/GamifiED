import streamlit as st
from Authentication import login_page  # or from Authentication import login_page if it's a subfolder

def main():
    login_page.login_page()

if __name__ == "__main__":
    main()
