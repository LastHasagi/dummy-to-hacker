# Capítulo 1: Introdução - Redes de Computadores (Tanenbaum)

## Visão Geral

O Capítulo 1 do livro "Redes de Computadores" de Andrew S. Tanenbaum estabelece os fundamentos e conceitos introdutórios que são essenciais para entender toda a arquitetura e funcionamento das redes modernas.

---

## 1.1 Usos das Redes de Computadores

### Aplicações para Empresas

As redes corporativas permitem:
- **Compartilhamento de recursos**: Impressoras, servidores, storage
- **Comunicação**: Email, mensageria instantânea, videoconferência
- **Acesso remoto**: Trabalho remoto, acesso a sistemas internos
- **Colaboração**: Documentos compartilhados, versionamento

### Aplicações Domésticas

- **Acesso à informação**: Web browsing, notícias, pesquisa
- **Comunicação pessoa-a-pessoa**: Email, redes sociais, VoIP
- **Entretenimento interativo**: Streaming, jogos online
- **Comércio eletrônico**: Compras online, banking
- **Internet das Coisas (IoT)**: Casa inteligente, dispositivos conectados

### Usuários Móveis

- **Comunicação sem fio**: Celulares, tablets
- **Localização**: GPS, mapas
- **Aplicações móveis**: Apps que dependem de conectividade

---

## 1.2 Hardware de Rede

### Métodos de Transmissão: Unicast, Broadcast e Multicast

Em redes de computadores, existem três métodos principais para transmitir dados entre máquinas:

#### 1. Unicast (Ponto a Ponto / Peer-to-Peer)

**Definição:** Transmissão direta entre **dois nós específicos** na rede.

**Características:**
- Uma máquina envia dados para **um único destinatário** específico
- Endereço de destino é **único e específico** (endereço MAC ou IP de uma máquina)
- Comunicação **um-para-um**

**Exemplo Visual:**
```
Máquina A ──────→ Máquina B
(A envia para B especificamente)
```

**Características técnicas:**
- ✅ **Eficiente** para comunicação direta
- ✅ **Privacidade**: Apenas o destinatário recebe
- ✅ **Controle de fluxo** mais simples
- ⚠️ **Overhead** quando precisa enviar para muitos destinatários (múltiplas transmissões)

**Exemplos práticos:**
- Download de arquivo de um servidor web
- Email enviado para um destinatário específico
- SSH conectando a um servidor específico
- Navegação web (seu navegador → servidor web)

**Endereços:**
- **IPv4**: Endereço IP individual (ex: 192.168.1.100)
- **IPv6**: Endereço unicast (ex: 2001:db8::1)
- **MAC**: Endereço físico único da placa de rede

---

#### 2. Broadcast (Difusão)

**Definição:** Transmissão para **todos os dispositivos** na mesma rede (domínio de broadcast).

**Características:**
- Uma máquina envia dados e **todos os dispositivos na rede recebem**
- Não há necessidade de saber endereços específicos
- Comunicação **um-para-todos**

**Exemplo Visual:**
```
Máquina A ────→ [Rede]
                ├─→ Máquina B
                ├─→ Máquina C
                ├─→ Máquina D
                └─→ Máquina E
(Todos recebem, mesmo que não seja para eles)
```

**Características técnicas:**
- ✅ **Simples**: Não precisa conhecer todos os destinatários
- ✅ **Descoberta automática**: Útil para protocolos de descoberta (ARP, DHCP)
- ⚠️ **Ineficiente**: Todos processam o pacote, mesmo que não seja para eles
- ⚠️ **Consome largura de banda** em toda a rede
- ⚠️ **Não roteável**: Fica limitado ao segmento de rede local

**Tipos de Broadcast:**

**Broadcast de Camada 2 (MAC):**
- Endereço MAC: `FF:FF:FF:FF:FF:FF`
- Limita-se ao segmento Ethernet/WiFi
- Não atravessa roteadores

**Broadcast de Camada 3 (IP):**
- **IPv4 Broadcast limitado**: `255.255.255.255` (toda a rede local)
- **IPv4 Broadcast direcionado**: `192.168.1.255` (rede 192.168.1.0/24)
- **IPv6**: Não possui broadcast nativo (usa multicast)

