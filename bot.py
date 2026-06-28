from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random # Importamos a biblioteca de aleatoriedade
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Inicializa o navegador e acessa o LinkedIn
navegador = webdriver.Chrome()
navegador.get("https://www.linkedin.com/login")
time.sleep(6)


# Etapa 1: Login atualizado com XPATHs combinados para evitar campos ocultos
campo_email = navegador.find_element(By.XPATH, "//input[@type='email' and @autocomplete='username webauthn']")
campo_email.send_keys("victorhs1993@gmail.com")

# Busca todos os campos de senha da página
campos_senha = navegador.find_elements(By.XPATH, "//input[@type='password']")

# Tenta digitar no segundo campo caso o primeiro esteja oculto
if len(campos_senha) > 1:
    campo_senha = campos_senha[1]
else:
    campo_senha = campos_senha[0]

campo_senha.send_keys("T&rr1v&l")

# Busca apenas botões cujo texto interno seja exatamente 'Entrar'
botoes_entrar = navegador.find_elements(By.XPATH, "//button[normalize-space()='Entrar']")

# Seleciona o botão ativo da lista
botao_entrar = botoes_entrar[1] if len(botoes_entrar) > 1 else botoes_entrar[0]

# ⚡ Força o clique no botão de entrar correto usando JavaScript
navegador.execute_script("arguments[0].click();", botao_entrar)

print("🔍 Verificando se o LinkedIn vai pedir código de segurança...")

# 🛡️ ETAPA DE VERIFICAÇÃO DA PAUSA
try:
    # Procura por algum elemento típico da tela de código (ex: um campo de texto para o PIN)
    # Vamos dar até 5 segundos para a página carregar e ver se o campo aparece
    navegador.implicitly_wait(5)
    
    # Tentamos localizar o campo onde digita o código de verificação
    # (Nota: Se o seu bot usa outro seletor para o campo do código, ajuste aqui)
    campo_codigo = navegador.find_element(By.XPATH, "//input[@name='pin' or @id='input-pin']")
    
    # Se encontrou o campo sem dar erro, significa que a tela de bloqueio apareceu!
    print("⚠️ Tela de segurança detectada! Bot pausado por 60 segundos. Digite o código no navegador...")
    navegador.implicitly_wait(10) # Restaura o tempo padrão de espera do seu bot
    time.sleep(60) 

except:
    # Se o Selenium não achou o campo de código em 5 segundos, significa que fomos direto para o feed!
    print("✅ Tela de segurança não detectada ou dispositivo já lembrado. Pulando a pausa!")
    navegador.implicitly_wait(10) # Restaura o tempo padrão de espera do seu bot

# 🚀 O processo de networking continua normalmente aqui:
print("▶️ Iniciando o processo de networking...")

# ETAPA 2: Busca Direta via URL
termo_busca = "Recrutador Tech"
url_busca = f"https://www.linkedin.com/search/results/people/?keywords={termo_busca}"
navegador.get(url_busca)
time.sleep(5)

# ⚙️ Configuração do limite por execução
limite_conexoes = 5
conexoes_feitas = 0

print("▶️ Iniciando o processo de networking...")

# 🔄 Loop controlado pela quantidade de conexões feitas
while conexoes_feitas < limite_conexoes:
    try:
        print("🔍 Procurando botão 'Conectar' na página...")
        
        # ⏱️ Espera até 10 segundos para o primeiro botão 'Conectar' carregar na tela
        da_tempo = WebDriverWait(navegador, 10)
        botao_conectar = da_tempo.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Conectar')]"))
        )
        
        # 📜 Move a tela até o botão encontrado
        navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_conectar)
        time.sleep(1)
        
    
    # ⚡ Clica no botão
        navegador.execute_script("arguments[0].click();", botao_conectar)
        print(f"🤖 Botão 'Conectar' clicado. Aguardando pop-up...")
        
        # 📸 TIRA UMA FOTO DA TELA PARA DIAGNÓSTICO (Remover o comentário se precisar ter um screenshot)
        # navegador.save_screenshot("debug_clique.png")
        # print("📸 Foto da tela salva como 'debug_clique.png' na pasta do projeto.")
        
        # ⏱️ Pausa longa para garantir que o pop-up (se existir) apareça
        time.sleep(3)
        
        # ✉️ Tenta lidar com a janela de confirmação via Shadow DOM
        try:
            print("⏱️ Acessando o Shadow DOM para clicar em 'Enviar sem nota'...")
            
            # 1. Espera o elemento hospedeiro (host) aparecer na tela principal
            da_tempo = WebDriverWait(navegador, 10)
            host = da_tempo.until(
                EC.presence_of_element_located((By.ID, "interop-outlet"))
            )
            
            # Pausa rápida para dar tempo do conteúdo dentro do shadow-root renderizar
            time.sleep(2) 
            
            # 2. Executa o JavaScript para entrar no shadowRoot e clicar no botão
            script_js = """
                let shadow = arguments[0].shadowRoot;
                let botao = shadow.querySelector("button[aria-label='Enviar sem nota']");
                if (botao) {
                    botao.click();
                    return true;
                } else {
                    return false;
                }
            """
            
            sucesso = navegador.execute_script(script_js, host)
            
            if sucesso:
                print("✉️ Sucesso: Clicou em 'Enviar sem nota' via Shadow DOM!")
                conexoes_feitas += 1
            else:
                print("❌ O botão não foi encontrado dentro do Shadow DOM.")
                
            time.sleep(2)
            
        except Exception as e:
            print(f"❌ Erro ao acessar o Shadow DOM. Detalhe: {e}")


        
        # 🎲 Pausa anti-bloqueio aleatória antes do próximo perfil
        tempo_espera = random.randint(4, 9)
        print(f"✅ Conexão {conexoes_feitas}/{limite_conexoes} processada com sucesso! Aguardando {tempo_espera}s...")
        time.sleep(tempo_espera)
        
    except Exception as e:
        # Se o Selenium não encontrar o botão 'Conectar', o loop quebra pois acabaram os perfis
        print("🔎 Não foram encontrados mais botões 'Conectar' nesta página.")
        break

print(f"🏁 Processo finalizado! Total de conexões realizadas: {conexoes_feitas}")

print("🏁 Processo de networking da página finalizado!")