# Capítulo 3: A Camada de Enlace de Dados - Redes de Computadores (Tanenbaum)

## Visão Geral

O Capítulo 3 do livro "Redes de Computadores" de Andrew S. Tanenbaum trata da **Camada de Enlace de Dados** (Data Link Layer), que é responsável pela transmissão confiável de frames entre nós adjacentes em uma rede. Esta camada garante que os dados transmitidos pela camada física sejam recebidos corretamente, detectando e corrigindo erros, e controlando o fluxo de dados.

---

## 3.1 Serviços da Camada de Enlace

### Funções Principais

A camada de enlace de dados fornece serviços essenciais para comunicação confiável:

**1. Framing (Enquadramento):**
- Divide o fluxo de bits em **frames** (quadros) delimitados
- Adiciona headers e trailers para identificar início e fim de cada frame
- Permite que o receptor identifique onde cada frame começa e termina

**2. Detecção de Erros:**
- Identifica erros que possam ter ocorrido durante a transmissão
- Usa técnicas como checksums e CRC (Cyclic Redundancy Check)
- Não corrige, apenas detecta (correção fica para camadas superiores ou retransmissão)

**3. Correção de Erros:**
- Retransmissão de frames com erro (ARQ - Automatic Repeat Request)
- Correção forward (FEC - Forward Error Correction) usando códigos de correção

**4. Controle de Fluxo:**
- Previne que o transmissor sobrecarregue o receptor
- Garante que o receptor tenha capacidade para processar os dados recebidos

**5. Controle de Acesso ao Meio:**
- Gerencia acesso quando múltiplos nós compartilham o mesmo meio físico
- Evita colisões e conflitos de transmissão

### Modelo de Serviço

**Serviços oferecidos pela camada de enlace:**
- **Não confiável, sem conexão**: Frames são enviados sem garantia de entrega (ex: Ethernet)
- **Confiável, sem conexão**: Frames são confirmados, mas não há estabelecimento de conexão
- **Confiável, orientado à conexão**: Estabelece conexão, garante entrega ordenada (ex: HDLC)

---

## 3.2 Detecção e Correção de Erros

### Tipos de Erros

**Erro de Bit:**
- Um ou mais bits são alterados durante a transmissão
- Causas: Ruído, interferência, atenuação

**Burst Error (Erro em Rajada):**
- Múltiplos bits consecutivos são corrompidos
- Mais comum em transmissão de dados
- Causado por interferências temporárias (relâmpagos, motores, etc.)

### Detecção de Erros

#### Parity (Paridade)

**Parity Simples (Bit de Paridade):**
- Adiciona um bit extra para tornar número total de 1s par (even) ou ímpar (odd)
- **Even Parity**: Número total de 1s é par
- **Odd Parity**: Número total de 1s é ímpar

**Exemplo:**
```
Dados: 1010101 (4 uns)
Even Parity: 1010101 0 (4 uns, par)
Odd Parity:  1010101 1 (5 uns, ímpar)
```

**Limitações:**
- ❌ Detecta apenas **número ímpar** de erros
- ❌ Não detecta se dois bits erram simultaneamente (número par de erros)
- ✅ Simples e rápido

**Aplicação:**
- Comunicação serial básica (UART)
- Memória (RAM com ECC usa paridade)

#### Checksum (Soma de Verificação)

**Funcionamento:**
1. Soma todos os bytes/dados
2. Adiciona carry ao resultado (se houver)
3. Complemento de 1 (inverte bits)
4. Anexa como checksum ao frame

**Verificação:**
- Receptor repete o processo
- Se resultado for 0, assume sem erros
- Se resultado não for 0, frame tem erro

**Características:**
- ✅ Melhor que paridade (detecta mais erros)
- ✅ Simples de implementar
- ⚠️ Menos robusto que CRC
- ⚠️ Pode não detectar alguns padrões de erro

**Uso:**
- UDP checksum
- TCP checksum
- IPv4 header checksum

**Exemplo:**
```
Dados: 1100 1010 0110 1101
Soma:  1100 + 1010 + 0110 + 1101 = 1 0001 (com carry)
Carry: 1 + 0001 = 0010
Complemento: 1101
Checksum: 1101
```

#### CRC (Cyclic Redundancy Check)

**Conceito:**
- Usa divisão polinomial (álgebra de campos finitos)
- Mais robusto que checksum
- Detecta erros de burst e erros isolados

**Funcionamento:**

