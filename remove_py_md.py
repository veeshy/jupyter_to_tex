"""
Removes all python code from a markdown file created from a jupyter notebook


Assumes python code is of the form
```python
code
```

And runtime warnings look like (spacing included)
    //anaconda/lib/python3.5/site-packages/coupleorigen/plots/tally_plots.py:378: RuntimeWarning: invalid value encountered in true_divide
      rel_comp = comp.values / comp_val.values

"""
import os
import argparse

def remove_py(file):
    file_parts = os.path.splitext(file)
    
    # check if file has an extension or not to create output
    if file_parts[1]:
        output = file_parts[0] + "_no_py" + file_parts[1]
    else:
        output = file_parts[0] + "_no_py"

    with open(file, 'r') as f:
        lines = f.readlines()
    
    with open(output, 'w') as f:
        write_line = True
        previous_line_warning = False
        for line in lines:
            skip_line = False
            if line.startswith("```python"):
                write_line = False
                skip_line = True
            
            elif line.startswith("```"):
                write_line = True
                skip_line = True
        
            # Runtime warnings might be 1 or 2 lines long. Anything longer is not supported here
            elif 'RuntimeWarning: ' in line:
                skip_line = True
                previous_line_warning = True
            elif previous_line_warning:
                previous_line_warning = False
                if line.startswith("      "):
                    skip_line = True
        
            if write_line and not skip_line:
                f.write(line)

def create_parser():
    parser = argparse.ArgumentParser(description="Perform statistical analysis of time store",
                                     epilog="Creates or appends to a std_dev store based on mean_time_store path")

    parser.add_argument('file', help="Path to markdown file to edit")
    
    return parser
if __name__ == "__main__":
    
    parser = create_parser()
    args = parser.parse_args()
    
    remove_py(args.file)
    
    
    
    