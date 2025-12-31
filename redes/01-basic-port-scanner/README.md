# Scanner Básico de Portas TCP

## Descrição

Este é um scanner básico de portas TCP desenvolvido em Python puro (sem dependências externas).

Estudamos nele fundamentos de:

- Protocolo TCP/IP
- Conexões de rede
- Threading em Python
- Metodologia de scanning (primeira fase do penetration testing)

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

## Como Funciona

1. **Conexão TCP**: O script tenta estabelecer uma conexão TCP completa (handshake) com cada porta
2. **Threading**: Usa múltiplas threads para escanear várias portas simultaneamente (mais rápido)
3. **Timeout**: Cada tentativa de conexão tem um timeout de 1 segundo (padrão)
4. **Identificação de Serviços**: Tenta identificar serviços conhecidos nas portas abertas

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