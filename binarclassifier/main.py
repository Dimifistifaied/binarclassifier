from network import Network
from symbolic import Symbolic as sy
from propositional import Propositional as pr

Network.create_network()

symbolic = sy()
formal = symbolic.evaluator("John is a singer and dancer but not a driver")
propose_evl = pr()
propose_evl.propositional_evaluation(formal)



