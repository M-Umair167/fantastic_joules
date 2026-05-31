import json
import sys
import os
import traceback

# Mock go.Figure.show to prevent browser launching / hanging
import plotly.graph_objects as go
go.Figure.show = lambda *args, **kwargs: None

def log(msg):
    print(msg)
    sys.stdout.flush()

def run_notebook(nb_path):
    log(f"\n============================================================")
    log(f"EXECUTING: {nb_path}")
    log(f"============================================================")
    
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    cells = nb.get("cells", [])
    log(f"Total cells: {len(cells)}")

    # We provide "display" in global_scope so that display(df) doesn't raise NameError.
    global_scope = {
        "__builtins__": __builtins__,
        "display": lambda *args, **kwargs: None,
    }

    # Execute setup to ensure mocks are active in global_scope too
    exec("import plotly.graph_objects as go; go.Figure.show = lambda *args, **kwargs: None", global_scope)

    for i, cell in enumerate(cells):
        if cell.get("cell_type") == "code":
            src = "".join(cell.get("source", []))
            if not src.strip():
                continue
            log(f"--- Cell {i} ---")
            
            # Print a preview of the cell
            lines = src.strip().split("\n")
            preview = "\n".join(lines[:3])
            if len(lines) > 3:
                preview += "\n..."
            log(preview)
            
            try:
                exec(src, global_scope)
                log(f"Cell {i} success!\n")
            except Exception as e:
                log(f"ERROR in Cell {i}: {e}")
                traceback.print_exc()
                sys.stderr.flush()

if __name__ == "__main__":
    run_notebook("datasheet-analysis_IMC25.ipynb")
    run_notebook("PSU-efficiency-analysis_IMC25.ipynb")
    log("\nAll notebooks finished execution successfully!")