**Exemplos práticos:**
- **ARP (Address Resolution Protocol)**: "Quem tem o IP X.X.X.X?" - todos recebem
- **DHCP Discovery**: Cliente procurando servidor DHCP na rede
- **NetBIOS**: Descoberta de recursos em redes Windows
- **Routing protocols**: Alguns protocolos de roteamento usam broadcast

**Limitações:**
- Roteadores **não encaminham** broadcasts (por padrão) - proteção contra broadcast storms
- Consumo desnecessário de recursos quando apenas alguns precisam receber

---

#### 3. Multicast (Multidifusão)

**Definição:** Transmissão para **um grupo específico** de dispositivos que expressaram interesse em receber.

**Características:**
- Uma máquina envia dados para **múltiplos destinatários**, mas apenas aqueles que fazem parte do grupo recebem
- Dispositivos devem **se inscrever no grupo** multicast para receber
- Comunicação **um-para-muitos** (grupo específico)

**Exemplo Visual:**
```
Máquina A ────→ [Grupo Multicast]
                ├─→ Máquina B (inscrita) ✓
                ├─→ Máquina C (não inscrita) ✗
                ├─→ Máquina D (inscrita) ✓
                └─→ Máquina E (inscrita) ✓
(Apenas B, D e E recebem)
```

**Características técnicas:**
- ✅ **Eficiente**: Uma transmissão serve múltiplos destinatários interessados
- ✅ **Escalável**: Economiza largura de banda comparado a múltiplos unicasts
- ✅ **Roteável**: Pode atravessar roteadores (com suporte adequado)
- ✅ **Seletivo**: Apenas membros do grupo recebem
- ⚠️ **Mais complexo**: Requer gerenciamento de grupos (IGMP, MLD)

**Endereços Multicast:**

**IPv4:**
- Faixa: `224.0.0.0` a `239.255.255.255` (Classe D)
- Exemplos:
  - `224.0.0.1`: Todos os sistemas na sub-rede
  - `224.0.0.2`: Todos os roteadores na sub-rede
  - `239.255.255.250`: SSDP (UPnP)

**IPv6:**
- Prefixo: `FF00::/8`
- Exemplo: `FF02::1` (todos os nós na rede local)

**MAC (Ethernet):**
- Endereços MAC multicast começam com `01:00:5E` para IPv4
- Mapeamento: IP multicast → MAC multicast

**Exemplos práticos:**
- **Streaming de vídeo**: TV ao vivo para múltiplos espectadores
- **Aplicações de voz/vídeo**: Videoconferências, webinars
- **Jogos online**: Atualizações de estado para múltiplos jogadores
- **Routing protocols**: OSPF, EIGRP usam multicast
- **Service discovery**: mDNS (Bonjour, ZeroConf)
- **Backup simultâneo**: Atualização de sistemas para múltiplos servidores

**Protocolos relacionados:**
- **IGMP (Internet Group Management Protocol)**: IPv4 - gerenciamento de grupos multicast
- **MLD (Multicast Listener Discovery)**: IPv6 - equivalente ao IGMP
- **PIM (Protocol Independent Multicast)**: Roteamento multicast entre redes

---

### Tabela Comparativa: Unicast vs Broadcast vs Multicast

| Característica | Unicast (P2P) | Broadcast | Multicast |
|----------------|---------------|-----------|-----------|
| **Destinatários** | 1 específico | Todos na rede | Grupo específico |
| **Eficiência** | Alta (1-para-1) | Baixa (todos processam) | Média/Alta (apenas interessados) |
| **Largura de Banda** | Mínima | Alta (redundação) | Moderada (otimizada) |
| **Escalabilidade** | Baixa (múltiplas conexões) | Limitada (rede local) | Alta (uma transmissão) |
| **Roteável** | ✅ Sim | ❌ Não (limitado) | ✅ Sim (com suporte) |
| **Complexidade** | Baixa | Baixa | Alta (gerenciamento de grupos) |
| **Uso comum** | Comunicação direta | Descoberta/protocolos | Streaming/atualizações em grupo |
| **Endereço IPv4** | IP individual | 255.255.255.255 | 224.0.0.0 - 239.255.255.255 |
| **Endereço IPv6** | Unicast address | Não existe | FF00::/8 |
| **Endereço MAC** | MAC único | FF:FF:FF:FF:FF:FF | 01:00:5E:xx:xx:xx |

