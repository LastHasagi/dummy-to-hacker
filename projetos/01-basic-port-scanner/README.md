# Scanner Básico de Portas TCP

## Descrição

Este é um scanner básico de portas TCP desenvolvido em Python puro (sem dependências externas). 

Desenvolvido no contexto de **cybersegurança industrial para OT (Operational Technology)** e **setores críticos da sociedade** (energia, água, transporte, infraestrutura), este projeto fornece fundamentos essenciais para profissionais que atuam na proteção de infraestruturas críticas.

Estudamos nele fundamentos de:

- Protocolo TCP/IP
- Conexões de rede
- Threading em Python
- Metodologia de scanning (primeira fase do penetration testing)
- Aplicação em ambientes industriais e OT

## Objetivos Educacionais

Ao completar e estudar este projeto, você aprenderá:

1. **Como funcionam as conexões TCP**
   - Entendimento do handshake TCP
   - Diferença entre portas abertas, fechadas e filtradas

2. **Fundamentos de Rede**
   - Protocolo TCP vs UDP
   - Portas e serviços comuns
   - Resolução de DNS (quando usar hostname)

3. **Programação para Security**
   - Sockets em Python
   - Threading para paralelização
   - Manipulação de exceções de rede

4. **Metodologia de Ethical Hacking**
   - Primeira fase: Reconnaissance (Footprinting)
   - Segunda fase: Scanning
   - Identificação de serviços

5. **Aplicação em Ambientes Industriais (OT)**
   - Scan de portas em infraestruturas críticas
   - Identificação de dispositivos industriais (PLCs, SCADA)
   - Protocolos industriais e portas comuns em OT
   - Conformidade e regulamentações para setores críticos

## Requisitos

- Python 3.6 ou superior
- Nenhuma biblioteca externa necessária (usa apenas bibliotecas padrão do Python)

## Uso

### Uso Básico

Escanear portas comuns no localhost:
```bash
python port_scanner.py 127.0.0.1
```

### Escanear Portas Específicas

```bash
python port_scanner.py 127.0.0.1 80,443,8080
```

### Escanear Range de Portas

```bash
python port_scanner.py 127.0.0.1 1-100
```

### Combinar Portas e Ranges

```bash
python port_scanner.py 127.0.0.1 80,443,8080-8090
```

### Escanear Host Remoto (Apenas se autorizado!)

```bash
python port_scanner.py scanme.nmap.org 20-100
```

**IMPORTANTE:** O serviço `scanme.nmap.org` é autorizado para scanning pela equipe do Nmap. **NUNCA escaneie sistemas sem autorização explícita!**

---

## Fundamentos de Rede: TCP/UDP e o que Acontece por Trás dos Panos

### Modelo OSI e Pilha TCP/IP

Para entender como o scanner funciona, precisamos compreender como as redes funcionam em camadas:

```
┌─────────────────────────────────────┐
│  CAMADA 7 - Aplicação (HTTP, FTP)   │
├─────────────────────────────────────┤
│  CAMADA 6 - Apresentação (SSL/TLS)  │
├─────────────────────────────────────┤
│  CAMADA 5 - Sessão                  │
├─────────────────────────────────────┤
│  CAMADA 4 - Transporte (TCP/UDP)    │ ← Aqui que estamos trabalhando
├─────────────────────────────────────┤
│  CAMADA 3 - Rede (IP)               │
├─────────────────────────────────────┤
│  CAMADA 2 - Enlace (Ethernet)       │
├─────────────────────────────────────┤
│  CAMADA 1 - Física (Cabos/WiFi)     │
└─────────────────────────────────────┘
```

Nosso scanner trabalha na **Camada 4 (Transporte)**, especificamente com o protocolo **TCP**.

### O Que São Portas?

Portas são como "portas de entrada" em um servidor. Imagine um prédio (o IP do servidor) com várias portas (números de porta). Cada porta está associada a um serviço específico:

- **Porta 80**: Servidor Web (HTTP)
- **Porta 443**: Servidor Web Seguro (HTTPS)
- **Porta 22**: SSH (acesso remoto seguro)
- **Porta 25**: Email (SMTP)

As portas vão de **0 a 65535**:
- **0-1023**: Portas bem conhecidas (Well-Known Ports) - requerem privilégios de root
- **1024-49151**: Portas registradas (Registered Ports)
- **49152-65535**: Portas dinâmicas/privadas (Dynamic/Private Ports)

### TCP vs UDP: As Duas Faces do Transporte

