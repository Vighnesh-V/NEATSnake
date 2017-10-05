from Innovation import Innovation
from InnovationType import InnovationType
from NeuronType import NeuronType
nclass InnovationDatabase(object):
	#Innovation ID's start at one! invariant
	#neuron ID's start at one! invariant
	def __init__(self, startlinks, startneurons):
		self.next_innovation_id = 1
		self.next_neuronID = 1
		self.innov_list = []

		#add the neurons to the innovation list
		for neuron in startneurons:
			new_inno = Innovation()
			new_inno.neuron_ctor(neuron,self.next_innovation_id, self.next_neuronID)
			self.next_innovation_id += 1
			self.next_neuronID += 1
			self.innov_list.append(new_inno)
		#add links to innovation list

		for link in startlinks:
			new_inno = Innovation()
			
			new_inno.default_ctor(link.from, link.to, InnovationType.LINK, self.next_innovation_id)
			new_inno.neuronID = -1
			self.next_innovation_id +=1
			self.innov_list.append(new_inno)

	#returns innov id if innovation has occured, otherwise returns -1
	def exists_innovation(self, nin, nout, type):
		for innovation in self.innov_list:
			if((nin == innovation.neuron_in) and (nout == innovation.neuron_out) and (type is innovation.innovation_type)):
				return innovation.innovation_id

		return -1


	








