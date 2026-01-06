# Capítulo 2: A Camada Física - Redes de Computadores (Tanenbaum)

## Visão Geral

O Capítulo 2 do livro "Redes de Computadores" de Andrew S. Tanenbaum trata da **Camada Física** do modelo OSI, que é responsável pela transmissão real de bits através de meios físicos. Esta é a base fundamental sobre a qual todas as outras camadas constroem seus serviços.

---

## 2.1 Fundamentos Teóricos da Comunicação de Dados

### Sinais e Espectro

**Sinais Analógicos:**
- Variações contínuas no tempo
- Representam informações através de amplitude, frequência ou fase
- Exemplo: Ondas de rádio, sinais de voz em telefonia tradicional

**Sinais Digitais:**
- Valores discretos (0s e 1s)
- Representam informações através de estados (ligado/desligado, alto/baixo)
- Exemplo: Dados em computadores, Ethernet

**Espectro de Frequência:**
- **Bandwidth (Largura de Banda)**: Range de frequências que um sinal ocupa ou que um meio pode transportar
- Medido em Hz (Hertz)
- Exemplo: 20 Hz - 20 kHz (espectro audível humano)

### Sinais Periódicos e Não-Periódicos

**Sinais Periódicos:**
- Repetem-se em intervalos regulares
- Podem ser representados como soma de senos/cossenos (série de Fourier)
- Exemplo: Onda senoidal pura

**Sinais Não-Periódicos:**
- Não se repetem
- Requerem espectro contínuo para representação
- Exemplo: Pulso único de dados

### Análise de Fourier

**Teorema de Fourier:**
- Qualquer sinal periódico pode ser decomposto em componentes senoidais
- Frequência fundamental + harmônicos

**Implicações:**
- Sinais de alta frequência necessitam meios com maior largura de banda
- Dados digitais requerem largura de banda infinita (na teoria)
- Na prática: limitamos largura de banda → distorção de sinal

---

## 2.2 Meios de Transmissão Guiados

### Meios Magnéticos

**Tipo de Transmissão:** Não é realmente transmissão de dados em tempo real, mas armazenamento físico.

**Características:**
- Fitas magnéticas, discos
- Alta capacidade, baixo custo
- Latência muito alta (transporte físico necessário)
- Uso: Backup, arquivamento

**Aplicação em OT:**
- Backup de configurações de PLCs
- Logs históricos de sistemas SCADA
- Arquivo de dados de processo

---

### Par Trançado (Twisted Pair)

**Construção:**
- Dois fios de cobre isolados entrelaçados
- O entrelaçamento reduz interferência eletromagnética (EMI)

**Tipos:**

**UTP (Unshielded Twisted Pair):**
- Sem blindagem adicional
- Categoria 5 (Cat5), Cat5e, Cat6, Cat6a, Cat7
- Uso: Redes Ethernet domésticas e corporativas

**STP (Shielded Twisted Pair):**
- Blindagem metálica adicional
- Maior proteção contra interferência
- Uso: Ambientes industriais com muito ruído eletromagnético

**Características:**

| Característica | Descrição |
|----------------|-----------|
| **Distância máxima** | ~100 metros (sem repetidor) |
| **Largura de banda** | 100 MHz (Cat5) até 600 MHz (Cat7) |
| **Velocidade** | 100 Mbps (Fast Ethernet) até 10 Gbps (10GBASE-T) |
| **Custo** | Baixo |
| **Imunidade a ruído** | Moderada (melhor com STP) |
| **Segurança** | Baixa (pode ser interceptado fisicamente) |

**Categorias de Cabo:**

- **Cat5**: 100 Mbps, 100 MHz
- **Cat5e**: 1 Gbps, 100 MHz (melhor qualidade que Cat5)
- **Cat6**: 1-10 Gbps, 250 MHz
- **Cat6a**: 10 Gbps, 500 MHz
- **Cat7**: 10 Gbps, 600 MHz, melhor blindagem

**Aplicação em OT:**
- Conectividade entre PLCs e HMIs
- Redes de controle em plantas industriais
- Preferir STP em ambientes com equipamentos elétricos pesados

---

### Cabo Coaxial

**Construção:**
- Condutor central de cobre
- Camada isolante
- Blindagem metálica (malha ou folha)
- Capa externa protetora

**Tipos:**

