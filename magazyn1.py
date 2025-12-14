import streamlit as st

# Magazyn jest zdefiniowany jako zwykła lista
# UWAGA: Ta lista zostanie zresetowana przy każdym przebiegu skryptu Streamlit
inventory = ["Laptop", "Monitor", "Myszka", "Klawiatura"]

st.title("📦 Prosty Magazyn Streamlit (Bez Session State)")
st.markdown("Aplikacja demonstrująca logikę dodawania/usuwania na stałej liście.")

# Funkcje modyfikujące stan (który jest tymczasowy)
def add_item(new_item, current_inventory):
    """Dodaje nowy towar do przekazanej listy."""
    if new_item and new_item not in current_inventory:
        current_inventory.append(new_item)
        st.success(f"Dodano: {new_item}")
    elif new_item in current_inventory:
        st.warning(f"Towar '{new_item}' już znajduje się w magazynie.")

def delete_item(item_to_delete, current_inventory):
    """Usuwa wybrany towar z przekazanej listy."""
    if item_to_delete in current_inventory:
        current_inventory.remove(item_to_delete)
        st.success(f"Usunięto: {item_to_delete}")
    else:
        st.error(f"Błąd: Towar '{item_to_delete}' nie znaleziono.")

# --- Sekcja Dodawania Towaru ---
st.header("➕ Dodaj Nowy Towar")
with st.form("add_form", clear_on_submit=True):
    new_item_input = st.text_input("Nazwa Towaru:")
    submitted_add = st.form_submit_button("Dodaj do Magazynu")

    if submitted_add:
        # Konwersja na tytułowy format i wywołanie funkcji
        add_item(new_item_input.strip().title(), inventory)

# --- Sekcja Usuwania Towaru ---
st.header("➖ Usuń Towar")
with st.form("remove_form"):
    if inventory:
        # Wybieranie towaru do usunięcia
        item_to_remove = st.selectbox(
            "Wybierz towar do usunięcia:",
            options=inventory
        )
        submitted_remove = st.form_submit_button("Usuń Wybrany Towar")

        if submitted_remove:
            delete_item(item_to_remove, inventory)
    else:
        st.info("Magazyn jest pusty.")

# --- Sekcja Wyświetlania Magazynu ---
st.header("📊 Aktualny Magazyn")
if inventory:
    # Wyświetlanie aktualnej listy (po ewentualnej modyfikacji w formularzu)
    st.dataframe(
        {"Towar": inventory},
        use_container_width=True,
        hide_index=True
    )
else:
    st.info("Magazyn jest pusty. Dodaj pierwszy towar!")
