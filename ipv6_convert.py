import ipaddress as ip

def expand_ipv6_address(shortened_address):
    full_address = ip.ip_address(shortened_address).exploded
    return full_address

def converting_to_standard():
    shortened_address = input("Supply the shortened IPv6 address: ")
    full_address = expand_ipv6_address(shortened_address)
    print(full_address)

def shorten_ipv6_address(full_address):
    compressed_address = ip.ip_address(full_address).compressed
    if '::' in compressed_address:
        parts = compressed_address.split(':')
        for i, part in enumerate(parts):
            if part == '':
                parts[i] = '0'  
            else:
                parts[i] = str(hex(int(part, 16)))[2:]  
        compressed_address = ':'.join(parts)
    return compressed_address

def converting_to_shortened():
    expanded_address = input("Supply the full address to be shortened: ")
    shortened_address = shorten_ipv6_address(expanded_address)
    print(shortened_address)

def main():
    choice = input("Would you like to shorten or expand (E/S): ")
    if choice == "E":
        converting_to_standard()
    elif choice == "S":
        converting_to_shortened()
    else:
        print("Input not recognized")

if __name__ == "__main__":
    main()