---

### Redes de Difusão vs Redes Ponto a Ponto

#### Redes de Difusão (Broadcast Networks)

Todas as máquinas na rede compartilham o mesmo canal de comunicação:

**Características:**
- Canal **compartilhado** por todos
- Broadcast e multicast são **nativos**
- Controle de acesso ao meio necessário (MAC layer)

**Topologias:**
- **Barramento (Bus)**: Todos conectados a um cabo comum (Ethernet clássico)
- **Anel (Ring)**: Máquinas conectadas em círculo (Token Ring)
- **Estrela (Star)**: Todos conectados a um hub central (Ethernet moderno)

**Exemplos:**
- Ethernet (LANs)
- WiFi (IEEE 802.11)
- Token Ring (legado)

#### Redes Ponto a Ponto (Point-to-Point Networks)

Conexão direta entre pares de máquinas:

**Características:**
- Conexões **dedicadas** entre nós
- Unicast é o método primário
- **Roteamento** necessário para chegar a destinos distantes
- Maior complexidade, mas mais escalável

**Exemplos:**
- Internet (rede de redes com roteadores)
- Redes corporativas complexas
- WANs (Wide Area Networks)
- Conexões serial ponto-a-ponto

**Diferenças principais:**

| Aspecto | Redes Broadcast | Redes Ponto a Ponto |
|---------|----------------|---------------------|
| **Canal** | Compartilhado | Dedicado por conexão |
| **Método principal** | Broadcast/Multicast | Unicast |
| **Roteamento** | Não necessário | Essencial |
| **Complexidade** | Mais simples | Mais complexa |
| **Escalabilidade** | Limitada ao segmento | Altamente escalável |
| **Exemplo** | Ethernet LAN | Internet |

---

### Aplicação em Contexto OT e Red Team

#### Por Que Isso Importa?

**Análise de Tráfego:**
- **Unicast**: Comunicação normal cliente-servidor (esperado)
- **Broadcast excessivo**: Pode indicar ataque (ex: ARP spoofing, broadcast storms)
- **Multicast**: Protocolos industriais podem usar (verificar se é legítimo)

**Segmentação de Rede:**
- Broadcasts não atravessam roteadores → use roteadores para isolar domínios
- Multicast requer configuração adequada em switches/roteadores

**Segurança:**
- Broadcasts podem ser usados para reconnaissance (descobrir dispositivos)
- Monitorar tráfego broadcast anômalo
- Implementar controle de broadcast storms

**Exemplo em OT:**
- **Unicast**: PLC comunicando com SCADA
- **Broadcast**: ARP descobrindo endereços MAC (normal, mas monitorar)
- **Multicast**: Protocolos industriais como IEC 61850 podem usar para sincronização

---

### Resumo Visual dos Métodos

```
UNICAST (P2P)
┌─────┐      ┌─────┐
│  A  │─────→│  B  │
└─────┘      └─────┘
(1-para-1)

BROADCAST
┌─────┐      
│  A  │───┬──→ ┌─────┐
└─────┘   │    │  B  │
          ├───→│  C  │
          ├───→│  D  │
          └───→│  E  │
               └─────┘
(1-para-todos)

MULTICAST
┌─────┐      
│  A  │───┬──→ ┌─────┐ (grupo)
└─────┘   │    │  B  │✓
          ├───→│  C  │✗
          ├───→│  D  │✓
          └───→│  E  │✓
               └─────┘
(1-para-muitos [grupo])
```

---

## 1.3 Software de Rede

### Hierarquias de Protocolos

Os protocolos são organizados em **camadas** (layers), onde cada camada:
- Usa serviços da camada inferior
- Fornece serviços para a camada superior
- Mantém **abstração** - camada superior não precisa conhecer detalhes da inferior

