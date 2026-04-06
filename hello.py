from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# 1️⃣ Create TypedDict for the state
class Mystate(TypedDict):
    """This class represents the state of the graph"""
    name: str
    friends: list[str]
    family: list[str]
    message: str

# 2️⃣ Node to find friends
def find_friend(state: Mystate) -> Mystate:
    """This function finds friends"""
    state['friends'] = ['Ram', 'Shyam']
    
    return state

# 3️⃣ Node to find family
def find_family(state: Mystate) -> Mystate:
    """This function finds family"""
    state['family'] = ['Sita', 'Gita']
   
    return state

# 4️⃣ Create the state graph
graph = StateGraph(Mystate)
graph.add_node("friends", find_friend)
graph.add_node("family", find_family)
graph.add_edge(START, "friends")
graph.add_edge("friends", "family")
graph.add_edge("family", END)

# 5️⃣ Compile the graph
compiled_graph = graph.compile()

# 6️⃣ Run the graph
if __name__ == "__main__":
    initial_state: Mystate = {
        "name": "abc",
        "friends": [],
        "family": [],
        "message": ""
    }
    response = compiled_graph.invoke(initial_state)
    print(response)