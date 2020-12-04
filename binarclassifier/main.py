from network import Network
from symbolic import Symbolic as sy
from propositional import Propositional as pr

Network.create_network()

symbolic = sy()
formal = symbolic.evaluator("The sun is a star and a sphere then not a planet")
propose_evl = pr()
propose_evl.propositional_evaluation(formal)