**Vantagens:**
- Modularidade
- Facilita manutenção e atualização
- Permite diferentes implementações

### Design de Camadas

**Princípios fundamentais:**
- Cada camada deve executar uma função bem definida
- Interfaces entre camadas devem ser bem definidas
- Número de camadas deve ser suficiente, mas não excessivo

### Interligação de Redes

**Roteadores**: Dispositivos que conectam redes diferentes
- Operam na camada de rede
- Fazem decisões de roteamento baseadas em endereços de rede

**Gateways**: Conectam redes com protocolos diferentes
- Podem fazer tradução de protocolos

---

## 1.4 Modelos de Referência

### Modelo OSI (Open Systems Interconnection)

Sete camadas definidas pela ISO:

```
┌─────────────────────────────────────┐
│  7. Aplicação (Application)         │ ← HTTP, FTP, SMTP
├─────────────────────────────────────┤
│  6. Apresentação (Presentation)     │ ← SSL/TLS, criptografia
├─────────────────────────────────────┤
│  5. Sessão (Session)                │ ← Gerenciamento de sessões
├─────────────────────────────────────┤
│  4. Transporte (Transport)          │ ← TCP, UDP
├─────────────────────────────────────┤
│  3. Rede (Network)                  │ ← IP, roteamento
├─────────────────────────────────────┤
│  2. Enlace de Dados (Data Link)     │ ← Ethernet, frames
├─────────────────────────────────────┤
│  1. Física (Physical)               │ ← Cabos, sinais elétricos
└─────────────────────────────────────┘
```

**Camada 7 - Aplicação:**
- Interface entre aplicações e rede
- Protocolos: HTTP, FTP, SMTP, DNS, Telnet

**Camada 6 - Apresentação:**
- Formatação e apresentação de dados
- Criptografia, compressão, conversão de caracteres

**Camada 5 - Sessão:**
- Estabelecimento, gerenciamento e término de sessões
- Sincronização de diálogo

**Camada 4 - Transporte:**
- Comunicação de ponta a ponta
- Controle de fluxo, correção de erros
- TCP, UDP

**Camada 3 - Rede:**
- Roteamento de pacotes através de múltiplas redes
- Endereçamento lógico (IP)
- IP, ICMP, ARP

**Camada 2 - Enlace de Dados:**
- Transferência confiável de frames entre nós adjacentes
- Detecção e correção de erros
- Ethernet, WiFi

**Camada 1 - Física:**
- Transmissão de bits brutos sobre meio físico
- Especificações elétricas, mecânicas, funcionais

### Modelo TCP/IP

Quatro camadas (mais simples e prático que OSI):

```
┌─────────────────────────────────────┐
│  Aplicação                          │ ← HTTP, FTP, SMTP, DNS
├─────────────────────────────────────┤
│  Transporte                         │ ← TCP, UDP
├─────────────────────────────────────┤
│  Internet                           │ ← IP, ICMP
├─────────────────────────────────────┤
│  Interface de Rede                  │ ← Ethernet, WiFi
└─────────────────────────────────────┘
```

**Comparação OSI vs TCP/IP:**
- OSI: Modelo teórico, 7 camadas
- TCP/IP: Modelo prático, 4 camadas, baseado na Internet real

---

## 1.5 Exemplos de Redes

### Internet

**Estrutura:**
- **Backbone**: Redes tronco de alta velocidade
- **ISPs (Internet Service Providers)**: Fornecedores de acesso
- **Níveis**: Tier 1 (tronco global), Tier 2 (regionais), Tier 3 (locais)

**Protocolos principais:**
- IP (Internet Protocol)
- TCP (Transmission Control Protocol)
- HTTP (HyperText Transfer Protocol)
- DNS (Domain Name System)

### Redes 3G e 4G (Agora 5G)

**Evolução das redes móveis:**
- **1G**: Analógico, apenas voz
- **2G**: Digital, SMS, dados básicos
- **3G**: Internet móvel, dados mais rápidos
- **4G/LTE**: Internet de alta velocidade
- **5G**: Ultra alta velocidade, baixa latência, IoT

### LANs Sem Fio (WiFi - IEEE 802.11)

