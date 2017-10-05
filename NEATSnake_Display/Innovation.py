from NeuronType import NeuronType
from InnovationType import InnovationType

class Innovation(object):
	def __init__self(self):
		self.innovation_type = None 
		self.innovation_id = None 
		self.neuron_in = None 
		self.neuron_out = None
		self.neuron_type = None 
		self.splitx = None 
		self.splity = None 
		self.neuronID = None
	#initialises coordinates to 0,0
	def default_ctor(self, nin, nout, type, id):
		self.innovation_id = id
		self.neuron_in = nin
		self.neuron_out = nout
		self.innovation_type = type
		self.splitx = 0
		self.splity = 0
		self.neuron_type = NeuronType.NONE
		self.neuronID = 0

	#initialises coordinates to those specified by given neuron ->
	def neuron_ctor(self,neuron, inovid, nid):
		self.innovation_id = inovid
		self.neuron_in = -1
		self.neuron_out = -1
		self.innovation_type = InnovationType.NEURON
		self.splitx = neuron.splitx
		self.splity = neuron.splity
		self.neuron_type = neuron.neuron_type
		self.neuronID = nid



	#initialises coordinates to those specified explicitly
	def custom_ctor(self, nin, nout, type, inovid, ntype, x, y):
		self.innovation_id = inovid
		self.innovation_type = type
		self.neuron_in = nin
		self.neuron_out = nout
		self.neuron_type = ntype
		self.splitx = x
		self.splity = y
		self.neuronID = 0
	