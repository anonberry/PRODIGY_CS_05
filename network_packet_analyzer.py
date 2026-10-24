"""
Network Packet Analyzer (Educational)

Captures a limited number of packets on an interface you are authorized to
monitor, then displays basic metadata and a short payload preview.

Use only on your own device/network or with explicit permission.
Payload previews are intentionally short; avoid collecting sensitive traffic.
"""

from datetime import datetime
from scapy.all import sniff, IP, IPv6, TCP, UDP, ICMP, DNS, Raw, get_if_list


MAX_PAYLOAD_PREVIEW = 48


def protocol_name(packet):
    """Return a simple protocol label based on packet layers."""
    if packet.haslayer(DNS):
        return "DNS"
    if packet.haslayer(TCP):
        return "TCP"
    if packet.haslayer(UDP):
        return "UDP"
    if packet.haslayer(ICMP):
        return "ICMP"
    if packet.haslayer(IP):
        return "IPv4"
    if packet.haslayer(IPv6):
        return "IPv6"
    return "Other"


def endpoints(packet):
    """Extract source/destination IP addresses and ports when available."""
    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst
    elif packet.haslayer(IPv6):
        src = packet[IPv6].src
        dst = packet[IPv6].dst
    else:
        return "N/A", "N/A", "", ""

    src_port = dst_port = ""
    if packet.haslayer(TCP):
        src_port, dst_port = str(packet[TCP].sport), str(packet[TCP].dport)
    elif packet.haslayer(UDP):
        src_port, dst_port = str(packet[UDP].sport), str(packet[UDP].dport)

    return src, dst, src_port, dst_port


def safe_payload_preview(packet):
    """Show only a short, printable preview; do not dump full payloads."""
    if not packet.haslayer(Raw):
        return "(no exposed payload)"

    data = bytes(packet[Raw].load)[:MAX_PAYLOAD_PREVIEW]
    preview = "".join(chr(b) if 32 <= b <= 126 else "." for b in data)
    suffix = "..." if len(bytes(packet[Raw].load)) > MAX_PAYLOAD_PREVIEW else ""
    return repr(preview + suffix)


def analyze_packet(packet, index):
    src, dst, src_port, dst_port = endpoints(packet)
    protocol = protocol_name(packet)
    timestamp = datetime.now().strftime("%H:%M:%S")

    print(f"\n[{index}] {timestamp} | {protocol}")
    print(f"    Source:      {src}" + (f":{src_port}" if src_port else ""))
    print(f"    Destination: {dst}" + (f":{dst_port}" if dst_port else ""))
    print(f"    Packet size: {len(packet)} bytes")
    print(f"    Payload:     {safe_payload_preview(packet)}")


def main():
    print("=" * 58)
    print("           EDUCATIONAL NETWORK PACKET ANALYZER")
    print("=" * 58)
    print("Use only on networks/devices you own or are authorized to monitor.")
    print("\nAvailable interfaces:")
    for interface in get_if_list():
        print(f"  - {interface}")

    interface = input(
        "\nInterface name (press Enter for Scapy's default): "
    ).strip() or None

    try:
        packet_limit = int(input("Number of packets to capture (1-100): ").strip())
        if not 1 <= packet_limit <= 100:
            raise ValueError
    except ValueError:
        print("Please enter a whole number between 1 and 100.")
        return

    print(f"\nListening for up to {packet_limit} packets...")
    print("Press Ctrl+C to stop early.\n")

    count = {"value": 0}

    def handle(packet):
        count["value"] += 1
        analyze_packet(packet, count["value"])

    try:
        sniff(
            iface=interface,
            prn=handle,
            store=False,
            count=packet_limit,
        )
    except KeyboardInterrupt:
        print("\nCapture stopped by user.")
    except PermissionError:
        print("\nPermission denied. Packet capture may require administrator/root rights.")
        print("Run only with appropriate authorization.")
    except OSError as exc:
        print(f"\nCapture error: {exc}")
        print("Check the interface name and capture permissions.")

    print(f"\nFinished. Packets displayed: {count['value']}")


if __name__ == "__main__":
    main()