**Cabo Coaxial Fino (Thin Coax / 10BASE2):**
- Diâmetro: ~5mm
- Distância máxima: 185 metros
- Velocidade: 10 Mbps
- Uso: Legacy Ethernet (obsoleto)

**Cabo Coaxial Grosso (Thick Coax / 10BASE5):**
- Diâmetro: ~10mm
- Distância máxima: 500 metros
- Velocidade: 10 Mbps
- Uso: Legacy Ethernet (obsoleto)

**Cabo Coaxial Moderno:**
- RG-6, RG-59: TV a cabo, internet por cabo
- RG-58: Aplicações de rádio/antena
- Melhor imunidade a ruído que par trançado
- Maior distância que par trançado

**Características:**

| Característica | Descrição |
|----------------|-----------|
| **Distância máxima** | 185-500m (depende do tipo) |
| **Largura de banda** | Até 500 MHz |
| **Velocidade** | 10 Mbps - 100 Mbps (moderno) |
| **Custo** | Moderado |
| **Imunidade a ruído** | Boa |
| **Segurança** | Moderada |

**Aplicação em OT:**
- Menos comum em novas instalações
- Pode ser encontrado em sistemas legados
- Cabo TV em instalações industriais remotas

---

### Fibra Óptica

**Construção:**
- Núcleo de vidro ou plástico (transporte de luz)
- Casca (cladding) com índice de refração diferente
- Capa protetora externa

**Princípio de Funcionamento:**
- **Reflexão Interna Total**: Luz fica confinada no núcleo devido à diferença de índice de refração
- Transmissão através de pulsos de luz (LED ou Laser)

**Tipos:**

**Multimodo (MMF - Multi-Mode Fiber):**
- Núcleo maior (50-62.5 μm)
- Múltiplos modos (caminhos) de luz
- Distâncias menores
- Custo mais baixo
- Uso: LANs, distâncias curtas

**Modo Único (SMF - Single-Mode Fiber):**
- Núcleo menor (8-10 μm)
- Apenas um modo de luz
- Distâncias muito maiores
- Maior largura de banda
- Custo mais alto
- Uso: Backbones, longas distâncias

**Comprimentos de Onda:**
- **850 nm**: Multimodo (distâncias curtas)
- **1310 nm**: Multimodo e monomodo (distâncias médias)
- **1550 nm**: Monomodo (longas distâncias, menor atenuação)

**Padrões:**

- **1000BASE-SX**: 1 Gbps, multimodo, até 550m
- **1000BASE-LX**: 1 Gbps, monomodo/multimodo, até 5-10km
- **10GBASE-SR**: 10 Gbps, multimodo, até 400m
- **10GBASE-LR**: 10 Gbps, monomodo, até 10km
- **100GBASE**: 100 Gbps, várias variações

**Características:**

| Característica | Descrição |
|----------------|-----------|
| **Distância máxima** | Até 100+ km (monomodo) |
| **Largura de banda** | Muito alta (até terabits) |
| **Velocidade** | Até 400 Gbps (e mais) |
| **Custo** | Alto (instalação e equipamentos) |
| **Imunidade a ruído** | Excelente (não afetado por EMI) |
| **Segurança** | Muito alta (detecta interceptação física) |
| **Peso** | Muito leve |
| **Interferência** | Imune a interferência eletromagnética |

**Vantagens:**
- ✅ Imunidade total a interferência eletromagnética
- ✅ Alta segurança (dificulta interceptação)
- ✅ Alta largura de banda
- ✅ Longas distâncias sem repetidores
- ✅ Leve e fino

**Desvantagens:**
- ⚠️ Custo mais alto
- ⚠️ Instalação mais complexa (requer expertise)
- ⚠️ Equipamentos mais caros (transceivers ópticos)

**Aplicação em OT:**
- Backbones de redes industriais
- Conexões entre plantas distantes
- Ambientes com muito ruído eletromagnético
- Sistemas críticos onde segurança é fundamental
- Redes de controle que precisam de alta confiabilidade

---

### Comparação de Meios Guiados

| Característica | Par Trançado | Coaxial | Fibra Óptica |
|----------------|--------------|---------|--------------|
| **Custo** | Baixo | Moderado | Alto |
| **Velocidade** | 1-10 Gbps | 10-100 Mbps | Até 400+ Gbps |
| **Distância** | ~100m | 185-500m | 100m-100+ km |
| **Imunidade EMI** | Moderada | Boa | Excelente |
| **Segurança** | Baixa | Moderada | Alta |
| **Facilidade Instalação** | Fácil | Moderada | Difícil |
| **Uso Principal** | LANs | TV/Cable (legacy) | Backbones, WANs |