#### TCP (Transmission Control Protocol)

**TCP é orientado a conexão e confiável:**

```
Cliente                          Servidor
  │                                 │
  │─── SYN (Synchronize) ──────────>│
  │                                 │
  │<── SYN-ACK (Sync + Ack) ─────── │
  │                                 │
  │─── ACK (Acknowledge) ──────────>│
  │                                 │
  │    CONEXÃO ESTABELECIDA         │
  │                                 │
  │<─────────── DADOS ─────────────>│
  │                                 │
  │─── FIN (Finish) ───────────────>│
  │                                 │
  │<── FIN-ACK ──────────────────── │
  │                                 │
```

**Características do TCP:**
- ✅ **Confiável**: Garante entrega dos pacotes
- ✅ **Ordenado**: Pacotes chegam na ordem correta
- ✅ **Controle de fluxo**: Ajusta velocidade conforme capacidade
- ✅ **Controle de congestionamento**: Evita sobrecarregar a rede
- ⚠️ **Mais lento**: Overhead maior devido às garantias
- ⚠️ **Mais overhead**: Headers maiores (20-60 bytes)

**Uso:** HTTP, HTTPS, FTP, SSH, Telnet, SMTP, POP3, IMAP

#### UDP (User Datagram Protocol)

**UDP é sem conexão e não confiável:**

```
Cliente                          Servidor
  │                                 │
  │─── DATAGRAMA ──────────────────>│
  │                                 │
  │<── DATAGRAMA ───────────────────│
  │                                 │
  │    SEM HANDSHAKE                │
  │    SEM GARANTIA DE ENTREGA      │
```

**Características do UDP:**
- ⚡ **Rápido**: Sem overhead de handshake
- ⚡ **Leve**: Headers pequenos (8 bytes)
- ⚠️ **Não confiável**: Não garante entrega
- ⚠️ **Não ordenado**: Pacotes podem chegar fora de ordem
- ⚠️ **Sem controle de fluxo**: Pode perder pacotes

**Uso:** DNS, DHCP, Streaming (vídeo/áudio), Jogos online, SNMP

### O Handshake TCP (Three-Way Handshake)

Quando nosso scanner tenta conectar a uma porta, este é o processo que acontece:

#### 1. Cliente envia SYN (Synchronize)
```
Cliente -> Servidor
Flags: SYN=1, SEQ=x
"Quero me conectar na porta 80"
```

#### 2. Servidor responde SYN-ACK (se porta aberta)
```
Servidor -> Cliente
Flags: SYN=1, ACK=1, SEQ=y, ACK=x+1
"OK, podemos nos conectar"
```

#### 3. Cliente envia ACK (Acknowledge)
```
Cliente -> Servidor
Flags: ACK=1, SEQ=x+1, ACK=y+1
"Confirmado! Conexão estabelecida"
```

#### Se a Porta Estiver Fechada

```
Cliente -> Servidor: SYN (porta 8080)
Servidor -> Cliente: RST (Reset)
                  "Porta fechada, conexão rejeitada"
```

#### Se a Porta Estiver Filtrada (Firewall)

```
Cliente -> Servidor: SYN (porta 8080)
... (timeout) ...
Nenhuma resposta - pacote descartado silenciosamente
```

### O Que Nosso Scanner Faz (Tecnicamente)

Quando você executa `python port_scanner.py 127.0.0.1 80`, aqui está o que acontece:

1. **Criação do Socket:**
   ```python
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   ```
   - `AF_INET`: Usa IPv4
   - `SOCK_STREAM`: Usa TCP (orientado a conexão)

2. **Configuração de Timeout:**
   ```python
   sock.settimeout(1)  # 1 segundo
   ```
   - Evita que o programa trave esperando indefinidamente

3. **Tentativa de Conexão:**
   ```python
   sock.connect_ex((host, port))
   ```
   - Internamente, isso envia um **SYN packet** ao servidor
   - Espera por **SYN-ACK** (porta aberta) ou **RST** (porta fechada)
   - Se timeout: porta filtrada ou host inacessível

4. **Interpretação do Resultado:**
   - `result == 0`: Conexão bem-sucedida → Porta **ABERTA**
   - `result != 0`: Conexão falhou → Porta **FECHADA** ou **FILTRADA**
   - `socket.gaierror`: Erro de DNS → **HOST INVÁLIDO**
   - Timeout: **PORT MEIOS FILTRADA** ou host offline

### Tipos de Scan de Portas

