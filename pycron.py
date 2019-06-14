from hardware_object import Scheduler as SC

SC = SC()

def daily(rep):
    for i in range(rep):
        SC.daily()

#def pair_impair(rep)
#    for i in range(rep):
#        SC.pair_impair()

def select():
    print("What would you like to setup:")
    selection = raw_input("""
start at reboot [r]
set a daily [d]
""")
    if selection == "d":
        rep = int(input("How many daily schedules do you want?"))
        daily(rep)
    if selection == "r":
        SC.start_at_boot()
    else:
        pass

if __name__== "__main__":
    try:
        while True:
            select()
    except KeyboardInterrupt:
        print("END pycron")