**Padrões:**
- **802.11a/b/g/n**: Evolução das velocidades
- **802.11ac (WiFi 5)**: Alta velocidade, 5GHz
- **802.11ax (WiFi 6)**: Melhor eficiência, mais dispositivos

**Aplicações:**
- Redes domésticas
- Hotspots públicos
- Redes corporativas

### RFID e Redes de Sensores

**RFID (Radio Frequency Identification):**
- Identificação por radiofrequência
- Tags passivas e ativas
- Aplicações: Logística, controle de acesso

**Redes de Sensores:**
- Múltiplos sensores colaborando
- Baixo consumo de energia
- Aplicações: Monitoramento ambiental, IoT

---

## 1.6 Arquiteturas de Rede

### Arquitetura da Internet

**Componentes principais:**
- **Roteadores**: Encaminham pacotes entre redes
- **Switches**: Conectam dispositivos na mesma rede
- **Hosts**: Computadores finais (clientes e servidores)
- **Enlaces**: Meios físicos de transmissão

**Hierarquia:**
```
Internet Backbone (Tier 1 ISPs)
    ↓
Regional ISPs (Tier 2)
    ↓
Local ISPs (Tier 3)
    ↓
Usuários finais
```

### Arquitetura de Serviços

**Comunicação orientada à conexão:**
- Estabelece conexão antes de transferir dados
- Garante entrega ordenada e confiável
- Exemplo: TCP

**Comunicação sem conexão:**
- Não estabelece conexão prévia
- Cada pacote é independente
- Mais rápido, menos confiável
- Exemplo: UDP

---

## 1.7 Padronização

### Quem Faz os Padrões?

**Organizações importantes:**

**ISO (International Organization for Standardization):**
- Padrões internacionais
- Modelo OSI

**IEEE (Institute of Electrical and Electronics Engineers):**
- Padrões técnicos
- IEEE 802 (Ethernet, WiFi)

**IETF (Internet Engineering Task Force):**
- Padrões da Internet
- RFCs (Request for Comments)
- TCP/IP, HTTP, DNS

**ITU (International Telecommunication Union):**
- Telecomunicações
- Padrões de telefonia

**ANSI (American National Standards Institute):**
- Padrões nacionais dos EUA

### Padrões de Rede

**Processo de padronização:**
1. **Problema identificado**: Necessidade de padronização
2. **Proposta**: Documento técnico (RFC, draft)
3. **Discussão e revisão**: Feedback da comunidade
4. **Padrão final**: Aprovação e publicação
5. **Implementação**: Produtos e serviços

**Importância:**
- Garante **interoperabilidade**
- Permite competição e inovação
- Facilita adoção global

---

## 1.8 Questões de Desempenho

### Bandwidth vs Throughput

**Bandwidth (Largura de Banda):**
- Capacidade teórica máxima do canal
- Medida em bits por segundo (bps)
- Exemplo: 1 Gbps (Gigabit por segundo)

**Throughput (Taxa de Transferência):**
- Taxa real de dados transferidos
- Sempre menor que bandwidth devido a overhead
- Afetado por: latência, congestionamento, protocolos

### Latência

**Componentes:**
- **Latência de propagação**: Tempo que sinal leva para atravessar o meio
- **Latência de transmissão**: Tempo para colocar dados no meio
- **Latência de processamento**: Tempo para processar pacotes
- **Latência de fila**: Tempo em filas de roteadores

**Fórmula:**
```
Latência Total = Propagação + Transmissão + Processamento + Fila
```

### Jitter

- Variação na latência
- Importante para aplicações em tempo real (voz, vídeo)
- Baixo jitter = mais consistente

### Relação Delay × Bandwidth

**Delay-Bandwidth Product:**
- Quantidade de dados "em trânsito" no enlace
- Importante para otimização de protocolos
- Exemplo: Satélite com alta bandwidth mas alta latência

---

## 1.9 Questões de Segurança

### Ameaças Comuns

**Confidencialidade:**
- Dados interceptados por terceiros
- Necessita criptografia

**Integridade:**
- Dados modificados durante transmissão
- Necessita checksums, hashes, assinaturas digitais