Nosso scanner usa **TCP Connect Scan** (também chamado de "Full Connect Scan"):

#### TCP Connect Scan (O que implementamos)
- ✅ Estabelece conexão TCP completa
- ✅ Não requer privilégios especiais
- ✅ Muito detectável (deixa logs no servidor)
- ⚠️ Mais lento (completa o handshake)

```
Cliente: SYN → Servidor
Servidor: SYN-ACK → Cliente
Cliente: ACK → Servidor
Cliente: RST → Servidor (fecha conexão)
```

#### SYN Scan (Half-Open Scan) - Mais Avançado
- ⚡ Mais rápido (não completa o handshake)
- ⚡ Mais stealth (não deixa conexão completa)
- ⚠️ Requer privilégios de root/admin
- ⚠️ Mais difícil de implementar

```
Cliente: SYN → Servidor
Servidor: SYN-ACK → Cliente
Cliente: RST → Servidor (fecha sem enviar ACK)
```

#### UDP Scan - Para Protocolos UDP
- ⚠️ Mais difícil (UDP não responde quando fechado)
- ⚠️ Pode ser muito lento
- ⚠️ Resultados menos confiáveis

```
Cliente: UDP Packet → Servidor
Servidor: [Porta aberta] → Responde
Servidor: [Porta fechada] → ICMP Port Unreachable
Servidor: [Porta filtrada] → Sem resposta (timeout)
```

### Por Que Escanear Portas é Importante?

No contexto de **Ethical Hacking** e **Penetration Testing**, o scan de portas é crucial porque:

1. **Reconhecimento (Reconnaissance)**: Primeira fase do teste de penetração
2. **Identificação de Serviços**: Saber quais serviços estão rodando
3. **Identificação de Vulnerabilidades**: Serviços desatualizados ou mal configurados
4. **Mapeamento de Superfície de Ataque**: Entender o que está exposto

---

## Contexto Industrial: OT e Setores Críticos

### O Que é OT (Operational Technology)?

**Operational Technology (OT)** refere-se ao hardware e software que monitora e controla dispositivos físicos, processos e eventos no mundo real. Diferente de IT (Information Technology), que lida com dados, OT está diretamente ligada a operações industriais e infraestruturas críticas.

```
IT (Information Technology)          OT (Operational Technology)
├─ Servidores Web                    ├─ SCADA (Supervisory Control)
├─ Bancos de Dados                   ├─ PLCs (Programmable Logic Controllers)
├─ Aplicações de Negócio             ├─ RTUs (Remote Terminal Units)
├─ Foco: Dados e Informação          ├─ HMI (Human-Machine Interface)
└─ Impacto: Financeiro/Empresarial   └─ Impacto: Físico/Segurança Pública
```

### Setores Críticos da Sociedade

Em ambientes de **cybersegurança industrial para setores críticos**, o scan de portas tem implicações muito mais sérias:

#### 1. **Energia e Utilities**
- **Usinas de Geração (Nuclear, Hidrelétrica, Termelétrica)**
- **Subestações Elétricas**
- **Rede de Distribuição de Energia**
- **Sistemas de Petróleo e Gás**

**Por que o scan é crítico:**
- Identificar **portas abertas indevidamente** em PLCs que controlam geradores
- Detectar **serviços vulneráveis** em sistemas SCADA expostos
- Mapear **superfície de ataque** antes que atacantes o façam
- Identificar **conexões não autorizadas** entre rede corporativa e rede de produção

**Portas comuns em OT (Energia):**
- **502 (Modbus TCP)**: Protocolo industrial amplamente usado em sistemas elétricos
- **20000 (DNP3)**: Protocolo para automação e controle de sistemas de energia
- **2404 (IEC 61850)**: Protocolo padrão para comunicação em subestações

#### 2. **Água e Saneamento**
- **Estações de Tratamento de Água (ETAs)**
- **Estações de Tratamento de Esgoto (ETEs)**
- **Sistemas de Distribuição de Água**
- **Bombas e Válvulas de Controle**

**Por que o scan é crítico:**
- Identificar **sistemas de controle expostos** que podem ser manipulados
- Detectar **acesso não autorizado** a sistemas que controlam químicos e cloração
- Garantir **isolamento de rede** entre sistemas de produção e administrativos

**Portas comuns em OT (Água):**
- **502 (Modbus TCP)**: Controle de bombas e válvulas
- **47808 (BACnet)**: Automação de edifícios e HVAC

