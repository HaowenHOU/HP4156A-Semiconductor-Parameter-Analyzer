# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 00:26:15 2015

@author: Hou Haowen
"""
import visa
#import time

class HP4156A():
    def __init__(self):
        
        pass
    
    def open_connection(self,address):
        self.address=address
        self.rm = visa.ResourceManager()
        self.myinst = self.rm.open_resource(self.address)
        self.myinst.timeout=5000 #tuning the timeout
        
    def reset(self):
        """Resets configuration of HP4156A to default."""
        self.myinst.write("*rst")
        pass
    
    def measurementMode(self, arg1):
        #arg1 is the measurement mode. 
        #Valid arguements are Sweep = SWE, Sampling = SAMP.
        if (arg1 == "SWE" or arg1 == "SAMP"):
            self.myinst.write(":PAGE:CHAN:MODE " + arg1)
	
        else:
            print "Invalid measurement mode."
            pass
    
    def smuSetup(self,smu_name,smu_parameters):
        """smu_name is the SMU name, ie SMU1, SMU2, etc."""
        """smu_parameters is the parameters [VNMAE,INAME,MODE,FUCNTION] for the SMU. ie [VS,IS,COMMON,CONS] """
        self.smu_parameters = self.smuSetup_string(smu_parameters)
        self.smu_cmd = ":PAGE:CHAN:" + smu_name + ":"
        self.myinst.write(self.smu_cmd + "VNAME %s" % self.smu_parameters[0])
        self.myinst.write(self.smu_cmd + "INAME %s" % self.smu_parameters[1])
        self.myinst.write(self.smu_cmd + "MODE %s" % self.smu_parameters[2])
        self.myinst.write(self.smu_cmd + "FUNC %s" % self.smu_parameters[3])
        
    def smuSetup_string(self, arg):
    		"""To generate correct cmd for smuSetup."""
    		arg[0] = "'" + arg[0] + "'"
    		arg[1] = "'" + arg[1] + "'"
    		return arg
      
    def sweepSetup(self,var_name,var_parameters):
        
        self.var_parameters = var_parameters
        self.var_cmd = ":PAGE:MEAS:" + var_name + ":"
        if var_name == "VAR1":
            self.myinst.write(self.var_cmd + "STAR %s" % self.var_parameters[0])
            self.myinst.write(self.var_cmd + "STOP %s" % self.var_parameters[1])
            self.myinst.write(self.var_cmd + "STEP %s" % self.var_parameters[2])
            self.myinst.write(self.var_cmd + "COMP %s" % self.var_parameters[3])
            
        elif var_name == "VAR2":
            self.myinst.write(self.var_cmd + "STAR %s" % self.var_parameters[0])
            self.myinst.write(self.var_cmd + "STEP %s" % self.var_parameters[1])
            self.myinst.write(self.var_cmd + "POIN %s" % self.var_parameters[2])
            self.myinst.write(self.var_cmd + "COMP %s" % self.var_parameters[3])
            
        else:
            print "Invalid variable."
            
    def samplingSetup(self,smu_name,var_parameters):
        
        self.var_parameters = var_parameters
        self.var_cmd = ":PAGE:MEAS:SAMP:CONS:" + smu_name
        self.myinst.write(self.var_cmd + " %s" % self.var_parameters[0])
        self.myinst.write(":PAGE:MEAS:SAMP:IINT" + " %s" % self.var_parameters[1])
        self.myinst.write(":PAGE:MEAS:SAMP:POIN" + " %s" % self.var_parameters[2])
            
    def singleMeasurement(self,integration_time):
        """Performs a single smeasurement."""
        if (integration_time == "SHOR" or integration_time == "MED" or integration_time == "LONG"):
            self.myinst.write(":PAGE:MEAS:MSET:ITIM " + integration_time)
            self.myinst.write(":PAGE:SCON:SING")
            self.myinst.write("*WAI")
        else:
            print "Invalid integration time."
            pass
        
    def dataAcquisition(self,data_name):
        self.data_list = []
        for data in data_name:
            self.data_unicode=self.myinst.query(":DATA? " + data)
            self.data_split = self.data_unicode.split(",")
            self.data=map(float,self.data_split)
            self.data_list.append(self.data)
        return self.data_list