---

## 2.3 Meios de Transmissão Não Guiados

### Ondas de Rádio

**Características:**
- Transmissão através do espaço livre
- Frequências de rádio (RF): 3 kHz - 300 GHz
- Propagação via ondas eletromagnéticas

**Propagação:**

**Linha de Visada (Line-of-Sight):**
- Sinal viaja em linha reta
- Limitação: Curvatura da Terra
- Frequências: VHF, UHF, micro-ondas

**Onda Terrestre:**
- Segue a curvatura da Terra
- Frequências baixas (LF, MF)

**Onda Ionosférica:**
- Refletida pela ionosfera
- Frequências médias (MF, HF)
- Permite comunicação de longa distância

**Espectro de Radiofrequência:**

| Banda | Frequência | Comprimento de Onda | Uso |
|-------|------------|---------------------|-----|
| **LF (Low)** | 30-300 kHz | 1-10 km | Rádio AM longo alcance |
| **MF (Medium)** | 300 kHz - 3 MHz | 100 m - 1 km | Rádio AM |
| **HF (High)** | 3-30 MHz | 10-100 m | Rádio de ondas curtas |
| **VHF (Very High)** | 30-300 MHz | 1-10 m | TV, FM, aviação |
| **UHF (Ultra High)** | 300 MHz - 3 GHz | 10 cm - 1 m | TV, celular, WiFi 2.4 GHz |
| **SHF (Super High)** | 3-30 GHz | 1-10 cm | Satélite, WiFi 5 GHz |
| **EHF (Extremely High)** | 30-300 GHz | 1 mm - 1 cm | Rádio de ondas milimétricas |

**Aplicações:**
- **Comunicação celular**: 800-900 MHz, 1.8-2.1 GHz
- **WiFi**: 2.4 GHz, 5 GHz, 6 GHz
- **Bluetooth**: 2.4 GHz
- **Satélite**: 4-30 GHz
- **Rádio amador**: Várias bandas

---

### Micro-ondas

**Características:**
- Frequências: 1-300 GHz
- Requer linha de visada
- Usado para comunicação ponto-a-ponto de longa distância

**Tipos:**

**Micro-ondas Terrestres:**
- Torres com antenas parabólicas
- Distâncias: até 50 km por hop
- Uso: Backbone de telecomunicações

**Micro-ondas via Satélite:**
- Satélites geossíncronos (35,786 km)
- Cobertura global
- Latência alta (~250 ms ida e volta)

**Aplicação em OT:**
- Comunicação com instalações remotas (oleodutos, linhas de transmissão)
- Sistemas SCADA remotos
- Backup de comunicação quando fibra não está disponível

---

### Infravermelho

**Características:**
- Frequências: 300 GHz - 430 THz
- Requer linha de visada direta
- Não atravessa objetos sólidos
- Seguro (não interfere com outros sinais)

**Aplicações:**
- Controles remotos (TV, ar condicionado)
- Comunicação de curto alcance (legacy)
- IrDA (obsoleto para dados, substituído por Bluetooth)

**Limitações:**
- Curta distância
- Requer alinhamento direto
- Não atravessa paredes

---

### Comunicação via Luz (Li-Fi)

**Características:**
- Usa luz LED para transmissão de dados
- Frequências: Visível e infravermelho próximo
- Alta velocidade teórica
- Requer linha de visada

**Vantagens:**
- Não interfere com RF
- Alta segurança (luz não atravessa paredes)
- Potencial para altas velocidades

**Desvantagens:**
- Limitado a linha de visada
- Não funciona sem iluminação
- Em desenvolvimento

---

## 2.4 Comunicação Sem Fio

### Espectro Eletromagnético

**Alocação de Frequências:**
- **Regulamentado**: Governos controlam uso de frequências
- **Não licenciado**: Bandeiras ISM (Industrial, Scientific, Medical)
  - 2.4 GHz: WiFi, Bluetooth, Zigbee
  - 5 GHz: WiFi
  - 915 MHz: RFID, Zigbee (região específica)

**Interferência:**
- Múltiplos dispositivos competindo pelo mesmo espectro
- Exemplo: WiFi 2.4 GHz pode sofrer interferência de micro-ondas, Bluetooth

---

### Transmissão Digital vs Analógica