#### 3. **Transporte e Infraestrutura**
- **Sistemas de Sinalização Ferroviária**
- **Sistemas de Controle de Tráfego Aéreo**
- **Sistemas de Gerenciamento de Portos**
- **Sistemas de Semáforos e Trânsito**

**Por que o scan é crítico:**
- Identificar **pontos de entrada** em sistemas de controle de tráfego
- Detectar **conexões não seguras** em sistemas críticos de segurança
- Mapear **topologia de rede** para criar zonas de segurança adequadas

#### 4. **Manufatura e Indústria**
- **Linhas de Produção Automatizadas**
- **Sistemas de Robótica Industrial**
- **Controladores de Processo (DCS)**
- **Sistemas de Qualidade e Inspeção**

**Por que o scan é crítico:**
- Identificar **dispositivos legados** com vulnerabilidades conhecidas
- Detectar **dispositivos não gerenciados** (shadow IT industrial)
- Garantir **segmentação adequada** entre zonas de produção

### Diferenças Críticas: IT vs OT

| Aspecto | IT (Information Technology) | OT (Operational Technology) |
|---------|----------------------------|-----------------------------|
| **Foco Principal** | Confidencialidade dos dados | Disponibilidade e Integridade do processo |
| **Tempo de Atualização** | Frequentemente (semanas/meses) | Raramente (anos/décadas) |
| **Dispositivos** | Servidores, PCs, mobile | PLCs, RTUs, sensores, atuadores |
| **Impacto de Downtime** | Perda de produtividade | Risco à segurança, ambiente, vidas |
| **Protocolos** | HTTP, HTTPS, SSH, FTP | Modbus, DNP3, IEC 61850, EtherNet/IP |
| **Tolerância a Risco** | Bugs aceitáveis com patches | Zero tolerância a falhas críticas |
| **Ambiente de Testes** | Ambientes de dev/staging | Limitações extremas em ambientes de produção |

### Aplicação de Port Scanning em OT

#### 1. **Asset Discovery e Inventário**

Em ambientes OT, muitas vezes **não há documentação completa** dos dispositivos conectados:

```python
# Exemplo de uso em ambiente industrial
python port_scanner.py 10.0.100.0 502,20000,2404,47808
```

**Objetivo:** Descobrir todos os dispositivos industriais (PLCs, RTUs, HMIs) que respondem nas portas de protocolos industriais.

#### 2. **Segmentação de Rede e Zonas de Segurança**

Baseado no padrão **IEC 62443** (Segurança Cibernética para OT), redes industriais devem ser divididas em **zonas** e **condutos**:

```
Zona 1: Produção (PLCs, Sensores)
  │
  ├─ Conduto → Zona 2: Supervisão (SCADA, HMI)
  │
  └─ Conduto → Zona 3: Corporativa (Servidores, IT)
```

**Scan de portas ajuda a:**
- Verificar se **firewalls estão funcionando corretamente**
- Detectar **comunicação não autorizada** entre zonas
- Validar **isolamento de rede** crítico

#### 3. **Detecção de Dispositivos Legados e Vulneráveis**

Muitos dispositivos OT têm:
- **Sistemas operacionais antigos** (Windows XP, sistemas proprietários)
- **Firmwares desatualizados** (difíceis ou impossíveis de atualizar)
- **Protocolos inseguros** (Modbus TCP sem autenticação, telnet)

**Port scanning identifica:**
- Dispositivos respondendo em **portas inseguras** (23/Telnet, 21/FTP)
- Serviços **não documentados** que podem ser vetores de ataque
- **Shadow devices** (dispositivos conectados sem conhecimento da equipe de segurança)

#### 4. **Conformidade e Auditoria**

Organizações de setores críticos precisam cumprir regulamentações:

- **ANSI/ISA 62443**: Padrão internacional de segurança para OT
- **NERC CIP**: Requisitos de segurança para o setor elétrico (EUA)
- **Regulamentações Nacionais**: Cada país tem suas próprias exigências

**Port scanning é parte essencial de:**
- Auditorias de segurança periódicas
- Relatórios de conformidade
- Avaliações de risco cibernético

### Casos de Uso Reais em Ambientes Críticos

#### Cenário 1: Usina de Energia

**Problema:** Identificar todos os PLCs conectados à rede que controlam geradores.

**Solução com Port Scanning:**
```bash
# Scan em range de IPs da rede de produção
python port_scanner.py 192.168.1.100 502  # Modbus TCP
```

