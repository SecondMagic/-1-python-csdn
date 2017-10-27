import socket
import wmi

def getWinProList():
    ProList = [] 
    c = wmi.WMI() 
    for process in c.Win32_Process(): 
        ProList.append(str(process.Name)) 
    return ProList
def getWinSerList():
    SerList = [] 
    c = wmi.WMI() 
    for service in c.Win32_Service(): 
        SerList.append(str(service.Name)) 
    return SerList
def getSystemInfo():
    c = wmi.WMI()
    systemInfo=''
    for sys in c.Win32_OperatingSystem():
        systemInfo+='Version:'+sys.Caption+' Vernum:'+sys.BuildNumber
        systemInfo+=' '+sys.OSArchitecture
    for processor in c.Win32_Processor():
        systemInfo+=" Process Name:"+processor.Name.strip()
        for Memory in c.Win32_PhysicalMemory():
            systemInfo+=" Memory Capacity:"+str(int(Memory.Capacity)/1024/1024/1024)+' GB'
    return systemInfo
def getIp():
    c = wmi.WMI()
    ipInfo=''
    for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled= True):
        ipInfo+="MAC:"+interface.MACAddress
        for ip_address in interface.IPAddress:
            ipInfo+=" ip:"+ip_address
    return ipInfo
def scanSystem():
    resultInfo=''
    resultInfo+=getIp()+' '+getSystemInfo()
    systemCheck1=systemCheck2=systemCheck3='N'
    ProList=getWinProList()
    for pro in ProList:
        if pro == 'PccNTMon.exe':
            systemCheck1='Y'
    SerList=getWinSerList()
    for ser in SerList:
        if ser == 'TMBMServer':
            systemCheck2='Y'		
        if ser == 'wuauserv':
            systemCheck3='Y'	
    if systemCheck1 == 'Y':
        resultInfo+=' 趋势防病毒软件进程已开启'
    else:
        resultInfo+=' 趋势防病毒软件进程未开启'
    if systemCheck2 == 'Y':
        resultInfo+=' 趋势防病毒服务已开启'
    else:
        resultInfo+=' 趋势防病毒服务未开启'
    if systemCheck3 == 'Y':
        resultInfo+=' 系统已开启自动更新'
    else:
        resultInfo+=' 系统未开启自动更新'
    return resultInfo

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('服务器地址', 9999))
print(s.recv(1024).decode('utf-8'))
s.send(bytes(scanSystem(),encoding='utf-8'))
s.close()