**Disponibilidade:**
- Serviços indisponíveis (DoS, DDoS)
- Necessita redundância, proteção contra ataques

**Autenticação:**
- Verificar identidade de usuários/sistemas
- Senhas, certificados digitais, tokens

**Não-repúdio:**
- Prevenir negação de ações
- Assinaturas digitais, logs

### Mecanismos de Segurança

**Criptografia:**
- Dados protegidos durante transmissão
- Simétrica e assimétrica

**Firewalls:**
- Filtrar tráfego de rede
- Bloquear acesso não autorizado

**IDS/IPS:**
- Detecção e prevenção de intrusões
- Monitoramento de padrões suspeitos

---

## Conceitos-Chave para Red Team / Cybersegurança OT

### Por Que Isso É Importante?

**Para profissionais de Red Team em ambientes críticos:**

1. **Compreensão da Superfície de Ataque:**
   - Entender camadas ajuda a identificar pontos de ataque
   - Cada camada tem vulnerabilidades específicas

2. **Análise de Tráfego:**
   - Identificar protocolos e serviços
   - Detectar comunicação anômala
   - Entender o que está "normal" vs "suspeito"

3. **Segmentação de Rede:**
   - Aplicar princípios de camadas para criar zonas seguras
   - Isolar sistemas críticos (OT) de redes corporativas (IT)

4. **Protocolos Industriais:**
   - Muitos protocolos OT operam nas camadas de aplicação e transporte
   - Compreender modelo OSI ajuda a analisar protocolos como Modbus, DNP3

5. **Arquitetura de Segurança:**
   - Defender em múltiplas camadas (defense in depth)
   - Implementar controles em cada nível

### Aplicação Prática em OT

**Exemplo - Análise de Rede Industrial:**

```
Camada 7 (Aplicação):  Modbus TCP, DNP3, IEC 61850
Camada 4 (Transporte): TCP (porta 502, 20000, etc.)
Camada 3 (Rede):       IP dos PLCs e SCADAs
Camada 2 (Enlace):     Ethernet industrial (muitas vezes sem switch management)
Camada 1 (Física):     Cabeamento industrial (mais robusto que IT)
```

**Pontos críticos:**
- Protocolos OT frequentemente **não criptografados** (Camada 7)
- **Falta de autenticação** em protocolos antigos
- Necessidade de entender **comunicação entre camadas** para detectar anomalias

---

## Resumo dos Conceitos Principais

### 1. Hierarquia de Protocolos
- Organização em camadas facilita design e manutenção
- Cada camada tem responsabilidade específica
- Modelo OSI (7 camadas) vs TCP/IP (4 camadas)

### 2. Modelo OSI
- Camadas: Física → Enlace → Rede → Transporte → Sessão → Apresentação → Aplicação
- Cada camada adiciona informações (headers) aos dados
- Comunicação peer-to-peer entre camadas equivalentes

### 3. Tipos de Redes
- Broadcast: Canal compartilhado (Ethernet, WiFi)
- Point-to-Point: Conexões diretas (Internet)

### 4. Padronização
- Essencial para interoperabilidade
- Organizações: ISO, IEEE, IETF, ITU

### 5. Desempenho
- Bandwidth vs Throughput
- Latência e seus componentes
- Jitter para aplicações em tempo real

### 6. Segurança
- Múltiplas camadas de defesa
- Criptografia, autenticação, integridade
- Ameaças: interceptação, modificação, DoS

---

## Projetos Práticos Sugeridos

1. **Mapear Topologia de Rede Local**
   - Usar `arp`, `netstat`, `ipconfig/ifconfig`
   - Identificar dispositivos na sua rede

2. **Identificar Protocolos em Uso**
   - Capturar tráfego com Wireshark
   - Identificar protocolos em cada camada OSI

3. **Analisar Headers de Pacotes**
   - Examinar headers Ethernet, IP, TCP em Wireshark
   - Entender que informações cada camada adiciona

4. **Criar Diagrama de Rede**
   - Documentar arquitetura de uma rede simples
   - Identificar camadas OSI em cada componente