**Resultado:** Identificados 15 PLCs respondendo na porta 502, 3 deles não estavam no inventário oficial.

**Impacto:** Dispositivos "fantasma" poderiam ser alvos de atacantes sem conhecimento da equipe de segurança.

#### Cenário 2: Estação de Tratamento de Água

**Problema:** Validar que firewalls estão bloqueando comunicação entre rede corporativa e rede SCADA.

**Solução com Port Scanning:**
```bash
# Scan a partir da rede corporativa tentando acessar rede SCADA
python port_scanner.py 10.100.50.0 502,47808,20000
```

**Resultado:** Nenhuma porta aberta detectada (esperado). Firewall funcionando corretamente.

**Impacto:** Conformidade com regulamentações de isolamento de rede crítica.

#### Cenário 3: Linha de Produção Industrial

**Problema:** Identificar dispositivos usando protocolos inseguros (Telnet, FTP).

**Solução com Port Scanning:**
```bash
# Scan completo para identificar serviços inseguros
python port_scanner.py 172.16.0.0 21,23,80,443
```

**Resultado:** 8 dispositivos respondendo em Telnet (porta 23), protocolo sem criptografia.

**Impacto:** Risco de interceptação de credenciais e controle não autorizado de dispositivos.

### Considerações Especiais para OT

⚠️ **IMPORTANTE - Leia antes de escanear ambientes OT:**

1. **Coordenação com Operações:**
   - Sempre coordenar scans com equipe de operações
   - Alguns scans podem causar **interrupções** em dispositivos sensíveis
   - Alguns PLCs antigos podem **crashar** com tráfego inesperado

2. **Horários de Manutenção:**
   - Preferencialmente executar durante **janelas de manutenção**
   - Evitar scans durante **operações críticas**
   - Ter **plano de rollback** caso algo dê errado

3. **Velocidade de Scan:**
   - Em OT, **scans muito rápidos** podem sobrecarregar dispositivos
   - Considerar aumentar **timeout** para dispositivos lentos
   - Usar **menos threads** para não sobrecarregar a rede

4. **Documentação:**
   - Documentar **todos os scans** realizados
   - Manter **rastro de auditoria** para conformidade
   - Comparar resultados ao longo do tempo para detectar mudanças

### Portas Críticas em Ambientes OT

**Protocolos Industriais Comuns:**

| Porta | Protocolo | Uso | Segurança |
|-------|-----------|-----|-----------|
| 502 | Modbus TCP | Controle industrial amplamente usado | ⚠️ Sem autenticação nativa |
| 20000 | DNP3 | Sistemas de energia elétrica | ⚠️ Autenticação opcional |
| 2404 | IEC 61850 | Subestações elétricas | ✅ Mais seguro (com configuração adequada) |
| 47808 | BACnet | Automação predial/HVAC | ⚠️ Sem criptografia por padrão |
| 44818 | EtherNet/IP | Automação industrial | ⚠️ Sem segurança por padrão |
| 9600 | Omron FINS | Controle industrial | ⚠️ Sem autenticação |

**Portas de Serviços (geralmente indesejadas em OT):**
- **23 (Telnet)**: ⚠️⚠️⚠️ Nunca deveria estar aberto (sem criptografia)
- **21 (FTP)**: ⚠️⚠️ Raramente necessário (usar SFTP)
- **80 (HTTP)**: ⚠️ Preferir HTTPS (443)
- **3389 (RDP)**: ⚠️ Usar VPN antes de acessar

### Benefícios do Port Scanning em OT para Setores Críticos

1. **Prevenção de Incidentes:**
   - Identificar vulnerabilidades **antes** que atacantes as descubram
   - Reduzir **superfície de ataque** exposta

2. **Conformidade Regulatória:**
   - Atender requisitos de **auditoria**
   - Demonstrar **devida diligência** em segurança

3. **Visibilidade:**
   - Criar **inventário preciso** de ativos
   - Identificar **dispositivos não gerenciados**

4. **Preparação para Incidentes:**
   - Ter **baseline** do ambiente normal
   - Detectar **mudanças suspeitas** rapidamente

### Próximos Passos no Contexto OT

Após dominar o scan básico de portas, no contexto industrial você aprenderá:

1. **Protocol-Specific Scanning**: Escanear protocolos industriais específicos (Modbus, DNP3)
2. **Passive Network Monitoring**: Usar ferramentas como Wireshark para não interferir em processos
3. **Industrial Firewall Configuration**: Configurar firewalls para segmentação OT
4. **Risk Assessment**: Avaliar riscos específicos de cada dispositivo encontrado
5. **Incident Response para OT**: Como responder a incidentes sem interromper produção

