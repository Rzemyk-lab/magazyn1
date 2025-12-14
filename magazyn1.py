import streamlit as st

# --- Konfiguracja Strony Streamlit ---
st.set_page_config(
    page_title="📦 Smart Magazyn App",
    page_icon="🚛",
    layout="centered", # Można zmienić na "wide" dla szerszego układu
    initial_sidebar_state="auto"
)

# --- Inicjalizacja Magazynu ---
if 'inventory' not in st.session_state:
    st.session_state.inventory = ["Laptop", "Monitor", "Myszka", "Klawiatura"]

# --- Funkcje Logiki Magazynu ---
def add_item(new_item):
    """Dodaje nowy towar do magazynu."""
    if new_item and new_item not in st.session_state.inventory:
        st.session_state.inventory.append(new_item)
        st.success(f"✅ Dodano: **{new_item}** do magazynu.")
    elif new_item in st.session_state.inventory:
        st.warning(f"⚠️ Towar '*{new_item}*' już znajduje się w magazynie.")

def delete_item(item_to_delete):
    """Usuwa wybrany towar z magazynu."""
    if item_to_delete in st.session_state.inventory:
        st.session_state.inventory.remove(item_to_delete)
        st.success(f"🗑️ Usunięto: **{item_to_delete}** z magazynu.")
    else:
        st.error(f"❌ Błąd: Towar '*{item_to_delete}*' nie znaleziono.")

# --- CSS dla ulepszeń wizualnych ---
st.markdown("""
<style>
    .reportview-container .main .block-container{
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 2rem;
    }
    .stApp {
        background-color: #f0f2f6; /* Jasnoszary */
        color: #333333;
    }
    h1 {
        color: #0e1117;
        font-size: 2.5em;
        text-align: center;
        margin-bottom: 0.5em;
    }
    h2 {
        color: #1a4d2e; /* Ciemnozielony */
        font-size: 1.8em;
        border-bottom: 2px solid #a3e635; /* Jasnozielony */
        padding-bottom: 0.3em;
        margin-top: 1.5em;
    }
    .stButton>button {
        background-color: #a3e635; /* Jasnozielony */
        color: white;
        border-radius: 5px;
        border: none;
        padding: 0.6rem 1.2rem;
        font-size: 1rem;
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #8cc34a; /* Ciemniejszy zielony */
        transform: translateY(-2px);
    }
    .stTextInput>div>div>input {
        border: 1px solid #a3e635;
        border-radius: 5px;
    }
    .stSelectbox>div>div>div {
        border: 1px solid #a3e635;
        border-radius: 5px;
    }
    .css-1r6dm7w { /* Streamlit success message */
        background-color: #d4edda;
        color: #155724;
        border-radius: 5px;
        padding: 10px;
    }
    .css-1r6dm7w p { /* Streamlit success message text */
        color: #155724;
    }
    .css-1kv699v { /* Streamlit warning message */
        background-color: #fff3cd;
        color: #856404;
        border-radius: 5px;
        padding: 10px;
    }
    .css-1kv699v p { /* Streamlit warning message text */
        color: #856404;
    }
    .css-1l00y5a { /* Streamlit info message */
        background-color: #d1ecf1;
        color: #0c5460;
        border-radius: 5px;
        padding: 10px;
    }
    .css-1l00y5a p { /* Streamlit info message text */
        color: #0c5460;
    }
</style>
""", unsafe_allow_html=True)


# --- Nagłówek i Obrazek Banerowy ---
st.title("📦 Smart Magazyn App")
st.markdown("### Intuicyjne zarządzanie zapasami na wyciągnięcie ręki!")

# Możesz tu użyć obrazka banerowego
# Jeśli plik 'warehouse_banner.png' znajduje się w tym samym katalogu
try:
    st.image("warehouse_banner.png", caption="Twoje centrum zarządzania zapasami", use_column_width=True)
except FileNotFoundError:
    st.warning("Plik 'warehouse_banner.png' nie znaleziony. Upewnij się, że jest w tym samym katalogu.")
    # Fallback, jeśli obrazka nie ma
    st.markdown("<p style='text-align: center; color: gray;'><i>Wizualizacja magazynu</i></p>", unsafe_allow_html=True)


# 1. Sekcja Dodawania Towaru
st.header("➕ Dodaj Nowy Towar")
st.info("Wpisz nazwę towaru i dodaj go do swojego magazynu.")
with st.form("add_form", clear_on_submit=True):
    new_item_input = st.text_input("Nazwa Towaru:", key="new_item_key", placeholder="Np. Drukarka laserowa")
    submitted = st.form_submit_button("🛒 Dodaj do Magazynu")

    if submitted:
        add_item(new_item_input.strip().title())


# 2. Sekcja Wyświetlania Magazynu
st.header("📊 Aktualny Stan Magazynu")

if st.session_state.inventory:
    # Możemy dodać niestandardowe style do dataframe, ale Streamlit już ma estetyczne domyślne.
    # Używamy prostego formatowania z ikoną obok każdego elementu.
    display_inventory = [{"Towar": f"💡 {item}"} for item in st.session_state.inventory]
    
    st.dataframe(
        display_inventory,
        use_container_width=True,
        hide_index=True
    )

    # 3. Sekcja Usuwania Towaru
    st.header("🗑️ Usuń Towar")
    st.info("Wybierz towar z listy, który chcesz usunąć.")
    item_to_remove = st.selectbox(
        "Wybierz towar do usunięcia:",
        options=st.session_state.inventory,
        key="remove_item_key"
    )

    if st.button("🔴 Usuń Wybrany Towar", key="delete_button"):
        delete_item(item_to_remove)
        st.experimental_rerun() # Odświeżenie aplikacji, aby lista się zaktualizowała
        
else:
    st.info("Twój magazyn jest aktualnie pusty. Czas coś dodać! 🚀")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'><i>Aplikacja magazynowa stworzona za pomocą Streamlit.</i></p>", unsafe_allow_html=True)