1. **Escolher Polinômio Gerador (G):**
   - Representado como sequência de bits
   - Exemplo: CRC-32: `x³² + x²⁶ + x²³ + x²² + x¹⁶ + x¹² + x¹¹ + x¹⁰ + x⁸ + x⁷ + x⁵ + x⁴ + x² + x + 1`
   - Representação binária: `100000100110000010001110110110111`

2. **Processo de Cálculo:**
   - Anexa zeros ao frame (número de bits do CRC menos 1)
   - Divide frame por polinômio gerador (usando XOR)
   - Resto da divisão é o CRC
   - Anexa CRC ao frame original

3. **Verificação:**
   - Receptor divide frame completo (dados + CRC) pelo mesmo polinômio
   - Se resto for 0, assume sem erros
   - Se resto não for 0, frame tem erro

**Polinômios Padrão:**

| Nome | Tamanho | Polinômio | Uso |
|------|---------|-----------|-----|
| **CRC-8** | 8 bits | x⁸ + x² + x + 1 | Comunicação simples |
| **CRC-16** | 16 bits | x¹⁶ + x¹⁵ + x² + 1 | Modbus, USB |
| **CRC-32** | 32 bits | Padrão IEEE 802.3 | Ethernet, ZIP, PNG |

**Vantagens:**
- ✅ Detecta erros de burst muito longos
- ✅ Detecta erros de bit isolados
- ✅ Muito eficiente computacionalmente (hardware)
- ✅ Baixa probabilidade de falso positivo

**Aplicação em OT:**
- **Ethernet**: CRC-32 em cada frame
- **Modbus**: CRC-16
- **Protocolos industriais**: Muitos usam CRC para detecção de erros

#### Hamming Code (Código de Hamming)

**Conceito:**
- Código de **correção de erros** (não apenas detecção)
- Adiciona bits redundantes para permitir correção

**Funcionamento:**
- Bits de dados + bits de paridade
- Bits de paridade em posições que são potências de 2 (1, 2, 4, 8, ...)
- Permite identificar e corrigir erro de 1 bit

**Exemplo Simplificado (7,4) Hamming:**
- 4 bits de dados + 3 bits de paridade = 7 bits total
- Pode detectar e corrigir 1 erro

**Aplicação:**
- Memória ECC (Error-Correcting Code)
- Comunicações onde retransmissão é difícil/cara

---

### Correção de Erros

#### ARQ (Automatic Repeat Request)

**Conceito:**
- Receptor detecta erro e solicita retransmissão
- Transmissor reenvia frame quando recebe solicitação

**Tipos de ARQ:**

**Stop-and-Wait ARQ:**
- Transmissor envia 1 frame e espera ACK
- Se ACK recebido, envia próximo frame
- Se timeout ou NAK, retransmite

```
Transmissor              Receptor
    |                       |
    |─── Frame 0 ──────────>|
    |                       | (processa)
    |<─── ACK ──────────────|
    |                       |
    |─── Frame 1 ──────────>|
    |                       | (erro detectado)
    |<─── NAK ──────────────|
    |                       |
    |─── Frame 1 ──────────>| (retransmissão)
    |                       |
```

**Go-Back-N ARQ:**
- Transmissor pode enviar múltiplos frames antes de receber ACK
- Janela deslizante (sliding window)
- Se erro detectado, retransmite frame errado e todos os subsequentes

```
Janela: [0][1][2][3][4]
        ↑
      Enviado, aguardando ACK
```

**Selective Repeat ARQ:**
- Apenas frame com erro é retransmitido
- Mais eficiente que Go-Back-N
- Requer buffer maior no receptor

#### FEC (Forward Error Correction)

**Conceito:**
- Códigos de correção permitem receptor corrigir erros sem retransmissão
- Adiciona redundância extra (mais bits)
- Útil quando retransmissão é difícil/impossível

**Exemplos:**
- Código de Hamming
- Códigos Reed-Solomon
- Turbo codes
- LDPC (Low-Density Parity-Check)

**Aplicação:**
- Comunicação espacial (satélites)
- Streaming (corrige erros sem retransmissão)
- CD/DVD (correção de erros de leitura)

---

## 3.3 Protocolos Elementares da Camada de Enlace

### Protocolo Utopiano (Ideal)

**Características:**
- Meio de transmissão sem erros
- Receptor sempre pronto
- Processamento instantâneo
- Infinitamente rápido

