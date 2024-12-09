import streamlit as st
from streamlit_authenticator import Authenticate
import streamlit as st
# Importation du module
from streamlit_option_menu import option_menu
# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}
authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire
)
authenticator.login()
def accueil_acceuil():
    st.title("Bienvenue sur ma page, elle regroupe des infos concernant DOFUS !")
def acceuil_photos():
    st.title("Bienvenue sur l'album photo des classes DOFUS")
if st.session_state["authentication_status"]:
    with st.sidebar:
        st.write('Bienvenue')
        selection = option_menu(
                                        menu_title=None,
                                        options = ["Accueil", "Album photos"]
                                    )
# Le bouton de déconnexion
        authenticator.logout("Déconnexion")
#  Création du menu qui va afficher les choix qui se trouvent dans la variable options
# On indique au programme quoi faire en fonction du choix
    if selection == "Accueil":
        accueil_acceuil()
        st.image(r"dofus.png")
    elif selection == "Album photos":
        acceuil_photos()
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Feca")
            st.image(r"feca.jpg")
        with col2:
            st.header("Osamodas")
            st.image(r"Osamodas.jpg")
        with col3:
            st.header("ENU")
            st.image(r"ENU.jpg")
# ... et ainsi de suite pour les autres pages
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')