**Transmissão Analógica:**
- Modulação de onda portadora
- AM (Amplitude Modulation)
- FM (Frequency Modulation)
- PM (Phase Modulation)

**Transmissão Digital:**
- Codificação de bits em sinais
- Representação direta (nível alto = 1, baixo = 0)
- Codificação de linha (Manchester, NRZ, etc.)

---

## 2.5 Codificação de Dados

### Codificação Digital-Digital

**NRZ (Non-Return-to-Zero):**
- 0 = nível baixo, 1 = nível alto
- Problema: Clock recovery difícil (longas sequências de 0s ou 1s)
- Uso limitado

**NRZI (Non-Return-to-Zero Inverted):**
- Mudança = 1, sem mudança = 0
- Melhor que NRZ para clock recovery

**Manchester:**
- 0 = transição alta→baixa no meio do bit
- 1 = transição baixa→alta no meio do bit
- Auto-sincronizante (sempre há transição no meio)
- Uso: Ethernet 10BASE-T

**4B/5B:**
- Mapeia 4 bits em 5 bits codificados
- Garante transições frequentes
- Uso: Fast Ethernet (100BASE-TX)

**8B/10B:**
- Mapeia 8 bits em 10 bits
- Garante DC balance e transições
- Uso: Gigabit Ethernet, Fibre Channel

**PAM-5 (Pulse Amplitude Modulation):**
- 5 níveis de amplitude diferentes
- Permite transmitir mais informação por símbolo
- Uso: Gigabit Ethernet sobre par trançado

---

### Codificação Analógica-Digital (Modulação)

**ASK (Amplitude Shift Keying):**
- Varia amplitude da portadora
- 0 = amplitude baixa, 1 = amplitude alta
- Suscetível a ruído

**FSK (Frequency Shift Keying):**
- Varia frequência da portadora
- 0 = frequência baixa, 1 = frequência alta
- Mais resistente a ruído que ASK

**PSK (Phase Shift Keying):**
- Varia fase da portadora
- BPSK: 2 fases (0° e 180°)
- QPSK: 4 fases (0°, 90°, 180°, 270°)
- 8-PSK, 16-PSK: Mais fases = mais bits por símbolo

**QAM (Quadrature Amplitude Modulation):**
- Combina amplitude e fase
- QAM-16, QAM-64, QAM-256
- Mais eficiente (mais bits por símbolo)
- Requer melhor relação sinal-ruído
- Uso: WiFi, TV digital, DSL

---

## 2.6 Multiplexação

### Multiplexação por Divisão de Frequência (FDM)

**Conceito:**
- Divide espectro de frequências em canais
- Cada canal transporta sinal diferente
- Canais separados por bandas de guarda (guard bands)

**Exemplos:**
- **Rádio AM/FM**: Cada estação em frequência diferente
- **TV analógica**: Cada canal em frequência diferente
- **Telefonia**: Cada chamada em frequência diferente
- **DSL**: Dados em altas frequências, voz em baixas

**Aplicação em OT:**
- Sistemas de rádio para comunicação operacional
- Canais separados para voz e dados SCADA

---

### Multiplexação por Divisão de Tempo (TDM)

**Conceito:**
- Divide tempo em slots (intervalos)
- Cada slot transporta dados de uma fonte diferente
- Transmissão em rodízio (round-robin)

**TDM Síncrono:**
- Slots fixos, mesmo que fonte não tenha dados
- Eficiência pode ser baixa se fontes não transmitem constantemente

**TDM Assíncrono (Estatístico):**
- Slots dinâmicos, apenas para fontes com dados
- Mais eficiente
- Requer endereçamento (identificar fonte)

**Exemplos:**
- **Telefonia digital (T1/E1)**: 24/32 canais de voz multiplexados
- **SONET/SDH**: Multiplexação síncrona de alta velocidade
- **Ethernet switching**: TDM implícito no compartilhamento de meio

---

### Multiplexação por Divisão de Comprimento de Onda (WDM)

**Conceito:**
- Usa diferentes comprimentos de onda (cores) de luz em fibra óptica
- Cada comprimento de onda transporta sinal diferente
- Permite múltiplos canais na mesma fibra

**DWDM (Dense WDM):**
- Muitos comprimentos de onda próximos (ex: 80+ canais)
- Canais espaçados por 0.8 nm (100 GHz) ou menos
- Uso: Backbones de alta capacidade

