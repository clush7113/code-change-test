import time

def greenBottles():
    bottles=int(input("How many green bottles? "))
    for x in range(bottles):
        if bottles-1==1:
            plural="bottle"
        else:
            plural="bottles"
        print("""{0} green bottles, sitting on the wall
                 {0} green bottles, sitting on the wall
                 but if 1 green bottle should accidentally fall
                 there'll be {1} green {2} sitting on the wall""".format(bottles,bottles-1,plural))
        bottles=bottles-1
        time.sleep(0.5)
greenBottles()
