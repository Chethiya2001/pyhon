from mc import MAC_CHANGER

if __name__ == "__main__":
    mc = MAC_CHANGER()
    mac = mc.Get_mac("eth0")
    print(mc)

    cr_mac=mc.change_mac("eth0", "00:23:45:67:89:10")
    print(cr_mac)
