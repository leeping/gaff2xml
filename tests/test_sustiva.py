import simtk.unit as u
from simtk.openmm import app
import simtk.openmm as mm
import gafftools
import system_checker

temperature = 300 * u.kelvin
friction = 0.3 / u.picosecond
timestep = 0.1 * u.femtosecond

prmtop = app.AmberPrmtopFile("./sample_files/sustiva.prmtop")
inpcrt = app.AmberInpcrdFile("./sample_files/sustiva.inpcrd")

system_prm = prmtop.createSystem(nonbondedMethod=app.NoCutoff, nonbondedCutoff=1.0*u.nanometers, constraints=None)

mol2 = gafftools.Mol2Parser("./sample_files/sustiva.mol2")
top, xyz = mol2.to_openmm()

forcefield = app.ForceField("out.xml")

system_xml = forcefield.createSystem(top, nonbondedMethod=app.NoCutoff, nonbondedCutoff=1.0*u.nanometers, constraints=None)

checker = system_checker.SystemChecker(system_prm, system_xml)
checker.check_forces()
