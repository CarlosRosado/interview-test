"""
Juggers Utils
"""
import copy

class TargetFound(Exception):
	pass

class Jugger(object):
	"""
	Class for all Juggers with all states (fill, full, empty)
	"""
	def __init__(self, jug_capacity):
		self.jug_capacity = jug_capacity
		self.quantity = 0
	
	def full(self):
		"""
		Function for fixed full jugger
		"""
		self.quantity = self.jug_capacity
		
	def empty(self):
		"""
		Function for fixed empty jugger
		"""
		self.quantity = 0
		
	def insert_water(self, jug):
		"""
		Function for insert water in a specific jugger
		:param jug: jugger to insert water
		"""
		r = jug.fill_jug(self.quantity)
		self.quantity = r
		
	def fill_jug(self, quantity):
		"""
		Function for remove water in a specific jugger
		:param jug: jugger to remove water
		:return: jugger quantity
		"""
		self.quantity += quantity
		if self.quantity > self.jug_capacity:
			r = self.quantity - self.jug_capacity
			self.quantity -= r
			return r
		else:
			return 0
		
	def __repr__(self):
		return "Jugger: %i/%i" % (self.quantity, self.jug_capacity)

class StateJugger(object):
	"""
	Class for all state of Juggers.
	"""
	def __init__(self, juggers):
		"""
		Function for initialice all stages of a jugger
		:param juggers: juggers
		"""
		self.juggers = [copy.copy(j) for j in juggers]
		self.next_states = []
		self.parent = None
		self.target = False
		
	def add_jugger_state(self, juggers_state):
		"""
		Function for adding a jugger state
		:param juggers_state: jugger state to add
		"""
		self.next_states.append(juggers_state)
		juggers_state.parent = self
		
	def same_jugger_state(self, jugger_state):
		"""
		Function for check if is the same state
		:param juggers_state: jugger state for check
		:return: Return True if is the same state or False if is different
		"""
		for i, j in enumerate(self.juggers):
			if j.jug_capacity == jugger_state.juggers[i].jug_capacity and j.quantity != jugger_state.juggers[i].quantity:
				return False
			
		return True
	
	def fill_quantity(self, quantity):
		"""
		Function to check quantity of water in a jugger
		:param quantity: quantity of water to check in a jugger
		:return: True or False for check quantity of jugger
		"""
		for j in self.juggers:
			if j.quantity == quantity:
				return True
			
		return False
		
class JuggersGraph(object):
	"""
	Take list of Juggs and select the best way to solve the problem using a graph.
	"""
	def __init__(self, juggers, target):
		"""
		Function for init a jugger graph
		:param juggers: juggers 
		:param target: target liters
		"""
		self.start = StateJugger(juggers)
		self.target = target
		self.graphed = False
		
	def state_existing(self, state):
		"""
		Function for check the state of jugger
		:param state: state to check 
		:return: return the target if this exist
		"""
		def help(self_state):
			t_states = [state.same_jugger_state(s) for s in self_state.next_states]
			childs = [help(s) for s in self_state.next_states]
			
			state_exist = False
			for ts in t_states:
				state_exist = state_exist or ts
			for cs in childs:
				state_exist = state_exist or cs
			
			return state_exist
		
		t_state = state.same_jugger_state(self.start)
		childs = help(self.start)
		return t_state or childs
	
	def grapher(self):
		"""
		Function for define all steps in jugger graph
		"""
		def help(state_current):
			try:
				for i,j in enumerate(state_current.juggers):
					state_fill = StateJugger(state_current.juggers)
					state_fill.juggers[i].full()
					# Check the duplicates
					if not self.state_existing(state_fill):
						state_current.add_jugger_state(state_fill)
					# Stop condition
					if state_fill.fill_quantity(self.target):
						state_fill.target = True
						raise TargetFound()
						
					state_empty = StateJugger(state_current.juggers)
					state_empty.juggers[i].empty()
					# check states for duplicates
					if not self.state_existing(state_empty):
						state_current.add_jugger_state(state_empty)
					# check for target condition
					if state_empty.fill_quantity(self.target):
						state_empty.target = True
						raise TargetFound()
						
					# Check if the jugg is in other jugg
					for k in range(len(state_current.juggers)):
						if i == k:
							continue
						state_transfer = StateJugger(state_current.juggers)
						state_transfer.juggers[i].insert_water(state_transfer.juggers[k])
						# check states for duplicates
						if not self.state_existing(state_transfer):
							state_current.add_jugger_state(state_transfer)
						# check for goal condition
						if state_transfer.fill_quantity(self.target):
							state_transfer.target = True
							raise TargetFound()
							
				for s in state_current.next_states:
					if s.target:
						raise TargetFound()
					help(s)
			# stop processing
			except TargetFound:
				pass
			
		self.graphed = True
		help(self.start)

	def print_graph_solutions(self):
		"""
		This function is for print the best result.
		"""

		self.number_solution = 0
		self.list_solutions = []

		# look for the target flag
		def states_traverse(state_current):
			if state_current.target:
				self.number_solution += 1

				list_state = state_path_get(state_current)

				self.list_solutions.append({
					"steps": len(list_state),
					"list": list_state
				})
			else:
				for s in state_current.next_states:
					states_traverse(s)

		def state_path_get(state_current, path = []):
			path = [state_current] + path
			if state_current.parent:
				return state_path_get(state_current.parent, path)
			else:
				return path

		if self.graphed:
			# print all solutions
			states_traverse(self.start)
			if self.number_solution == 0:
				print("Sorry, Don't have a Solution!")
			# Print the best solution
			else:
				print("\nSolution is:")
				steps_min = 9999999999
				sol = None
				for s in self.list_solutions:
					if s["steps"] < steps_min:
						steps_min = s["steps"]
						solution = s
				for s in solution["list"]:
					print(s.juggers)

		else:
			# Error control
			print("Error, You execeute the graph first.")
		