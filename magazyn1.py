import streamlit as st

# --- Konfiguracja i Inicjalizacja Magazynu ---

# Inicjalizacja magazynu w st.session_state, jeśli jeszcze nie istnieje
if 'inventory' not in st.session_state:
    st.session_state.inventory = ["Laptop", "Monitor", "Myszka", "Klawiatura"]

def add_item(new_item):
    """Dodaje nowy towar do magazynu."""
    if new_item and new_item not in st.session_state.inventory:
        st.session_state.inventory.append(new_item)
        st.success(f"Dodano: {new_item}")
    elif new_item in st.session_state.inventory:
        st.warning(f"Towar '{new_item}' już znajduje się w magazynie.")

def delete_item(item_to_delete):
    """Usuwa wybrany towar z magazynu."""
    if item_to_delete in st.session_state.inventory:
        st.session_state.inventory.remove(item_to_delete)
        st.success(f"Usunięto: {item_to_delete}")
    else:
        st.error(f"Błąd: Towar '{item_to_delete}' nie znaleziono.")

# --- Interfejs Użytkownika Streamlit ---

st.title("📦 Prosty Magazyn Streamlit")
st.markdown("Aplikacja do zarządzania prostym magazynem za pomocą listy.")


# 1. Sekcja Dodawania Towaru
st.header("➕ Dodaj Nowy Towar")
with st.form("add_form", clear_on_submit=True):
    new_item_input = st.text_input("Nazwa Towaru:", key="new_item_key")
    submitted = st.form_submit_button("Dodaj do Magazynu")

    if submitted:
        # Konwersja na tytułowy format i wywołanie funkcji dodawania
        add_item(new_item_input.strip().title())


# 2. Sekcja Wyświetlania Magazynu
st.header("📊 Aktualny Magazyn")

if st.session_state.inventory:
    # Używamy st.dataframe do schludnego wyświetlenia listy
    inventory_df = st.dataframe(
        {"Towar": st.session_state.inventory},
        use_container_width=True,
        hide_index=True
    )

    # 3. Sekcja Usuwania Towaru
    st.header("➖ Usuń Towar")
    # Widget st.selectbox do wyboru towaru do usunięcia
    item_to_remove = st.selectbox(
        "Wybierz towar do usunięcia:",
        options=st.session_state.inventory,
        key="remove_item_key"
    )

    if st.button("Usuń Wybrany Towar", key="delete_button"):
        delete_item(item_to_remove)
        # Ponowne uruchomienie, aby odświeżyć listę (wymagane w tym prostym przypadku użycia)
        st.experimental_rerun() 
        
else:
    st.info("Magazyn jest pusty. Dodaj pierwszy towar!")
