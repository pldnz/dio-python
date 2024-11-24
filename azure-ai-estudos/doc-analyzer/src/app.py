import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analyze_credit_card

def configure_interface():
    st.title("Upload de Arquivos no Azure")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["pdf", "png", "jpg", "jpeg"])

    if uploaded_file is not None:
        filename = uploaded_file.name

        # Enviar para o blob storage
        blob_url = upload_blob(uploaded_file, filename)

        if blob_url:
            st.write(f"Arquivo {filename} enviado com sucesso!")
            credit_card_info = analyze_credit_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else: 
            st.write("Erro ao enviar o arquivo")

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem enviada", use_container_width=True)
    st.write("O Azure identificou as seguintes informações:")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown("### Informações do Cartão de Crédito")
        st.write(f"Nome do cartão: {credit_card_info['card_name']}")
        st.write(f"Número do cartão: {credit_card_info['card_number']}")
        st.write(f"Banco emissor: {credit_card_info['bank_name']}")
    else:
        st.write("Nenhuma informação de cartão de crédito encontrada")

if __name__ == "__main__":
    configure_interface()