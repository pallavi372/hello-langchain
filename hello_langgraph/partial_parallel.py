from langgraph.graph import StateGraph, START, END
from typing import TypedDict

#  Define State 
class State(TypedDict):
    fin_dept: bool
    lib_dept: bool
    sports_dept: bool
    student_id: str


#  Node functions must return dictionary
def financial_department_check(state: State):
    return {"fin_dept": True}


def library_department_check(state: State):
    return {"lib_dept": True}


def sports_department_check(state: State):
    return {"sports_dept": True}


#  Create graph
graph = StateGraph(State)

# Add nodes
graph.add_node("fin", financial_department_check)
graph.add_node("lib", library_department_check)
graph.add_node("sports", sports_department_check)

# Add edges (parallel execution)
graph.add_edge(START, "fin")
graph.add_edge(START, "lib")
graph.add_edge(START, "sports")

graph.add_edge("fin", END)
graph.add_edge("lib", END)
graph.add_edge("sports", END)

# Run graph
if __name__ == "__main__":
    compile_graph = graph.compile()

    result = compile_graph.invoke(State(student_id='i1001'))
    print(result)