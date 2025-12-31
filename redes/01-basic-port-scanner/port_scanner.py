import socket
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def _get_service_name(port):
    """
    Obtém o nome do serviço associado à porta.
    
    Args:
        port: Número da porta
    
    Returns:
        str: Nome do serviço ou None se não encontrado
    """
    try:
        return socket.getservbyport(port, 'tcp')
    except (OSError, socket.error):
        return None


def scan_port(host, port, timeout=1):
    """
    Tenta conectar a uma porta específica no host alvo.
    
    Args:
        host: Endereço IP ou hostname do alvo
        port: Número da porta a ser escaneada
        timeout: Tempo máximo de espera para conexão (segundos)
    
    Returns:
        tuple: (porta, status, servico) onde status é 'open', 'closed' ou 'error'
    """
    status, servico = 'closed', None
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            
            if result == 0:
                status = 'open'
                servico = _get_service_name(port)
    except socket.gaierror:
        status, servico = 'error', 'Host inválido'
    except socket.error:
        status, servico = 'error', 'Erro de conexão'
    except Exception as e:
        status, servico = 'error', str(e)
    
    return (port, status, servico)


def scan_port_range(host, ports, max_workers=50):
    """
    Escaneia um range de portas usando múltiplas threads.
    
    Args:
        host: Endereço IP ou hostname do alvo
        ports: Lista de portas a serem escaneadas
        max_workers: Número máximo de threads simultâneas
    
    Returns:
        list: Lista de tuplas (porta, status, servico)
    """
    resultados = []
    
    print(f"[*] Escaneando {host}...")
    print(f"[*] Total de portas: {len(ports)}\n")
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_port = {
            executor.submit(scan_port, host, port): port 
            for port in ports
        }
        
        for future in as_completed(future_to_port):
            resultado = future.result()
            resultados.append(resultado)
    
    return sorted(resultados, key=lambda x: x[0])


def parse_ports(port_string):
    """
    Converte uma string de portas em uma lista de números.
    Suporta formatos: '80', '80,443', '80-100', '80,443,8080-8090'
    
    Args:
        port_string: String com portas
    
    Returns:
        list: Lista de números de portas
    """
    ports = []
    
    for item in port_string.split(','):
        item = item.strip()
        if '-' in item:
            inicio, fim = item.split('-')
            ports.extend(range(int(inicio), int(fim) + 1))
        else:
            ports.append(int(item))
    
    return sorted(set(ports))


def print_results(resultados):
    """
    Imprime os resultados do scan de forma formatada.
    """
    portas_abertas = [r for r in resultados if r[1] == 'open']
    
    print("\n" + "="*60)
    print("RESULTADOS DO SCAN")
    print("="*60)
    
    if portas_abertas:
        print(f"\n[+] {len(portas_abertas)} porta(s) aberta(s):\n")
        print(f"{'Porta':<10} {'Status':<10} {'Serviço':<20}")
        print("-" * 40)
        for porta, status, servico in portas_abertas:
            print(f"{porta:<10} {status:<10} {servico or 'N/A':<20}")
    else:
        print("\n[-] Nenhuma porta aberta encontrada.")
    
    print("\n" + "="*60)


def main():
    """
    Função principal do scanner.
    """
    
    # Validação dos argumentos
    if len(sys.argv) < 2:
        print("Uso: python port_scanner.py <host> [portas]")
        print("\nExemplos:")
        print("  python port_scanner.py 127.0.0.1")
        print("  python port_scanner.py 127.0.0.1 80,443,8080")
        print("  python port_scanner.py scanme.nmap.org 1-1000")
        sys.exit(1)
    
    host = sys.argv[1]
    
    # Define portas padrão ou usa as fornecidas
    if len(sys.argv) > 2:
        try:
            ports = parse_ports(sys.argv[2])
        except ValueError:
            print("[-] Erro: Formato de portas inválido.")
            print("    Use: 80 ou 80,443 ou 80-100 ou 80,443,8080-8090")
            sys.exit(1)
    else:
        # Portas comuns para scan rápido
        ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 
                 993, 995, 1723, 3306, 3389, 5900, 8080]
    
    # Executa o scan
    inicio = time.time()
    resultados = scan_port_range(host, ports)
    tempo_total = time.time() - inicio
    
    # Exibe resultados
    print_results(resultados)
    print(f"\n[*] Scan concluído em {tempo_total:.2f} segundos")


if __name__ == "__main__":
    main()