import sys

def lineprint(lines):
  for line in lines:
    print line
  return

def natfinder(config):
  natconfig=[]
  for line in config:
    if '(' in line:
      natconfig.append(line)
  return natconfig

# Function to strip static nat related statements out of configuration
def staticnat(nat_statements):
  static_nat_statements=[]
  for line in nat_statements:
    if 'static' in line:
      static_nat_statements.append(line)
  #print static_nat_statements
  print 'Your static NAT config is'
  for line in static_nat_statements:
    #print line
    static_nat_line_elements=line.split()
    #lineprint(static_nat_line_elements)
    print ('object network static-'+static_nat_line_elements[3])
    print('  host '+static_nat_line_elements[3])
    print('  nat '+static_nat_line_elements[1]+' '+static_nat_line_elements[0]+' '+static_nat_line_elements[2])
  return static_nat_statements

# Function to find global and matching nat statements
def patconverter_orig(config):
  localnat=[]
  globalnat=[]
  splitlocal=[]
  splitglobal=[]
  globalconfig=[]
  localconfig=[]
  nattuples=[]
  # Iterate through config and find local and global nat statements
  for line in config:
    if 'nat (' in line:
      localnat.append(line)
    elif 'global (' in line:
      globalnat.append(line)
  #lineprint(globalnat)
  #lineprint(localnat)
  # Iterate through list of global nat statements and find matching local nat statement(s)
  for line in globalnat:
    splitglobal=line.split()
    #print 'matching for '+line
	# need to fix the following line so globalconfig is of type list, and not string
    globalconfig.append(line)
    for line in localnat:
      splitlocal=line.split()
      if splitglobal[2]==splitlocal[2]:
        #print 'matched statements found for '+line
        localconfig.append(line)
    nattuple=(globalconfig,localconfig)
    globalconfig=[]
    #print nattuple
    localconfig=[]
    nattuples.append(nattuple)
  print nattuples
  return nattuples

#Alternate function using lists, instead of tuples to match PAT statements
def patconverter(config):
  localnat=[]
  globalnat=[]
  splitlocal=[]
  splitglobal=[]
  globalconfig=[]
  localconfig=[]
  completenatlist=[]
  listofnatstatements=[]
  # Iterate through config and find local and global nat statements
  for line in config:
    if 'nat (' in line:
      localnat.append(line)
    elif 'global (' in line:
      globalnat.append(line)
  #lineprint(globalnat)
  #lineprint(localnat)
  # Iterate through list of global nat statements and find matching local nat statement(s)
  for line in globalnat:
    splitglobal=line.split()
    #print 'matching for '+line
	# need to fix the following line so globalconfig is of type list, and not string
    globalconfig.append(line)
    for line in localnat:
      splitlocal=line.split()
      if splitglobal[2]==splitlocal[2]:
        #print 'matched statements found for '+line
        globalconfig.append(line)
    listofnatstatements.append(globalconfig)
    globalconfig=[]
    #print nattuple
    localconfig=[]
    #completenatlist.append(listofnatstatements)
  #print listofnatstatements
  return listofnatstatements


def main():
  file=open(sys.argv[1],'r')
  #print '\nyour NAT config lines are'
  natlines=natfinder(file)
  #lineprint(natlines)
  #static_nat=[]
  static_nat_lines=staticnat(natlines)
  print 'PAT statements are'
  file=open(sys.argv[1],'r')
  pattuples=patconverter(file)
  print pattuples

if __name__=="__main__":
  main()

