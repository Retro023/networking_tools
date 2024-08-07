import ipaddress
import argparse

def calculate_hosts(subnetmask: str) -> int:
    # Splitting the subnet into octets and then to an int
    octets = subnetmask.split('.')
    
    # Convert the subnet mask to binary "110010101"
    network_bits = sum(bin(int(octet)).count('1') for octet in octets)
    
    # Total bits for a IPV4 addr
    total_bits = 32
    
    # Calculate number of host bits 
    host_bits = total_bits - network_bits
    
    # Calculate number of hosts on a network
    if host_bits == 0:
        number_of_hosts = 0
    else:
        number_of_hosts = (2 ** host_bits) - 2
    
    return number_of_hosts

def detailed_output(subnetmask: str):
    try:
        # Validate and create network from dotted-decimal subnet mask
        if '/' not in subnetmask:
            mask_bits = sum(bin(int(octet)).count('1') for octet in subnetmask.split('.'))
            network = ipaddress.ip_network(f"0.0.0.0/{mask_bits}", strict=False)
        else:
            network = ipaddress.ip_network(subnetmask, strict=False)
        
        print(f"Network Address: {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Usable IP Range: {network.network_address + 1} - {network.broadcast_address - 1}")
        print(f"Number of Usable Hosts: {calculate_hosts(subnetmask)}")
    except ValueError as e:
        print(f"Invalid subnet mask: {e}")

def main():
    # args
    parser = argparse.ArgumentParser(description='Subnet calculator')
    parser.add_argument('subnetmask', type=str, help='Subnet mask in CIDR or dotted-decimal format')
    parser.add_argument('-v', '--verbose', action='store_true', help='Detailed output')
    args = parser.parse_args()

    # Calculate number of hosts
    try:
        hosts = calculate_hosts(args.subnetmask)
    except ValueError as e:
        print(f"Invalid subnet mask: {e}")
        return

    if args.verbose:
        # Print detailed output if -v is specified
        detailed_output(args.subnetmask)
    else:
        # Print basic output
        print(f"The number of hosts available is: {hosts}")

if __name__ == "__main__":
    main()
