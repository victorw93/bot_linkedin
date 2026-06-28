# Bot LinkedIn - Automação de Conexões

Este projeto é um robô de automação desenvolvido em Python com Selenium, focado na **otimização de tempo** durante o envio de convites de conexão no LinkedIn. O robô automatiza o processo repetitivo de busca e conexão, permitindo uma gestão de networking mais eficiente.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python
- **Automação:** Selenium WebDriver
- **Técnicas:** Manipulação de Shadow DOM via JavaScript injection

## 🚀 Funcionalidades
- Navegação automática em listas de contatos.
- Identificação e clique no botão de "Conectar".
- Tratamento de pop-ups de confirmação utilizando acesso direto ao Shadow DOM.
- Controle de fluxo e temporização para simular comportamento humano.

## 💡 Desafios Técnicos
O principal desafio superado foi o contorno do **Shadow DOM** utilizado pelo LinkedIn. O robô utiliza injeção de JavaScript para acessar componentes isolados, garantindo que o botão "Enviar sem nota" seja clicado de forma consistente, independentemente da renderização dinâmica dos elementos web.

## 📝 Como usar
1. Clone este repositório.
2. Configure o seu ambiente Python.
3. Execute o script para iniciar o processo de networking.