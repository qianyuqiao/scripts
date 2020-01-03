import os
ports = []
f = open("ovs_port.txt", "r")
for line in f.readlines():
    if "error" in line:
        ports.append(line[54:].split(" ")[0])

for port in ports:
    cmd = "ovs-vsctl del-port %s" % port
    os.system(cmd)
