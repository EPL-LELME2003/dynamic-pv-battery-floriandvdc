from pyomo.environ import ConcreteModel, Var, Objective, Constraint, NonNegativeReals, minimize, SolverFactory
import matplotlib.pyplot as plt

# Data / Parameters
model.lf_pv           = pyo.Param(initialize=990)     # [/]
model.load            = pyo.Param(initialize=990)


load = [99,93, 88, 87, 87, 88, 109, 127, 140, 142, 142, 140, 140, 140, 137, 139, 146, 148, 148, 142, 134, 123, 108, 93] #KWh 
lf_pv = [0.00E+00, 0.00E+00, 0.00E+00, 0.00E+00, 9.80E-04, 2.47E-02, 9.51E-02, 1.50E-01, 2.29E-01, 2.98E-01, 3.52E-01, 4.15E-01, 4.58E-01, 3.73E-01, 2.60E-01, 2.19E-01, 1.99E-01, 8.80E-02, 7.03E-02, 3.90E-02, 9.92E-03, 1.39E-06, 0.00E+00, 0.00E+00]
timestep = len(load)  #nbre de pas de temps
c_pv = 2500  #cout du PV Euro/kw 
c_batt = 1000  #euro/kwh 
eff_batt_in = 0.95  
eff_batt_out = 0.95  
chargetime = 4  # hours to charge fully the battery  # en h peut y avoir un discharge time egalement

# Model
model = ConcreteModel()

# Define model variables
model.pv_installed = pyo.Var(within=pyo.NonNegativeReals)       # [kW]
model.battery_installed = pyo.Var(within=pyo.NonNegativeReals)   # [kWh]
model.state_of_charge_temp = pyo.Var(within=pyo.NonNegativeReals) # [kWh]
model.Epv_temp = pyo.Var(within=pyo.NonNegativeReals)             # [kWh]
model.Pbatt_in_temp = pyo.Var(within=pyo.NonNegativeReals)         #kw 
model.Pbatt_out = pyo.Var(within=pyo.NonNegativeReals)             #KW 

# Define the constraints
def capacity_battery_constraint(model):
    return model.Epv_temp <= lf_pv * model.pv_installed

def max_charge_battery_constraint(model):
    return model.Pbatt_in_temps <= model.battery_installed / chargetime

def max_charge_battery_constraint(model):
    return model.Pbatt_out_temps <= model.battery_installed / chargetime
  
def storage_battery_max_constraint(model):
  model.state_of_charge_temp <= model.battery_installed

def equilibrium_constraint(model):
   model.Epv_temp  + model.Pbatt_out_temps -  model.Pbatt_in_temps = model.load
  


# Define the objective functions
##########################################
############ CODE TO ADD HERE ############
##########################################


# Specify the path towards your solver (gurobi) file
solver = SolverFactory('...')
solver.solve(model)

# Results - Print the optimal PV size and optimal battery capacity
##########################################
############ CODE TO ADD HERE ############
##########################################


# Plotting - Generate a graph showing the evolution of (i) the load, 
# (ii) the PV production and, (iii) the soc of the battery
##########################################
############ CODE TO ADD HERE ############
##########################################
