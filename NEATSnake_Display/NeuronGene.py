from  NeuronType import NeuronType
import random
class NeuronGene(object):

	def __init__(self, ids, nt, brec, dsplity, dsplitx, inov_id):
		self.id = id
		self.neuron_type = nt
		self.is_recurrent = brec
		self.activation_response = random.uniform(-1,1)
		self.splity = dsplity
		self.splitx = dsplitx
		self.innovation_id = inov_id
