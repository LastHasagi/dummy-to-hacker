# ARpy - Analisador de Rede Python baseado na tabela ARP
# Autor: Rodrigo Graça

# Tive 40 minutos pra fazer isso e não usei o scapy
# Pra próxima versão, usar o scapy para scan da rede e obter o hostname, além de usar o comando ping para verificar se o dispositivo está ativo
# Dá para usar o scapy para fazer requisição ARP ativa, detectar dispositivos novos na rede, monitorar o tráfego de rede, etc...
# Dá inclusive pra transformar isso aqui em um programa de sniffing de rede, mas acho que foge um pouco do exercício 

import sys
import subprocess
import re
import socket
import ipaddress

def obter_tabela_arp():
    """Obtém a tabela ARP do sistema e retorna lista de (IP, MAC)."""
    try:
        resultado = subprocess.run(['arp', '-a'], capture_output=True, text=True)
        if resultado.returncode != 0:
            return []
        
        dispositivos = []
        for linha in resultado.stdout.splitlines():
            ip_match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', linha)
            mac_match = re.search(r'([0-9a-fA-F]{2}[-:]){5}[0-9a-fA-F]{2}', linha)
            
            if ip_match and mac_match:
                ip = ip_match.group(0)
                mac = mac_match.group(0).upper().replace('-', ':')
                dispositivos.append((ip, mac))
        
        return dispositivos
    except Exception as e:
        print(f"[-] Erro ao obter tabela ARP: {e}")
        return []

def obter_ip_local():
    """Descobre o IP local conectando a um IP externo."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return None

def obter_gateway():
    """Obtém o gateway padrão via comando route (Windows)."""
    try:
        resultado = subprocess.run(['route', 'print', '0.0.0.0'], 
                                  capture_output=True, text=True, timeout=5)
        for linha in resultado.stdout.splitlines():
            if '0.0.0.0' in linha:
                partes = linha.split()
                if len(partes) >= 3:
                    gateway = partes[2]
                    if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', gateway):
                        return gateway
    except Exception:
        pass
    return None

def identificar_tipo(ip, gateway):
    """Identifica se dispositivo é roteador ou host."""
    if ip == gateway:
        return 'Roteador'
    if ip.endswith('.1') or ip.endswith('.254'):
        return 'Roteador (possível)'
    return 'Host'

def obter_hostname(ip):
    """Tenta obter hostname do IP."""
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return ip # Se não conseguir obter o hostname, retorna o IP

def escanear_rede(rede, timeout=0.5):
    """Escaneia rede tentando conectar na porta 80 de cada IP.""" # Talvez isso possa ser melhorado para usar o comando ping para verificar se o dispositivo está ativo
    hosts_ativos = []
    print(f"[*] Escaneando {rede} (isso pode levar alguns segundos)...\n")
    
    for ip in rede.hosts():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            if sock.connect_ex((str(ip), 80)) == 0:
                hosts_ativos.append(str(ip))
            sock.close()
        except Exception:
            pass
    
    return hosts_ativos

def exibir_resultados(dispositivos, ip_local, gateway, rede, hosts_escaneados):
    """Exibe todos os resultados formatados."""
    print("=" * 70)
    print("DIAGRAMA DE TOPOLOGIA DE REDE")
    print("=" * 70)
    print(f"\nRede: {rede}")
    print(f"Seu IP: {ip_local}")
    if gateway:
        print(f"Gateway: {gateway}")
    
    print("\n" + "=" * 70)
    print("DISPOSITIVOS DESCOBERTOS")
    print("=" * 70 + "\n")
    
    # Agrupa por tipo
    roteadores = []
    hosts = []
    
    for ip, mac in dispositivos:
        tipo = identificar_tipo(ip, gateway)
        hostname = obter_hostname(ip)
        
        if 'Roteador' in tipo:
            roteadores.append((ip, mac, hostname, tipo))
        else:
            hosts.append((ip, mac, hostname, tipo))
    
    # Exibe roteadores
    if roteadores:
        print("[ROTEADORES]")
        print("-" * 70)
        print(f"{'IP':<18} {'MAC Address':<20} {'Hostname':<30}")
        print("-" * 70)
        for ip, mac, hostname, tipo in roteadores:
            hostname_curto = hostname[:29] if len(hostname) > 29 else hostname
            print(f"{ip:<18} {mac:<20} {hostname_curto:<30}")
        print()
    
    # Exibe hosts
    if hosts:
        print("[HOSTS]")
        print("-" * 70)
        print(f"{'IP':<18} {'MAC Address':<20} {'Hostname':<30}")
        print("-" * 70)
        for ip, mac, hostname, tipo in hosts:
            hostname_curto = hostname[:29] if len(hostname) > 29 else hostname
            marcador = " (VOCÊ)" if ip == ip_local else ""
            print(f"{ip:<18} {mac:<20} {hostname_curto}{marcador:<30}")
        print()
    
    # Estatísticas
    print("=" * 70)
    print("ESTATÍSTICAS")
    print("=" * 70)
    print(f"Dispositivos na tabela ARP: {len(dispositivos)}")
    print(f"Hosts escaneados: {len(hosts_escaneados)}")
    
    # Diagrama
    print("\n" + "=" * 70)
    print("DIAGRAMA")
    print("=" * 70)
    print("\n                    [Internet]")
    print("                         |")
    
    if gateway:
        print(f"                    [{gateway}]")
        print("                    (Roteador)")
        print("                         |")
        print("                  [Rede Local]")
        print(f"                  {rede}")
        print("                         |")
        
        todos_hosts = roteadores + hosts
        for i, (ip, mac, hostname, tipo) in enumerate(todos_hosts):
            if ip != gateway:
                marcador = " (VOCÊ)" if ip == ip_local else ""
                conector = "├── " if i < len(todos_hosts) - 1 else "└── "
                print(f"                    {conector}[{ip}]{marcador}")
    
    print("\n" + "=" * 70)

def main():
    """Função principal."""
    print("=" * 70)
    print("ARpy - Analisador de Rede Python")
    print("=" * 70)
    
    # Obtém informações da rede
    print("[*] Obtendo informações da rede...")
    ip_local = obter_ip_local()
    if not ip_local:
        print("[-] Erro: Não foi possível obter IP local.")
        sys.exit(1)
    
    gateway = obter_gateway()
    rede = ipaddress.IPv4Network(f"{ip_local}/24", strict=False)
    
    print(f"[+] IP Local: {ip_local}")
    if gateway:
        print(f"[+] Gateway: {gateway}")
    print(f"[+] Rede: {rede}\n")
    
    # Obtém tabela ARP
    print("[*] Obtendo tabela ARP...")
    dispositivos = obter_tabela_arp()
    if not dispositivos:
        print("[-] Tabela ARP vazia. Tente acessar alguns dispositivos na rede primeiro.")
        sys.exit(1)
    
    print(f"[+] {len(dispositivos)} dispositivos encontrados.\n")
    
    # Scan opcional
    hosts_escaneados = []
    try:
        escolha = input("[?] Deseja escanear a rede? (s/N): ").strip().lower()
        if escolha == 's':
            hosts_escaneados = escanear_rede(rede)
            print(f"[+] {len(hosts_escaneados)} hosts ativos encontrados.\n")
    except KeyboardInterrupt:
        print("\n[*] Scan cancelado.\n")
    
    exibir_resultados(dispositivos, ip_local, gateway, rede, hosts_escaneados)
    
    print("\n[+] Análise concluída!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[*] Interrompido pelo usuário.")
        sys.exit(0)
    except Exception as e:
        print(f"\n[-] Erro: {e}")
        sys.exit(1)