5. **Comparar Modelos OSI e TCP/IP**
   - Criar tabela comparativa
   - Mapear protocolos para cada modelo

---

## Referências e Leitura Complementar

**Do Capítulo 1 do Tanenbaum:**
- Seção 1.1: Usos das redes
- Seção 1.2: Hardware de rede
- Seção 1.3: Software de rede
- Seção 1.4: Modelos de referência
- Seção 1.5: Exemplos de redes
- Seção 1.6: Arquiteturas de rede
- Seção 1.7: Padronização
- Seção 1.8: Questões de desempenho
- Seção 1.9: Questões de segurança

**Recursos Adicionais:**
- RFCs relevantes (disponíveis em ietf.org)
- Documentação IEEE 802
- Padrões ISO relevantes

---

## Checklist de Aprendizado

Marque quando dominar cada conceito:

- [ ] Entendo o modelo OSI e suas 7 camadas
- [ ] Compreendo diferença entre OSI e TCP/IP
- [ ] Sei identificar tipos de redes (broadcast vs point-to-point)
- [ ] Entendo conceitos de bandwidth, throughput e latência
- [ ] Compreendo importância da padronização
- [ ] Sei relacionar ameaças de segurança às camadas OSI
- [ ] Consigo aplicar conceitos em contexto de OT/redes industriais
- [ ] Entendo hierarquia e estrutura da Internet
- [ ] Compreendo comunicação orientada à conexão vs sem conexão

---

## 3 Ideias de Projetos Práticos

### Projeto 1: Analisador de Topologia de Rede --> ARpy

**Objetivo:** Criar um script que mapeia a topologia básica de uma rede local, identificando dispositivos e seus relacionamentos.

**O que você vai fazer:**
- Usar `arp -a` ou `ip neigh` para listar dispositivos conhecidos
- Fazer scan de rede para descobrir dispositivos ativos
- Identificar tipos de dispositivos (roteadores, switches, hosts)
- Gerar um diagrama simples da topologia

**Conceitos aplicados:**
- Modelo OSI (identificar em qual camada cada ferramenta opera)
- Redes broadcast vs point-to-point
- Endereçamento de rede
- Protocolos de descoberta (ARP)

**Ferramentas:** Python, scapy, networkx (para visualização), arp-scan, nmap

---

### Projeto 2: Monitor de Protocolos em Rede

**Objetivo:** Desenvolver um monitor que captura e classifica tráfego de rede por protocolo e camada OSI.

**O que você vai fazer:**
- Capturar pacotes usando biblioteca Python (scapy ou pyshark)
- Identificar protocolos em diferentes camadas OSI
- Classificar tráfego (HTTP na camada 7, TCP na camada 4, IP na camada 3, Ethernet na camada 2)
- Gerar estatísticas de uso por protocolo

**Conceitos aplicados:**
- Hierarquia de protocolos
- Modelo OSI em prática
- Headers de diferentes camadas
- Análise de tráfego de rede

**Ferramentas:** Python, scapy/pyshark, Wireshark (para validação)

---

### Projeto 3: Simulador de Comunicação em Camadas

**Objetivo:** Implementar uma simulação simples de comunicação seguindo o modelo OSI, onde dados passam por diferentes camadas.

**O que você vai fazer:**
- Criar classes Python para cada camada OSI
- Simular encapsulamento (cada camada adiciona header)
- Simular desencapsulamento (cada camada remove seu header)
- Visualizar como dados são transformados em cada camada

**Conceitos aplicados:**
- Modelo OSI completo
- Encapsulamento de dados
- Hierarquia de protocolos
- Interfaces entre camadas

**Ferramentas:** Python (classes, objetos), visualização (matplotlib ou diagramas texto)

**Exemplo de saída:**
```
Aplicação: "Hello"
  ↓ adiciona header
Transporte: [TCP Header]"Hello"
  ↓ adiciona header
Rede: [IP Header][TCP Header]"Hello"
  ↓ adiciona header
Enlace: [Ethernet Header][IP Header][TCP Header]"Hello"
```

---

**Próximo Capítulo:** [Capítulo 2 - A Camada Física](../cap2/README.md)

