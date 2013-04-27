# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b_precompiled_27 import *
#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    ##setting up the time Steps, population variable
    popAtEnd=[]
    timeBegin=0
    timeMiddle=75
    timeEnd=timeMiddle+150
        
    ##going through all of the trials:
    trialNum=0    
    while trialNum<numTrials:
        ##setting up baseline variables
        numViruses=100
        maxPop=1000
        maxBirthProb=.1
        clearProb=.05
        resistances={'guttagonol': False}
        mutProb=.005
        ##setting up the list of viruses to start
        trialViruses=[]
        for x in range(numViruses):
            trialViruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        ##creating the test patient
        testPatient=TreatedPatient(trialViruses, maxPop)
        
        for step in range(timeBegin, timeMiddle):
            testPatient.update()
        testPatient.addPrescription('guttagonol')
        for step in range(timeMiddle, timeEnd):
            testPatient.update()
            ## print step
        trialNum+=1
        popAtEnd.append(testPatient.getTotalPop())
                        

    print popAtEnd
    ##create the gorram histogram

    pylab.hist(popAtEnd,bins=10)
    pylab.xlabel('End population if scrip added after '+ str(timeMiddle)+' steps')
    pylab.ylabel('Number of Trials')
    pylab.title ('End Virus Population')
    pylab.show()
    return

      
   
##    ##create the gorram plot
##    pylab.figure(1)
##    pylab.plot(avgPopAtTime)
##    pylab.plot(avgResistPopAtTime)
##    pylab.title('Average Resistant Virus Population, drug introduced @ time')
##    pylab.xlabel('Time Steps')
##    pylab.ylabel('Average Virus Population')
##    pylab.legend('total pop') 
##    pylab.show()
    
    




#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