**CWDM (Coarse WDM):**
- Menos canais, espaçamento maior (20 nm)
- Custo mais baixo
- Uso: Distâncias menores

**Vantagens:**
- Aumenta capacidade de fibra sem adicionar cabos
- Cada comprimento de onda pode ser tratado independentemente

**Aplicação em OT:**
- Backbones de rede entre plantas
- Maximizar uso de infraestrutura de fibra existente

---

## 2.7 Switching

### Circuit Switching

**Conceito:**
- Estabelece caminho dedicado (circuito) antes da transmissão
- Caminho permanece durante toda a comunicação
- Recursos reservados mesmo quando não há transmissão

**Características:**
- ✅ Garantia de largura de banda
- ✅ Latência previsível e baixa (após estabelecimento)
- ✅ Ordem de pacotes garantida
- ⚠️ Ineficiência se circuito não está sendo usado
- ⚠️ Tempo para estabelecer circuito

**Exemplos:**
- **Telefonia tradicional (PSTN)**: Circuito dedicado por chamada
- **ISDN**: Serviços digitais de telefonia

---

### Packet Switching

**Conceito:**
- Dados divididos em pacotes
- Cada pacote roteado independentemente
- Compartilhamento de recursos (estatistical multiplexing)

**Tipos:**

**Packet Switching por Datagrama:**
- Cada pacote roteado independentemente
- Pacotes podem seguir caminhos diferentes
- Ordem pode ser alterada
- Exemplo: Internet (IP)

**Packet Switching por Circuito Virtual:**
- Estabelece caminho lógico (virtual) antes da transmissão
- Todos os pacotes seguem o mesmo caminho
- Ordem preservada
- Exemplo: Frame Relay, X.25 (legacy)

**Características:**
- ✅ Eficiente uso de recursos
- ✅ Flexível e robusto
- ✅ Escalável
- ⚠️ Latência variável (jitter)
- ⚠️ Overhead de headers
- ⚠️ Possível perda de pacotes

**Aplicação em OT:**
- Redes IP industriais usam packet switching
- Considerações: Latência, jitter, perda de pacotes
- Pode necessitar QoS (Quality of Service) para tráfego crítico

---

### Comparação: Circuit vs Packet Switching

| Aspecto | Circuit Switching | Packet Switching |
|---------|-------------------|------------------|
| **Estabelecimento** | Necessário | Não necessário (datagrama) |
| **Largura de Banda** | Garantida | Compartilhada |
| **Eficiência** | Baixa (recursos ociosos) | Alta (recursos compartilhados) |
| **Latência** | Baixa e previsível | Variável |
| **Ordem de Pacotes** | Garantida | Não garantida (datagrama) |
| **Robustez** | Baixa (falha afeta todo circuito) | Alta (roteamento alternativo) |
| **Custo** | Baseado em tempo de conexão | Baseado em volume de dados |
| **Uso** | Telefonia tradicional | Internet, redes modernas |

---

## 2.8 Meios de Comunicação em Contexto OT

### Requisitos Especiais para Ambientes Industriais

**Ambientes Hostis:**
- Temperaturas extremas
- Vibração
- Umidade
- Químicos corrosivos
- Ruído eletromagnético intenso

**Cabo Industrial vs Comercial:**

**Cabos Industriais:**
- Blindagem melhorada
- Resistência a temperatura (-40°C a 85°C+)
- Resistência a óleo, produtos químicos
- Construção mais robusta
- Certificações: UL, CE, RoHS

**Exemplo - Ethernet Industrial:**
- Cat5e/Cat6 com blindagem STP
- Conectores robustos (M12, M8 para ambientes hostis)
- Proteção contra EMI/RFI

**Fibra Óptica em OT:**
- Imune a interferência eletromagnética
- Segurança física (dificulta interceptação)
- Longas distâncias entre plantas
- Uso comum em backbones industriais

---

### Redes Sem Fio em Ambiente Industrial

**Desafios:**
- Interferência de equipamentos (motores, inversores)
- Estruturas metálicas (reflexão, bloqueio)
- Áreas classificadas (explosivos, gases)

**Soluções:**
- **WiFi Industrial**: 802.11 robusto, antenas direcionais
- **Redes Mesh**: Redundância, múltiplos caminhos
- **Redes Celulares (4G/5G)**: Para instalações remotas
- **Protocolos Industriais**: Zigbee, LoRaWAN para sensores