**Limitação:**
- Não existe na prática (apenas teórico)

### Protocolo Stop-and-Wait Simples

**Funcionamento:**
- Transmissor envia frame e espera ACK
- Receptor processa e envia ACK
- Transmissor envia próximo frame após receber ACK

**Problema:**
- Se ACK é perdido, transmissor retransmite
- Receptor pode receber frame duplicado
- Necessita números de sequência

### Protocolo Stop-and-Wait para Canais com Ruído

**Melhorias:**
- Números de sequência (0 e 1 alternados)
- Timeout para detectar ACK perdido
- Receptor descarta frames duplicados (mesmo número de sequência)

**Fluxo:**
```
Transmissor              Receptor
    |                       |
    |─── Frame 0 ──────────>|
    |                       | (processa, espera Frame 1)
    |<─── ACK ──────────────|
    |                       |
    |─── Frame 1 ──────────>|
    |                       | (erro, descarta)
    | (timeout)             |
    |─── Frame 1 ──────────>| (retransmissão)
    |                       |
```

---

## 3.4 Protocolos de Janela Deslizante (Sliding Window)

### Conceito de Janela

**Janela Deslizante:**
- Permite transmissor enviar múltiplos frames antes de receber ACK
- Aumenta eficiência (não precisa esperar cada ACK)
- Janela "desliza" conforme ACKs são recebidos

**Componentes:**

**Janela de Transmissão:**
- Frames que podem ser enviados sem ACK
- Tamanho da janela controla número de frames "em trânsito"

**Janela de Recepção:**
- Frames que receptor está pronto para receber
- Frames fora da janela são descartados

**Números de Sequência:**
- Cada frame tem número único
- Permite ordenação e detecção de duplicatas
- Tamanho do campo determina número máximo de frames

### Go-Back-N

**Funcionamento:**
- Janela de transmissão de tamanho N
- Transmissor pode enviar até N frames sem ACK
- Receptor processa frames em ordem
- Se frame com erro recebido, descarta ele e todos subsequentes
- Transmissor retransmite a partir do frame com erro

**Características:**
- ✅ Mais eficiente que Stop-and-Wait
- ✅ Simples de implementar no receptor
- ⚠️ Ineficiente em canais com muitos erros (retransmite tudo)
- ⚠️ Receptor precisa apenas buffer de 1 frame

**Exemplo:**
```
Janela = 4 frames
Frames enviados: 0, 1, 2, 3
Frame 1 tem erro → Receptor descarta 1, 2, 3
Transmissor retransmite: 1, 2, 3, 4
```

### Selective Repeat

**Funcionamento:**
- Janela de transmissão e recepção
- Receptor aceita frames fora de ordem
- Apenas frame com erro é retransmitido
- Receptor mantém buffer para frames recebidos fora de ordem

**Características:**
- ✅ Mais eficiente que Go-Back-N
- ✅ Retransmite apenas frame com erro
- ⚠️ Mais complexo (buffer maior no receptor)
- ⚠️ Requer ACKs seletivos (SACK - Selective ACK)

**Exemplo:**
```
Janela = 4 frames
Frames enviados: 0, 1, 2, 3
Frame 1 tem erro → Receptor guarda 2, 3 em buffer
Transmissor retransmite apenas: 1
Receptor processa: 0, [1 retransmitido], 2, 3
```

### Comparação de Protocolos

| Característica | Stop-and-Wait | Go-Back-N | Selective Repeat |
|----------------|---------------|-----------|------------------|
| **Eficiência** | Baixa | Média | Alta |
| **Complexidade Receptor** | Baixa | Baixa | Alta |
| **Buffer Receptor** | 1 frame | 1 frame | Múltiplos frames |
| **Retransmissão** | Frame errado | Frame errado + subsequentes | Apenas frame errado |
| **Uso de Largura de Banda** | Baixo | Médio | Alto |
| **Robustez a Erros** | Boa | Média | Boa |

---

## 3.5 Exemplos de Protocolos da Camada de Enlace

### HDLC (High-Level Data Link Control)

**Características:**
- Protocolo orientado à conexão
- Bit-oriented (orientado a bit)
- Usa flags para delimitação de frames
- Controle de fluxo e detecção de erros

**Estrutura de Frame:**
```
[Flag][Address][Control][Data][FCS][Flag]
 8b     8b       8b      var   16b   8b
```

