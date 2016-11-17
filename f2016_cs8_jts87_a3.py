def adddistance(distances,name,distance):
    #if the name is not in distances
    if name not in distances:
        distances[name] = [distance]+distances.get(name,[])
    #otherwise,distances for this name is increment by current distance
    distances[name] = [distance]+distances[name]
def addcount(frequencies,name):
    #if the name is not in frequencies, name counter is zero
    if name not in frequencies:
        frequencies[name] = 0
    #otherwise, frequencies increment by 1
    else:
        frequencies[name] += 1
file = open('f2016_cs8_a3.data.txt','r')
outfile = open('f2016_cs8_jts87_a3.data.output.csv','w')
#number of files read
numfiles=0
#total number of lines read
numlines=0
#total distance run
totaldistance=0
distances={}
frequencies={}
for namefile in file:
    numfiles+=1
    currentfile=open(namefile.rstrip(),'r')
    #total distance run for each participant
    totalindividualdistance=0
    currentfile.readline()
    for namefile in currentfile:
        name,distance = namefile.split(',')
        totaldistance+=float(distance)
        numlines+=1
        totalindividualdistance+=float(distance)
        #add to dictionaries
        adddistance(distances,name,float(distance))
        addcount(frequencies,name)
#number of participants with multiple records
numbermultiple=0
#total number of participants
numberparticipants=0
#max distance run
max=0
#min distance run
min=totalindividualdistance
#find number of participants with multiple records
for participant in frequencies:
    numberparticipants+=1
    if frequencies[participant]>1:
        numbermultiple +=1
#find min and max distances run  by participant
for participant in distances:
    dist=sum(distances[participant])
    #print output to the file
    print(participant.rstrip()+','+str(frequencies[participant])+','+str(dist), file=outfile)
    if dist>max:
        max=dist
    if dist<min:
        min=dist
#strings for the participants within  min and max distances run
participantsmin=''
participantsmax=''
for participant in distances:
    dist=sum(distances[participant])
    if dist==max:
        participantsmax+=participant+' '
    if dist==min:
        participantsmin+=participant+' '
#print outputs in format:
#
#Number of Input files read : xx
#Total number of lines read : xx
#Total distance run         : xxxx.xxxxx
#Max distance run           : xxxx.xxxxx
# by participant            : participant name
#Min distance run           : xxxx.xxxxx
# by participant            : participant name
#Total number of participants : xx
#Number of participants
# with multiple records     : xx
print('Number of Input files read: '+str(numfiles))
print('Total number of lines read: '+str(numlines))
print('Total distance run        : '+str(totaldistance))
print('Max distance run          : '+str(max))
print('   by participant         : '+participantsmax)

print('Min distance run          : '+str(min))
print('   by participant         : '+participantsmin)
  
print('Total number of participants: '+str(numberparticipants))
print('Number of participants\nwith multiple records: '+str(numbermultiple))