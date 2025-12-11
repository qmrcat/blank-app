import streamlit as st

st.title("🎈 La meva primera aplicaccio")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


quantitat = st.slider("Selecciona la quantitat")

st.write(f'La quantitat seleccionada es: {quantitat}')

for i in range(quantitat):
    st.button(f'{i+1}')