- **Flag**: 01111110 (delimitador)
- **Address**: Endereço da estação
- **Control**: Tipo de frame, números de sequência
- **Data**: Dados (tamanho variável)
- **FCS**: Frame Check Sequence (CRC)

**Tipos de Frames:**
- **Information (I)**: Transporta dados
- **Supervisory (S)**: Controle (ACK, NAK)
- **Unnumbered (U)**: Estabelecimento/liberamento de conexão

**Aplicação:**
- WANs (Frame Relay baseado em HDLC)
- Alguns protocolos industriais legados

### PPP (Point-to-Point Protocol)

**Características:**
- Protocolo para conexões ponto-a-ponto
- Usado em conexões dial-up, DSL, serial
- Suporta múltiplos protocolos de rede (multiplexação)

**Estrutura de Frame:**
```
[Flag][Address][Control][Protocol][Data][FCS][Flag]
 8b     8b       8b       16b      var   16b   8b
```

**Fases:**
1. **Link Dead**: Sem conexão
2. **Link Establishment**: Negociação de parâmetros (LCP)
3. **Authentication**: Autenticação (PAP, CHAP)
4. **Network Layer**: Configuração de protocolos de rede (IPCP)
5. **Link Open**: Dados fluindo
6. **Link Termination**: Encerramento

**Aplicação:**
- Conexões DSL
- Conexões seriais
- VPNs ponto-a-ponto

### SLIP (Serial Line IP) - Legacy

**Características:**
- Protocolo simples, sem controle de fluxo
- Apenas para IP
- Obsoleto (substituído por PPP)

---

## 3.6 Detalhes de Implementação

### Hardware vs Software

**Processamento em Hardware:**
- CRC calculado por circuitos dedicados
- Muito rápido
- Baixo uso de CPU

**Processamento em Software:**
- Mais flexível
- Pode ser mais lento
- Usa mais recursos de CPU

### Buffering

**Buffers de Transmissão:**
- Armazena frames aguardando transmissão
- Necessário quando transmissor é mais rápido que meio físico

**Buffers de Recepção:**
- Armazena frames recebidos
- Permite processamento assíncrono
- Necessário em Selective Repeat

---

## 3.7 A Camada de Enlace em Contexto OT

### Requisitos Especiais para Ambientes Industriais

**Confiabilidade:**
- Sistemas críticos não podem ter perda de dados
- Necessita detecção e correção robusta de erros
- Retransmissão rápida em caso de erro

**Tempo Real:**
- Alguns sistemas têm requisitos de tempo determinístico
- Latência previsível é importante
- Protocolos industriais podem ter timeout muito baixos

**Ambientes Hostis:**
- Mais ruído eletromagnético → mais erros
- CRC robusto é essencial
- Pode necessitar códigos de correção (FEC)

### Protocolos Industriais na Camada de Enlace

**Modbus RTU:**
- Usa CRC-16 para detecção de erros
- Comunicação serial (RS-485)
- Timeout configurável

**Profibus:**
- CRC para detecção de erros
- Suporta comunicação em tempo real
- Usado em automação industrial

**Ethernet Industrial:**
- Usa Ethernet padrão (CRC-32)
- Protocolos industriais rodam sobre Ethernet
- Pode ter mecanismos adicionais para garantir tempo real

### Redundância e Tolerância a Falhas

**Protocolos Redundantes:**
- Múltiplos caminhos de comunicação
- Se um falhar, outro assume
- Exemplo: PRP (Parallel Redundancy Protocol), HSR (High-availability Seamless Redundancy)

**Ring Topology:**
- Frames podem fluir em ambas direções
- Se um enlace falha, tráfego reverte
- Garante conectividade mesmo com falha

---

## Conceitos-Chave para Red Team / Cybersegurança OT

### Por Que a Camada de Enlace É Importante?

**Para profissionais de Red Team em ambientes críticos:**

1. **Análise de Frames:**
   - Entender estrutura de frames Ethernet
   - Analisar headers da camada 2 (MAC addresses)
   - Detectar anomalias no nível de frame

2. **Detecção de Erros:**
   - Frames com CRC inválido podem indicar:
     - Interferência maliciosa
     - Equipamentos com problemas
     - Ataques de jamming/interceptação

3. **MAC Address Spoofing:**
   - Ataques que falsificam endereços MAC
   - Bypass de controles baseados em MAC
   - Man-in-the-Middle em LANs

4. **VLAN Hopping:**
   - Ataques que exploram configurações de VLAN
   - Tráfego entre VLANs isoladas
   - Necessita entendimento de frames 802.1Q