**Considerações de Segurança:**
- Criptografia obrigatória (WPA3)
- Autenticação forte
- Segmentação de rede
- Monitoramento de tráfego

---

### Topologias em Redes Industriais

**Anel (Ring Topology):**
- Redundância: Se um enlace falhar, dados fluem na direção oposta
- Uso: Sistemas críticos que não podem parar
- Exemplo: Protocolos como RSTP (Rapid Spanning Tree Protocol)

**Estrela (Star Topology):**
- Todos conectados a switch central
- Ponto único de falha (mitigado com switches redundantes)
- Mais comum em redes Ethernet industriais

**Bus (Bus Topology):**
- Menos comum em redes modernas
- Pode ser encontrado em sistemas legados

---

## Conceitos-Chave para Red Team / Cybersegurança OT

### Por Que a Camada Física É Importante?

**Para profissionais de Red Team em ambientes críticos:**

1. **Ataques à Camada Física:**
   - **Interceptação de cabos**: Tap em cabos de rede
   - **Inserção de dispositivos**: Hub, switch ou dispositivo malicioso
   - **Jamming**: Bloqueio de sinais sem fio
   - **Comprometimento de infraestrutura**: Acesso físico a equipamentos

2. **Defesa em Profundidade:**
   - Controles físicos: Acesso restrito a cabos, racks, equipamentos
   - Detecção de interceptação: Monitoramento de fibra óptica
   - Criptografia: Mesmo se interceptado, dados não podem ser lidos

3. **Análise de Tráfego:**
   - Entender meios físicos ajuda a entender limitações e vulnerabilidades
   - Saber qual meio está sendo usado ajuda em testes de penetração

4. **Segmentação Física:**
   - Isolar fisicamente redes críticas
   - Air-gapping (isolamento completo) para sistemas mais críticos
   - Redes dedicadas para OT separadas de IT

5. **Comunicação Sem Fio:**
   - Identificar pontos de acesso não autorizados
   - Detectar interferência maliciosa (jamming)
   - Analisar tráfego WiFi em ambientes industriais

---

## Resumo dos Conceitos Principais

### 1. Meios Guiados
- **Par Trançado**: UTP/STP, Cat5-Cat7, até 100m, 1-10 Gbps
- **Coaxial**: Legacy, melhor imunidade que par trançado
- **Fibra Óptica**: Multimodo (curtas distâncias) e Monomodo (longas), muito alta velocidade, imune a EMI

### 2. Meios Não Guiados
- **Rádio**: Várias bandas (LF a EHF), WiFi, celular
- **Micro-ondas**: Linha de visada, satélite, backbones
- **Infravermelho**: Curto alcance, linha de visada

### 3. Codificação
- **Digital-Digital**: NRZ, Manchester, 4B/5B, 8B/10B
- **Analógica-Digital**: ASK, FSK, PSK, QAM

### 4. Multiplexação
- **FDM**: Divisão por frequência
- **TDM**: Divisão por tempo
- **WDM**: Divisão por comprimento de onda (fibra óptica)

### 5. Switching
- **Circuit**: Caminho dedicado, garantia de recursos
- **Packet**: Recursos compartilhados, mais eficiente

---

## Projetos Práticos Sugeridos

1. **Identificar Meios Físicos na Rede**
   - Inspecionar cabos (Cat5, Cat6, fibra)
   - Identificar tipos de conectores
   - Medir comprimentos de cabo

2. **Analisar Características de Cabos**
   - Testar com cable tester
   - Medir atenuação
   - Identificar problemas físicos

3. **Configurar e Testar WiFi**
   - Analisar espectro 2.4 GHz e 5 GHz
   - Identificar interferências
   - Testar alcance e velocidade

4. **Capturar e Analisar Sinais**
   - Usar analisador de espectro (software)
   - Identificar dispositivos WiFi na área
   - Analisar congestionamento de espectro

5. **Estudar Multiplexação**
   - Configurar VLANs (multiplexação lógica)
   - Analisar TDM em capturas de rede
   - Entender WDM em backbones de fibra

---

## Referências e Leitura Complementar

**Do Capítulo 2 do Tanenbaum:**
- Seção 2.1: Fundamentos teóricos
- Seção 2.2: Meios guiados
- Seção 2.3: Meios não guiados
- Seção 2.4: Comunicação sem fio
- Seção 2.5: Codificação
- Seção 2.6: Multiplexação
- Seção 2.7: Switching

