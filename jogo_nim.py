import random

def computador_escolhe_jogada(n, m, dificuldade):
    m_remove = 1
    remova = False
    if dificuldade == 1:
        m_remove = random.randint(1, min(m, n))
    elif dificuldade == 2:
        if random.randint(0, 1) == 0:
            while (not remova) and (m_remove < m):
                if m > n:
                    m_remove = n
                if (n-m_remove) % (m+1) == 0:
                    remova = True
                else:
                    m_remove = m_remove + 1
        else:
            m_remove = random.randint(1, min(m, n))
    else:
        while (not remova) and (m_remove < m):
            if m > n:
                m_remove = n
            if (n-m_remove) % (m+1) == 0:
                remova = True
            else:
                m_remove = m_remove + 1
    print("\nO computador tirou",m_remove,"peça.")
    if (n-m_remove) != 0:
        print("Agora restam",n-m_remove,"peças no tabuleiro.\n")
    return m_remove

def usuario_escolhe_jogada(n, m):
    m_remove = int(input("Quantas peças você vai tirar? "))
    if (m_remove > m) or (m_remove <= 0) or (m_remove > n):
        jogada_valida = False
        while (not jogada_valida):
            print("\nOops! Jogada inválida! Tente de novo.")
            m_remove = int(input("\nQuantas peças você vai tirar? "))
            if (m_remove <= m) and (m_remove > 0):
                jogada_valida = True
    print("\nVoce tirou",m_remove,"peça.")
    if (n-m_remove) != 0:
        print("Agora restam",n-m_remove,"peças no tabuleiro.")
    return m_remove

def partida(dificuldade):
    n = int(input("\nQuantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if (n % (m+1)) == 0:
        q_joga = 1
        print("\nVoce começa!")
        n = n - usuario_escolhe_jogada(n,m)
        if (n <= 0):
            print("Fim do jogo! O jogador ganhou!")
        q_joga = q_joga - 1
        
    else:
        q_joga = 0
        print("\nComputador começa!")
        n = n - computador_escolhe_jogada(n,m)
        if (n <= 0):
            print("Fim do jogo! O computador ganhou!")
        q_joga = q_joga + 1
    while (n > 0):
            if (q_joga == 1):
                n = n - usuario_escolhe_jogada(n,m)
                q_joga = q_joga - 1
                if n == 0:
                    print("Fim do jogo! O jogador ganhou!")
                    return 1
            else:
                n = n - computador_escolhe_jogada(n,m,dificuldade)
                q_joga = q_joga + 1
                if n == 0:
                    print("Fim do jogo! O computador ganhou!")
                    return 0
def campeonato():
    i = 1
    pc = 0
    jog = 0
    while i <= 3:
        print("\n**** Rodada",i,"****")
        if partida(dificuldade) == 0:
            pc = pc + 1
        else:
            jog = jog + 1
        i = i + 1
    print("\n**** Final do campeonato! ****")
    print("\nPlacar: Você",jog,"X",pc,"Computador")
    

print("Bem-vindo ao jogo do NIM! Escolha:")
print()
dificuldade = int(input("Selecione a dificuldade \n1 - Fácil \n2 - Médio \n3 - Difícil \n"))
print()
opcao = int(input("1 - para jogar uma partida isolada \n2 - para jogar um campeonato "))
print()
if opcao == 1:
    print("Voce escolheu uma partida isolada!")
    partida(dificuldade)
else:
    print("Voce escolheu um campeonato!")
    campeonato()