5. **ARP Spoofing/Poisoning:**
   - Ataque na resolução de endereços
   - Interceptação de tráfego em LAN
   - Baseado em frames ARP (camada 2/3)

6. **Switch Security:**
   - Port security (limitar MACs por porta)
   - Spanning Tree Protocol attacks
   - MAC flooding (sobrecarregar tabela MAC do switch)

7. **Frame Analysis:**
   - Capturar e analisar frames com Wireshark
   - Identificar protocolos da camada 2
   - Detectar tráfego anômalo

### Técnicas de Análise

**Captura de Frames:**
- Modo promiscuo da interface de rede
- Captura todos os frames no segmento (não apenas destinados à máquina)
- Essencial para análise de segurança

**Análise de CRC:**
- Frames com CRC inválido são descartados normalmente
- Mas podem ser capturados e analisados
- Podem indicar problemas físicos ou interferência

**MAC Address Analysis:**
- Identificar dispositivos na rede
- Detectar MACs duplicados (possível spoofing)
- Rastrear movimento de dispositivos

---

## Resumo dos Conceitos Principais

### 1. Serviços da Camada de Enlace
- Framing: Divisão em frames delimitados
- Detecção de erros: CRC, checksum, paridade
- Correção de erros: ARQ, FEC
- Controle de fluxo: Previne sobrecarga do receptor
- Controle de acesso ao meio: Gerencia compartilhamento

### 2. Detecção de Erros
- **Parity**: Simples, detecta erros ímpares
- **Checksum**: Soma de verificação, usado em TCP/UDP
- **CRC**: Mais robusto, usado em Ethernet

### 3. Correção de Erros
- **ARQ**: Retransmissão (Stop-and-Wait, Go-Back-N, Selective Repeat)
- **FEC**: Correção forward (Hamming, Reed-Solomon)

### 4. Protocolos de Janela Deslizante
- Permite múltiplos frames em trânsito
- Go-Back-N: Retransmite a partir do erro
- Selective Repeat: Retransmite apenas frame com erro

### 5. Protocolos Práticos
- **HDLC**: Orientado à conexão, WANs
- **PPP**: Ponto-a-ponto, DSL, serial
- **Ethernet**: Protocolo dominante em LANs (será visto no Cap. 4)

---

## Projetos Práticos Sugeridos

1. **Implementar Calculadora de CRC**
   - Calcular CRC-16 e CRC-32
   - Verificar frames Ethernet
   - Validar checksums de TCP/UDP

2. **Analisar Frames Ethernet com Wireshark**
   - Examinar estrutura de frames
   - Identificar endereços MAC (source/destination)
   - Analisar campo Type/Length
   - Verificar CRC (FCS)

3. **Implementar Protocolo Stop-and-Wait Simples**
   - Simular transmissão com detecção de erros
   - Implementar números de sequência
   - Tratar timeouts e retransmissões

4. **Estudar ARP (Address Resolution Protocol)**
   - Capturar frames ARP
   - Entender resolução IP → MAC
   - Analisar tabela ARP local

5. **Analisar Protocolos Industriais**
   - Capturar frames Modbus sobre Ethernet
   - Examinar estrutura de frames
   - Verificar CRC em protocolos industriais

6. **MAC Address Analysis**
   - Listar MACs na rede local
   - Identificar fabricantes (OUI - Organizationally Unique Identifier)
   - Detectar possíveis spoofing

---

## Referências e Leitura Complementar

**Do Capítulo 3 do Tanenbaum:**
- Seção 3.1: Serviços da camada de enlace
- Seção 3.2: Detecção e correção de erros
- Seção 3.3: Protocolos elementares
- Seção 3.4: Protocolos de janela deslizante
- Seção 3.5: Exemplos de protocolos

**Padrões e Especificações:**
- IEEE 802.3 (Ethernet) - Frame structure
- RFC 1661 (PPP - Point-to-Point Protocol)
- ISO 3309 (HDLC frame structure)
- Modbus protocol specifications

**Recursos Adicionais:**
- Wireshark documentation (análise de frames)
- CRC calculation algorithms
- Protocolos industriais (Modbus, Profibus)

---

## Checklist de Aprendizado

Marque quando dominar cada conceito:

