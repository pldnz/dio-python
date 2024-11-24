# Document Analyzer - Validação de Cartão de Crédito

Este projeto é um **App para análise de cartões de crédito**, desenvolvido com o objetivo de validar se um cartão de crédito é legítimo. Ele realiza a validação através de duas integrações com serviços do Azure:

1. **Upload de Imagem no Azure Blob Storage**:  
   A imagem do cartão de crédito é enviada e armazenada no serviço de armazenamento do Azure, garantindo a organização e acessibilidade dos dados.

2. **Análise com Azure Document Intelligence**:  
   Após o upload, o app utiliza o serviço Azure Document Intelligence para processar a imagem e identificar se ela corresponde a um cartão de crédito válido.

Este fluxo automatizado torna a validação rápida e eficiente, utilizando tecnologias confiáveis e escaláveis oferecidas pela Azure.
