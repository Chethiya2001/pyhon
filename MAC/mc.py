import subprocess #run the commnds
import re #regular expressions

class MAC_CHANGER:
    def __init__(self):
        self.MAC = ""
    
    def Get_mac(self,iface):
        output = subprocess.run(["ifconfig", iface], shell=False, capture_output=True)

        cmd_reslt = output.stdout.decode('utf-8')
        

        pattern = r'ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'

        regex = re.compile(pattern)

        answer = regex.search(cmd_reslt)

        new_mac = answer.group().split(" ") [1]
        self.MAC = new_mac
        return new_mac

    def change_mac(self, iface, new_mac):
        print("[+] Current MAC address is : ", self.Get_mac(iface))

        output = subprocess.run(["ifconfig", iface,"down"], shell=False, capture_output=True)

        print(output.stderr.decode('utf-8')) # if have nd error print it

        #ifconfig etho0 hw ether 00:11:22:33:44:55
        output = subprocess.run(["ifconfig", iface,"hw", "ether", new_mac], shell=False, capture_output=True)
        print(output.stderr.decode('utf-8'))

        #ifconfig eth0 up
        output = subprocess.run(["ifconfig", iface,"up"], shell=False, capture_output=True)
        print(output.stderr.decode('utf-8'))

        print("[+] Updated MAC ddress is",self.Get_mac(iface))

        return self.Get_mac(iface)

