easyPacket = bytes([0x59, 0x59, 0x03, 0xE8, 0x0, 0x64, 0xB8, 0x7, 0xC0])
errorPacket = bytes([0x59, 0x59, 0x03, 0xE8, 0x0, 0x64, 0xB8, 0x7, 0xC1])
hardPacket = bytes([0x59,0x59,0x59,0x0, 0x10, 0x45,0xB8, 0x7, 0x1F])
easyStream = bytes(easyPacket[2:] + easyPacket + easyPacket)
hardSteam = bytes(hardPacket[1:] + hardPacket)
compountPacket = bytes(easyPacket + hardPacket)

print(len(easyPacket))
print(easyPacket[0])
print(easyPacket)
print(chr(easyPacket[0]))
print(hex(easyPacket[0]))
print(ord('Y'))
print(bin(easyPacket[0]))

for myElement in easyPacket:
        print(myElement)

def getDistance(packet):
    total = sum(packet[:-1])
    check = (0x00FF & total)
    
    if check == packet[8]:
        distLow = packet[2]
        distHigh = packet[3]
        distance = distLow | (distHigh << 8)
        print("check = %x" % check)
        print("checkd = %d" % check)
    
        print("disLow = %x/n " % distLow)
        print("distHigh = %x/n " % distHigh)
    
        return distance
    else:
        print("the milks gon bad")
        return 0

def getstrength(packet):
    total = sum(packet[:-1])
    check = (0x00FF & total)
    
    if check == packet[8]:
        strengthLow = packet[3]
        strengthHigh = packet[4]
        strength = strengthLow | (strengthHigh << 8)
        print("check = %x" % check)
        print("checkd = %d" % check)
    
        print("strengthLow = %x/n " % strengthLow)
        print("strengthHigh = %x/n " % strengthHigh)
    
        return strength
    else:
        print("the milks gon bad")
        return 0
    
print(getstrength(easyPacket))
print("strength = %x " %(getstrength(easyPacket)))

print("strength = %x " %(getstrength(errorPacket)))