- [ ] Entendo funções da camada de enlace de dados
- [ ] Compreendo diferenças entre detecção e correção de erros
- [ ] Sei como funciona CRC e posso calcular
- [ ] Entendo checksum e suas limitações
- [ ] Compreendo protocolos ARQ (Stop-and-Wait, Go-Back-N, Selective Repeat)
- [ ] Sei como funciona janela deslizante
- [ ] Entendo estrutura de frames (HDLC, PPP, Ethernet)
- [ ] Compreendo controle de fluxo na camada de enlace
- [ ] Sei aplicar conceitos em análise de segurança (Wireshark)
- [ ] Compreendo implicações em redes industriais (OT)
- [ ] Entendo MAC addresses e sua importância em segurança
- [ ] Sei identificar e analisar frames com erros

---

## 3 Ideias de Projetos Práticos

### Projeto 1: Calculadora e Validador de CRC

**Objetivo:** Implementar calculadora de CRC (CRC-16 e CRC-32) e validador para verificar integridade de frames.

**O que você vai fazer:**
- Implementar algoritmo de CRC-16 (usado em Modbus, USB)
- Implementar algoritmo de CRC-32 (usado em Ethernet)
- Criar função para calcular CRC de dados
- Criar função para validar CRC de frames recebidos
- Testar com frames Ethernet reais capturados

**Conceitos aplicados:**
- CRC (Cyclic Redundancy Check)
- Detecção de erros na camada de enlace
- Polinômios geradores
- Operações XOR e divisão polinomial

**Ferramentas:** Python (implementação manual ou usar biblioteca `crcmod`), Wireshark (para capturar frames de teste)

**Exemplo:**
```python
data = b"Hello World"
crc16 = calculate_crc16(data)
print(f"CRC-16: {crc16:04X}")

# Validar frame recebido
is_valid = validate_crc(frame_data, received_crc)
```

---

### Projeto 2: Analisador de Frames Ethernet

**Objetivo:** Criar ferramenta para analisar e decodificar frames Ethernet capturados, extraindo informações da camada de enlace.

**O que você vai fazer:**
- Capturar frames Ethernet (usando scapy ou pcap)
- Decodificar estrutura do frame (preamble, destino MAC, origem MAC, Type/Length, dados, FCS)
- Extrair e analisar endereços MAC
- Identificar tipos de protocolos (pelo campo Type/Length)
- Detectar frames com erros (CRC inválido)
- Gerar estatísticas (tamanho de frames, distribuição de protocolos)

**Conceitos aplicados:**
- Estrutura de frames Ethernet
- Endereçamento MAC
- Delimitação de frames
- Detecção de erros (CRC/FCS)
- Campos Type vs Length

**Ferramentas:** Python, scapy, pypcap (ou pyshark), Wireshark (para comparação)

**Saída esperada:**
```
Frame 1:
  Destino MAC: AA:BB:CC:DD:EE:FF
  Origem MAC:  11:22:33:44:55:66
  Type: 0x0800 (IPv4)
  Tamanho: 1514 bytes
  CRC: Válido ✓
```

---

### Projeto 3: Simulador de Protocolo Stop-and-Wait com ARQ

**Objetivo:** Implementar simulação de protocolo Stop-and-Wait com detecção de erros e retransmissão (ARQ).

**O que você vai fazer:**
- Implementar transmissor que envia frames numerados
- Implementar receptor que detecta erros e envia ACK/NAK
- Simular perda de frames e ACKs
- Implementar timeout e retransmissão
- Implementar números de sequência para detectar duplicatas
- Visualizar fluxo de comunicação (frames enviados, ACKs recebidos, retransmissões)

**Conceitos aplicados:**
- Protocolos da camada de enlace
- ARQ (Automatic Repeat Request)
- Stop-and-Wait protocol
- Detecção e correção de erros
- Números de sequência
- Timeouts e retransmissão

**Ferramentas:** Python (classes para transmissor/receptor), visualização (texto ou gráfico simples)

**Exemplo de simulação:**
```
Transmissor: Enviando frame 0
Receptor:    Recebido frame 0, enviando ACK
Transmissor: ACK recebido, enviando frame 1
Receptor:    Erro detectado, enviando NAK
Transmissor: NAK recebido, retransmitindo frame 1
Receptor:    Recebido frame 1, enviando ACK
```

---

**Capítulo Anterior:** [Capítulo 2 - A Camada Física](../cap2/README.md)  
**Próximo Capítulo:** [Capítulo 4 - A Subcamada de Controle de Acesso ao Meio](../cap4/README.md)

