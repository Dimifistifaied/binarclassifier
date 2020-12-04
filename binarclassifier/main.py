from network import Network
from symbolic import Symbolic as sy
from propositional import Propositional as pr

Network.create_network()

symbolic = sy()
formal = symbolic.evaluator("If the sun is a star and a fiery boul of molthing lava then it is not a planet")
propose_evl = pr()
propose_evl.propositional_evaluation(formal)