---

### Threading: Por Que Usamos?

Escanear portas uma por uma seria **muito lento**:

```
Scan sequencial (porta por porta):
Porta 1: 1 segundo
Porta 2: 1 segundo
...
Porta 1000: 1 segundo
Total: 1000 segundos (16.6 minutos!) ❌
```

Com threading, escaneamos múltiplas portas simultaneamente:

```
Scan paralelo (50 threads):
1000 portas ÷ 50 threads = 20 rodadas
Total: ~20 segundos ✅
```

Nosso scanner usa `ThreadPoolExecutor` para criar até 50 threads simultâneas, cada uma escaneando uma porta diferente ao mesmo tempo.

### Por Que Sockets?

**Sockets** são a interface de programação para comunicação em rede. Eles abstraem a complexidade do TCP/IP e permitem que programas se comuniquem pela rede como se fosse uma operação de arquivo.

```python
# Criar socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar (equivalente a "abrir arquivo")
sock.connect((host, port))

# Enviar/receber dados (equivalente a "ler/escrever arquivo")
sock.send(data)
data = sock.recv(1024)

# Fechar (equivalente a "fechar arquivo")
sock.close()
```

### Resolução DNS

Quando você passa um hostname como `scanme.nmap.org`, o sistema precisa resolver para um IP:

```
1. Aplicação pede: "scanme.nmap.org"
2. Sistema consulta DNS server
3. DNS retorna: "45.33.32.156"
4. Socket usa o IP para conectar
```

O Python faz isso automaticamente através de `socket.connect()`, mas internamente usa a função `getaddrinfo()` para resolver DNS.

---

## Como Funciona (Resumo Prático)

Nosso scanner implementa um **TCP Connect Scan** básico:

1. **Cria Socket TCP**: Para cada porta, cria um socket TCP (SOCK_STREAM)
2. **Tentativa de Conexão**: Usa `connect_ex()` para iniciar o three-way handshake
3. **Interpreta Resultado**: 
   - `0` = Porta aberta (handshake completo)
   - `!= 0` = Porta fechada (RST recebido)
   - Timeout = Porta filtrada ou inacessível
4. **Threading Paralelo**: Usa até 50 threads simultâneas para acelerar o processo
5. **Identificação de Serviço**: Consulta tabela de serviços do sistema para portas conhecidas

**Fluxo Simplificado:**
```
Para cada porta:
  ├─ Criar socket TCP
  ├─ Tentar conectar (envia SYN)
  ├─ Se SYN-ACK recebido → Porta ABERTA
  ├─ Se RST recebido → Porta FECHADA
  └─ Se timeout → Porta FILTRADA
```

## Exemplo de Saída

```
[*] Escaneando 127.0.0.1...
[*] Total de portas: 20

============================================================
RESULTADOS DO SCAN
============================================================

[+] 2 porta(s) aberta(s):

Porta      Status     Serviço
----------------------------------------
80         open       http
443        open       https

============================================================

[*] Scan concluído em 2.15 segundos
```

## Portas Comuns Escaneadas (Padrão)

Quando não especificado, o scanner verifica as seguintes portas comuns:

- 21 (FTP)
- 22 (SSH)
- 23 (Telnet)
- 25 (SMTP)
- 53 (DNS)
- 80 (HTTP)
- 110 (POP3)
- 111 (RPC)
- 135 (RPC)
- 139 (NetBIOS)
- 143 (IMAP)
- 443 (HTTPS)
- 445 (SMB)
- 993 (IMAPS)
- 995 (POP3S)
- 1723 (PPTP)
- 3306 (MySQL)
- 3389 (RDP)
- 5900 (VNC)
- 8080 (HTTP-Proxy)

## Melhorias Futuras

Ideias para expandir o projeto:

- [ ] Implementar SYN scan (mais rápido e stealth)
- [ ] Adicionar suporte a UDP
- [ ] Implementar detecção de OS fingerprinting
- [ ] Adicionar banner grabbing
- [ ] Salvar resultados em arquivo
- [ ] Adicionar opções de verbosidade
- [ ] Implementar scan aleatório de portas

## Referências

- [TCP/IP Guide](http://www.tcpipguide.com/)
- [Nmap Documentation](https://nmap.org/book/)
- [Python Socket Programming](https://docs.python.org/3/library/socket.html)