import os
import sys
from src.vectorstore import load_vectorstore
from src.agent import build_agent

try:
    vs = load_vectorstore()
    agent = build_agent(vs)
    graph = agent.get_graph()
    
    # Generate Mermaid diagram PNG or ASCII
    png_data = graph.draw_mermaid_png()
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent_graph.png")
    with open(output_path, "wb") as f:
        f.write(png_data)
    print(f"SUCCESS: Generated LangGraph visual diagram at '{output_path}'")
except Exception as exc:
    print(f"Mermaid PNG fallback: {exc}")
    try:
        print("Mermaid graph code:")
        print(graph.draw_mermaid())
    except Exception as e:
        print(e)
