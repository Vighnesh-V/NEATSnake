class LinkGene(object):

	def __init__(self, fromN, toN, enabledb, inov):

		self.from = fromN
		self.to = toN
		self.is_enabled = enabledb
		self.is_recurrent = (fromN == toN)
		self.innovation_id = inov