**Padrões e Especificações:**
- IEEE 802.3 (Ethernet) - Especificações de meios físicos
- TIA/EIA 568 - Padrões de cabeamento estruturado
- IEC 61850 - Padrões para subestações (inclui especificações físicas)

**Recursos Adicionais:**
- Especificações de cabos (Cat5e, Cat6, etc.)
- Documentação de fibra óptica (multimodo vs monomodo)
- Padrões WiFi (802.11 a/b/g/n/ac/ax)

---

## Checklist de Aprendizado

Marque quando dominar cada conceito:

- [ ] Entendo diferenças entre meios guiados (cabo, fibra)
- [ ] Compreendo características de par trançado (UTP, STP, categorias)
- [ ] Sei diferenças entre fibra multimodo e monomodo
- [ ] Entendo espectro de radiofrequência e suas aplicações
- [ ] Compreendo codificação digital (Manchester, 4B/5B, etc.)
- [ ] Sei como funciona modulação (ASK, FSK, PSK, QAM)
- [ ] Entendo multiplexação (FDM, TDM, WDM)
- [ ] Compreendo diferenças entre circuit switching e packet switching
- [ ] Sei aplicar conceitos em contexto de redes industriais (OT)
- [ ] Compreendo implicações de segurança na camada física

---

## 3 Ideias de Projetos Práticos

### Projeto 1: Analisador de Meios Físicos e Cabeamento

**Objetivo:** Criar um guia prático e ferramenta para identificar e analisar diferentes tipos de cabos e meios físicos em uma rede.

**O que você vai fazer:**
- Documentar tipos de cabos encontrados (par trançado UTP/STP, categoria, fibra óptica)
- Criar script para identificar características de cabos (usando informações de dispositivos de rede)
- Medir distâncias e testar integridade básica (se tiver access a cable tester)
- Gerar relatório de infraestrutura física

**Conceitos aplicados:**
- Meios guiados (par trançado, coaxial, fibra)
- Características de cada meio (distância, velocidade, imunidade a ruído)
- Categorias de cabo (Cat5, Cat6, etc.)
- Diferenças entre UTP e STP

**Ferramentas:** Python (scripting), documentação de cabos, multímetro (opcional), cable tester (se disponível)

---

### Projeto 2: Analisador de Espectro WiFi

**Objetivo:** Desenvolver uma ferramenta para analisar o espectro de radiofrequência usado por redes WiFi (2.4 GHz e 5 GHz).

**O que você vai fazer:**
- Usar bibliotecas Python para escanear redes WiFi disponíveis
- Identificar canais ocupados (2.4 GHz: canais 1-14, 5 GHz: múltiplos canais)
- Detectar interferências e congestionamento
- Visualizar distribuição de redes por canal
- Sugerir canais menos congestionados

**Conceitos aplicados:**
- Meios não guiados (ondas de rádio)
- Espectro de radiofrequência
- Multiplexação por divisão de frequência (FDM)
- Interferência em redes sem fio

**Ferramentas:** Python, biblioteca `wifi` ou `pywifi`, netifaces, visualização (matplotlib)

**Exemplo de saída:**
```
Canal 1 (2.4 GHz): 5 redes detectadas
Canal 6 (2.4 GHz): 8 redes detectadas ⚠️ CONGESTIONADO
Canal 11 (2.4 GHz): 3 redes detectadas ✓ RECOMENDADO
```

---

### Projeto 3: Comparador de Performance de Meios

**Objetivo:** Criar testes práticos para comparar performance de diferentes meios de transmissão (Ethernet vs WiFi).

**O que você vai fazer:**
- Implementar testes de throughput (velocidade de transferência)
- Medir latência (ping) em diferentes meios
- Testar perda de pacotes
- Comparar resultados entre Ethernet (cabo) e WiFi
- Gerar relatório comparativo

**Conceitos aplicados:**
- Bandwidth vs Throughput
- Latência e seus componentes
- Características de meios guiados vs não guiados
- Jitter e variação de latência

**Ferramentas:** Python, socket programming, bibliotecas de rede, ferramentas de benchmark (iperf3, se disponível)

**Métricas a comparar:**
- Throughput máximo
- Latência média e jitter
- Perda de pacotes
- Estabilidade da conexão

---

**Capítulo Anterior:** [Capítulo 1 - Introdução](../cap1/README.md)  
**Próximo Capítulo:** [Capítulo 3 - A Camada de Enlace de Dados](../cap3/README.md)


